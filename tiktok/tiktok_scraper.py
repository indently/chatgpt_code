import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox


def get_tiktok_followers(username):
    url = f'https://www.tiktok.com/@{username}'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        followers_section = soup.find('strong', {'title': 'Followers'})

        if followers_section:
            followers = followers_section.get_text()
            return followers
        else:
            return "Unable to find the followers count. The account may not exist or is private."
    else:
        return f"Error {response.status_code}: Unable to access the TikTok account."


def get_followers():
    tiktok_username = username_entry.get()
    followers = get_tiktok_followers(tiktok_username)
    result_label.config(text=f"Current amount of followers for @{tiktok_username}: {followers}")


app = tk.Tk()
app.title("TikTok Followers")

# Create and place the input label, entry, and button
username_label = tk.Label(app, text="Enter the TikTok username:")
username_label.grid(row=0, column=0, padx=(20, 5), pady=(20, 0))

username_entry = tk.Entry(app)
username_entry.grid(row=0, column=1, padx=(5, 20), pady=(20, 0))

submit_button = tk.Button(app, text="Get Followers", command=get_followers)
submit_button.grid(row=1, column=0, columnspan=2, pady=(10, 20))

# Create and place the result label
result_label = tk.Label(app, text="", wraplength=250)  # Set wraplength to wrap text within a specified width
result_label.grid(row=2, column=0, columnspan=2, padx=(20, 20), pady=(0, 20))

# Run the application
app.mainloop()
