import cv2
import os

def extract_frames(video_path, output_folder, frame_interval=69):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Unable to open video file")
        return
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Initialize variables
    frame_count = 0
    success = True
    
    # Loop through frames and save every frame_interval-th frame
    while success:
        success, image = cap.read()
        if frame_count % frame_interval == 0 and success:
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, image)  # Save the frame as an image
        frame_count += 1
    
    # Release the VideoCapture object and close the window
    cap.release()
    cv2.destroyAllWindows()



def get_image_paths(folder_path):
  image_paths = []

  for root, dirs, files in os.walk(folder_path):
      for file in files:
          if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
              image_paths.append(os.path.join(root, file))
  return image_paths
