# # from detector import detection
# # import streamlit as st

# # image_path = 'images/16.jpg'

# # detection(image_path)


# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# # import streamlit as st
# # from detector import detection

# # # Title of the app
# # st.title('YOLO v8 Image Detection')

# # # Image upload widget
# # uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# # if uploaded_image is not None:
# #     # Convert uploaded image to a temporary path or handle it directly
# #     with open("temp_image.jpg", "wb") as f:
# #         f.write(uploaded_image.getbuffer())
    
# #     # Call the detection function with the temporary image path
# #     detection("temp_image.jpg")


# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # import streamlit as st
# # from detector import detection
# # import os

# # # Set page configuration (optional)
# # st.set_page_config(page_title="YOLOv8 Detection App", layout="wide")

# # # Sidebar Menu
# # with st.sidebar:
# #     st.image("./logo.png", width=150)  # Logo image path set to ./logo.png
# #     st.title("Main Menu")

# #     # Create buttons for each page
# #     if st.button("Home"):
# #         st.session_state.page = "Home"
# #     if st.button("About"):
# #         st.session_state.page = "About"
# #     if st.button("Contact Us"):
# #         st.session_state.page = "Contact Us"

# # # Set default page if not already set
# # if "page" not in st.session_state:
# #     st.session_state.page = "Home"

# # # Home Page
# # if st.session_state.page == "Home":
# #     # Main page title
# #     st.markdown("<h1 style='text-align: left; color: #b30000;'>YOLOv8 Image Detection</h1>", unsafe_allow_html=True)

# #     # Patient Information Form
# #     with st.form(key='patient_info_form'):
# #         st.subheader("Patient Information")
# #         patient_name = st.text_input("Patient Name")
# #         age = st.number_input("Age", min_value=0)
# #         gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
        
# #         # Image Upload
# #         uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# #         # Detect button
# #         detect_button = st.form_submit_button("Detect")

# #         if detect_button:
# #             # Check if temp_image.jpg exists and delete it
# #             if os.path.exists("temp_image.jpg"):
# #                 os.remove("temp_image.jpg")

# #             # Save uploaded image to a temporary file
# #             if uploaded_image is not None:
# #                 with open("temp_image.jpg", "wb") as f:
# #                     f.write(uploaded_image.getbuffer())

# #                 # Display uploaded image in the app (resized)
# #                 st.image(uploaded_image, caption="Uploaded Image", use_column_width=False, width=300)

# #                 # Run YOLOv8 detection on the uploaded image
# #                 detection("temp_image.jpg")

# #                 # Display detected image (will be handled in the detection function)
# #             else:
# #                 st.error("Please upload an image.")

# #         # X-Ray Details input below images
# #         xray_details = st.text_area("X-Ray Details")

# #         # Final Submit button to save patient info
# #         submit_button = st.form_submit_button("Submit Patient Info")

# #         if submit_button:
# #             # Write patient information to a text file
# #             with open("patient_info.txt", "a") as f:
# #                 f.write(f"Patient Name: {patient_name}\n")
# #                 f.write(f"Age: {age}\n")
# #                 f.write(f"Gender: {gender}\n")
# #                 f.write(f"X-Ray Details: {xray_details}\n")
# #                 f.write("\n")  # Blank line between records
# #             st.success("Patient information saved successfully.")

# # # About Page
# # elif st.session_state.page == "About":
# #     st.title("About")
# #     st.write("This application uses YOLOv8 for object detection in images.")
# #     st.write("You can upload an image, and the model will detect and annotate the objects present in it.")

# # # Contact Us Page
# # elif st.session_state.page == "Contact Us":
# #     st.title("Contact Us")
# #     st.write("For inquiries, please contact us at:")
# #     st.write("Email: info@example.com")
# #     st.write("Phone: +123456789")

# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# # import streamlit as st
# # from detector import detection
# # import os

# # # Set page configuration (optional)
# # st.set_page_config(page_title="YOLOv8 Detection App", layout="wide")

# # # Sidebar Menu
# # with st.sidebar:
# #     st.image("./logo.png", width=150)  # Logo image path set to ./logo.png
# #     st.title("Main Menu")

