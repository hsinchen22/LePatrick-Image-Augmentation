<a id="readme-top"></a>
## LePatrick Image Augmentation for Better Detection & Clipping

<img src="images/logo.png" align="right" width="360">

Meet Mr. Dr. Professor Patrick — the ultimate game-changer in image augmentation! 🎩✨

This project cranks up object detection and supercharges LeBron’s highlight clipping, turning ordinary moments into slam-dunk spectacles like never before.

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
<div align="center">
	<img src="AP@50-90.svg" width="400">
</div>

<table>
	<thead>
		<tr>
			<th>Method</th>
			<th>Precision</th>
			<th>Recall</th>
			<th>F1-Score</th>
			<th>AP<sub>50</sub></th>
			<th>AP<sub>50-95</sub></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Baseline</td>
			<td>95.7</td>
			<td>86.4</td>
			<td>90.8</td>
			<td>91.7</td>
			<td>72.4</td>
		</tr>
		<tr>
			<td>Random Erasing [1]</td>
			<td>95.2</td>
			<td>87.0</td>
			<td>90.9</td>
			<td>91.6</td>
			<td>71.7</td>
		</tr>
		<tr>
			<td>Hide-and-Seek [2]<sub></td>
			<td>95.5</td>
			<td>85.2</td>
			<td>90.1</td>
			<td>91.2</td>
			<td>71.1</td>
		</tr>
		<tr>
			<td>Copy-Paste [3]</td>
			<td>91.0 <span style="color:red;">(-4.7)</span></td>
			<td>91.0 <a>(+3.6)</a></td>
			<td>91.0 <a>(+0.2)</a></td>
			<td>92.2 <a>(+0.5)</a></td>
			<td>74.2 <a>(+0.5)</a></td>
		</tr>
		<tr>
			<td>Patrick</td>
			<td>96.5 <a>(+0.8)</a></td>
			<td>88.4 <a>(+2.0)</a></td>
			<td>92.3 <a>(+1.5)</a></td>
			<td>93.1 <a>(+1.4)</a></td>
			<td>73.9 <a>(+1.5)</a></td>
		</tr>
		<tr style="font-weight: bold;">
			<td>Copy-Paste + Patrick</td>
			<td>96.7 <a>(+1.0)</a></td>
			<td>90.5 <a>(+3.1)</a></td>
			<td>92.8 <a>(+2.0)</a></td>
			<td>93.3 <a>(+1.6)</a></td>
			<td>75.1 <a>(+2.7)</a></td>
		</tr>
  	</tbody>
</table>

<a id="1-3"></a>
### Highlight Clipping

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

### <a href="#readme-top">Back to top</a>
