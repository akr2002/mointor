#!/usr/bin/env python

from datetime import datetime
import requests


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            log_status(f"{url} is up and running.")
        else:
            log_status(f"{url} is down. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def log_status(message):
    with open("/home/user/.logs/monitor.log", "a+") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


websites = [
    "https://adityakumar.xyz",
    "https://blog.adityakumar.xyz",
    "https://git.adityakumar.xyz",
    "https://forgejo.adityakumar.xyz",
    "https://dsa.adityakumar.xyz",
]

for website in websites:
    check_website(website)
