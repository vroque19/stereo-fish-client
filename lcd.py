import os
import sys
import time
import logging
import spidev as SPI
from cam import stream
sys.path.append("..")
# from fisheye import six_dm_video, test
from lib import LCD_2inch
from PIL import Image, ImageDraw, ImageFont

import picamera
from picamera import PiCamera
import cv2
import numpy as np
from datetime import datetime

photo_path = 'static/'
# filename = photo_path + 'fish.png'
# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)


def init_display():
    disp = LCD_2inch.LCD_2inch()
    disp.Init()
    disp.clear()
    disp.bl_DutyCycle(50)
    return disp


def show_welcome(disp):
    image = Image.new("RGB", (disp.height, disp.width), "BLACK")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("./Font/Font00.ttf", 24)
    text = "Welcome to StereoPi\nFish Measurement Tool"
    w, h = draw.textsize(text, font=font)
    x = (disp.height - w) // 2
    y = (disp.width - h) // 2
    draw.text((x, y), text, fill="WHITE", font=font, align="center")
    disp.ShowImage(image)
    time.sleep(3)  # Optional delay before starting stream
    image = Image.new("RGB", (disp.height, disp.width), "BLUE")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("./Font/Font00.ttf", 24)
    text = "1. Place fish in frame\n2. Press button to capture"
    w, h = draw.textsize(text, font=font)
    x = (disp.height - w) // 2
    y = (disp.width - h) // 2
    draw.text((x, y), text, fill="WHITE", font=font, align="center")
    disp.ShowImage(image)
    time.sleep(3)
def stream_cam():
  # Capture frames from the camera
  while True:
      camera.capture(capture, format="bgra", use_video_port=True, resize=(img_width, img_height))
      frame = capture[:, :, :3]  # Extract the RGB channels
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      img = Image.fromarray(frame)
      img = img.resize((320, 240), Image.LANCZOS)
      disp.ShowImage(img)
      # Display the frame in an OpenCV window
      # cv2.imshow('Frame', frame)

      # Check for key press
      key = cv2.waitKey(1) & 0xFF
      if key == ord("q"):
        if (os.path.isdir("./scenes")==False):
            os.makedirs("./scenes")
        cv2.imwrite(filename, frame)
        exit(0)
        break

