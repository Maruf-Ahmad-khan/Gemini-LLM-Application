import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

class GeminiChatbotApp:
    
    def __init__(self):
        
        # Load environment variables
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.image = None
        self.response = None
        self.model = genai.GenerativeModel('gemini-1.5-flash')


    def get_gemini_response(self, user_input, uploaded_image):
        if user_input:
            self.response = self.model.generate_content([user_input, uploaded_image])
        else:
            self.response = self.model.generate_content(uploaded_image)
        return self.response.text


    def render_header(self):
        st.set_page_config(page_title="Gemini Image")
        col = st.columns([1])[0]  
        with col:
            st.image(
                r"C:\Users\mk744\OneDrive - Poornima University\Desktop\LLM\robot3.jpg", 
                caption="Hello, I am a Gemini bot", 
                width=250
            )



        

    def render_input_section(self):
        user_input = st.text_input("Ask anything, I am here to assist you.", key="input")
        uploaded_file = st.file_uploader("Upload the image ...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            self.image = Image.open(uploaded_file)
            st.image(self.image, caption="Uploaded Image.", use_container_width=True)

        return user_input


    def render_output_section(self, user_input):
        
        if st.button("Tell me about the image"):
            if user_input or self.image:
                response_text = self.get_gemini_response(user_input, self.image)
                st.subheader("The Response is:")
                st.write(response_text)
                
            else:
                st.warning("Please provide input or upload an image.")


    def run(self):
        self.render_header()
        user_input = self.render_input_section()
        self.render_output_section(user_input)


# Run the application
if __name__ == "__main__":
    app = GeminiChatbotApp()
    app.run()
