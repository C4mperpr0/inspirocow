import requests
from os import system as cmd
from os import remove
from io import BytesIO as Buffer
from time import time, sleep

r = requests.get("https://inspirobot.me/api?generate=true")
img = requests.get(r.content.decode("utf-8"))
filepath = f"/tmp/{round(time()*10000)}.jpg"
with open(filepath, "wb+") as file:
    file.write(img.content)
cmd(f"xcowsay -d {filepath} -t 14 && rm {filepath}")
