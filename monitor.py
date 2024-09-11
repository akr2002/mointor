#!/usr/bin/env python

from datetime import datetime
import requests
import subprocess


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            MESSAGE_UP = f"{url} is up and running"
            log_status(MESSAGE_UP)
        else:
            MESSAGE_DOWN = f"{url} is down. Status code: {response.status_code}"
            notify_user(MESSAGE_DOWN)
            log_status(MESSAGE_DOWN)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def log_status(message):
    with open("/home/user/.logs/monitor.log", "a+") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


def notify_user(message):
    subprocess.run(["notify-send", "-a", "Monitor", message])


websites = [
    "https://adityakumar.xyz",
    "https://blog.adityakumar.xyz",
    "https://git.adityakumar.xyz",
    "https://forgejo.adityakumar.xyz",
    "https://dsa.adityakumar.xyz",
]

for website in websites:
    check_website(website)
