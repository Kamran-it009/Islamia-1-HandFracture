import streamlit as st
import base64



# Page Configuration
st.set_page_config(page_title="Hand Fracture Detection System", layout="wide")

# Function to Encode Image in Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load Background and Logo Images
background_image = get_base64_image("./hands_png.png")  # Ensure this file exists in the same directory
logo_image = get_base64_image("./logo_png.png")  # Ensure this file exists in the same directory

# Custom CSS for Logo, "HFDS" Text, and Layout
page_bg_img = f"""
<style>
    /* Black background for the app */
    .stApp {{
        background-color: black;
        color: white;
    }}
    /* Logo and HFDS Text Styling */
    .logo-section {{
        position: fixed;
        top: 10%;
        left: 3%;
        display: flex;
        align-items: center; /* Align logo and text vertically */
        gap: 0px; /* Space between logo and text */
        z-index: 10;
    }}
    .logo-container img {{
        max-width: 80px; /* Adjust logo size */
        height: 80px;
    }}
    .logo-text {{
        font-size: 1.5rem;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
        margin: 0;
    }}
    /* Main content on the left */
    .main-content {{
        position: fixed;
        top: 30%; /* Adjusted to align text vertically */
        left: 5%; /* Align with the logo */
        display: flex;
        flex-direction: column;
        justify-content: flex-start; /* Align items vertically */
        align-items: flex-start; /* Align items to the left */
        text-align: left; /* Align text to the left */
        color: white;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7);
    }}
    .title-primary {{
        font-size: 2.1rem;
        font-weight: normal;
        margin-bottom: -1.5rem;
        color: white;
    }}
    .title-secondary {{
        font-size: 4rem; /* Adjust font size */
        font-weight: bold;
        margin-bottom: -0.5rem;
        letter-spacing: 0.3em; /* Increase spacing between letters */
        color: white; /* Set text color */
        font-family: 'Futura'; /* Use Futura or fallback to Arial   'Arial', sans-serif */
        text-transform: uppercase; /* Convert text to uppercase */
    }}
    .subtitle {{
        font-size: 1.4rem;
        font-weight: 300;
        margin-bottom: 2rem;
    }}
    .button-container {{
        display: flex;
        flex-direction: column; /* Stack buttons vertically */
        gap: 15px; /* Reduce spacing between buttons */
        margin-top: 1rem;
    }}
    .button {{
        padding: 12px 48px; /* Smaller buttons with adjusted padding */
        font-size: 1rem;
        font-weight: bold;
        color: white !important; /* Force white text */
        background: linear-gradient(90deg, #007B77, #00A8A8); /* Gradient background */
        border: none;
        border-radius: 20px;
        text-decoration: none;
        cursor: pointer;
        transition: background 0.3s ease, transform 0.2s ease;
    }}
    .button:hover {{
        background: linear-gradient(90deg, #005A5A, #007777);
        transform: scale(1.05); /* Slightly enlarge the button on hover */
    }}
    /* Image on the right side */
    .image-container {{
        position: fixed;
        top: 57%;
        right: 7%; /* Adjust this to control horizontal positioning */
        transform: translateY(-50%);
        max-width: 100%; /* Adjusted smaller image size */
        max-height: 100%; /* Maintain proportional scaling */

    }}
</style>
"""

# Inject Custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add Logo and "HFDS" Text at the Top-Left Corner
st.markdown(f"""
    <div class="logo-section">
        <div class="logo-container">
            <img src="data:image/jpeg;base64,{logo_image}" alt="Logo">
        </div>
        <div class="logo-text">HFDS</div>
    </div>
""", unsafe_allow_html=True)

# Main Content on the Left
st.markdown("""
    <div class="main-content">
        <div class="title-primary"> H A N D</div>
        <div class="title-secondary">FRACTURE</div>
        <div class="subtitle">DETECTION  SYSTEM</div>
        <div class="button-container">
            <a href="/Patient_Info" target="_self" class="button">Patient Info</a>
            <a href="#" class="button">Download</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Image on the Right
st.markdown(f"""
    <div class="image-container">
        <img src="data:image/jpeg;base64,{background_image}" alt="Hand Fracture Image" style="width: 100%; height: auto;">
    </div>
""", unsafe_allow_html=True)






#_________________________________________________________________________________#






