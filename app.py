from gtts import gTTS
import os
import tempfile
import logging
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import io
import google.generativeai as genai

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini Pro API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the input prompt
input_prompt = """
You are an expert in understanding invoices.
We will upload an image as an invoice, and you will have to answer any questions based on the uploaded invoice image.
"""

# Function to create a Blob from the image
def create_blob(image):
    """Create a Blob object from the PIL image."""
    img_byte_arr = io.BytesIO()  # Create a bytes buffer
    image.save(img_byte_arr, format='PNG')  # Save the image in PNG format to the buffer
    blob_data = img_byte_arr.getvalue()  # Get the byte data from the buffer
    return {
        'mime_type': 'image/png',
        'data': blob_data
    }

# Function to get response from Gemini Pro Vision API
def get_gemini_response(input_text, image, prompt):
    logging.info("Starting response generation...")
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Create a Blob from the image
    image_blob = create_blob(image)
    logging.info("Image converted to Blob.")

    # Generate content
    response = model.generate_content([input_text, image_blob, prompt])
    logging.info("Response generated.")
    return response.text
def text_to_audio(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
        tts.save(f"{tmp_file.name}.mp3")
        return tmp_file.name + ".mp3"


# Initialize Streamlit app
st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extraction by Gemini Pro")
st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")

# Explanation text
text = """
Utilizing Gemini Pro AI, this project effortlessly extracts vital information from diverse multilingual documents,
transcending language barriers with precision and efficiency for enhanced productivity and decision-making.
"""
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

# File uploader for the document image
uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    if uploaded_file.size > 2 * 1024 * 1024:  # Limit to 2 MB
        st.error("File size should be less than 2 MB.")
    else:
        image = Image.open(uploaded_file)  # Open the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Button to trigger document extraction
        if st.button("Tell me about the document"):
            with st.spinner("Processing..."):
                try:
                    # Call the API and get the response
                    response_text = get_gemini_response(input_prompt, image, "Extract information from this invoice.")
                    st.subheader("The response is:")
                    st.write(response_text)
                    audio_file = text_to_audio(response_text)
                    st.audio(audio_file, format="audio/mp3")
                except Exception as e:
                    st.error(f"An error occurred: {e}")