# #     # Create buttons for each page
# #     if st.button("Home"):
# #         st.session_state.page = "Home"
# #     if st.button("About"):
# #         st.session_state.page = "About"
# #     if st.button("Contact Us"):
# #         st.session_state.page = "Contact Us"

# # # Set default page if not already set
# # if "page" not in st.session_state:
# #     st.session_state.page = "Home"

# # # Home Page
# # if st.session_state.page == "Home":
# #     # Main page title
# #     st.markdown("<h1 style='text-align: left; color: #b30000;'>YOLOv8 Image Detection</h1>", unsafe_allow_html=True)

# #     # Patient Information Form
# #     with st.form(key='patient_info_form'):
# #         st.subheader("Patient Information")
# #         patient_name = st.text_input("Patient Name")
# #         age = st.number_input("Age", min_value=0)
# #         gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
        
# #         # Image Upload
# #         uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# #         # Detect button
# #         detect_button = st.form_submit_button("Detect")

# #         if detect_button:
# #             # Check if temp_image.jpg exists and delete it
# #             if os.path.exists("temp_image.jpg"):
# #                 os.remove("temp_image.jpg")

# #             # Save uploaded image to a temporary file
# #             if uploaded_image is not None:
# #                 with open("temp_image.jpg", "wb") as f:
# #                     f.write(uploaded_image.getbuffer())

# #                 # Display uploaded image in the app (resized)
# #                 st.image(uploaded_image, caption="Uploaded Image", use_column_width=False, width=300)

# #                 # Run YOLOv8 detection on the uploaded image
# #                 detection("temp_image.jpg")
# #             else:
# #                 st.error("Please upload an image.")

# #         # X-Ray Details input below images
# #         xray_details = st.text_area("X-Ray Details")

# #         # Final Submit button to save patient info
# #         submit_button = st.form_submit_button("Submit Patient Info")

# #         if submit_button:
# #             # Write patient information to a text file
# #             with open("patient_info.txt", "a") as f:
# #                 f.write(f"Patient Name: {patient_name}\n")
# #                 f.write(f"Age: {age}\n")
# #                 f.write(f"Gender: {gender}\n")
# #                 f.write(f"X-Ray Details: {xray_details}\n")
# #                 f.write("\n")  # Blank line between records
# #             st.success("Patient information saved successfully.")

# # # About Page
# # elif st.session_state.page == "About":
# #     st.title("About")
# #     st.write("This application uses YOLOv8 for object detection in images.")
# #     st.write("You can upload an image, and the model will detect and annotate the objects present in it.")

# # # Contact Us Page
# # elif st.session_state.page == "Contact Us":
# #     st.title("Contact Us")
# #     st.write("For inquiries, please contact us at:")
# #     st.write("Email: info@example.com")
# #     st.write("Phone: +123456789")



# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # import streamlit as st
# # from detector import detection
# # import os
# # import base64

# # # Function to encode image to base64
# # def get_base64_image(image_path):
# #     with open(image_path, "rb") as img_file:
# #         return base64.b64encode(img_file.read()).decode()

# # # Set page configuration (optional)
# # st.set_page_config(page_title="YOLOv8 Detection App", layout="wide")

# # # Load the background image and convert it to base64
# # background_image = get_base64_image("./bgimg.jpg")

# # # Custom CSS for background image and sidebar styling
# # page_bg_img = f'''
# # <style>
# #     /* Set the background image for the main page */
# #     .stApp {{
# #         background-image: url("data:image/jpg;base64,{background_image}");
# #         background-size: cover;
# #     }}

# #     /* Make sidebar background dark blue */
# #     .css-1d391kg {{
# #         background-color: #003366 !important;  /* Dark blue */
# #     }}

# #     /* Sidebar title and text color */
# #     .css-18ni7ap h1, .css-18ni7ap h2, .css-18ni7ap h3 {{
# #         color: white !important;
# #     }}

# #     /* Adjust the form's styling */
# #     .stForm {{
# #         background-color: rgba(255, 255, 255, 0.8); /* Make form background semi-transparent */
# #         padding: 20px;
# #         border-radius: 10px;
# #         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
# #     }}
# # </style>
# # '''

# # # Inject custom CSS
# # st.markdown(page_bg_img, unsafe_allow_html=True)

# # # Sidebar Menu
# # with st.sidebar:
# #     st.image("./logo.jpg", width=150)  # Logo image path set to ./logo.png
# #     st.title("Main Menu")

