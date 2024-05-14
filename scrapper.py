import csv
import re
import requests

def fetch_reviews(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "Dnt": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
        "X-Amzn-Trace-Id": "Root=1-663baf50-0d9b24fd131da68d497cf5ee",
        "origin": "205.254.163.128",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        reviews = re.findall(r'"description":"(.*?)"', response.text)
        ratings = re.findall(r'"ratingValue":(\d)', response.text)

        if reviews and ratings:
            with open('reviews.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for review, rating in zip(reviews, ratings):
                    writer.writerow([rating, review])
        else:
            print("No reviews found.")
    else:
        print("Failed to retrieve page:", response.status_code)

# Prompt the user to enter the URL
url = input("Enter the URL of the Zomato page you want to analyze: ")

# Fetch reviews from the specified URL
print("Fetching reviews from:", url)
fetch_reviews(url)
