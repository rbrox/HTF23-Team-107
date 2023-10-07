import PyPDF2
import re

def extract_text_from_pdf(file_path):
    """
    This function takes in a file path of a PDF and returns the extracted text from the PDF.
    """
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
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

def main():
    path = r'C:\Users\dell\Rishav\ResumeEval\HTF23-Team-107\data\data\data\ACCOUNTANT\10554236.pdf'
    
    print(extract_text_from_pdf(path))
    
    
import requests

def get_codeforces_user_info(api_key, user_handle):
    """
    Get Codeforces user information by handle.
    
    Args:
        api_key (str): Your Codeforces API key (if required).
        user_handle (str): The Codeforces handle (username) of the user.
    
    Returns:
        dict: User information as a dictionary.
    """
    # Define the API endpoint URL for the user.info method
    url = f'https://codeforces.com/api/user.info?handles={user_handle}&apiKey={api_key}' if api_key else f'https://codeforces.com/api/user.info?handles={user_handle}'

    try:
        # Make the API request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'OK':
                user_info = data['result'][0]  # Extract user information from the response
                return user_info
            else:
                return {'error': 'API request failed. Check the "comment" field for details.'}
        else:
            return {'error': 'API request failed. Check the status code and response content.'}
    except Exception as e:
        return {'error': f'An error occurred: {str(e)}'}

# Usage example:
# Replace 'your_api_key' with your actual Codeforces API key (if required)
api_key = 'your_api_key'

# Replace 'your_user_handle' with the Codeforces handle (username) of the user you want to query
user_handle = 'your_user_handle'

user_info = get_codeforces_user_info(api_key, user_handle)

if 'error' in user_info:
    print(f"Error: {user_info['error']}")
else:
    print("User Info:")
    print(f"Handle: {user_info['handle']}")
    print(f"Rating: {user_info['rating']}")
    print(f"Max Rating: {user_info['maxRating']}")

    
if __name__ == '__main__':
    main()