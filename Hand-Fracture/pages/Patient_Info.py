import streamlit as st 
try:
    from detector import detection
    print("detector module is working.")
except ImportError as e:
    print("Error importing detector:", e)
from fpdf import FPDF
import base64
from PIL import Image
from streamlit_option_menu import option_menu

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set page configuration
st.set_page_config(page_title="YOLOv8 Detection App", layout="wide")

# Load the background image and convert it to base64
background_image = get_base64_image("./bgimg.jpg")

page_bg_img = f'''
<style>
        /* Minimalist Sidebar styling */
        [data-testid=stSidebar] {{
            background-color: white;
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
        /* Add margin to move the images down by 50px */
        .image-container img {{
            margin-top: 50px;
        }}
</style>
'''

# Inject custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    # Custom CSS to adjust the logo position
    st.markdown(
        '''
        <style>
            /* Move the logo upwards by 100px */
            img {
                margin-top: -100px;  
            }
        </style>
        ''',
        unsafe_allow_html=True
    )
    # Increase logo width
    st.image("./logo.jpg", width=200, use_column_width=False, output_format="auto", caption="")  # Increase logo width
    selected = option_menu("Main Menu", ["Home", 'Downloads', 'About',  'Contact Us'],
                        icons=['house', 'cloud-arrow-down', 'info-square', 'envelope', ], menu_icon="cast", default_index=0,
                        styles={"nav-link-selected": {"background-color": "#1f7888"}})


# Home Page
if selected == "Home":
    # Custom CSS for background image
    page_bg_img = f'''
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{background_image}");
            background-size: cover;
        }}
        /* Minimalist Sidebar styling */
        [data-testid=stSidebar] {{
            background-color: white;
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
            color: #00000;
        }}
        /* Adjust the form's styling */
        .stForm {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
        }}
        h1 {{
            color: white;
        }}
    </style>
    '''
    # Inject custom CSS
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.title("HF X-Ray")

    # Form for patient information and image upload
    with st.form(key='patient_info_form'):
        st.subheader("Patient Information")
        patient_name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, step=1)
        gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

        # Image Upload
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

        # Detect button
        detect_button = st.form_submit_button("Detect")

        if detect_button:
            # Input Validation for "Detect"
            if not patient_name:
                st.error("Please enter the patient's name.")
            elif age == 0:
                st.error("Please provide the patient's age.")
            elif gender == "Select":
                st.error("Please select the patient's gender.")
            elif uploaded_image is None:
                st.error("Please upload an image.")
            else:
                # Save uploaded image temporarily
                with open("temp_image.jpg", "wb") as f:
                    f.write(uploaded_image.getbuffer())

                # Resize the uploaded image to match the size of the detected image (300x250)
                image = Image.open(uploaded_image)
                resized_uploaded_image = image.resize((300, 250))

                # Columns for inline display of images
                col1, col2 = st.columns(2)

                # Display resized uploaded image in the first column
                with col1:
                    st.markdown('<div class="image-container">', unsafe_allow_html=True)
                    st.image(resized_uploaded_image, caption="Uploaded Image", use_column_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                # Run YOLOv8 detection on the uploaded image and get resized detection result
                detected_image = detection("temp_image.jpg")
                print(type(detected_image))

                # Display the detected image in the second column
                with col2:
                    st.markdown('<div class="image-container">', unsafe_allow_html=True)
                    st.image(detected_image, caption="Detection Results", use_column_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)

        # X-Ray Details input
        xray_details = st.text_area("X-Ray Details")

        # Final Submit button to save patient info
        submit_button = st.form_submit_button("Submit Patient Info")

        if submit_button:
            # Input Validation for "Submit"
            if not patient_name:
                st.error("Please enter the patient's name.")
            elif age == 0:
                st.error("Please provide the patient's age.")
            elif gender == "Select":
                st.error("Please select the patient's gender.")
            elif not xray_details:
                st.error("Please provide X-Ray details.")
            else:
                # Create a PDF to save patient information
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)

                # Title
                pdf.set_font("Arial", size=16, style="B")
                pdf.cell(200, 10, txt="Patient Information", ln=True, align="C")
                pdf.ln(10)

                # Patient Details
                pdf.set_font("Arial", size=12)
                pdf.cell(0, 10, txt=f"Patient Name: {patient_name}", ln=True)
                pdf.cell(0, 10, txt=f"Age: {age}", ln=True)
                pdf.cell(0, 10, txt=f"Gender: {gender}", ln=True)
                pdf.cell(0, 10, txt=f"X-Ray Details: {xray_details}", ln=True)
                pdf.ln(10)

                # Add the detected image to the PDF
                detected_image_path = "detected_image.jpg"
                detected_image.save(detected_image_path)  # Save the detected image to a file

                pdf.image(detected_image_path, x=10, y=None, w=100)  # Add image to PDF (adjust x, y, and w as needed)

                # Save the PDF
                pdf_file_path = f"{patient_name}_info.pdf"
                pdf.output(pdf_file_path)

                # Inform the user and provide a download link
                st.success("Patient information saved successfully!")
                with open(pdf_file_path, "rb") as file:
                    pdf_bytes = file.read()
                    b64 = base64.b64encode(pdf_bytes).decode()
                    href = f'<a href="data:application/pdf;base64,{b64}" download="{pdf_file_path}">Download PDF</a>'
                    st.markdown(href, unsafe_allow_html=True)


