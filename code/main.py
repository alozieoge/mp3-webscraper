from bs4 import BeautifulSoup
import requests
from time import sleep


def ends_with_mp3(css_href):
    """
    Checks if the href attribute value ends with 'mp3'.
    Returns True if the input string is not None and the above condition is met, otherwise returns False.
    :param css_href: A string of the href value.
    :return: A boolean depending on the value of css_href.
    """
    return css_href is not None and css_href.endswith("mp3")


# Provide the website URL and target folder / directory location.
SOURCE_URL = "..."
TARGET_FOLDER = "..."

# Get the response and extract the webpage text from the website URL.
response = requests.get(url=SOURCE_URL)
web_page = response.text

# Parse the webpage HTML to a new BeautifulSoup object.
soup = BeautifulSoup(markup=web_page, parser="html.parser", features="lxml")

# Find all <a></a> tag elements with href value ending with "mp3".
a_tags_mp3 = soup.find_all(name="a", href=ends_with_mp3)

# Extract the href mp3 links into a list. 
a_tags_mp3_links = []
for tag in a_tags_mp3:
    a_tags_mp3_links.append(tag.get("href"))
    
# Specify how many mp3 files will be downloaded.
print("Downloading", len(a_tags_mp3_links), "files ...")

# For each mp3 url link, request the source and write the content of the response (mp3 file) to the target folder in binary mode.
# Each file is named as a Chapter.
for url_mp3 in a_tags_mp3_links:
    response_mp3 = requests.get(url=url_mp3)
    filename = "Chapter" + url_mp3.split("/")[-1]
    
    # Persist the mp3 file in binary mode and provide completion status.
    with open(TARGET_FOLDER + filename, "wb") as mp3:
        mp3.write(response_mp3.content)
        print("Finished writing", filename, "...")
    
    # 1 second delay.
    sleep(1) 
