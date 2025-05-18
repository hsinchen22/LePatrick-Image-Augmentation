<a id="readme-top"></a>
## LePatrick Image Augmentation for Better Detection & Clipping

<img src="images/logo.png" align="right" width="360">

Meet Mr. Dr. Professor Patrick — the ultimate game-changer in image augmentation! 🎩✨

This project cranks up object detection and supercharges LeBron’s highlight clipping, turning ordinary moments into slam-dunk spectacles like never before.

[Explore the repo and see how this surprising combo is making it happen! »]()

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
<ul>
	<li><a href="#1">Overview - Who're you callin pinhead?!</a></li>
    <ul>
		<li><a href="#1-1">How It Works</a></li>
		<li><a href="#1-2">Results & Comparison</a></li>
		<li><a href="#1-3">Highlight Clipping</a></li>
	</ul>
    <li><a href="#2">Usage - We're not cavemen! WE HAVE TECHNOLOGY!</a></li>
    <ul>
        <li><a href="#2-1">Prerequisites</a></li>
        <li><a href="#2-2">Installation</a></li>
    </ul>
    <li><a href="#3">License - We should take Bikini Bottom, and push it somewhere else!</a></li>
    <li><a href="#4">Contact - Marty?! Janet?! Who are you people?!</a></li>
</ul>
<br/>

<a id="1"></a>
## Overview - Who're you callin pinhead?!

This project playfully pushes the boundaries of image augmentation to seriously amp up object detection and give highlight clipping a major upgrade, bringing you LeBron's epic moments like never before.

<a id="1-1"></a>
### How It Works

The augmentation pipeline employs a series of transformations to generate diverse training samples:

* ["Patrick" Imprinting]():
The specific visual element is randomly color-augmented with hue and saturation adjustments and randomly scaled within a range of 0.8 to 1.2. This introduces varied appearances and placements to help the model better generalize across different visual conditions.

* [Dynamic Positioning]():
Augmented Patricks are positioned based on a 2D Gaussian distribution centered on the LeBron bounding boxes, introducing controlled randomness that mimics natural variations and occlusions between players. This helps the model learn to recognize objects despite shifts and partial overlaps in their locations.

<a id="1-2"></a>
### Results & Comparison

We compare the performance of various augmentation techniques.

<div align="center" style="display: inline-block;">
	<img src="images/comparison.png" width="60%" style="vertical-align: middle;">
    <img src="images/AP@50-90.svg" width="34%" style="vertical-align: middle;">
</div>
<br/>

* Patrick substantially improves detection performance and is additive with Copy-Paste;
* The combination of Patrick and Copy-Paste consistently outperforms other augmentation methods.

<a id="1-3"></a>
### Highlight Clipping

[LeBron Detection]():
A YOLO model is used to detect LeBron in each video frame, generating bounding boxes to isolate him from the background. To maintain consistent localization, the bounding box coordinates are slightly padded. This process ensures reliable tracking and minimizes jitter across frames.

<img src="images/confusion_matrix.png" align="right" width="300">

[Action Classification]():
Detected clips are preprocessed and fed into a fine-tuned 3D ResNet (R3D-18) model, which classifies actions into four categories: NONE, SHOOT, LAYUP, and DUNK.

The model is fine-tuned using **Focal Loss** to address the class imbalance inherent in sports highlight detection, where non-highlight actions are significantly more frequent. 
This loss function down-weights easy examples, allowing the model to focus on harder, rarer events. Probability scores are smoothed over consecutive frames to enhance prediction stability.

[Highlight Extraction]():
Frames are buffered to form short clips of 15 frames each. If the average action probability within the buffer exceeds a confidence threshold (0.4), the clip is marked as a highlight. This method efficiently captures high-impact moments while filtering out irrelevant frames.

<a id="2"></a>
## Usage - We're not cavemen! WE HAVE TECHNOLOGY!

<a id="2-1"></a>
### Prerequisites

<a id="2-2"></a>
### Installation

<a id="3"></a>
## License - We should take Bikini Bottom, and push it somewhere else!
Distributed under the Unlicense License. See LICENSE.txt for more information. This means you're free to use, modify, and distribute LePatrick as you see fit – no strings attached!

<a id="4"></a>
## Contact - Marty?! Janet?! Who are you people?!
Have questions, suggestions, or just want to share your favorite bar crawl story? Feel free to reach out!

<table>
<tr>
	<td width="50"><img src="https://github.com/hsinchen22.png" style="border-radius: 50%;"></td>
	<td>
		<strong><span style="font-size: 1.2em;">Hsin Chen</span></strong><br/>
		Email: <a href="mailto:hsinchen@stanford.edu">hsinchen@stanford.edu</a><br/>
		GitHub: <a href="https://github.com/hsinchen22">github.com/hsinchen22</a>
	</td>
</tr>
</table>

<!-- Change it to yours-->
<table>
<tr>
	<td width="50"><img src="https://github.com/hsinchen22.png" style="border-radius: 50%;"></td>
	<td>
		<strong><span style="font-size: 1.2em;">Hsin Chen</span></strong><br/>
		Email: <a href="mailto:hsinchen@stanford.edu">hsinchen@stanford.edu</a><br/>
		GitHub: <a href="https://github.com/hsinchen22">github.com/hsinchen22</a>
	</td>
</tr>
</table>

We look forward to assisting you and ensuring your experience with our product is successful and enjoyable!

<a href="#readme-top">Back to top</a>
