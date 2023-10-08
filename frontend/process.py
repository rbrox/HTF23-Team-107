from model.resume_parser import *

def analyze_resume(file_path = r'./data/New_Sent/default.pdf'):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Parse the PDF file using the imported functions
        resume_text = extract_text_from_pdf(file_path)
        #resume_data = extract_data_from_text(resume_text)
        # Return the parsed data
        return resume_text

def main():
    file_path = r'./data/New_Sent/default.pdf'
    resume_data = analyze_resume(file_path)
    print(resume_data)

if __name__ == '__main__':
    main()
