import os
import sys
import time
import logging
import spidev as SPI

sys.path.append("..")
from lib import LCD_2inch
from PIL import Image, ImageDraw, ImageFont

import picamera
from picamera import PiCamera
import cv2
import numpy as np
from datetime import datetime
