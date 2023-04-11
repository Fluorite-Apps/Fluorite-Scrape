import cv2
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication()

# Load the video
cap = cv2.VideoCapture('temp/videos/video.mp4')

# Get the first frame of the video
ret, frame = cap.read()

# Convert the frame to a QImage
height, width, channel = frame.shape
bytesPerLine = 3 * width
qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

# Create a QLabel to display the thumbnail
label = QLabel()
label.setPixmap(QPixmap.fromImage(qImg))

# Show the QLabel
label.show()

# Start the event loop
app.exec()
