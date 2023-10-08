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

def get_github_contributions_and_repos(username):
    # Replace 'YOUR_USERNAME' with your GitHub username
    # Construct the URL to fetch user contributions
    contributions_url = f'https://api.github.com/users/{username}/events/public'

    try:
        # Send a GET request to the GitHub API
        response = requests.get(contributions_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            events = response.json()
            
            # Initialize dictionaries to store contributions and repositories
            contributions = {}
            repositories = []

            # Loop through events to extract contributions and repositories
            for event in events:
                if event['type'] == 'PushEvent':
                    # Extract contributions (pushes to repositories)
                    repo_name = event['repo']['name']
                    if repo_name not in contributions:
                        contributions[repo_name] = 0
                    contributions[repo_name] += 1
                
                # Extract repositories where user has contributed
                if 'repo' in event:
                    repo_name = event['repo']['name']
                    if repo_name not in repositories:
                        repositories.append(repo_name)

            return {
                'contributions': contributions,
                'repositories': repositories
            }
        else:
            return {'error': 'GitHub API request failed. Check the status code and response content.'}
    except Exception as e:
        return {'error': f'An error occurred: {str(e)}'}

def assess_github_coding_proficiency(username, github_token=None):
    # Construct the API endpoint URL for the user's repositories
    base_url = 'https://api.github.com'
    user_url = f'{base_url}/users/{username}/repos'
    
    # Set headers with the user's GitHub token (if provided)
    headers = {'Authorization': f'token {github_token}'} if github_token else {}
    
    try:
        # Send a GET request to fetch user repositories
        response = requests.get(user_url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            repositories = response.json()
            
            if not repositories:
                return {'error': 'No repositories found for the user.'}
            
            # Initialize variables to calculate metrics
            commit_count = 0
            open_source_contributions = 0
            project_count = len(repositories)
            languages = set()
            
            # Loop through user repositories to gather data
            for repo in repositories:
                if 'stargazers_count' in repo:
                    commit_count += repo['stargazers_count']
                if 'forks_count' in repo and repo['forks_count'] > 0:
                    open_source_contributions += 1
                if 'language' in repo and repo['language']:
                    languages.add(repo['language'])
            
            # Calculate metrics
            commit_frequency = commit_count / project_count if project_count > 0 else 0
            
            return {
                'commit_frequency': commit_frequency,
                'open_source_contributions': open_source_contributions,
                'project_count': project_count,
                'languages': list(languages)
            }
        else:
            return {'error': 'GitHub API request failed. Check the status code and response content.'}
    except Exception as e:
        return {'error': f'An error occurred: {str(e)}'}

def main():
    path = r'C:\Users\dell\Rishav\ResumeEval\HTF23-Team-107\data\data\data\ACCOUNTANT\10554236.pdf'
    
    #print(extract_text_from_pdf(path))
    handle = 'rishavsci'
    #info = get_codeforces_user_info(None, handle)
    github_handle = 'rbrox'
    info = assess_github_coding_proficiency(github_handle)
    print(info)


    
if __name__ == '__main__':
    main()