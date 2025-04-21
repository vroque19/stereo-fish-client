import requests
import time
import os
from dotenv import load_dotenv

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["OMP_NUM_THREADS"] = "2"
os.environ["TF_NUM_INTRAOP_THREADS"] = "2"
os.environ["TF_NUM_INTEROP_THREADS"] = "2"

load_dotenv()
SECRET = os.environ.get("SECRET_KEY")


def get_secret():
    return os.environ.get("SECRET_KEY")


url = "https://api.vanessa.codes"


def send_image(filename="FISH1.jpg"):
    start = time.time()
    SECRET = get_secret()
    endpoint = url + "/upload-image/"
    header = {"Authorization": f"Bearer {SECRET}"}
    with open(f"static/fish/{filename}", "rb") as f:
        file = {"file": (filename, f, "image/jpg")}
        response = requests.post(endpoint, headers=header, files=file)
        print(response.text)
        print("Status Code:", response.status_code)
        # print("Response Body:", response.json())
    end = time.time()
    print(f"Seconds: {end-start}")


send_image()
