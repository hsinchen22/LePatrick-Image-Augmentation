import unittest
import numpy as np
import cv2
import random
import tempfile
from pathlib import Path
from LePatrick import Patrick

def create_dummy_data(folder: Path):
    images_dir = folder / "images"
    labels_dir = folder / "labels"
    images_dir.mkdir(parents=True, exist_ok=True)
    labels_dir.mkdir(parents=True, exist_ok=True)
    H = random.randint(100, 360)
    W = random.randint(100, 640)
    N = random.randint(2, 10)
    for i in range(N):
        image = np.random.randint(0, 256, (H, W, 3), dtype=np.uint8)
        cv2.imwrite(str(images_dir / f"src_{i}.jpg"), image)
        with open(labels_dir / f"src_{i}.txt", "w") as f:
            f.write(f"0 {random.random()} {random.random()} {random.random()} {random.random()} {random.random()} {random.random()}\n")

def create_invalid_data(folder: Path):
    images_dir = folder / "images"
    labels_dir = folder / "labels"
    images_dir.mkdir(parents=True, exist_ok=True)
    labels_dir.mkdir(parents=True, exist_ok=True)
    for i in range(2):
        image = np.random.randint(0, 256, (360, 640, 3), dtype=np.uint8)
        cv2.imwrite(str(images_dir / f"src_{i}.jpg"), image)
        with open(labels_dir / f"src_{i}.txt", "w") as f:
            f.write(f"0\n")

class TestPatrick(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.source_dir = Path(self.tmp_dir.name) / "source"
        self.output_dir = Path(self.tmp_dir.name) / "output"

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_output_no_jitter(self):
        create_dummy_data(self.source_dir)
        Patrick(
            source_dir=str(self.source_dir),
            output_dir=str(self.output_dir),
            num_outputs=10,
            enable_scale_jitter=False,
            enable_copy_paste=False
        )
        out_images = list((self.output_dir / "images").glob("*jpg"))
        out_labels = list((self.output_dir / "labels").glob("*txt"))
        self.assertEqual(len(out_images), 10)
        self.assertEqual(len(out_labels), 10)
        
        H, W = cv2.imread(str(self.source_dir / "images" / "src_0.jpg")).shape[:2]
        for image_path in out_images:
            image = cv2.imread(str(image_path))
            self.assertTupleEqual(image.shape, (H, W, 3))
        
        for label_path in out_labels:
            with open(label_path, "r") as file:
                lines = file.readlines()
                self.assertEqual(len(lines), 1)
    
    def test_output_with_copy_paste(self):
        create_dummy_data(self.source_dir)
        Patrick(
            source_dir=str(self.source_dir),
            output_dir=str(self.output_dir),
            num_outputs=10,
            enable_scale_jitter=True,
            enable_copy_paste=True,
        )
        out_labels = list((self.output_dir / "labels").glob("*txt"))
        
        for label_path in out_labels:
            with open(label_path, "r") as file:
                for line in file:
                    parts = line.strip().split()
                    self.assertEqual(len(parts), 5)
                    self.assertEqual(parts[0], "0")
                    for coord in map(float, parts[1:]):
                        self.assertGreaterEqual(coord, 0.0)
                        self.assertLessEqual(coord, 1.0)

    def test_output_overwrite(self):
        create_dummy_data(self.source_dir)
        Patrick(
            source_dir=str(self.source_dir),
            output_dir=str(self.output_dir),
            num_outputs=1
        )
        ori_image = cv2.imread(str(self.output_dir / "images" / "patrick_0.jpg"))

        Patrick(
            source_dir=str(self.source_dir),
            output_dir=str(self.output_dir),
            num_outputs=1,
            overwrite_existing=False
        )
        new_image = cv2.imread(str(self.output_dir / "images" / "patrick_0.jpg"))
        self.assertTrue(np.array_equal(ori_image, new_image))

        Patrick(
            source_dir=str(self.source_dir),
            output_dir=str(self.output_dir),
            num_outputs=1,
            overwrite_existing=True
        )
        new_image = cv2.imread(str(self.output_dir / "images" / "patrick_0.jpg"))
        self.assertFalse(np.array_equal(ori_image, new_image))
    
    def test_invalid_source(self):   
        with self.assertRaises(FileNotFoundError):
            Patrick(
                source_dir=str(self.source_dir),
                output_dir=str(self.output_dir),
                num_outputs=1
            )
        
    def test_invalid_label(self):
        create_invalid_data(self.source_dir)
        Patrick(
            source_dir=str(self.source_dir),
            output_dir=str(self.output_dir),
            num_outputs=1
        )
        out_images = list((self.output_dir / "images").glob("*jpg"))
        self.assertEqual(len(out_images), 0)