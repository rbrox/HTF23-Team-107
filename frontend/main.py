import streamlit as st

def main():
    st.title("PDF Uploader")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        st.write("You selected the following file:")
        st.write(uploaded_file)

if __name__ == "__main__":
    main()
