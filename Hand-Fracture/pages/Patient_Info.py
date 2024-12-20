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
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
        detect_button = st.form_submit_button("Detect")

        detected_image_path = "detected_image.jpg"

        if detect_button:
            if not patient_name:
                st.error("Please enter the patient's name.")
            elif age == 0:
                st.error("Please provide the patient's age.")
            elif gender == "Select":
                st.error("Please select the patient's gender.")
            elif uploaded_image is None:
                st.error("Please upload an image.")
            else:
                with open("temp_image.jpg", "wb") as f:
                    f.write(uploaded_image.getbuffer())

                image = Image.open(uploaded_image)
                resized_uploaded_image = image.resize((300, 250))
                col1, col2 = st.columns(2)

                with col1:
                    st.image(resized_uploaded_image, caption="Uploaded Image", use_column_width=True)

                detected_image = detection("temp_image.jpg")
                detected_image.save(detected_image_path)  # Save detected image to file

                with col2:
                    st.image(detected_image, caption="Detection Results", use_column_width=True)

        xray_details = st.text_area("X-Ray Details")
        submit_button = st.form_submit_button("Submit Patient Info")

        if submit_button:
            if not patient_name:
                st.error("Please enter the patient's name.")
            elif age == 0:
                st.error("Please provide the patient's age.")
            elif gender == "Select":
                st.error("Please select the patient's gender.")
            elif not xray_details:
                st.error("Please provide X-Ray details.")
            else:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.set_font("Arial", size=16, style="B")
                pdf.cell(200, 10, txt="Patient Information", ln=True, align="C")
                pdf.ln(10)

                pdf.set_font("Arial", size=12)
                pdf.cell(0, 10, txt=f"Patient Name: {patient_name}", ln=True)
                pdf.cell(0, 10, txt=f"Age: {age}", ln=True)
                pdf.cell(0, 10, txt=f"Gender: {gender}", ln=True)
                pdf.cell(0, 10, txt=f"X-Ray Details: {xray_details}", ln=True)
                pdf.ln(10)

                if detected_image_path:
                    pdf.image(detected_image_path, x=10, y=None, w=100)

                pdf_file_path = f"{patient_name}_info.pdf"
                pdf.output(pdf_file_path)

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


