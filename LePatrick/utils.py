import cv2
import random
import numpy as np
from importlib.resources import files

def load_segment(path):
    image = cv2.imread(str(path))
    if image is None:
        raise FileNotFoundError(f"Image not found: {path}")

    H, W, _ = image.shape
    label_file = path.parent.parent / "labels" / f"{path.stem}.txt"
    with open(label_file, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) > 5:
                points = np.array(parts[1:], dtype=float).reshape(-1, 2)
                return image, (points * [W, H]).astype(int)

    raise ValueError(f"Segment not found in: {label_file}")

def resize_foreground(args, enable_jitter=True):
    image, segment = args
    H, W, _ = image.shape
    mask = np.zeros((H, W), dtype=np.uint8)
    cv2.fillPoly(mask, [segment], 255)

    if enable_jitter:
        # Random horizontal flip
        if random.random() < 0.5:
            image = cv2.flip(image, 1)
            mask = cv2.flip(mask, 1)

        # Random scaling
        w, h = np.ptp(segment, axis=0)
        max_scale = min(W / w, H / h, 1.2)
        scale = random.uniform(0.8, max_scale)
        image = cv2.resize(image, None, fx=scale, fy=scale)
        mask = cv2.resize(mask, None, fx=scale, fy=scale)
        _, mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)

    # Crop to bounding box
    x, y, w, h = cv2.boundingRect(mask)
    return image[y:y+h, x:x+w], mask[y:y+h, x:x+w]

def resize_background(args, enable_jitter=True):
    image, segment = args
    if not enable_jitter:
        x1, y1 = np.min(segment, axis=0)
        x2, y2 = np.max(segment, axis=0)
        return image, np.array([[x1, y1], [x2, y2]])

    H, W, _ = image.shape
    canvas = np.zeros_like(image)

    # Random scaling
    scale = random.uniform(0.8, 1.2)
    image = cv2.resize(image, None, fx=scale, fy=scale)
    h, w, _ = image.shape
    x1, y1 = (np.min(segment, axis=0) * scale).astype(int)
    x2, y2 = (np.max(segment, axis=0) * scale).astype(int)

    # Random horizontal flip
    if random.random() < 0.5:
        image = cv2.flip(image, 1)
        x1, x2 = w - x2, w - x1

    # Place resized image onto canvas
    canvas[:min(H, h), :min(W, w)] = image[:min(H, h), :min(W, w)]
    if x1 < W and y1 < H:
        return canvas, np.array([[x1, y1], [min(x2, W), min(y2, H)]])
    return canvas, None

def load_patrick(shape="default"):
    if shape == "square":
        return np.full((100, 100, 3), 255, dtype=np.uint8), np.full((100, 100), 255, dtype=np.uint8)
    if shape == "sphere":
        mask = np.zeros((100, 100), dtype=np.uint8)
        cv2.circle(mask, (50, 50), 50, 255, -1)
        return np.full((100, 100, 3), 255, dtype=np.uint8), mask

    # Load image and alpha mask
    path = files("LePatrick.assets").joinpath("patrick.png")
    with path.open("rb") as f:
        data = np.asarray(bytearray(f.read()), dtype=np.uint8)
        image = cv2.imdecode(data, cv2.IMREAD_UNCHANGED)
    b, g, r, a = cv2.split(image)
    image = cv2.merge((b, g, r))
    _, mask = cv2.threshold(a, 128, 255, cv2.THRESH_BINARY)

    # Crop to bounding box
    x, y, w, h = cv2.boundingRect(a)
    return image[y:y+h, x:x+w], mask[y:y+h, x:x+w]

def augment_patrick(image, mask, max_size, enable_color_jitter, enable_scale_jitter):
    if enable_color_jitter:
        # Random hue and saturation
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv[..., 0] = random.randint(0, 179)
        hsv[..., 1] = random.randint(0, 255)
        image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    h, w, _ = image.shape
    scale = 0.75

    if enable_scale_jitter:
        scale = random.uniform(0.5, 1.0)
        
        # Random horizontal flip
        if random.random() < 0.5:
            image = cv2.flip(image, 1)
            mask = cv2.flip(mask, 1)

    fx = scale * max_size[0] / w
    fy = scale * max_size[1] / h
    image = cv2.resize(image, None, fx=fx, fy=fy)
    mask = cv2.resize(mask, None, fx=fx, fy=fy)
    _, mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)

    return image, mask

def imprint_patrick(background, image, mask, box, nums=5, enable_color_jitter=True, enable_scale_jitter=True):
    if box is None:
        return

    H, W, _ = background.shape
    center = (box[0] + box[1]) / 2
    spread = (box[1] - box[0])

    for _ in range(nums):
        aug_image, aug_mask = augment_patrick(image, mask, box[1] - box[0], enable_color_jitter, enable_scale_jitter)
        h, w, _ = aug_image.shape

        # Sample position using Gaussian spread
        dx = int(np.clip(random.gauss(center[0], spread[0]) - w / 2, 0, W - w))
        dy = int(np.clip(random.gauss(center[1], spread[1]) - h / 2, 0, H - h))

        roi = background[dy:dy+h, dx:dx+w]
        bg_part = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(aug_mask))
        fg_part = cv2.bitwise_and(aug_image, aug_image, mask=aug_mask)
        background[dy:dy+h, dx:dx+w] = cv2.add(bg_part, fg_part)

def save_label(file, box):
    x, y = (box[0] + box[1]) / 2
    w, h = box[1] - box[0]
    file.write(f"0 {x} {y} {w} {h}\n")