# #     # Create buttons for each page
# #     if st.button("Home"):
# #         st.session_state.page = "Home"
# #     if st.button("About"):
# #         st.session_state.page = "About"
# #     if st.button("Contact Us"):
# #         st.session_state.page = "Contact Us"

# # # Set default page if not already set
# # if "page" not in st.session_state:
# #     st.session_state.page = "Home"

# # # Home Page
# # if st.session_state.page == "Home":
# #     # Main page title
# #     st.markdown("<h1 style='text-align: left; color: #b30000;'>YOLOv8 Image Detection</h1>", unsafe_allow_html=True)

# #     # Patient Information Form
# #     with st.form(key='patient_info_form'):
# #         st.subheader("Patient Information")
# #         patient_name = st.text_input("Patient Name")
# #         age = st.number_input("Age", min_value=0)
# #         gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
        
# #         # Image Upload
# #         uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# #         # Detect button
# #         detect_button = st.form_submit_button("Detect")

# #         if detect_button:
# #             # Check if temp_image.jpg exists and delete it
# #             if os.path.exists("temp_image.jpg"):
# #                 os.remove("temp_image.jpg")

# #             # Save uploaded image to a temporary file
# #             if uploaded_image is not None:
# #                 with open("temp_image.jpg", "wb") as f:
# #                     f.write(uploaded_image.getbuffer())

# #                 # Display uploaded image in the app (resized)
# #                 st.image(uploaded_image, caption="Uploaded Image", use_column_width=False, width=300)

# #                 # Run YOLOv8 detection on the uploaded image
# #                 detected_image = detection("temp_image.jpg")

# #                 # Display the detected image
# #                 st.image(detected_image, caption="Detection Results", use_column_width=False)

# #             else:
# #                 st.error("Please upload an image.")

# #         # X-Ray Details input below images
# #         xray_details = st.text_area("X-Ray Details")

# #         # Final Submit button to save patient info
# #         submit_button = st.form_submit_button("Submit Patient Info")

# #         if submit_button:
# #             # Write patient information to a text file
# #             with open("patient_info.txt", "a") as f:
# #                 f.write(f"Patient Name: {patient_name}\n")
# #                 f.write(f"Age: {age}\n")
# #                 f.write(f"Gender: {gender}\n")
# #                 f.write(f"X-Ray Details: {xray_details}\n")
# #                 f.write("\n")  # Blank line between records
# #             st.success("Patient information saved successfully.")

# # # About Page
# # elif st.session_state.page == "About":
# #     st.title("About")
# #     st.write("This application uses YOLOv8 for object detection in images.")
# #     st.write("You can upload an image, and the model will detect and annotate the objects present in it.")

# # # Contact Us Page
# # elif st.session_state.page == "Contact Us":
# #     st.title("Contact Us")
# #     st.write("For inquiries, please contact us at:")
# #     st.write("Email: info@example.com")
# #     st.write("Phone: +123456789")

# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# # import streamlit as st
# # from detector import detection
# # import os
# # import base64

# # # Function to encode image to base64
# # def get_base64_image(image_path):
# #     with open(image_path, "rb") as img_file:
# #         return base64.b64encode(img_file.read()).decode()

# # # Set page configuration (optional)
# # st.set_page_config(page_title="YOLOv8 Detection App", layout="wide")

# # # Load the background image and convert it to base64
# # background_image = get_base64_image("./bgimg.jpg")

# # # Custom CSS for background image and sidebar styling
# # page_bg_img = f'''
# # <style>
# #     /* Set the background image for the main page */
# #     .stApp {{
# #         background-image: url("data:image/jpg;base64,{background_image}");
# #         background-size: cover;
# #     }}

# #     /* Make sidebar background dark blue */
# #     [data-testid=stSidebar] {{
# #         background-color: #003366 !important;  /* Dark blue */
# #     }}

# #     /* Sidebar title and text color */
# #     .css-18ni7ap h1, .css-18ni7ap h2, .css-18ni7ap h3 {{
# #         color: white !important;
# #     }}

# #     /* Set header text color to black */
# #     [data-testid=stHeader] {{
# #         color: black !important;
# #     }}

