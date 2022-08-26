print("⚠️کاربران گرامی شما حق ویرایش یا ادیت سورس پایتون آرین بات را ندارید درصورت مشاهده آپدیت های سورس بنده دراختیار شما قرار نمی گیرد⚠️")

from rubika.client import Bot
import time
from time import sleep
import json
from json import loads,dumps,load

print(".............................................")
Soal_karbar = input("آیا اکانت شما تائید 2 مرحله ای دارد؟")

if Soal_karbar == "yes":
	while(1):
		try:
			with open(f"AppName.json", "r") as file:
				jget = json.load(file)
				s = jget["data"]["auth"]
				v = Bot.registerDevice(s)
				print(v)
		except:continue

elif Soal_karbar == "y":
	phonenumber = input("شماره تلفن خود را وارد کنید: ")
	print(".............................................")
	pass_your = input("رمز خود را وارد کنید:")
	print(".............................................")
	Sendcode = Bot.Send_Code_pass(phonenumber,pass_your).get("data").get("phone_code_hash")
	sleep(2)
	vorodacoaunt = Bot.signIn(phonenumber,Sendcode, input("کد ورود خود را وارد کنید: "))
	authe:str= vorodacoaunt["data"]["auth"]
	with open(f"AppName.json", "a+") as file:
		file.write(dumps(vorodacoaunt, indent=4, ensure_ascii=False))
	print(authe)
	print(".............................................")
	ph = input("start:")
	if ph == "yess":
		while(1):
			try:
				with open(f"AppName.json", "r") as file:
					jget = json.load(file)
				s = jget["data"]["auth"]
				v = Bot.registerDevice(s)
				print(v)
			except:continue
	else:pass
else:
	if Soal_karbar == "n":
		phonenumber = input("شماره تلفن خود را وارد کنید: ")
		Sendcode = Bot.Send_Code(phonenumber).get("data").get("phone_code_hash")
		sleep(2)
		vorodacoaunt = Bot.signIn(phonenumber,Sendcode, input("کد ورود خود را وارد کنید: "))
		authe:str= vorodacoaunt["data"]["auth"]
		with open(f"AppName.json", "w") as file:
			file.write(dumps(vorodacoaunt, indent=4, ensure_ascii=False))
		print(authe)
		print(".............................................")
		ph = input("start:")
		if ph == "yess":
			while(1):
				try:
					with open(f"AppName.json", "r") as file:
						jget = json.load(file)
					s = jget["data"]["auth"]
					v = Bot.registerDevice(s)
					print(v)
				except:continue
		else:pass
	else:pass

