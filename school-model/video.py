import cv2
import json
from files import extract_frames, get_image_paths
from model import run_model
from phone import call
from database import add_call
from dotenv import load_dotenv

load_dotenv()

# First extract the video and frames, we don't need this if we have the files already in
# video_path = "ex_gun_video2.mp4"
# output_folder = "frames2"
# extract_frames(video_path, output_folder)


predictions = []

# MODIFY THIS LINE MODIFY THIS LINEMODIFY THIS LINE MODIFY THIS LINE MODIFY THIS LINE MODIFY THIS LINE
folder_path = "frames2"
# folder_path = "frames1"

image_paths = get_image_paths(folder_path)

for path in image_paths:
  prediction = run_model(path)
  predictions.append(prediction)



with open("predictions.json", "w") as f:
   json.dump(predictions, f)


with open('predictions.json', 'r') as f:
    # Load the data from the file
    data = json.load(f)
    total_avg = 0.00;
    avg_elements = 0;

    for line in data:
        if (line["predictions"]):
            avg_elements += 1
            total_avg += (line["predictions"][0]["confidence"] * 100)

    avg = total_avg / avg_elements

    if (avg > 50):
        # Call the cops
        print("Calling 911! Confidence: ", avg)
        add_call("Gun Video 2", "Gun detected in videos!")
        call()