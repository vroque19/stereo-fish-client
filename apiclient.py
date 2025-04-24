import requests
import time
import os
import json
import cv2
from dotenv import load_dotenv

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["OMP_NUM_THREADS"] = "2"
os.environ["TF_NUM_INTRAOP_THREADS"] = "2"
os.environ["TF_NUM_INTEROP_THREADS"] = "2"
# Pose point params
color1 = (197, 106, 55)  # blue
color2 = (0, 204, 96)  # green
color3 = (255, 51, 153)  # yellow
color4 = (102, 255, 255)  # purple
# Needed to fix errors, need to figure out why
adj_l = 1.244356955  # Adjustment param length
adj_w = 1.959055118  # Adjustment param width
point_colors = [color1, color2, color3, color4]
pose_pnt_thickness = -1
pose_pnt_circle_radius = 30
load_dotenv()
SECRET = os.environ.get("SECRET_KEY")


def get_secret():
    return os.environ.get("SECRET_KEY")


myfish = "captured_img.jpg"
url = "https://api.vanessa.codes"
root = "/home/ubuntu/repos/stereo-cam-client"
image = root + "static/uploaded_images"
fish = f"{root}/static/fish/{myfish}"


def send_image(filename="FISH1.jpg"):
    start = time.time()
    SECRET = get_secret()
    endpoint = url + "/upload-image/"
    header = {"Authorization": f"Bearer {SECRET}"}
    with open(f"static/fish/{filename}", "rb") as f:
        file = {"file": (filename, f, "image/jpg")}
        print(file)
        response = requests.post(endpoint, headers=header, files=file)
        points = response.text
        data = json.loads(points)
        print(data["dimensions"])
        print("Status Code:", response.status_code)
        label_image(fish, data)
        # print("Response Body:", response.json())
    end = time.time()
    print(f"Seconds: {end-start}")


# FISH1
data1 = {
    "points": [
        [382.2874233722687, 2415.8681497573853],
        [2547.2472988963127, 1624.1200377941132],
        [4102.5273407697678, 1840.6755723953247],
        [2447.4448585510254, 2700.5393295288086],
    ],
    "dimensions": [[103.97687464562867, 53.06312127179164]],
}
# Henry
data2 = {
    "points": [
        [70, 250.5204129219055],
        [440.5932940244675, 250.7044534087181],
        [250.673421382904, 80.4719989299774],
        [250.4725728034973, 420.7164261341095],
    ],
    "dimensions": [[35.972746697759895, 38.79064460737814]],
}


def label_image(image_path, data):
    # Load the image with OpenCV
    print(f"Loading image from: {image_path}")
    image = cv2.imread(image_path)

    # Extract points from data
    points = data["points"]
    dimensions = data["dimensions"][0]  # It's a nested list

    # Unpack points
    # snout_x, snout_y = points[0]
    # tail_fin_x, tail_fin_y = points[1]
    # top_x, top_y = points[2]
    # bottom_x, bottom_y = points[3]

    # Draw the points on stereo images
    i = 0
    for x, y in [points[0], points[1], points[2], points[3]]:
        cv2.circle(
            image,
            (int(x), int(y)),
            radius=pose_pnt_circle_radius,
            color=point_colors[i],
            thickness=pose_pnt_thickness,
        )
        i += 1
    i = 0
    for x, y in [points[0], points[1], points[2], points[3]]:
        cv2.circle(
            image,
            (int(x) + 710, int(y) + 15),
            radius=pose_pnt_circle_radius,
            color=point_colors[i],
            thickness=pose_pnt_thickness,
        )
        i += 1

    length, width = dimensions
    cv2.putText(
        image,
        f"Length: {length:.2f}cm, Width: {width:.2f}cm",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
        cv2.LINE_4,
    )

    # Convert for display or save
    cv2.imwrite("output_labeled.jpg", image)


# send_image()
label_image(fish, data2)