# #     /* Adjust the form's styling */
# #     .stForm {{
# #         background-color: rgba(255, 255, 255, 0.8); /* Make form background semi-transparent */
# #         padding: 20px;
# #         border-radius: 10px;
# #         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
# #     }}
# # </style>
# # '''

# # # Inject custom CSS
# # st.markdown(page_bg_img, unsafe_allow_html=True)

# # # Sidebar Menu
# # with st.sidebar:
# #     st.image("./logo.jpg", width=150)  # Logo image path set to ./logo.png
# #     st.title("Main Menu")

# #     # Create buttons for each page
# #     if st.button("Home"):
# #         st.session_state.page = "Home"
# #     if st.button("About"):
# #         st.session_state.page = "About"
# #     if st.button("Contact Us"):
# #         st.session_state.page = "Contact Us"

# # # Set default page if not already set
# # if "page" not in st.session_state:
# #     st.session_state.page = "Home"

# # # Home Page
# # if st.session_state.page == "Home":
# #     # Main page title
# #     st.markdown("<h1 style='text-align: left;'>YOLOv8 Image Detection</h1>", unsafe_allow_html=True)

# #     # Patient Information Form
# #     with st.form(key='patient_info_form'):
# #         st.subheader("Patient Information")
# #         patient_name = st.text_input("Patient Name")
# #         age = st.number_input("Age", min_value=0)
# #         gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

# #         # Image Upload
# #         uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# #         # Detect button
# #         detect_button = st.form_submit_button("Detect")

# #         if detect_button:
# #             # Check if temp_image.jpg exists and delete it
# #             if os.path.exists("temp_image.jpg"):
# #                 os.remove("temp_image.jpg")

# #             # Save uploaded image to a temporary file
# #             if uploaded_image is not None:
# #                 with open("temp_image.jpg", "wb") as f:
# #                     f.write(uploaded_image.getbuffer())

# #                 # Display uploaded image in the app (resized)
# #                 st.image(uploaded_image, caption="Uploaded Image", use_column_width=False, width=300)

# #                 # Run YOLOv8 detection on the uploaded image
# #                 detected_image = detection("temp_image.jpg")

# #                 # Display the detected image
# #                 st.image(detected_image, caption="Detection Results", use_column_width=False)

# #             else:
# #                 st.error("Please upload an image.")

# #         # X-Ray Details input below images
# #         xray_details = st.text_area("X-Ray Details")

# #         # Final Submit button to save patient info
# #         submit_button = st.form_submit_button("Submit Patient Info")

# #         if submit_button:
# #             # Write patient information to a text file
# #             with open("patient_info.txt", "a") as f:
# #                 f.write(f"Patient Name: {patient_name}\n")
# #                 f.write(f"Age: {age}\n")
# #                 f.write(f"Gender: {gender}\n")
# #                 f.write(f"X-Ray Details: {xray_details}\n")
# #                 f.write("\n")  # Blank line between records
# #             st.success("Patient information saved successfully.")

# # # About Page
# # elif st.session_state.page == "About":
# #     st.title("About")
# #     st.write("This application uses YOLOv8 for object detection in images.")
# #     st.write("You can upload an image, and the model will detect and annotate the objects present in it.")

# # # Contact Us Page
# # elif st.session_state.page == "Contact Us":
# #     st.title("Contact Us")
# #     st.write("For inquiries, please contact us at:")
# #     st.write("Email: info@example.com")
# #     st.write("Phone: +123456789")


# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


import streamlit as st
from detector import detection
import os
import base64

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set page configuration
st.set_page_config(page_title="YOLOv8 Detection App", layout="wide")

# Load the background image and convert it to base64
background_image = get_base64_image("./bgimg.jpg")

# Custom CSS for background image and sidebar styling
page_bg_img = f'''
<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{background_image}");
        background-size: cover;
    }}
    /* Minimalist Sidebar styling */
    [data-testid=stSidebar] {{
        background-color: #00008B !important;
        padding: 20px;
    }}
    /* Sidebar link styling */
    .sidebar-link {{
        display: block;
        padding: 10px 0;
        font-size: 18px;
        color: #333;
        text-decoration: none;
    }}
    .sidebar-link:hover {{
        color: #ff0000;
    }}
    /* Adjust the form's styling */
    .stForm {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
    }}
    h1 {{
        color: lightgray;
    }}
</style>
'''

