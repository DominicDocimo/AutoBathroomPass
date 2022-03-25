from selenium import webdriver
from utils import get_period
from config import *

completed = False

while not completed:
    day = input("Day 1 or 2?")
    if not int(day) or int(day) not in [1, 2]:
        print("Invalid day, please select 1 or 2")
    else:
        completed = True

data = get_period(day=str(day))

if data is None:
    print("It doesn't appear to be school hours.")
    exit()

options = webdriver.ChromeOptions()
options.add_argument(rf"--user-data-dir=C:\Users\{windows_profile_name}\AppData\Local\Google\Chrome\User Data")
options.add_argument(rf"--profile-directory={chrome_profile_name}")
driver = webdriver.Chrome(options=options)
driver.maximize_window()

link = f"https://docs.google.com/forms/d/e/{form_id}/formResponse"
link += f"?{entries[0]}={data[0]}&{entries[1]}={data[1]}&{entries[2]}={name[0]}&{entries[3]}={name[1]}&" \
        f"{entries[4]}=Leaving Class&{entries[5]}={message}"
driver.get(link)
