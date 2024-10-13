# GeminiDecode

**GeminiDecode** is a web application that utilizes Gemini Pro AI for multilingual document extraction, specifically focusing on invoices. The application enhances user productivity by allowing users to upload documents and receive information in both text and audio formats.

## Features

- **Document Upload**: Easily upload images of documents in JPEG or PNG format.
- **Information Extraction**: Leverages Gemini Pro AI to extract vital information from invoices.
- **Audio Feedback**: Converts extracted text responses into audio, allowing users to listen to the information.
- **User-Friendly Interface**: An intuitive web interface built with Streamlit.

## Technologies Used

- Python 3.x
- Streamlit
- Google Generative AI (Gemini Pro)
- gTTS (Google Text-to-Speech)
- Pillow (PIL)
- dotenv
- Logging

## Installation

### Prerequisites

- Python 3.x
- Basic knowledge of Python and web application development

### Steps to Set Up

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>


2.Install dependencies:
   pip install -r requirements.txt

Set environment variables:

Create a .env file in the root directory.
Add your Google API key:
makefile
Copy code
GOOGLE_API_KEY=your_google_api_key
Run the application:

bash
Copy code
streamlit run app.py
Usage
Open the application in your web browser.
Upload an image of a document (maximum size: 2 MB).
Click the "Tell me about the document" button.
Wait for the response and listen to the audio feedback for extracted information.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature/YourFeature
Commit your changes:
bash
Copy code
git commit -m "Add your feature"
Push to your branch:
bash
Copy code
git push origin feature/YourFeature
Open a pull request for review.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to the creators of Streamlit and Google Generative AI for their amazing tools and APIs.
css
Copy code

### Instructions to Use

1. Replace `<repository-url>` with the actual URL of your GitHub repository.
2. If applicable, you may want to add a section for acknowledgments or references if you have utilized other resources or libraries.
3. Save this text in a file named `README.md` in the root directory of your project.

Feel free to adjust the content to better fit your project's needs!





