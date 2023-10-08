from model.resume_parser import *
import joblib
import numpy as np
import pandas as pd
import re
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def analyze_git(git_handle):
    
    return assess_github_coding_proficiency(git_handle)



def preprocess_input(job_category, resume_text):
    job_roles = ['Data Science', 'HR', 'Advocate', 'Arts', 'Web Designing', 'Mechanical Engineer', 'Sales', 'Health and fitness', 'Civil Engineer', 'Java Developer', 'Business Analyst', 'SAP Developer', 'Automation Testing', 'Electrical Engineering', 'Operations Manager', 'Python Developer', 'DevOps Engineer', 'Network Security Engineer', 'PMO', 'Database', 'Hadoop', 'ETL Developer', 'DotNet Developer', 'Blockchain', 'Testing']
    # Convert job category to lowercase
    job_category = job_roles.index(job_category)
    
    # Remove punctuation from resume text
    resume_text = resume_text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize resume text
    tokens = nltk.word_tokenize(resume_text)
    
    # Remove stop words from tokens
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join tokens back into text string
    resume_text = ' '.join(tokens)
    
    return job_category, resume_text

def analyze_resume(file_path = r'./data/New_Sent/default.pdf', job_category='Data Science'):
    # Load the classification model
    model = joblib.load('./regression.pkl')
    
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Parse the PDF file using the imported functions
        resume_text = extract_text_from_pdf(file_path)
        
        # Preprocess the job category and resume text inputs
        job_category, resume_text = preprocess_input(job_category, resume_text)
        
        # Create a DataFrame with the preprocessed inputs
        input_data = pd.DataFrame([[job_category, resume_text]], columns=['job_category', 'resume_text'])
        
        # Make a prediction using the loaded model
        prediction = model.predict(input_data)[0]
        
        # Display the prediction result
        print(f"Based on the resume, the predicted job category is {prediction}.")
        
def main():
    file_path = r'./data/New_Sent/default.pdf'
    analyze_resume(file_path)
    
    #b = np.load('matrix.npz')
    #print(b.files)
    

if __name__ == '__main__':
    main()
