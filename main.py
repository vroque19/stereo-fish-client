import requests
import time
import os
# from dotenv import load_dotenv
from lcd import init_display, show_welcome
from cam import stream
# from apiclient import send_image


def main():
    disp = init_display()
    show_welcome(disp)
    stream(disp)


if __name__ == "__main__":
    main()
