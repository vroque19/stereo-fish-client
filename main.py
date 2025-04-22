import requests
import time
import os
import sys
import termios
import tty
import select
# from dotenv import load_dotenv
from lcd import init_display, show_welcome
from cam import stream
# from apiclient import send_image


def main():
    disp = init_display()
    show_welcome(disp)
    # Setup terminal to read input without Enter
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(sys.stdin.fileno())
    try:
        stream(disp, fd, old_settings)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


if __name__ == "__main__":
    main()
