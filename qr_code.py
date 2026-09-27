import qrcode
import cv2


class QRCodeGenerator:
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    def generate_qr_code(self, url, name=None, color="black"):
        self.qr.clear()
        self.qr.add_data(url)
        self.qr.make(fit=True)

        img = self.qr.make_image(fill_color=color, back_color="white")
        img_name = f"{name}" if name else "qr_code.png"
        img.save(img_name)
        return f"QR code generated successfully as {img_name}"


class QRCodeAnalyzer:
    def __init__(self):
        self.detector = cv2.QRCodeDetector()

    def image_decode(self, image):
        img = cv2.imread(image)
        data, bbox, _ = self.detector.detectAndDecode(img)
        if bbox is not None and data:
            return data
        else:
            return "No QR code detected"


class QRCodeScanner(QRCodeAnalyzer):
    def __init__(self):
        super().__init__()
        self.cap = None

    def camera_decode(self):
        if not self.cap:
            self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            return "ERR"

        _, img = self.cap.read()
        data, bbox, _ = self.detector.detectAndDecode(img)
        if bbox is not None and data:
            result = "[+] QR code detected: data: " + data
        else:
            result = "No QR code detected"

        self.cap.release()
        self.cap = None
        cv2.destroyAllWindows()
        return result
