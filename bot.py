from requests import get
from re import findall
from libraryArsein.Arsein import Robot_Rubika
import time

bot = bot = Robot_Rubika("htvtmtmsvwazhdxzcvdbzmhomtceeppd")


while True:
	
	time.sleep(5)
	x = get("https://api.codebazan.ir/jok/").text
	cp = f"کانال جوک ما \n @sterik_jok"
	jok = f"{x}  \n {cp} \n "
	bot.sendMessage("c0BGjTP0602c2cc83b3eca88a00f1702", jok)
	print('sended')