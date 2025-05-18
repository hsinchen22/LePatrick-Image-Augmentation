<a id="readme-top"></a>
## LePatrick Image Augmentation for Better Detection & Clipping

<img src="images/logo.png" align="right" width="360">

LEEDLE LEEDLE LEEDLE LEE! We've cooked up something special with a friend named Patrick! 👑🔥

This project playfully pushes the boundaries of image augmentation to seriously amp up object detection and give highlight clipping a major upgrade, bringing you LeBron's epic moments like never before.

[Explore the repo and see how this surprising combo is making it happen! »]()

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
	<li><a href="#1">Overview - That's Mr. Dr. Professor Patrick to you!</a></li>
    <ul>
		<li><a href="#1-1">How It Works</a></li>
		<li><a href="#1-2">Results & Comparison</a></li>
		<li><a href="#1-3">Highlight Clipping</a></li>
	</ul>
    <li><a href="#2">Getting Started - We're not cavemen! WE HAVE TECHNOLOGY!</a></li>
    <ul>
        <li><a href="#2-1">Prerequisites</a></li>
        <li><a href="#2-2">Installation</a></li>
    </ul>
    <li><a href="#3">License - Is mayonnaise an instrument?</a></li>
    <li><a href="#4">Contact - Knowledge can never replace friendship</a></li>
</ul>
<br/>

<a id="1"></a>
## Overview - That's Mr. Dr. Professor Patrick to you!

This project playfully pushes the boundaries of image augmentation to seriously amp up object detection and give highlight clipping a major upgrade, bringing you LeBron's epic moments like never before.

<a id="1-1"></a>
### How It Works

The augmentation pipeline employs a series of transformations to generate diverse training samples:

* <a>"Patrick" Imprinting</a>:
The specific visual element is randomly color-augmented with hue and saturation adjustments and randomly scaled within a range of 0.8 to 1.2. This introduces varied appearances and placements to help the model better generalize across different visual conditions.

* <a>Dynamic Positioning</a>:
Augmented Patricks are positioned based on a 2D Gaussian distribution centered on the LeBron bounding boxes, introducing controlled randomness that mimics natural variations and occlusions between players. This helps the model learn to recognize objects despite shifts and partial overlaps in their locations.
