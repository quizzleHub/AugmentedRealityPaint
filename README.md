# Augmented Reality Paint
With AugmentedRealityPaint you can draw via object tracking. Simply hold an object into the camera, calibrate and start drawing by pressing space.

### hier beispielfoto einfügen

## Requirements
- Python3
- Webcam
- Win10 or linux or macOS

## Installation
Clone the project and navigate into project folder. Install the dependencies. Run.
```zsh
git clone https://github.com/quizzleHub/AugmentedRealityPaint.git
cd AugmentedRealityPaint
pip3 install -r requirements.txt
cd src
python3 Start.py
```
## Use
ARP prompts you at startup to calibrate the object you want to track. Once you calibrated, you can start drawing by holding space. 
#### Features:
- Change stroke color, width, pattern, linestyle
- Clear entire screen or erase single strokes
- Save and reopen drawings
- Export image as jpg (with or without camera background)

### Tipps
- Your environment should be well lit. 
- The color of the tracked object should be bright/vivid and distinct to your camera background. Avoid using skin tones.
