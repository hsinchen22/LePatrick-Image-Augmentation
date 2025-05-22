import cv2
import random
import numpy as np
from pathlib import Path
from .utils import *

def Patrick(
    source_dir: str,
    output_dir: str | None = None,
    num_outputs: int = 1000,
    num_patricks: int = 5,
    enable_color_jitter: bool = True,
    enable_scale_jitter: bool = True,
    enable_copy_paste: bool = True,
    rand_seed: int | None = None,
    mode: str = "save",  
    overwrite_existing: bool = False
) -> None:
    """
    High-level augmentation entrypoint.

    Args:
      source_dir: directory with "images/" and "labels/" subfolders.
      output_dir: where to write outputs; defaults to source_dir.
      num_outputs: number of augmented images to produce.
      num_patricks: number of Patrick imprints per image.
      enable_color_jitter: toggle HSV jitter on Patrick.
      enable_scale_jitter: toggle random flip/scale for segments.
      enable_copy_paste: toggle copying/pasting foreground segments.
      rand_seed: seed for reproducibility.
      mode: "save" writes files; "preview" displays images.
      overwrite_existing: if False, skip existing output files.
    """
    if rand_seed is not None:
        random.seed(rand_seed)
        np.random.seed(rand_seed)

    src_path = Path(source_dir)
    out_path = Path(output_dir or source_dir)
    (out_path / "images").mkdir(parents=True, exist_ok=True)
    (out_path / "labels").mkdir(parents=True, exist_ok=True)

    images = list((src_path / "images").glob("*.jpg"))
    if not images:
        raise FileNotFoundError(f"No images found in {src_path / 'images'}")

    for idx in range(num_outputs):
        img_file = out_path / "images" / f"patrick_{idx}.jpg"
        lbl_file = out_path / "labels" / f"patrick_{idx}.txt"
        if not overwrite_existing and img_file.exists():
            continue

        try:
            bg_path, fg_path = random.sample(images, 2)
            bg_img, bg_box = resize_background(load_segment(bg_path),enable_scale_jitter)
            H, W = bg_img.shape[:2]

            # -- Optional foreground copy-paste
            fg_box = None
            if enable_copy_paste:
                fg_roi, fg_mask = resize_foreground(load_segment(fg_path), enable_scale_jitter)
                h, w = fg_roi.shape[:2]
                x = random.randint(0, W - w)
                y = random.randint(0, H - h)
                roi = bg_img[y:y+h, x:x+w]
                pasted = cv2.add(
                    cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(fg_mask)),
                    cv2.bitwise_and(fg_roi, fg_roi, mask=fg_mask),
                )
                bg_img[y:y+h, x:x+w] = pasted
                fg_box = np.array([[x, y], [x+w, y+h]])

            # -- Load Patrick overlay
            p_src, p_mask = load_patrick()

            # -- Imprint Patrick
            imprint_patrick(bg_img, p_src, p_mask, fg_box, num_patricks, enable_color_jitter, enable_scale_jitter)
            imprint_patrick(bg_img, p_src, p_mask, bg_box, num_patricks, enable_color_jitter, enable_scale_jitter)

            # -- Save or preview
            if mode == "save":
                cv2.imwrite(str(img_file), bg_img)
                with open(lbl_file, "w") as f:
                    # write background label
                    save_label(f, bg_box / [W, H])
                    # write foreground label if used
                    if fg_box is not None:
                        save_label(f, fg_box / [W, H])
            else:
                # Preview mode
                disp = cv2.resize(bg_img, (640, 360))
                cv2.imshow("Patrick Preview", disp)
                cv2.waitKey(0)

        except Exception as e:
            print(f"[Patrick] Skipping idx={idx} due to {e!r}")