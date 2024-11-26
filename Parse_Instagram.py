import os
from bs4 import BeautifulSoup

def parse_instagram_html(file_path, post_type):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Extracting information
    user_id = soup.find('meta', {'property': 'instapp:owner_user_id'})
    description = soup.find('meta', {'name': 'description'})
    url = soup.find('link', {'rel': 'alternate', 'hreflang': 'x-default'})
    #category = soup.title.string if soup.title else "Not Available"

    # Clean and format
    result = {
        "Type": post_type,
        "UserID": user_id['content'] if user_id else "Not Available",
        "URL": url['href'] if url else "Not Available",
        "Category": "WORK IN PROGRESS",#category.strip() if category else "Not Available",
        "Description": description['content'] if description else "Not Available",
    }

    return result

# Folder containing the files
folder_path = './Sample'  # Adjust the path as needed if not in the current directory

# File names and their respective post types
files = {
    "reel.txt": "Reel",
    "carousel.txt": "Carousel",
    "portrait.txt": "Portrait",
    "square.txt": "Square"
}

output = []

# Parse each file
for file_name, post_type in files.items():
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        parsed_data = parse_instagram_html(file_path, post_type)
        output.append(parsed_data)
    else:
        print(f"File not found: {file_path}")

# Print formatted output
for entry in output:
    print("POST API CALLED {")
    for key, value in entry.items():
        print(f"  {key}: {value}")
    print("}")