import PyPDF2
import re

def extract_text_from_pdf(file_path):
    """
    This function takes in a file path of a PDF and returns the extracted text from the PDF.
    """
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ''
        for page in range(pdf_reader.getNumPages()):
            page_obj = pdf_reader.getPage(page)
            text += page_obj.extractText()
        return text

def extract_github_links(text):
    """
    This function takes in the extracted text from the PDF and returns the links to GitHub accounts.
    """
    github_links = re.findall(r'(https?://github\.com/\S+)', text)
    return github_links

def extract_useful_accounts(text):
    """
    This function takes in the extracted text from the PDF and returns other useful accounts.
    """
    useful_accounts = re.findall(r'(https?://\S+)', text)
    return useful_accounts

def extract_key_skill_tags(text):
    """
    This function takes in the extracted text from the PDF and returns the key skill tags.
    """
    key_skill_tags = re.findall(r'\b(?:python|java|c\+\+|javascript|html|css)\b', text, re.IGNORECASE)
    return key_skill_tags
