import requests

def download_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve content from {url}")
        return None

def main():
    url = ""  # Replace with the URL of the website you want to download

    website_source = download_website(url)
    if website_source:
        with open("website_source.html", "w", encoding="utf-8") as file:
            file.write(website_source)
        print("Website source code downloaded successfully.")

if __name__ == "__main__":
    main()
