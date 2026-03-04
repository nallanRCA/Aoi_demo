# Portable AOI Prototype

This project demonstrates a simple Automated Optical Inspection (AOI) system using Python and OpenCV.

The system compares a golden reference PCB image with a test PCB image to detect defects such as solder bridges, missing solder, or other anomalies.

## Features
- Golden board comparison
- Edge detection using OpenCV
- Difference analysis between boards
- Automatic defect highlighting
- Bounding box around detected defects

## Technology Used
- Python
- OpenCV
- NumPy

## Application
This prototype demonstrates how a low-cost AOI system can be developed for PCB inspection after wave soldering.

## How It Works
1. Load a golden reference PCB image.
2. Load a test PCB image.
3. Convert both images to grayscale.
4. Detect edges and compute differences.
5. Highlight potential defects on the test board.

## Future Improvements
- Automatic PCB alignment
- Real-time camera inspection
- Solder bridge detection optimization
- Zoom inspection
- Pass / Fail classification
