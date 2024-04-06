import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from model import run_model
from phone import call
from database import add_call
import base64
from dotenv import load_dotenv

load_dotenv()


# Variables
execute_frames = 50

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera.")
    exit()

# Create a figure and axes
fig, ax = plt.subplots()

# Counter to keep track of frames
frame_count = 0

# Function to update the plot with a new frame
def update(frame):
    global frame_count
    ret, frame = cap.read()  # Read a frame
    if not ret:
        print("Error: Couldn't read frame.")
        return
    ax.clear()
    ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # Display the frame

    # Perform something every ten frames
    frame_count += 1
    if frame_count % execute_frames == 0:
        cv2.imwrite(f'video_frames/frame_{frame_count}.jpg', frame)
        data = run_model(f'video_frames/frame_{frame_count}.jpg')

        print(data)

        avg = 0

        if data["predictions"]:
            avg += data["predictions"][0]["confidence"] * 100

        if avg > 40:
            # Call the cops
            print("Calling 911! Confidence:", avg)
            # Convert frame to base64 for storing in MongoDB
            with open(f'video_frames/frame_{frame_count}.jpg', 'rb') as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
            add_call(img_base64, "Gun detected in live streams!")
            call()

# Create an animation
ani = FuncAnimation(fig, update, interval=50)

# Show the plot
plt.show()

# Release the VideoCapture object
cap.release()