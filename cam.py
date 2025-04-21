import numpy as np
import cv2
import os
from picamera import PiCamera
from PIL import Image
# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0
device = 0
filename = './static/photo.png'

def stream(disp):
    print("live streaming")
    # Camera settings
    cam_width = 1280
    cam_height = 480
    scale_ratio = 1
    cam_width = int((cam_width + 31) / 32) * 32
    cam_height = int((cam_height + 15) / 16) * 16

    # Buffer for captured image settings
    img_width = int(cam_width * scale_ratio)
    img_height = int(cam_height * scale_ratio)
    capture = np.zeros((img_height, img_width, 4), dtype=np.uint8)

    # Initialize the camera
    camera = PiCamera(stereo_mode='side-by-side', stereo_decimate=False)
    camera.resolution = (cam_width, cam_height)
    camera.framerate = 10

    while True:
        camera.capture(capture, format="bgra", use_video_port=True, resize=(img_width, img_height))
        frame = capture[:, :, :3]  # Extract RGB

        img = Image.fromarray(frame)
        img = img.resize((320, 240), Image.LANCZOS)
        disp.ShowImage(img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            if not os.path.isdir("./static"):
                os.makedirs("./static")
            cv2.imwrite(filename, frame)
            break
