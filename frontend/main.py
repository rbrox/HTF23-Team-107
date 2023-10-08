from process import *
import streamlit as st
import os

def main():
    st.title("Resume Uploader")
    job_roles = ['Data Science', 'HR', 'Advocate', 'Arts', 'Web Designing', 'Mechanical Engineer', 'Sales', 'Health and fitness', 'Civil Engineer', 'Java Developer', 'Business Analyst', 'SAP Developer', 'Automation Testing', 'Electrical Engineering', 'Operations Manager', 'Python Developer', 'DevOps Engineer', 'Network Security Engineer', 'PMO', 'Database', 'Hadoop', 'ETL Developer', 'DotNet Developer', 'Blockchain', 'Testing']
    job_title = st.selectbox(" Select the job you're applying for", job_roles)
    
    
    # github
    github_handle = st.text_input("# Enter your GitHub handle")
    try:
        info = assess_github_coding_proficiency(github_handle)
        
        st.write(info)
    except Exception as e:
        st.write(":red[User not found]")
    
    # codeforces
    codeforces_handle = st.text_input("Enter your Codeforces handle")
    info= get_codeforces_user_info(None, codeforces_handle)
    try:
        
        st.image(info['avatar'])
        st.write(info)
    except Exception as e:
        st.write(":red[User not found]")
    
    
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