# Inject custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    st.image("./logo.jpg", width=150)  # Logo image path
    if st.button("Home"):
        st.session_state.page = "Home"
    if st.button("About"):
        st.session_state.page = "About"
    if st.button("Contact Us"):
        st.session_state.page = "Contact Us"

# Initialize the session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Home Page
if st.session_state.page == "Home":
    st.title("YOLOv8 Image Detection")

    # Form for patient information and image upload
    with st.form(key='patient_info_form'):
        st.subheader("Patient Information")
        patient_name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0)
        gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

        # Image Upload
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

        # Detect button
        detect_button = st.form_submit_button("Detect")

        if detect_button:
            if uploaded_image is not None:
                with open("temp_image.jpg", "wb") as f:
                    f.write(uploaded_image.getbuffer())

                # Display uploaded image
                st.image(uploaded_image, caption="Uploaded Image", use_column_width=False, width=300)

                # Run YOLOv8 detection on the uploaded image
                detected_image = detection("temp_image.jpg")

                # Display the detected image
                st.image(detected_image, caption="Detection Results", use_column_width=False)
            else:
                st.error("Please upload an image.")

        # X-Ray Details input below images
        xray_details = st.text_area("X-Ray Details")

        # Final Submit button to save patient info
        submit_button = st.form_submit_button("Submit Patient Info")

        if submit_button:
            # Write patient information to a text file
            with open("patient_info.txt", "a") as f:
                f.write(f"Patient Name: {patient_name}\n")
                f.write(f"Age: {age}\n")
                f.write(f"Gender: {gender}\n")
                f.write(f"X-Ray Details: {xray_details}\n\n")
            st.success("Patient information saved successfully.")

# About Page
elif st.session_state.page == "About":
    st.title("About")
    st.write("This application uses YOLOv8 for object detection in images.")
    st.write("You can upload an image, and the model will detect and annotate the objects present in it.")

# Contact Us Page
elif st.session_state.page == "Contact Us":
    st.title("Contact Us")
    st.write("For inquiries, please contact us at:")
    st.write("Email: info@example.com")
    st.write("Phone: +123456789")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# import io
# import numpy as np
# from PIL import Image
# import streamlit as st
# # from inference import predict
# from streamlit_option_menu import option_menu

# st.set_page_config(
#     page_title='Skin Disease Detection',
#     page_icon=":stethoscope:"
# )

# # 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Downloads', 'About',  'Contact Us'],
#                         icons=['house', 'cloud-arrow-down', 'info-square', 'envelope', ], menu_icon="cast", default_index=0,
#                         styles={"nav-link-selected": {"background-color": "green"}})
# if selected == 'Home':
#     # 2. Heading
#     st.header('Skin Disease :blue :stethoscope:', divider='rainbow')
#     # 3. Uploading file
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
#     click = None
#     if uploaded_file is not None:
#         st.image(uploaded_file, width=250)
#         image_bytes = uploaded_file.read()
#         image = Image.open(io.BytesIO(image_bytes))
#         image_array = np.array(image)
#         # image_array = image_array * 255.0
#         # image_array = np.resize(image_array, (224, 224))
#         # label = predict(image_array)
#         st.write('Image uploaded successfully..')

#         # Create a centered button
#         click = st.button(":white[Predict]", type='primary', disabled=False)
#     else:
#         st.button(":white[Predict]", type= 'primary', disabled=True)
#     if click:
#         st.subheader(f':green[Disease :] {'label'}')

# elif selected == 'Downloads':
#     st.header('Downloads', divider='rainbow')
#     st.write(':green[**Dataset:**    **https://www.kaggle.com/code/yousefzidan101/skindiseas/input**]')
#     st.write(':green[**Code:**]')
# elif selected == 'About':
#     st.header('About', divider='rainbow')
#     st.write(':blue[**Draikin is a prediagnostic progressive web app that helps to scan and analyse skin pathology.**]')
# else:
#     st.header('Contact Us', divider='rainbow')
#     st.write(':blue[If you have any questions about this Progressive Web App. You can contact us:]')
#     st.write(':green[**By email: motubas@gmail.com**]')
# st.sidebar.success('Select the above page')
