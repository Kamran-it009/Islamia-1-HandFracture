import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image

def detection(image_path):
    # Load the YOLOv8 model
    model = YOLO('best.pt')

    # Read the image (OpenCV reads the image in BGR format)
    frame = cv2.imread(image_path)
    
    # Resize the image if needed
    resized_frame = cv2.resize(frame, (600, 500))

    # Run YOLOv8 inference on the image
    results = model(resized_frame)

    # Visualize the results on the frame (this will draw bounding boxes)
    annotated_frame = results[0].plot()

    # Convert the annotated frame back to RGB format (PIL expects RGB)
    annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    # Convert the annotated frame into a PIL image
    annotated_image = Image.fromarray(annotated_frame_rgb)

    # Resize the annotated image for display
    annotated_image_small = annotated_image.resize((300, 250))  # Set desired dimensions

    return annotated_image_small  # Return the annotated image
