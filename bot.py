from requests import get
from re import findall
from rubika.client import Bot
import time

bot = Bot("AppName", auth="htvtmtmsvwazhdxzcvdbzmhomtceeppd")


while True:
	
	time.sleep(12)
	x = get("https://api.codebazan.ir/jok/").text
	cp = f"کانال جوک ما \n @sterik_jok"
	jok = f"{x}  \n {cp} \n "
	bot.sendMessage("c0BGjTP0602c2cc83b3eca88a00f1702", jok)
	print('sended')