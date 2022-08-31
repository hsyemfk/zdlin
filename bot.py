from requests import get
from re import findall
from rubika.client import Bot
import time

bot = Bot("AppName", auth="xffmaicbkrrlofhuysquscwmenjpriai")


while True:
	
	time.sleep(5)
	x = get("https://api.codebazan.ir/bio/").text
	cp = f"کانال بیو گزار ما \n@SPPORT_XSON"
	jok = f"{x}  \n {cp} \n "
	bot.sendMessage("c0BHMrc045e43034698bc7bd5d55bb1a", jok)
	print('sended')