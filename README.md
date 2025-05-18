<a id="readme-top"></a>
## LePatrick Image Augmentation for Better Detection & Clipping

<img src="images/logo.png" align="right" width="300">

Meet Mr. Dr. Professor Patrick — the ultimate game-changer in image augmentation! 🎩✨

This project cranks up object detection and supercharges LeBron’s highlight clipping, turning ordinary moments into slam-dunk spectacles like never before.

🔥🔥🔥 Explore the repo and see how this surprising combo is making it happen!

<br/>
<div>
	<img src="https://img.shields.io/badge/Python-FFD43B.svg?logo=Python&logoColor=blue" height="20"/>
	<img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=PyTorch&logoColor=white" height="20"/>
	<img src="https://img.shields.io/badge/OpenCV-8BDA67.svg?logo=OpenCV&logoColor=white" height="20"/>
	<img src="https://img.shields.io/badge/YOLOv11-111F68.svg?logo=YOLO&logoColor=white" height="20"/>
	<img src="https://img.shields.io/badge/Roboflow-6706CE.svg?logo=Roboflow&logoColor=white" height="20"/>
</div>

<br/>

### Table of Contents
- [Overview - Who're you callin pinhead?!](#-overview---whore-you-callin-pinhead)
	- [How It Works](#-how-it-works)
	- [Results & Comparison](#-results--comparison)
	- [Highlight Clipping](#-highlight-clipping)

- [Usage - We're not cavemen! WE HAVE TECHNOLOGY!](#-usage---were-not-cavemen-we-have-technology)
	- [Prerequisites](#-prerequisites)
	- [Installation](#-installation)

- [License - We should take Bikini Bottom, and push it somewhere else!](#-license---we-should-take-bikini-bottom-and-push-it-somewhere-else)

- [Contact - Marty?! Janet?! Who are you people?!](#-contact---marty-janet-who-are-you-people)

<br/>

## ⭐ Overview - Who're you callin pinhead?!

This project playfully pushes the boundaries of image augmentation to seriously amp up object detection and give highlight clipping a major upgrade, bringing you LeBron's epic moments like never before.

### How It Works

The augmentation pipeline employs a series of transformations to generate diverse training samples:

* ["Patrick" Imprinting]():
The specific visual element is randomly color-augmented with hue and saturation adjustments and randomly scaled within a range of 0.8 to 1.2. This introduces varied appearances and placements to help the model better generalize across different visual conditions.

* [Dynamic Positioning]():
Augmented Patricks are positioned based on a 2D Gaussian distribution centered on the LeBron bounding boxes, introducing controlled randomness that mimics natural variations and occlusions between players. This helps the model learn to recognize objects despite shifts and partial overlaps in their locations.

### Results & Comparison

We compare the performance of various augmentation techniques.

<div align="center" style="display: inline-block;">
	<img src="images/comparison.png" width="60%" style="vertical-align: middle;">
    <img src="images/AP@50-90.svg" width="34%" style="vertical-align: middle;">
</div>
<br/>

> [!IMPORTANT]
> Patrick substantially improves detection performance and is additive with Copy-Paste;
>
> The combination of Patrick and Copy-Paste consistently outperforms other augmentation methods.

### Highlight Clipping

* [LeBron Detection]():
A YOLO model is used to detect LeBron in each video frame, generating bounding boxes to isolate him from the background. To maintain consistent localization, the bounding box coordinates are slightly padded. This process ensures reliable tracking and minimizes jitter across frames.

* [Action Classification]():
Detected clips are preprocessed and fed into a fine-tuned 3D ResNet (R3D-18) model, which classifies actions into four categories: NONE, SHOOT, LAYUP, and DUNK. The model is fine-tuned using **Focal Loss** to address the class imbalance inherent in sports highlight detection, where non-highlight actions are significantly more frequent. 
This loss function down-weights easy examples, allowing the model to focus on harder, rarer events. Probability scores are smoothed over consecutive frames to enhance prediction stability.

<div align="center">
	<img src="images/confusion_matrix.png" width="400">
</div>
<br/>

* [Highlight Extraction]():
Frames are buffered to form short clips of 15 frames each. If the average action probability within the buffer exceeds a confidence threshold (0.4), the clip is marked as a highlight. This method efficiently captures high-impact moments while filtering out irrelevant frames.

<br/>

## 📦 Usage - We're not cavemen! WE HAVE TECHNOLOGY!

Here's how to get started:

### Prerequisites

Before you get started with LePatrick Augmentation, make sure you have the following installed:

### Installation

Follow these steps to get RunTini up and running:

<br/>

## 📝 License - We should take Bikini Bottom, and push it somewhere else!
Distributed under the Unlicense License. See LICENSE.txt for more information. This means you're free to use, modify, and distribute LePatrick as you see fit – no strings attached!

<br/>

## 📬 Contact - Marty?! Janet?! Who are you people?!
Have questions, suggestions, or just want to share your favorite bar crawl story? Feel free to reach out!

<b>Hsin Chen</b><br/>
Email: <a href="mailto:hsinchen@stanford.edu">hsinchen@stanford.edu</a><br/>
GitHub: <a href="https://github.com/hsinchen22">github.com/hsinchen22</a>

<!-- put yours-->


We look forward to assisting you and ensuring your experience with our product is successful and enjoyable!

<br/>
<a href="#readme-top">Back to top</a>
