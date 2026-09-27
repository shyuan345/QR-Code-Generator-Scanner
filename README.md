# QR Code Generator and Scanner

This project contains the QR code features I worked on: generating QR images, reading QR codes from image files, and scanning with a webcam. The code is in `qr_code.py` and has no graphical interface.

These features came from the [original EECE2140 team project](https://github.com/Rand-Sai/EECE2140-S24-Project), a QR code application built with Zekun Lin. The original repository includes the GUI and lists both of us as contributors.

## Setup

Install [qrcode](https://pypi.org/project/qrcode/) with Pillow support and [OpenCV](https://pypi.org/project/opencv-python/):

```bash
python -m pip install "qrcode[pil]" opencv-python
```

## Generate a QR code

```python
from qr_code import QRCodeGenerator

generator = QRCodeGenerator()
print(generator.generate_qr_code("https://example.com", "example.png"))
```

The second argument is the output filename. If you leave it out, the image is saved as `qr_code.png`. You can also pass a color as the third argument.

## Read a QR code from an image

```python
from qr_code import QRCodeAnalyzer

analyzer = QRCodeAnalyzer()
print(analyzer.image_decode("example.png"))
```

This returns the decoded text, or `No QR code detected` if the image has no readable QR code.

## Scan with a webcam

```python
from qr_code import QRCodeScanner

scanner = QRCodeScanner()
print(scanner.camera_decode())
```

The scanner reads one frame from the default camera and then releases it. It returns the decoded text with a status prefix, `No QR code detected`, or `ERR` if the camera cannot be opened.
