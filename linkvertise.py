# Coded by @venaxyt on Github
import requests
from os import system

link = input(" [>] Linkvertise link : ")

headers = {
"Host": "bypass.bot.nu",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
"Accept": "*/*",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://bypass.bot.nu/",
"Connection": "keep-alive",
    }

try:
    data = requests.get(f"https://bypass.bot.nu/bypass2?url={link}", headers=headers)
    link = data.json()["destination"]
    system("cls")
    print(f" [>] Destination link : {link}")
except:
    system("cls")
    print(banner)
    print(" [!] An unexpected error occurred")

system("pause >nul")