elif selected == 'Downloads':
    st.header('Downloads', divider='rainbow')
    st.write(':green[**Dataset:**    **https://www.kaggle.com/code/yousefzidan101/skindiseas/input**]')
    st.write(':green[**Code:**]')

elif selected == 'About':
    st.header('About', divider='rainbow')
    st.write(':blue[**Draikin is a prediagnostic progressive web app that helps to scan and analyse skin pathology.**]')

else:
    st.header('Contact Us', divider='rainbow')
    st.write(':blue[If you have any questions about this Progressive Web App. You can contact us:]')
    st.write(':green[**By email: motubas@gmail.com**]')

st.sidebar.success('Select the above page')









                # # Display success message and provide download link
                # st.success("Patient information saved successfully.")
                # with open(pdf_file_path, "rb") as pdf_file:
                #     pdf_data = pdf_file.read()
                #     st.download_button(
                #         label="Download Patient Info PDF",
                #         data=pdf_data,
                #         file_name=pdf_file_path,
                #         mime="application/pdf"
                #     )



# Sidebar Menu
# with st.sidebar:
#     st.image("./logo.jpg", width=200, use_column_width=False, output_format="auto", caption="")
#     selected = option_menu(
#         "Main Menu", 
#         ["Home", "Downloads", "About", "Contact Us"],
#         icons=['house', 'cloud-arrow-down', 'info-square', 'envelope'], 
#         menu_icon="cast", 
#         default_index=0,
#         styles={"nav-link-selected": {"background-color": "#1f7888"}}
#     )

# # Home Page
# if selected == "Home":
#     st.title("HF X-Ray")

#     # Form for patient information and image upload
#     with st.form(key='patient_info_form'):
#         st.subheader("Patient Information")
#         patient_name = st.text_input("Patient Name")
#         age = st.number_input("Age", min_value=0, step=1)
#         gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])

#         uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
#         xray_details = st.text_area("X-Ray Details")

#         # Detect button
#         detect_button = st.form_submit_button("Detect")
#         submit_button = st.form_submit_button("Submit Patient Info")

#         detected_image = None
#         if detect_button:
#             if not patient_name:
#                 st.error("Please enter the patient's name.")
#             elif age == 0:
#                 st.error("Please provide the patient's age.")
#             elif gender == "Select":
#                 st.error("Please select the patient's gender.")
#             elif uploaded_image is None:
#                 st.error("Please upload an image.")
#             else:
#                 with open("temp_image.jpg", "wb") as f:
#                     f.write(uploaded_image.getbuffer())

#                 detected_image = detection("temp_image.jpg")
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
#                 with col2:
#                     st.image(detected_image, caption="Detection Results", use_column_width=True)

        # if submit_button:
        #     if not patient_name:
        #         st.error("Please enter the patient's name.")
        #     elif age == 0:
        #         st.error("Please provide the patient's age.")
        #     elif gender == "Select":
        #         st.error("Please select the patient's gender.")
        #     elif not xray_details:
        #         st.error("Please provide X-Ray details.")
        #     elif detected_image is None:
        #         st.error("Please run detection before submitting.")
        #     else:
        #         # Generate PDF
        #         pdf = FPDF()
        #         pdf.add_page()
        #         pdf.set_font("Arial", size=12)

        #         # Add patient details to the PDF
        #         pdf.set_font("Arial", size=16, style="B")
        #         pdf.cell(200, 10, txt="Patient Information", ln=True, align="C")
        #         pdf.ln(10)

        #         pdf.set_font("Arial", size=12)
        #         pdf.cell(0, 10, txt=f"Patient Name: {patient_name}", ln=True)
        #         pdf.cell(0, 10, txt=f"Age: {age}", ln=True)
        #         pdf.cell(0, 10, txt=f"Gender: {gender}", ln=True)
        #         pdf.cell(0, 10, txt="X-Ray Details:", ln=True)
        #         pdf.multi_cell(0, 10, xray_details)

        #         # Save the detected image as a temporary file
        #         detected_image_path = "detected_image.jpg"
        #         detected_image.save(detected_image_path)

        #         # Add the detected image to the PDF
        #         pdf.ln(10)
        #         pdf.cell(0, 10, txt="Detection Results:", ln=True)
        #         pdf.image(detected_image_path, x=10, y=pdf.get_y() + 10, w=100)

        #         # Save the PDF
        #         pdf_file_path = f"{patient_name}_info.pdf"
        #         pdf.output(pdf_file_path)

        #         # Provide download button for the PDF
        #         with open(pdf_file_path, "rb") as pdf_file:
        #             pdf_data = pdf_file.read()
        #             st.download_button(
        #                 label="Download Patient Info PDF",
        #                 data=pdf_data,
        #                 file_name=pdf_file_path,
        #                 mime="application/pdf"
        #             )