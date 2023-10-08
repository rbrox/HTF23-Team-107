from process import *
import streamlit as st
import os

def main():
    st.title("PDF Uploader")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        st.write("You selected the following file:")
        st.write(uploaded_file)
        if not os.path.exists('./data/New_Sent'):
            os.makedirs('./data/New_Sent')
        file_path = './data/New_Sent/' + uploaded_file.name
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        resume_data = analyze_resume(file_path)
        st.write(resume_data)

    results = analyze_resume()
    st.write(results)

if __name__ == "__main__":
    main()
