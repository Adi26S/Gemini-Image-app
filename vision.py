from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
 
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load geminipro model to get responses
model = genai.GenerativeModel('gemini-1.5-flash-latest')
def get_gemini_response(input, image):
    if input!='':
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text


# initialize our streamlit app
st.set_page_config(page_title="Gemini-Image Demo")

st.header('Gemini LLM Application')

input = st.text_input('Input: ',key='input')
submit = st.button('Ask the question')

uploaded_file = st.file_uploader('Choose an image',type=['jpg','jpeg','png'])
image=''

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = 'Uploaded image', use_column_width=True)
    
submit = st.button('Tell me about the image')


# if submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader('The response is')
    st.write(response)