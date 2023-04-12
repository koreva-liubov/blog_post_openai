import requests
from bs4 import BeautifulSoup

url='https://www.maginepro.com/2023/03/09/revolutionise-your-content-delivery-with-ai-based-recommendations/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extract text content from the HTML
text_content = soup.get_text()

# Save the text content to a file
with open('output.txt', 'w') as f:
    f.write(text_content)