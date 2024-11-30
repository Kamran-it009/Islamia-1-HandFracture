# import cv2
# from ultralytics import YOLO


# '''Detection on single image'''

# def detection(image_path):

#     # Load the YOLOv8 model
#     model = YOLO('best.pt')

#     # Read the image
#     frame = cv2.imread(image_path)

#     # Run YOLOv8 inference on the image
#     resized_frame = cv2.resize(frame, (600, 500))
#     results = model(resized_frame)

#     # Visualize the results on the frame
#     annotated_frame = results[0].plot()

#     # Display the annotated frame
#     cv2.imshow("YOLOv8 Inference", annotated_frame)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# import cv2
# import numpy as np
# from ultralytics import YOLO
# import streamlit as st
# from PIL import Image

# '''Detection on single image'''

# def detection(image_path):

#     # Load the YOLOv8 model
#     model = YOLO('best.pt')

#     # Read the image (OpenCV reads the image in BGR format)
#     frame = cv2.imread(image_path)
    
#     # Resize the image if needed
#     resized_frame = cv2.resize(frame, (600, 500))

#     # Run YOLOv8 inference on the image
#     results = model(resized_frame)

#     # Visualize the results on the frame (this will draw bounding boxes)
#     annotated_frame = results[0].plot()

#     # Convert the annotated frame back to RGB format (PIL expects RGB)
#     annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

#     # Convert the annotated frame into a PIL image
#     annotated_image = Image.fromarray(annotated_frame_rgb)

#     # Use Streamlit to display the original and annotated images
#     st.image(annotated_image, caption="Detection Results", use_column_width=True)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# import cv2
# import numpy as np
# from ultralytics import YOLO
# import streamlit as st
# from PIL import Image

# '''Detection on single image'''

# def detection(image_path):
#     # Load the YOLOv8 model
#     model = YOLO('best.pt')

#     # Read the image (OpenCV reads the image in BGR format)
#     frame = cv2.imread(image_path)
    
#     # Resize the image if needed
#     resized_frame = cv2.resize(frame, (600, 500))

#     # Run YOLOv8 inference on the image
#     results = model(resized_frame)

#     # Visualize the results on the frame (this will draw bounding boxes)
#     annotated_frame = results[0].plot()

#     # Convert the annotated frame back to RGB format (PIL expects RGB)
#     annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

#     # Convert the annotated frame into a PIL image
#     annotated_image = Image.fromarray(annotated_frame_rgb)

#     # Resize the annotated image for display (small size)
#     annotated_image_small = annotated_image.resize((300, 250))  # Set desired dimensions

#     # Use Streamlit to display the original image (optional)
#     # st.image(resized_frame, caption="Uploaded Image", use_column_width=False, width=300)

#     # Use Streamlit to display the annotated (detected) image
#     st.image(annotated_image_small, caption="Detection Results", use_column_width=False)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


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
