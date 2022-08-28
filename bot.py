print("⚠️کاربران گرامی شما حق ویرایش یا ادیت سورس پایتون آرین بات را ندارید درصورت مشاهده آپدیت های سورس بنده دراختیار شما قرار نمی گیرد⚠️")
print(" ")
print(". . . . . . . . . . . ")


from requests import get
from re import findall
import os
import glob
from libraryArsein.Arsein import Robot_Rubika
import requests
from gtts import gTTS
from mutagen.mp3 import MP3
import json
from datetime import datetime
from json import loads , dumps
import time
from time import sleep
import random
import urllib.request
import io
from random import choice,randint
from PIL import Image
from colorama import Fore



#شناسه اکانت
bot = Robot_Rubika("htvtmtmsvwazhdxzcvdbzmhomtceeppd")
#......
# شناسه ربات اصلی
my_guid_bot = ""
#......
#شناسه گروه
target = "g0Bb18B06f7c85e83c00d8b62fc2a4ac"
#......
#شناسه کانال
channell = " "
#......
#شناسه کانال مورد نظر برای تبلیغات
channell_sin_tabl = " "
#......
# شناسه کانالی که میخواهید ربات برای شما فایل پست کند را وارد کنید
post_files_to_channell = " "

# Upgraded by arian abbasi(Upgrade by Arian)(Name Arian Bot)(libs for arian abbasi)
#آرین بات توسط بنده توسعه و ارتقا یافته است نامگذاری بات به اسم خود قابل قبول نیست در صورت مشاهده نسخه های بروز سورس بنده در اختیار شما قرار نمی گیرد و رفع باگ نیز نمی شوند


#شناسه کانال شما



GAP = bot.getGroupInfo(target)["data"]["group"]["group_title"]
p = Image.open('picture_Start/now.png')
bot.sendPhoto(target, 'picture_Start/now.png', p.size,caption=  f"اکانت هوشمند با موفقیت در گروه {GAP} فعال شد 😍🕺")
print(Fore.GREEN+"sended photo")



#آدرسدهی برای تغیر عکس گروه

#profile ="/storage/emulated/0/Download/arian.jpg"

def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me"]
	for i in links:
		if i in msg:
			return True

def hasInsult(msg):
	swData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in msg:
			swData = [True, i]
			break
		else: continue
	return swData


# static variable
answered, sleeped, retries,forward_Channell, answer,lock_fosh,st,list_gap,sttab2,st_tabl,deletergap = [] , False , {} , True , [] , False , False , [] , False , False , True
alerts, blacklist, stars, alert_stickers, alert_Gif, lock_GIF,lock_Sticker,star_sinza,sin_time,tab_time = [] , [] , [] , [] , [] , False , False , False , False , False



def alert(guid,user,link=False):
	alerts.append(guid)
	coun = int(alerts.count(guid))
	haslink = ""
	if link : haslink = "گزاشتن لینک در گروه ممنوع میباشد .\n\n"
	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما [1/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .", message_id=mesagidhoshdar)
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما [2/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .", message_id=mesagidhoshdar)
	elif coun == 3:
		blacklist.append(guid)
		bot.sendMessage(target, "🚫 کاربر [ @"+user+" ] \n [3/3] اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .", message_id=mesagidhoshdar)
		bot.banGroupMember(target, guid)
		bot.sendMessage(msg.get("author_object_guid"),"متاسفانه شما بدلیل تبلیغات از گروه حذف شدید\nباید قوانین گروه را مطالعه می کردید❗️")


def alert_sticker(guid_sti,user_sti):
	alert_stickers.append(guid_sti)
	coun = int(alert_stickers.count(guid_sti))
	hasgif = "گذاشتن استیکر در گروه ممنوع می باشد\n\n"
	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user_sti+" ] \n"+hasgif+" شما [1/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user_sti+" ] \n"+hasgif+" شما [2/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 3:
		blacklist.append(guid_sti)
		bot.sendMessage(target, "🚫 کاربر [ @"+user_sti+" ] \n [3/3] اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .")
		bot.banGroupMember(target, guid_sti)
		bot.sendMessage(msg.get("author_object_guid"),"متاسفانه شما بدلیل ارسال استیکر از گروه حذف شدید\nباید قوانین گروه را مطالعه می کردید❗️")


def alert_GIF(guid_GFS,user_GFS):
	alert_Gif.append(guid_GFS)
	coun = int(alert_Gif.count(guid_GFS))
	has_gif = "گذاشتن گیف در گروه ممنوع می باشد\n\n"
	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user_GFS+" ] \n"+has_gif+" شما [1/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user_GFS+" ] \n"+has_gif+" شما [2/3] اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 3:
		blacklist.append(guid_GFS)
		bot.sendMessage(target, "🚫 کاربر [ @"+user_GFS+" ] \n [3/3] اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .")
		bot.banGroupMember(target, guid_GFS)
		bot.sendMessage(msg.get("author_object_guid"),"متاسفانه شما بدلیل ارسال گیف از گروه حذف شدید\nباید قوانین گروه را مطالعه می کردید❗️")



def star(guid,user):
	stars.append(guid)
	star_count = int(stars.count(guid))
	if star_count == 1:
		bot.sendMessage(target,  f"شما {guil} از طرف مدیر گرامی [1/3] امتیاز دریافت کردید بعد از دریافت 3 امتیاز آدمین گروه می شوید 😍🙌", message_id=mesagid)
	elif star_count == 2:
		bot.sendMessage(target,  f"شما {guil} از طرف مدیر گرامی [2/3] امتیاز دریافت کردید بعد از دریافت 3 امتیاز آدمین گروه می شوید 😍🙌", message_id=mesagid)
	elif star_count == 3:
		bot.sendMessage(target,  f"شما {guil} از طرف مدیر گرامی [3/3] امتیاز دریافت کردید اکنون آدمین گروه می شوید 🎉😱", message_id=mesagid)
		bot.setGroupAdmin(target,guid)



def remove_star(guid,user):
	stars.remove(guid)
	remove_count = int(stars.count(guid))
	if remove_count == 2:
		bot.sendMessage(target,   f"از طرف مدیر گرامی [1/3] امتیاز از شما {guil} کسر شد بعد از کسر 3 امتیاز از آدمین بودن برکنار می شوید 😔💔", message_id=mesagid)
	elif remove_count == 1:
		bot.sendMessage(target,   f"از طرف مدیر گرامی [2/3] امتیاز از شما {guil} کسر شد بعد از کسر 3 امتیاز از آدمین بودن برکنار می شوید 😔💔", message_id=mesagid)
	elif remove_count == 0:
		bot.sendMessage(target,   f"از طرف مدیر گرامی [3/3] امتیاز از شما {guil} کسر شد اکنون از آدمینی برکنار می شوید 😭🖤", message_id=mesagid)
		bot.deleteGroupAdmin(target,user)


while 1:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		name_admins = [i["first_name"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]


		while 1:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		for msg in messages:
			try:
				if msg["type"]=="Text" and not msg.get("message_id") in answered:
					print("Group:" +"[" + msg.get("message_id") + "] >>> " + msg["type"] + ">>>" + " " + msg.get("text") + "\n")
					if not sleeped and not msg.get("author_object_guid") == my_guid_bot:
						if hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
							mesagidhoshdar = msg.get("message_id")
							guid = msg.get("author_object_guid")
							user = bot.getUserInfo(guid)["data"]["user"]["username"]
							alert(guid,user,True)
							bot.deleteMessages(target, [msg.get("message_id")])


						elif deletergap == True:
							try:
								bot.deleteChatHistory(target,msg.get("message_id"))
								deletergap = False
							except:
								print("err del gap tarikh")


						elif msg.get("text") == "ریستارت" or msg.get("text") == "\restart":
							try:
								if msg.get("author_object_guid") in admins:
								   sleeped = True
								   start_restart = "در حال راه اندازی مجدد....⏳"
								   my_id = bot.sendMessage(target,start_restart, message_id=msg.get("message_id"))
								   get_id = my_id["data"]["message_update"]
								   get__ID = get_id["message_id"]
								   sleep(2)
								   sleeped = False
								   finish_restart = "✅ متشکرم از همراهی شما ربات دوباره فعال شد"
								   bot.editMessage(target,finish_restart,get__ID)
								else:
									bot.sendMessage(target, '❌ اجازه دسترسی به شما داده نشد',message_id=msg.get("message_id"))
							except:
								print('error restart bot')

						elif msg.get("text") == "خاموش" or msg.get("text") == "\stop":
							try:
								if msg.get("author_object_guid") in admins:
								   sleeped = True
								   bot.sendMessage(target, "✅ ربات اکنون خاموش است", message_id=msg.get("message_id"))
								   bot.deleteChatHistory(target,msg.get("message_id"))
								else:
									bot.sendMessage(target, '❌ اجازه دسترسی به شما داده نشد',message_id=msg.get("message_id"))
							except:
								print('error off bot')

						elif msg.get("text").startswith("حذف") or msg.get("text").startswith("حذف پیام") and msg.get("author_object_guid") in admins :
							try:
								number = int(msg.get("text").split(" ")[1])
								answered.reverse()
								bot.deleteMessages(target, answered[0:number])

								bot.sendMessage(target, "✅ "+ str(number) +" پیام اخیر با موفقیت حذف شد", message_id=msg.get("message_id"))
								answered.reverse()

							except IndexError:
								bot.deleteMessages(target, [msg.get("reply_to_message_id")])
								bot.sendMessage(target, "✅ پیام با موفقیت حذف شد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text").startswith("اخراج") or msg.get("text").startswith("بن") and msg.get("author_object_guid") in admins :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									bot.banGroupMember(target, guid)
									# bot.sendMessage(target, "✅ کاربر با موفقیت از گروه اخراج شد", message_id=msg.get("message_id"))
								else :
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))

							except IndexError:
								getguidkr = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								user = bot.getUserInfo(getguidkr)["data"]["chat"]["abs_object"]["object_guid"]
								username = bot.getUserInfo(user)["data"]["user"]["first_name"]
								bot.forwardMessages(target,[msg.get("reply_to_message_id")],getguidkr)
								if msg.get('reply_to_message_id') != None:
									befrest = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if befrest['text'] != None:
										getmtns = befrest['text']
								bot.sendMessage(getguidkr,  f"کاربر {username} شما به دلیل << {getmtns} >> از گروه حذف و وارد لیست سیاه شدید🗑")
							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("آزاد") or msg.get("text").startswith("ازاد") and msg.get("author_object_guid") in admins :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if guid in admins:
									bot.unbanGroupMember(target, guid)
									linkgroupp = bot.getGroupLink(target)
									usernamep = bot.getUserInfo(guid)["data"]["user"]["first_name"]
									bot.sendMessage(target,   f"کاربر {usernamep} با موفقیت آزاد شد", message_id=msg.get("message_id"))
									bot.sendMessage(guid,   f"کاربر {usernamep} شما با موفقیت از لیست سیاه خارج شدید\nروی لینک کلیک کنید😍❤️👇\n\n {linkgroupp}")
								else:
									bot.sendMessage(target, "❌ شما آدمین نمی باشید", message_id=msg.get("message_id"))

							except IndexError:
								linkgroup = bot.getGroupLink(target)
								gydea = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								bot.unbanGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								user = bot.getUserInfo(gydea)["data"]["chat"]["abs_object"]["object_guid"]
								username = bot.getUserInfo(user)["data"]["user"]["first_name"]
								bot.sendMessage(target,   f"کاربر {username} با موفقیت آزاد شد", message_id=msg.get("message_id"))
								bot.sendMessage(user,   f"کاربر {username} شما با موفقیت از لیست سیاه خارج شدید\nروی لینک کلیک کنید😍❤️👇\n\n {linkgroup}")
							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))




						elif msg.get("text").startswith("افزودن") or msg.get("text").startswith("!addgap") :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]
								if guid in blacklist:
									if msg.get("author_object_guid") in admins:
										alerts.remove(guid)
										alerts.remove(guid)
										alerts.remove(guid)
										blacklist.remove(guid)

										bot.invite(target, [guid])
									else:
										bot.sendMessage(target, "❌ کاربر محدود میباشد", message_id=msg.get("message_id"))
								else:
									bot.invite(target, [guid])
									# bot.sendMessage(target, "✅ کاربر اکنون عضو گروه است", message_id=msg.get("message_id"))

							except IndexError:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("اضافه") or msg.get("text").startswith("!addch") :
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]
								if guid in blacklist:
									if msg.get("author_object_guid") in admins:
										blacklist.remove(guid)
										bot.inviteChannel(channell, [guid])
										bot.sendMessage(target, "✅ کاربر مورد نظر با موفقیت به کانال افزوده شد", message_id=msg.get("message_id"))
									else:
										bot.sendMessage(target, "❌ کاربر محدود میباشد", message_id=msg.get("message_id"))
								else:
									bot.inviteChannel(channell, [guid])
									bot.sendMessage(target, "✅ کاربر مورد نظر با موفقیت به کانال افزوده شد", message_id=msg.get("message_id"))

							except IndexError:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))



						elif msg.get("text") == "دستورات":
							try:
								G_U = msg.get("author_object_guid")
								ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
								NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
								if ID_karbar != None:
									ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
								else:
									if NAME_karbar != None:
										ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
									else:pass
								G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
								if msg.get("author_object_guid") in ozv_ajbar:
									rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
									bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
							except:
								try:
									G_U = msg.get("author_object_guid")
									ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
									NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
									if ID_karbar != None:
										ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
									else:
										if NAME_karbar != None:
											ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
										else:pass
									G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
									if msg.get("author_object_guid") in ozv_ajbar:
										rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
										bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
									else:
										bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
								except:
									print("err dastorat")

						elif msg.get("text") == "سرگرمی":
							try:
								rules = open("plays_arianbot/poer.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
								bot.pin(target, message_id=msg.get("message_id"))
								bot.sendMessage(target, "سوالات فرستاده شدند حالا بازی کنید😉☝️", message_id=msg.get("message_id"))
							except:
								print("err play")

						elif msg["text"].startswith("!number") or msg["text"].startswith("بشمار"):
							try:
								response = get(f"http://api.codebazan.ir/adad/?text={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])

						elif msg.get("text").startswith("زمان"):
							try:
								response = get("https://api.codebazan.ir/time-date/?td=all").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err answer time")

						elif msg.get("text") == "ساعت":
							try:
								bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))
							except:
								print("err time answer")

						elif msg.get("text") == "!date":
							try:
								bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))
							except:
								print("err date")

						elif msg.get("text") == "پاک" and msg.get("author_object_guid") in admins :
							try:
								bot.deleteMessages(target, [msg.get("reply_to_message_id")])
								bot.sendMessage(target, "پیام مورد نظر پاک شد...", message_id=msg.get("message_id"))
							except:
								print("err pak")

						elif msg.get("text").startswith("دانستنی عکس"):
								try:
									danestane = get("http://api.codebazan.ir/danestani/pic")
									with open("shot.jpg","wb") as shot:
										shot.write(danestane.content)
										p = Image.open('shot.jpg')
										bot.sendPhoto(target, "shot.jpg",p.size, caption="🤖آرین بات🤖", message_id=msg["message_id"])
										os.remove('screenshot.jpg')
								except:
									print("err  photo danestane")

						elif msg.get("text").startswith("اسکرین"):
								try:
									screenshot = get(f"http://api.codebazan.ir/webshot/?text=1000&domain={msg.get('text').split()[1]}")
									with open("screenshot.jpg","wb") as screen:
										screen.write(screenshot.content)
										p = Image.open('screenshot.jpg')
										bot.sendPhoto(target, "screenshot.jpg",p.size, caption="🤖آرین بات🤖", message_id=msg["message_id"])
										print("sended danestane")
										screen.close()
										os.remove('screenshot.jpg')
								except:
									print("err screenshot")


						elif msg.get("text").startswith("!cal") or msg.get("text").startswith("حساب"):
							msd = msg.get("text")
							if plus == True:
								try:
									call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
									if call[1] == "+":
										try:
											am = float(call[0]) + float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
											plus = False
										except:
											print("err answer +")

									elif call[1] == "-":
										try:
											am = float(call[0]) - float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer -")

									elif call[1] == "*":
										try:
											am = float(call[0]) * float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer *")

									elif call[1] == "/":
										try:
											am = float(call[0]) / float(call[2])
											bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
										except:
											print("err answer /")

								except IndexError:
									bot.sendMessage(target, "متاسفانه دستور شما اشتباه میباشد!" ,message_id=msg.get("message_id"))
									plus= True


						elif hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
							try:
								mesagidhoshdar = msg.get("message_id")
								guid = msg.get("author_object_guid")
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								alert(guid,user,True)
								bot.deleteMessages(target, [msg.get("message_id")])
							except:
								print("err deletelinks_komake")

						elif msg.get("text").startswith("سلام") or msg.get("text").startswith("سلم") or msg.get("text").startswith("صلام") or msg.get("text").startswith("صلم") or msg.get("text").startswith("سیلام") or msg.get("text").startswith("صیلام") or msg.get("text").startswith("شلام"):
							try:
								guidr= msg.get("author_object_guid")
								textw = bot.getUserInfo(guidr)["data"]["user"]["first_name"]
								taf = ["آقا 😍 🌈","عشقم 🌚🌺","خان 🤓💋","جووووون🤩🍓","خشگلم🌛🍁","عسل بابا👳‍♂🙋‍♂","نفسکم🙇‍♀💖"," 🌷عزیزم",]
								ren= choice(taf)
								p = Image.open('picture_hello/hello.jpg')
								bot.sendPhoto(target, 'picture_hello/hello.jpg', p.size,caption=  f"علیک {textw} {ren}", message_id=msg.get("message_id"))
								print(Fore.GREEN+"sended photo")
							except:
								try:
									guidr= msg.get("author_object_guid")
									textw = bot.getUserInfo(guidr)["data"]["user"]["first_name"]
									taf = ["آقا 😍 🌈","عشقم 🌚🌺","خان 🤓💋","جووووون🤩🍓","خشگلم🌛🍁","عسل بابا👳‍♂🙋‍♂","نفسکم🙇‍♀💖"," 🌷عزیزم",]
									ren= choice(taf)
									p = Image.open('picture_hello/hello.jpg')
									bot.sendPhoto(target, 'picture_hello/hello.jpg', p.size,caption=  f"علیک {textw} {ren}", message_id=msg.get("message_id"))
									print(Fore.GREEN+"sended photo")
								except:
									print("err hello")

						elif msg.get("text").startswith("خوبی") or msg.get("text").startswith("خبی"):
							try:
								bot.sendMessage(target, "تو چطوری؟🤪", message_id=msg.get("message_id"))
							except:
								print("err answer hay")

						elif msg.get("text").startswith("gham"):
							try:
								bot.sendSticker(target)
							except:
								print("err answer hay")


						elif msg.get("text").startswith("ایجاد کال"):
							try:
								bot.startVoiceChat(target)
								bot.sendMessage(target, "✅ با موفقیت ایجاد شد", message_id=msg.get("message_id"))
							except:
								print("err call voice")

						elif msg.get("text").startswith("قطع کال"):
							try:
								GAP = bot.getGroupInfo(target)["data"]["chat"]
								VOICE_CHAT = GAP["group_voice_chat_id"]
								bot.finishVoiceChat(target,VOICE_CHAT)
								bot.sendMessage(target, "✅ با موفقیت قطع شد", message_id=msg.get("message_id"))
							except:
								print("err call voice")

						elif msg.get("text").startswith("ارسال"):
							try:
								if msg.get('reply_to_message_id') != None:
									befrest = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if befrest['text'] != None:
										texts= befrest['text']
										usersendmatn = msg.get("text").split(" ")[1][1:]
									bot.sendMessage(bot.getInfoByUsername(usersendmatn)["data"]["chat"]["abs_object"]["object_guid"],texts)
							except:
								print("err send_massage_be_id")

						elif msg.get("text").startswith("چه خبر") or msg.get("text").startswith("چخبر"):
							try:
								bot.sendMessage(target, "ســلامـتیت😍♥", message_id=msg.get("message_id"))
							except:
								print("err CheKhabar")

						elif msg.get("text") == "تبلیغات روشن" and msg.get("author_object_guid") in admins:
							try:
								st_tabl = True
								bot.sendMessage(target, "🤖 با موفقیت تبلیغگر روشن شد برای شروع تبلیغگر ابتدا\nزمان به اتمام رسیدن تبلیغات را ثبت نمائید 🤖 \n\nبطور مثال: اتمام 02:44 یا اتمام 12:00 یا اتمام 1:02", message_id=msg.get("message_id"))
							except:
								print("error ersal start1")

						elif msg.get("text").startswith("اتمام"):
							try:
								if st_tabl == True:
									tab_time = True
									SAH = msg.get("text").split("اتمام")[1][1:]
									print(SAH)
									bot.sendMessage(target,f"با موفقیت زمان اتمام تبلیغگر در ساعت {SAH} ثبت شد ✅", message_id=msg.get("message_id"))
									bot.sendMessage(target, "🤖در پیام بعدی بنر مورد نظر خود را ارسال نمائید و سپس روی آن ریپ بزنید و بگوئید [ثبت تبلیغ]🤖\n\nتوجه: بنر باید فقط شامل متن باشد", message_id=msg.get("message_id"))
								else:pass
							except:
								print("err moharefe")

						elif msg.get("text").startswith("ثبت تبلیغ") and msg.get("author_object_guid") in admins:
							try:
								if tab_time != False:
									if msg.get('reply_to_message_id') != None:
										banner = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
										if banner['text'] != None:
											matnbanner  = banner['text']
											matntabligh = open("tabligh_arianbot/matnTABLIGH.txt","w",encoding='utf-8').write(str(matnbanner))
											bot.sendMessage(target, "✅  \n\nمتن مورد نظر برای تبلیغات ثبت شد\nبرای شروع تبلیغات [ تبلیغ کن ] را وارد کنید", message_id=msg.get("message_id"))
											sttab2 = True
								else:print(" is not true")
							except:
								print("err save tabligh")

						elif msg.get("text").startswith("تبلیغ کن") and msg.get("author_object_guid") in admins:
							while(1):
								try:
									if sttab2 != False:
										if datetime.now().strftime("%H:%M") != SAH:
											last_chat = bot.getChannelInfo(channell_sin_tabl)["data"]["chat"]["last_message_id"]
											messages_channell = bot.getMessages(channell_sin_tabl,last_chat) 
											sleep(1)
											for chat in messages_channell:
												try:
													chat = chat['text']
													link_Group = findall(r"https://rubika.ir/joing/\w{32}", chat)
													for linkes in link_Group:
														list_gap.append(linkes)
														randomli = choice(list_gap)
														tabyligh = open("tabligh_arianbot/matnTABLIGH.txt","r",encoding='utf-8').read()
														tabeligh = bot.joinGroup(randomli)
														print(f"JOINED TO:  {randomli}")
														print("_________________________")
														tabrligh = tabeligh['data']['group']['group_guid']
														bot.sendMessage(tabrligh,tabyligh)
														bot.leaveGroup(tabrligh)
												except:break
										else:
											if datetime.now().strftime("%H:%M") == SAH:
												bot.sendMessage(target,"🔔 زمان تبلیغگر به اتمام رسید 🔔")
												sttab2 = False
												st_tabl = False
												tab_time = False
												break
											else:continue
									else:break
									continue
									break
								except:break


						elif msg.get("text").startswith("ربات") or msg.get("text").startswith("بات") or msg.get("text").startswith("رباط") or msg.get("text").startswith("باط"):
							try:
								rew = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
								renn= choice(rew)
								bot.sendDocument(target,"video_robot/ARIANBOT.mp4", caption= f"{renn}", message_id=msg.get("message_id"))
								print(Fore.GREEN+"sended Document")
							except:
								try:
									rew = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
									renn= choice(rew)
									bot.sendDocument(target,"video_robot/ARIANBOT.mp4", caption= f"{renn}", message_id=msg.get("message_id"))
									print(Fore.GREEN+"sended Document")
								except:
									print("error robot")


						elif msg.get("text").startswith("آرین") or msg.get("text").startswith("ارین"):
							try:
								bot.sendMessage(target, "بابایی دارن صدات میکنن😁🙂", message_id=msg.get("message_id"))
							except:
								print("err father")

						elif msg.get("text").startswith("امتیاز"):
							try:
								mesagid = msg.get("message_id")
								user = msg.get("text").split(" ")[1][1:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								guil = bot.getInfoByUsername(user)["data"]["user"]["first_name"]
								star(guid,user)
							except:
								try:
									mesagid = msg.get("reply_to_message_id")
									guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
									user = bot.getUserInfo(guid)["data"]["chat"]["abs_object"]["object_guid"]
									guil = bot.getUserInfo(guid)["data"]["user"]["first_name"]
									star(guid,user)
								except:
									bot.sendMessage(target, "خطا در امتیازدهی❌", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("کسر امتیاز"):
							try:
								mesagid = msg.get("message_id")
								user = msg.get("text").split(" ")[2][2:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								guil = bot.getInfoByUsername(user)["data"]["user"]["first_name"]
								remove_star(guid,user)
							except:
								try:
									mesagid = msg.get("reply_to_message_id")
									guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
									user = bot.getUserInfo(guid)["data"]["chat"]["abs_object"]["object_guid"]
									guil = bot.getUserInfo(guid)["data"]["user"]["first_name"]
									remove_star(guid,user)
								except:
									bot.sendMessage(target, " خطا در کسر امتیازدهی❌", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("تعداد امتیاز"):
							try:
								getusername = msg.get("text").split(" ")[1][1:]
								getguid = bot.getInfoByUsername(getusername)["data"]["chat"]["abs_object"]["object_guid"]
								getyourname = bot.getInfoByUsername(getguid)["data"]["user"]["first_name"]
								numberstar = int(stars.count(getguid))
								bot.sendMessage(target,   f"مقدار امتیاز کاربر {getyourname} است به [{numberstar}] امتیاز مبارکش باشه😅💋", message_id=msg.get("message_id"))
							except:
								try:
									getusername = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
									getguid = bot.getUserInfo(getusername)["data"]["chat"]["abs_object"]["object_guid"]
									getyourname = bot.getUserInfo(getguid)["data"]["user"]["first_name"]
									numberstar = int(stars.count(getguid))
									bot.sendMessage(target,   f"مقدار امتیاز کاربر {getyourname} است به [{numberstar}] امتیاز مبارکش باشه😅💋", message_id=msg.get("message_id"))
								except:
									bot.sendMessage(target, " خطا در بررسی امتیاز های کاربر مورد نظر ئد❌", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("اصل") or msg.get("text").startswith("اثل"):
							try:
								bot.sendMessage(target, "😁اصل میخوایی شیطون بلا😁", message_id=msg.get("message_id"))
							except:
								print("err asl")


						elif msg.get("text").startswith("بپرس"):
							try:
								file = open("plays_arianbot/bepors.txt").read().split("\n")
								read = list(file)
								bot.sendMessage(target,choice(read), message_id=msg.get("message_id"))
							except:
								print("err bepors")


						elif msg.get("text").startswith("بوسم کن") or msg.get("text").startswith("بوس بده"):
							try:
								bot.sendMessage(target, "💋🙈", message_id=msg.get("message_id"))
							except:
								print("err bose")

						elif msg.get("text") == "!speak" or msg.get("text") == "speak" or msg.get("text") == "Speak" or msg.get("text") == "صوت":
							try:
								if msg.get('reply_to_message_id') != None:
									msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if msg_reply_info['text'] != None:
										text = msg_reply_info['text']
										speech = gTTS(text)
										changed_voice = io.BytesIO()
										speech.write_to_fp(changed_voice)
										b2 = changed_voice.getvalue()
										changed_voice.seek(0)
										audio = MP3(changed_voice)
										dur = audio.info.length
										dur = dur * 1000
										f = open('sound.ogg','wb')
										f.write(b2)
										f.close()
										bot.sendVoice(target , 'sound.ogg', dur,message_id=msg["message_id"])
										os.remove('sound.ogg')
										print(Fore.GREEN+'sended voice')
								else:
									bot.sendMessage(target, 'رو پیام انگلیسی که نوشتید ریپ بزنید❌',message_id=msg["message_id"])
							except:
								print('server gtts bug')

						elif msg.get("text").startswith("خش") or msg.get("text").startswith("خوشم") :
							try:
								bot.sendMessage(target, "همچنین عشقم😍🌹", message_id=msg.get("message_id"))
							except:
								print("err moharefe")


						elif msg.get("text") == "منشن":
							try:
								GAPE = bot.getGroupInfo(target)["data"]["group"]["group_title"]
								guidu = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								useru = bot.getUserInfo(guidu)["data"]["user"]["first_name"]
								caption =  f"{useru}"
								if not guidu in admins:
								    bot.sendMessage(target,f"کاربر {caption} نام شما هایپر شد" ,[{"from_index": 6,"length": len(caption),"type":"MentionText","mention_text_object_guid":guidu}], message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, f"کاربر {caption} نام شما هایپر شد",[{"from_index": 6,"length": len(caption),"type":"MentionText","mention_text_object_guid":guidu}], message_id=msg.get("message_id"))
							except:
								print('hiper karbar')

						elif msg.get("text").startswith("سین زن روشن") and msg.get("author_object_guid") in admins:
							try:
								star_sinza = True
								bot.sendMessage(target, "🤖 با موفقیت سین زن روشن شد برای شروع سین زنی\nابتدا زمان به اتمام رسیدن سین زنی را ثبت نمائید 🤖 \n\nبطور مثال: پایان 02:44 یا پایان 12:00 یا پایان 1:02", message_id=msg.get("message_id"))
							except:
								print("error ersal start1")

						elif msg.get("text").startswith("پایان"):
							try:
								if star_sinza == True:
									sin_time = True
									SAH_sin = msg.get("text").split("پایان")[1][1:]
									print(SAH_sin)
									bot.sendMessage(target,f"با موفقیت زمان اتمام سین زن در ساعت {SAH_sin} ثبت شد ✅", message_id=msg.get("message_id"))
									bot.sendMessage(target,"🤖 برای شروع سین زنی ابتدا بنر خود را ارسال یا فوروارد \nکرده و سپس روی آن ریپ بزنید و بگوئید [سین بزن] 🤖", message_id=msg.get("message_id"))
								else:pass
							except:
								print("err set time sinzan")

						elif msg.get("text").startswith("سین بزن") and not sleeped and msg.get("author_object_guid") in admins:
							while(1):
								try:
									if sin_time != False and not sleeped:
										if datetime.now().strftime("%H:%M") != SAH_sin:
											last_chat = bot.getChannelInfo(channell_sin_tabl)["data"]["chat"]["last_message_id"]
											messages_channell = bot.getMessages(channell_sin_tabl,last_chat) 
											sleep(1)
											for chat in messages_channell:
												try:
													chat = chat['text']
													link_Group = findall(r"https://rubika.ir/joing/\w{32}", chat)
													for linkes in link_Group:
														list_gap.append(linkes)
														randomli = choice(list_gap)
														tabeligh = bot.joinGroup(randomli)
														print(f"JOINED TO:  {randomli}")
														print("_________________________")
														tabrligh = tabeligh['data']['group']['group_guid']
														bot.forwardMessages(target,[msg.get("reply_to_message_id")],tabrligh)
														bot.leaveGroup(tabrligh)
												except:break
										else:
											if datetime.now().strftime("%H:%M") == SAH_sin:
												bot.sendMessage(target,"🔔 زمان سین زنی به اتمام رسید 🔔")
												star_sinza = False
												sin_time = False
												break
											else:continue
									else:break
									continue
									break
								except:break

						elif msg.get("text").startswith("!Mono") or msg.get("text").startswith("مونو"):
							try:
								if msg.get('reply_to_message_id') != None:
									Mono = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if Mono['text'] != None:
										textMono = Mono['text']
										if textMono != "!Mono" or textMono != "مونو":
											metn = textMono
											bot.sendMessage(target,textMono, metadata=[{"from_index": 0,"length": len(metn),"type":"Mono"}], message_id=msg.get("message_id"))
										else:pass
							except:
								print("err Mono font")

						elif msg.get("text").startswith("unmute") or msg.get("text").startswith("اعلان روشن") and msg.get("author_object_guid") in admins:
							try:
								bot.setActionChatun(target)
								bot.sendMessage(target, "✅ اعلان گروه برای شما مدیر گرامی با موفقیت روشن شد", message_id=msg.get("message_id"))
							except:
								print("err on Unmute")


						elif msg.get("text").startswith("visit") or msg.get("text").startswith("پیام اشکار") and msg.get("author_object_guid") in admins:
							try:
								bot.chatGroupvisit(target,["chat_history_for_new_members"])
								bot.sendMessage(target, "پیام های گروه با موفقیت اشکار شدند ✅", message_id=msg.get("message_id"))
							except:
								print("err visit msg")

						elif msg.get("text").startswith("hidden") or msg.get("text").startswith("پیام مخفی") and msg.get("author_object_guid") in admins:
							try:
								bot.chatGrouphidden(target,["chat_history_for_new_members"])
								bot.sendMessage(target, "پیام های گروه با موفقیت مخفی شدند ✅", message_id=msg.get("message_id"))
							except:
								print("err hidden msg")

						elif msg.get("text").startswith("mute") or msg.get("text").startswith("اعلان خاموش") and msg.get("author_object_guid") in admins:
							try:
								bot.setActionChatmut(target)
								bot.sendMessage(target, "✅ اعلان گروه  برای شما مدیر گرامی با موفقیت خاموش شد", message_id=msg.get("message_id"))
							except:
								print("err off Mute")

						elif msg.get("text").startswith("جوین چنل") and msg.get("author_object_guid") in admins:
							try:
								goinchannell = msg.get("text").strip("جوین چنل")
								bot.joinChannel(goinchannell)
								bot.sendMessage(target, "✅ اکانت هوشمند با موفقیت عضو چنل شد", message_id=msg.get("message_id"))
							except:
								print("err join Channel")

						elif msg.get("text").startswith("قفل استیکر روشن") and msg.get("author_object_guid") in admins:
							try:
								lock_Sticker = True
								bot.sendMessage(target, "با موفقیت قفل استیکر روشن شد ✅", message_id=msg.get("message_id"))
							except:
								print("err lock Sticker")

						elif msg.get("text").startswith("قفل استیکر خاموش") and msg.get("author_object_guid") in admins:
							try:
								lock_Sticker = False
								bot.sendMessage(target, "با موفقیت قفل استیکر خاموش شد ✅", message_id=msg.get("message_id"))
							except:
								print("err unlock Sticker")


						elif msg.get("text").startswith("قفل گیف روشن") and msg.get("author_object_guid") in admins:
							try:
								lock_GIF = True
								bot.sendMessage(target, "با موفقیت قفل گیف روشن شد ✅", message_id=msg.get("message_id"))
							except:
								print("err lock Gif")

						elif msg.get("text").startswith("قفل گیف خاموش") and msg.get("author_object_guid") in admins:
							try:
								lock_GIF = False
								bot.sendMessage(target, "با موفقیت قفل گیف خاموش شد ✅", message_id=msg.get("message_id"))
							except:
								print("err unlock Gif")


						elif msg.get("text").startswith("قفل فحش روشن") and msg.get("author_object_guid") in admins:
							try:
								lock_fosh = True
								bot.sendMessage(target, "با موفقیت قفل فحش روشن شد ✅", message_id=msg.get("message_id"))
							except:
								print("err lock fosh")

						elif msg.get("text").startswith("قفل فحش خاموش") and msg.get("author_object_guid") in admins:
							try:
								lock_fosh = False
								bot.sendMessage(target, "با موفقیت قفل فحش خاموش شد ✅", message_id=msg.get("message_id"))
							except:
								print("err unlock fosh")

						elif msg.get("text").startswith("تو خوبی") or msg.get("text").startswith("تو خبی"):
							try:
								bot.sendMessage(target, "منم خوبم متشکرم که حالمو پرسیدی❤️", message_id=msg.get("message_id"))
							except:
								print("err answer ghobe")

						elif msg.get("text").startswith("گلشیفته خودتو معرفی کن"):
							try:
								bot.sendMessage(target, "من گلشیفته هستم اهل تهران\n 17 سالمه خدمت گذار شما و روبیکا هستم ", message_id=msg.get("message_id"))
							except:
								print("err moharefe")

						elif msg.get("text").startswith("!single") or msg.get("text").startswith("سینگلم"):
							try:
								bot.sendMessage(target, "سینگلی بد دردیه😞🥀", message_id=msg.get("message_id"))
							except:
								print("err roz")

						elif msg.get("text").startswith("poll") and msg.get("text").startswith("نظرسنجی") and msg.get("author_object_guid") in admins:
							try:
								bot.sendPoll(target,"TEST",["TEST1","TEST2"])
							except:
								print("err sendPoll")

						elif hasInsult(msg.get("text"))[0] and not msg.get("author_object_guid") in admins:
							try:
								if lock_fosh == True:
									print("yek ahmagh fohsh dad")
									bot.deleteMessages(target, [str(msg.get("message_id"))])
									print("fohsh pak shod")
								else:pass
							except:
								print("err del fohsh Bug")

						elif msg.get("text").startswith("قلب"):
							try:
								matn_r = ["hello","arianbot","robot"]
								galb = ["💜","💙","💚"]
								my_id = bot.sendMessage(target,choice(matn_r), message_id=msg.get("message_id"))
								get_id = my_id["data"]["message_update"]
								get__ID = get_id["message_id"]
								sleep(5)
								bot.editMessage(target,choice(galb),get__ID)
							except:
								print("err edit")

						elif msg.get("text").startswith("استقلال"):
							try:
								bot.sendMessage(target, "قسم به تیم استقلال ، قسم به سیمای خوبان ، قسم به ناصر حجازی ، ندای ما استقلال 💙", message_id=msg.get("message_id"))
							except:
								print("err esteghlal")

						elif msg.get("text").startswith("پرسپولیس"):
							try:
								bot.sendMessage(target, " عشق آسیایی پرسپولیس خالق یک جامی گل بزن امشبو به یاد پروین و علی دایی ❤", message_id=msg.get("message_id"))
							except:
								print("ejab error perspolis")

						elif msg.get("text").startswith("عجب"):
							try:
								bot.sendMessage(target, "مش رجب 😓", message_id=msg.get("message_id"))
							except:
								print("ejab error")

						elif msg.get("text").startswith("🚶"):
							try:
								bot.sendMessage(target, "به این زودی میری🧐", message_id=msg.get("message_id"))
							except:
								print("ejab error")

						elif msg.get("text").startswith("هعی") or msg.get("text").startswith("هع"):
							try:
								bot.sendMessage(target, "چی شده عشقم نبینم ناراحت باشی😠", message_id=msg.get("message_id"))
							except:
								print("err he")

						elif msg.get("text").startswith("بای") or msg.get("text").startswith("لف") or msg.get("text").startswith("خداحافظ"):
							try:
								bot.sendMessage(target, "نخود نخود هر که رود خانه خود😂", message_id=msg.get("message_id"))
							except:
								print("err lef")

						elif msg.get("text").startswith("رل") or msg.get("text").startswith("رل میخوام") or msg.get("text").startswith("رل می خوام") or msg.get("text").startswith("رل پی"):
							try:
								bot.sendMessage(target, "اینجا جنده خونه نیست بیشعور😒💔 ", message_id=msg.get("message_id"))
							except:
								print("err he")

						elif msg.get("text").startswith("زر نزن") or msg.get("text").startswith("زور نزن"):
							try:
								bot.sendMessage(target, "😁💋رژ بزن", message_id=msg.get("message_id"))
							except:
								print("err answer hay")

						elif msg.get("text") == "لینک" or msg.get("text") == "لینک گپ" or msg.get("text") == "لینک گروه":
							try:
								rules = open("linkgap_arianbot/linker.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err link gap")

						elif msg.get("text") == "تولد" or msg.get("text") == "تولدمه" or msg.get("text") == "تولدم" :
							try:
								rules = open("telod.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							except:
								print("err link t")

						elif msg.get("text").startswith("😋") or msg.get("text").startswith("😛") or msg.get("text").startswith("😝") or msg.get("text").startswith("😜") or msg.get("text").startswith("🤪"):
							try:
								bot.sendMessage(target, "زبونتو بکن تو عه🙄👿", message_id=msg.get("message_id"))
							except:
								print("err answer zabon")

						elif msg.get("text").startswith("🙏") or msg.get("text").startswith("🙏🙏"):
							try:
								bot.sendMessage(target, "خواهش نکن😬", message_id=msg.get("message_id"))
							except:
								print("err khahesh")

						elif msg.get("text").startswith("☹️") or msg.get("text").startswith("🙁") or msg.get("text").startswith("😕"):
							try:
								bot.sendMessage(target, "بغض نکن دیگه😰 بخند", message_id=msg.get("message_id"))
							except:
								print("err akhm")

						elif msg.get("text").startswith("😘") or msg.get("text").startswith("😍"):
							try:
								bot.sendMessage(target, "زود فامیل میشیا🤫", message_id=msg.get("message_id"))
							except:
								print("err ghalb")

						elif msg.get("text").startswith("😡") or msg.get("text").startswith("🤬"):
							try:
								bot.sendMessage(target, "اییش دوباره گوجه شدی😤👊", message_id=msg.get("message_id"))
							except:
								print("err ghoge")

						elif msg.get("text").startswith("ممنون") or msg.get("text").startswith("ممنونم"):
							try:
								bot.sendMessage(target, "خجالتم نده کاری نکردم که وظیفم بود 😶😊💗", message_id=msg.get("message_id"))
							except:
								print("err memnone")

						elif msg.get("text").startswith("عر") or msg.get("text").startswith("عرر") or msg.get("text").startswith("جر") or msg.get("text").startswith("جرر") :
							try:
								bot.sendMessage(target, "پاره نشی😏", message_id=msg.get("message_id"))
							except:
								print("err  arr")

						elif msg.get("text").startswith("فحش داد") or msg.get("text").startswith("فهش داد"):
							try:
								bot.sendMessage(target, "گه خورد", message_id=msg.get("message_id"))
							except:
								print("err pe")

						elif msg.get("text").startswith("بنی") or msg.get("text").startswith("بونی"):
							try:
								bot.sendMessage(target, "بابایی دارن صدات میکنن😁🙂", message_id=msg.get("message_id"))
							except:
								print("err bone")

						elif msg.get("text").startswith("کونی") or msg.get("text").startswith("مادرجنده") or msg.get("text").startswith("🖕") :
							try:
								bot.sendMessage(target, "بیشعور رو نگاه ادبت کجا رفته 😒😪🥀", message_id=msg.get("message_id"))
							except:
								print("err adab")

						elif msg.get("text").startswith("دوست دارم") or msg.get("text").startswith("دوصت دارم"):
							try:
								bot.sendMessage(target, "عشق منی تو😻❤️", message_id=msg.get("message_id"))
							except:
								print("err DOSAT")

						elif msg.get("text").startswith("کجا") or msg.get("text").startswith("کجایی"):
							try:
								bot.sendMessage(target, "تو قلبت 😻💋", message_id=msg.get("message_id"))
							except:
								print("err kega")

						elif msg.get("text").startswith("فدات") or msg.get("text").startswith("فداتم"):
							try:
								bot.sendMessage(target, "نشی جیگر😻💖", message_id=msg.get("message_id"))
							except:
								print("err fadat")

						elif msg.get("text").startswith("با من ازدواج میکنی؟") or msg.get("text").startswith("با من ازدواج میکنی؟!") or msg.get("text").startswith("با من ازدواج میکنی"):
							try:
								bot.sendMessage(target, "با اجازه بزرگترا بله🙈👀", message_id=msg.get("message_id"))
							except:
								print("err aghd")

						elif msg.get("text").startswith("گلشیفته اصل بده"):
							try:
								bot.sendMessage(target, "من گلشیفته هستم اهل تهران\n 17 سالمه خدمت گذار شما و روبیکا هستم ", message_id=msg.get("message_id"))
							except:
								print("err gholasl")

						elif msg.get("text") == "عشق من کیه":
							try:
								bot.sendMessage(target, "من من😁💋", message_id=msg.get("message_id"))
							except:
								print("error")


						elif msg.get("text") == "نه":
							try:
								bot.sendMessage(target, "نکمه ، درد بگیری ایشالا", message_id=msg.get("message_id"))
							except:
								print("error no")

						elif msg.get("text") == "اموزش ساخت ربات" or msg.get("text") == "آموزش ساخت ربات" or msg.get("text") == "آموزش ساخت بات" or msg.get("text") == "اموزش ساخت بات" :
							try:
								bot.banGroupMember(target,msg.get("author_object_guid"))
								bot.sendMessage(target, "❌ آموزشی در گپ و پیوی ارائه نخواهد شد",)
							except:
								print("error remove amozesh")

						elif msg.get("text") == "تایم":
							try:
								bot.sendMessage(target, "❤💋: 💋❤ بفداتون", message_id=msg.get("message_id"))
							except:
								print("error timer")

						elif msg.get("text") == "من امدم":
							try:
								bot.sendMessage(target, "خوش امدی", message_id=msg.get("message_id"))
							except:
								print("error khosh1")

						elif msg.get("text").startswith("اره") or msg.get("text").startswith("آره") or msg.get("text").startswith("ارهه"):
							try:
								bot.sendMessage(target, "آجر پاره😎", message_id=msg.get("message_id"))
							except:
								print("err yes")

						elif msg.get("text") == "من آمدم":
							try:
								bot.sendMessage(target, "کاستو بیار ماست بگیر🐥", message_id=msg.get("message_id"))
							except:
								print("error khosh2")

						elif msg.get("text") == "راست میگی":
							try:
								bot.sendMessage(target, "کاستو بیار ماست بگیر🐥", message_id=msg.get("message_id"))
							except:
								print("error rast")

						elif msg.get("text") == "خر" or msg.get("text") == "گاو" or msg.get("text") == "الاغ" or msg.get("text") == "اسب" :
							try:
								bot.sendMessage(target, "خودتی", message_id=msg.get("message_id"))
							except:
								print("khar")

						elif msg.get("text") == "برسی":
							try:
								GAPE = bot.getGroupInfo(target)["data"]["group"]["group_title"]
								guidu = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								useru = bot.getUserInfo(guidu)["data"]["user"]["first_name"]
								caption =  f"{useru}"
								if not guidu in admins:
								    bot.sendMessage(target,f"کاربر {caption} یک شخص عادی در گروه {GAPE} می باشد" , metadata=[{"from_index": 6,"length": len(caption),"type":"MentionText","mention_text_object_guid":guidu}], message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, f"کاربر {caption} در گروه {GAPE} آدمین می باشد", metadata=[{"from_index": 6,"length": len(caption),"type":"MentionText","mention_text_object_guid":guidu}], message_id=msg.get("message_id"))
							except:
								print('analiz user')

						elif msg.get("text") == "لیست آدمین ها" or msg.get("text") == "لیست ادمین ها":
							try:
								GAP = bot.getGroupInfo(target)["data"]["group"]["group_title"]
								for x in name_admins:
									open("admins.txt","a+",encoding='utf-8').write(str("AD:" + " " + x + "\n"))
									get_admins = open("admins.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, f"لیست آدمین های گروه {GAP} به شرح زیر است:\n\n{get_admins}", message_id=msg.get("message_id"))
								os.remove('admins.txt')
							except:
								print("get admins in GAP")


						elif msg.get("text") == "😐":
							try:
								bot.sendMessage(target, "پوکر نشو با تشکر🌹", message_id=msg.get("message_id"))
							except:
								print("error")

						elif msg.get("text") == ".":
							try:
								bot.sendMessage(target, "به بابات بگو برات نت بخره😂🤣💔🖤", message_id=msg.get("message_id"))
							except:

								print("error net")

						elif msg.get("text") == "😁":
							try:
								bot.sendMessage(target, "نخند مسواک گرون میشه🖕🤣", message_id=msg.get("message_id"))
							except:
								print("error labkhand")

						elif msg.get("text") == "😭":
							try:
								bot.sendMessage(target, "گریه نکن گریه کنی دلم میگیرا😧💔", message_id=msg.get("message_id"))
							except:
								print("error")

						elif msg.get("text") == "😏":
							try:
								bot.sendMessage(target, "چیه هااا دعوا داری🤨🚬", message_id=msg.get("message_id"))
							except:
								print("error sigar")

						elif msg.get("text") == "😎":
							try:
								bot.sendMessage(target, "عینکشو نگاه😯", message_id=msg.get("message_id"))
							except:
								print("error khosh2")

						elif msg.get("text").startswith("😍"):
							try:
								bot.sendMessage(target, "چته خوشحالی؟🤓", message_id=msg.get("message_id"))
							except:
								print("err luagh")

						elif msg.get("text").startswith("😘"):
							try:
								bot.sendMessage(target, "زود فامیل میشیا🤫", message_id=msg.get("message_id"))
							except:
								print("err eshgh")

						elif msg.get("text").startswith("پست کن"):
							try:
								s = bot.getMessagesInfo(target,[msg.get('reply_to_message_id')])[0]
								dic = s["file_inline"]["dc_id"]
								file_id = s["file_inline"]["file_id"]
								files_name = s["file_inline"]["file_name"]
								files_caption = s["text"]
								files_sizes = s["file_inline"]["size"]
								files_access_hash_rec = s["file_inline"]["access_hash_rec"]
								files_mim = s["file_inline"]["mime"]
								bot.sendDocument_rplay(post_files_to_channell,file_id,files_mim,dic,files_access_hash_rec,files_name,files_sizes,caption=files_caption)
								print("sended post to channell")
							except:
								print("error post to channell")

						elif msg.get("text").startswith("مهمان") and msg.get("author_object_guid") in admins:
							try:
								st = True
								bot.sendMessage(target, "🤖 تعداد ممبرهایی که میخواهید از گروه به کانال شما\nاضافه شوند را ارسال کنید 🤖\n\nبطور مثال: تعداد 20", message_id=msg.get("message_id"))
							except:
								print("err mehman")

						elif msg.get("text").startswith("تعداد") and msg.get("author_object_guid") in admins:
							try:
								number_members = msg.get("text").split("تعداد")[1]
								success_added = 0
								num_ad = int(number_members)
								while(1):
									try:
										if success_added < num_ad:
											if not st != True:
												c = [i["member_guid"] for i in bot.getGroupMembers(target)["data"]["in_chat_members"]]
												start_setnumber = int(len(c))
												ch = choice(c)
												if ch in blacklist:
													if msg.get("author_object_guid") in admins:
														blacklist.remove(ch)
														bot.inviteChannel(channell, [ch])
														success_added += 1
														if success_added == num_ad:
															bot.sendMessage(target, "✅ کاربران مورد نظر با موفقیت به کانال افزوده شدند", message_id=msg.get("message_id"))
															st = False
															break
														else:continue
													else:
														bot.sendMessage(target, "❌ متاسفانه اجازه دسترسی به شما داده نشد", message_id=msg.get("message_id"))
												else:
													bot.inviteChannel(channell, [ch])
													success_added += 1
													if success_added == num_ad:
														bot.sendMessage(target, "✅ کاربران مورد نظر با موفقیت به کانال افزوده شدند", message_id=msg.get("message_id"))
														st = False
														break
													else:continue
											else:break
										else:break
									except:continue
							except:
								print("err add channell whith member group")


						elif msg.get("text").startswith("گلشیفته"):
							try:
								randen = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
								cho_ce = choice(randen)
								seda = io.BytesIO(open('voice_robot/ARIANBOT.ogg',"rb").read())
								seda_sen = MP3(seda)
								size_vo = seda_sen.info.length
								send_len = size_vo * 1000
								bot.sendVoice(target , 'voice_robot/ARIANBOT.ogg',send_len,caption=cho_ce,message_id=msg["message_id"])
								print(Fore.GREEN+"sended voice")
							except:
								print("err send voice golshifte")

						elif msg.get("text").startswith("خدمت کار"):
							try:
								randen = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
								cho_ce = choice(randen)
								seda = io.BytesIO(open('voice_robot/ARIANBOT.ogg',"rb").read())
								seda_sen = MP3(seda)
								size_vo = seda_sen.info.length
								bot.sendMusic(target , 'voice_robot/ARIANBOT.ogg',size_vo ,caption=cho_ce,message_id=msg["message_id"])
								print(Fore.GREEN+"sended music")
							except:
								print("err send voice golshifte")

						elif msg.get("text").startswith("تغیر نام گروه") and msg.get("author_object_guid") in admins:
							try:
								if msg.get('reply_to_message_id') != None:
									bego2 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego2['text'] != None:
										textss= bego2['text']
										BIO = bot.getGroupInfo(target)["data"]["group"]["description"]
										bot.editnameGroup(target,textss,B)
										bot.sendMessage(target,"با موفقیت نام گروه تغیر یافت ✅", message_id=msg.get("message_id"))
							except:
								print("err edit name group")

						elif msg.get("text").startswith("تغیر بیو گروه") and msg.get("author_object_guid") in admins:
							try:
								if msg.get('reply_to_message_id') != None:
									bego2 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego2['text'] != None:
										textss= bego2['text']
										GAP = bot.getGroupInfo(target)["data"]["group"]["group_title"]
										bot.editbioGroup(target,textss,GAP)
										bot.sendMessage(target,"با موفقیت بیوگرافی گروه تغیر یافت ✅", message_id=msg.get("message_id"))
							except:
								print("err edit bio group")

						elif msg.get("text").startswith("ارتقا") and msg.get("author_object_guid") in admins:
							try:
								setadminf = msg.get("text").split(" ")[1][1:]
								setadmind = bot.getInfoByUsername(setadminf)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getInfoByUsername(setadminf)["data"]["user"]["first_name"]
								if not setadmind in admins:
									bot.setGroupAdmin(target,setadmind)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت آدمین شد", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))

							except IndexError:
								guidzz = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								userz = bot.getUserInfo(guidzz)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getUserInfo(userz)["data"]["user"]["first_name"]
								if not userz in admins:
									bot.setGroupAdmin(target,userz)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت آدمین شد", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
							except:
								print('error setadmin')



						elif msg.get("text").startswith("تنزیل") and msg.get("author_object_guid") in admins:
							try:
								deletadminS = msg.get("text").split(" ")[1][1:]
								setdeletadminS = bot.getInfoByUsername(deletadminS)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getInfoByUsername(deletadminS)["data"]["user"]["first_name"]
								if setdeletadminS in admins:
									bot.deleteGroupAdmin(target,setdeletadminS)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت از آدمین بودن برکنار شد", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))

							except IndexError:
								guidzVz = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								userVz = bot.getUserInfo(guidzVz)["data"]["chat"]["abs_object"]["object_guid"]
								textwaa = bot.getUserInfo(userVz)["data"]["user"]["first_name"]
								if  userVz in admins:
									bot.deleteGroupAdmin(target,userVz)
									bot.sendMessage(target, f"کاربر {textwaa} با موفقیت از آدمین بودن برکنار شد", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
							except:
								print('error setdeletadmin')


						elif msg.get("text").startswith("بفرست") and msg.get("author_object_guid") in admins:
							try:
								if msg.get('reply_to_message_id') != None:
									bego2 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego2['text'] != None:
										textss= bego2['text']
										kanal = textss
										mine = bot.getChannelInfo(channell)
										test = mine["data"]["channel"]["channel_title"]
										bot.sendMessage(channell, kanal)
										bot.sendMessage(target, f"✅ با موفقیت ارسال شد به کانال {test}", message_id=msg.get("message_id"))
										print('error Channel')
								else:
									bot.sendMessage(target, 'رو پیامی که میخواهید به کانالتان ارسال شود ریپ زنید❌',message_id=msg["message_id"])
							except:
								print('error Channel')


						elif msg.get("text").startswith("info"):
							try:
								users = msg.get("text").split(" ")[1][1:]
								guids = bot.getInfoByUsername(users)["data"]["user"]["first_name"]
								guid1 = bot.getInfoByUsername(users)["data"]["user"]["username"]
								guid2 = bot.getInfoByUsername(users)["data"]["user"]["bio"]
								guid3 = bot.getInfoByUsername(users)["data"]["user"]["user_guid"]
								if not guids in admins:
									bot.sendMessage(target, f"نام شما: || {guids} || \n آیدی شما: || {guid1} || \n بیوی شما: || {guid2} || \n گوید شما: || {guid3} || ", message_id=msg.get("message_id"))

								else:
									bot.sendMessage(target, f"نام شما: || {guids} || \n آیدی شما: || {guid1} || \n بیوی شما: || {guid2} || \n گوید شما: || {guid3} || ", message_id=msg.get("message_id"))

							except IndexError:
								guidZZ = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								user1 = bot.getUserInfo(guidZZ)["data"]["user"]["first_name"]
								user2 = bot.getUserInfo(guidZZ)["data"]["user"]["username"]
								user3 = bot.getUserInfo(guidZZ)["data"]["user"]["bio"]
								user4 = bot.getUserInfo(guidZZ)["data"]["user"]["user_guid"]
								if not guidZZ in admins:
									bot.sendMessage(target, f"نام شما: || {user1} || \n آیدی شما: || {user2} || \n بیوی شما: || {user3} || \n گوید شما: || {user4} || ", message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, f"نام شما: || {user1} || \n آیدی شما: || {user2} || \n بیوی شما: || {user3} || \n گوید شما: || {user4} || ", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("بگو"):
							try:
								if msg.get('reply_to_message_id') != None:
									bego1 = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if bego1['text'] != None:
										texts= bego1['text']
										bot.sendMessage(target,texts, message_id=msg.get("message_id"))
										print(' sended begho')
								else:
									bot.sendMessage(target, 'رو متن مورد نظر ریپ نزدید❌',message_id=msg["message_id"])
							except:
								print('error begho')

						elif msg.get("text").startswith("تغیر پروفایل"):
							try:
								if msg.get("author_object_guid") in admins:
									Get_photo = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									FiLes_ID = Get_photo["file_inline"]["file_id"]
									bot.uploadAvatar_replay(target,FiLes_ID)
									bot.sendMessage(target, 'پروفایل گروه با موفقیت تغیر یافت ✅',message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, '❌ شما اجازه تغیر پرفایل گروه را ندارید',message_id=msg.get("message_id"))
							except:
								print("err change profile group")

						elif msg.get("text").startswith("آپدیت لینک") and msg.get("author_object_guid") in admins:
							try:
								rules = open("linkgap_arianbot/linker.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت لینک")))
								bot.sendMessage(target,  "✅آپدیت شد ", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "مشکلی پیش اومد مجددا تلاش کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "سنجاق" and msg.get("author_object_guid") in admins :
							try:
								bot.pin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg.get("message_id"))
							except:
								print("err pin")

						elif msg.get("text") == "برداشتن سنجاق" and msg.get("author_object_guid") in admins :
							try:
								bot.unpin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر از سنجاق برداشته شد!", message_id=msg.get("message_id"))
							except:
								print("err unpin")

						elif msg.get("text").startswith("!trans"):
							try:
								responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
								al = [responser["result"]]
								bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								pass


						elif msg.get("text").startswith("!font"):
							try:
								response = urllib.request.urlopen(f"http://api.codebazan.ir/font/?text={msg.get('text').split()[1]}")
								parsing = json.load(response)
								bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(parsing["result"].values())[:110])).text
								sleep(1)
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								pass

						elif msg.get("text").startswith("حروف"):
							try:
								responser = urllib.request.urlopen(f"https://api.codebazan.ir/num/?num={msg.get('text').split()[1]}")
								parsing = json.load(responser)
								al = [parsing["result"]["num"]]
								bot.sendMessage(target, "عدد شما به حروف:\n\n\n"+"".join(al), message_id=msg.get("message_id")).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								pass


						elif msg.get("text").startswith("واژه"):
							try:
								responser = get(f"https://api.codebazan.ir/vajehyab/?text={msg.get('text').split()[1]}").json()
								aww = responser["result"]["mani"]
								awd = responser["result"]["fa"]
								awv = responser["result"]["Fdehkhoda"]
								bot.sendMessage(target, f"کلمه مورد نظر شما: {awd}\n\nمعنی کلمه: {aww}\n\nمعنی کلمه در دهخدا: {awv}", message_id=msg.get("message_id")).text
							except:
								pass


						elif msg.get("text").startswith("عید"):
							try:
								responser = urllib.request.urlopen(f"https://api.codebazan.ir/new-year/")
								parsing = json.load(responser)
								al = [parsing["day"]]
								bot.sendMessage(target, "روز های مانده به عید 🌺\n"+"day: "+"".join(al), message_id=msg.get("message_id")).text
							except:
								pass


						elif msg.get("text").startswith("جوک") or msg.get("text").startswith("jok") or msg.get("text").startswith("!jok"):
							try:
								response = get("https://api.codebazan.ir/jok/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg["text"].startswith("arz"):
							try:
								response = get(f"http://api.codebazan.ir/arz/?type={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:50])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								pass


						elif msg.get("text").startswith("پسورد"):
							try:
								response = get(f"http://api.codebazan.ir/password/?length={msg['text'].split()[1]}").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("ویکی"):
							try:
								response = get(f"http://api.codebazan.ir/wiki/?search={msg['text'].split()[1]}").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass


						elif msg.get("text").startswith("ذکر") or msg.get("text").startswith("zekr") or msg.get("text").startswith("!zekr"):
							try:
								response = get("http://api.codebazan.ir/zekr/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("نام شاخ"):
							try:
								response = get("https://api.codebazan.ir/name/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("!chistan"):
							try:
								response = get("https://api.codebazan.ir/chistan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("حدیث") or msg.get("text").startswith("hadis") or msg.get("text").startswith("!hadis"):
							try:
								response = get("http://api.codebazan.ir/hadis/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("بیو") or msg.get("text").startswith("bio") or msg.get("text").startswith("!bio"):
							try:
								response = get("https://api.codebazan.ir/bio/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg["text"].startswith("!weather"):
							try:
								response = get(f"https://api.codebazan.ir/weather/?city={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								pass

						elif msg.get("text").startswith("دیالوگ"):
							try:
								response = get("http://api.codebazan.ir/dialog/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("دانستنی متن"):
							try:
								response = get("http://api.codebazan.ir/danestani/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("پ ن پ") or msg.get("text").startswith("!pa-na-pa") or msg.get("text").startswith("په نه په"):
							try:
								response = get("http://api.codebazan.ir/jok/pa-na-pa/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("الکی مثلا") or msg.get("text").startswith("!alaki-masalan"):
							try:
								response = get("http://api.codebazan.ir/jok/alaki-masalan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("داستان") or msg.get("text").startswith("!dastan"):
							try:
								response = get("http://api.codebazan.ir/dastan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								pass

						elif msg.get("text").startswith("!ping"):
							try:
								responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
								bot.sendMessage(target, responser,message_id=msg["message_id"])
							except:
								pass

						elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
							try:
								print("Yek ahmagh forwared Zad")
								bot.deleteMessages(target, [str(msg.get("message_id"))])
								print("tabligh forearedi pak shod")
							except:
								print("err delete forwared")

						elif msg.get("text") == "قوانین":
							try:
								rules = open("rules_arianbot/rules.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
								bot.sendMessage(msg.get("author_object_guid"),str(rules))
							except:
								print("err ghanon")

						elif msg.get("text") == "راهنما":
							try:
								G_U = msg.get("author_object_guid")
								ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
								NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
								if ID_karbar != None:
									ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
								else:
									if NAME_karbar != None:
										ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
									else:pass
								G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
								if msg.get("author_object_guid") in ozv_ajbar:
									rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
									bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
							except:
								try:
									G_U = msg.get("author_object_guid")
									ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
									NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
									if ID_karbar != None:
										ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
									else:
										if NAME_karbar != None:
											ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
										else:pass
									G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
									if msg.get("author_object_guid") in ozv_ajbar:
										rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
										bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
									else:
										bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
								except:
									print("err rahnama")



						elif msg.get("text") == "سازندت کیه":
							try:
								building = open("biowq.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, str(building), message_id=msg.get("message_id"))
							except:
								print("err building bot")

						elif msg.get("text").startswith("آپدیت قوانین") and msg.get("author_object_guid") in admins:
							try:
								rules = open("rules_arianbot/rules.txt","w",encoding='utf-8').write(str(msg.get("text").strip("آپدیت قوانین")))
								bot.sendMessage(target, "✅  قوانین بروزرسانی شد", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 10" or msg.get("text") == "حالت ارام 10" and msg.get("author_object_guid") in admins:
							try:
								number = 10
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 30" or msg.get("text") == "حالت ارام 30" and msg.get("author_object_guid") in admins:
							try:
								number1 = 30
								bot.setGroupTimer(target,number1)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number1)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 60" or msg.get("text") == "حالت ارام 60" and msg.get("author_object_guid") in admins:
							try:
								number2 = 60
								bot.setGroupTimer(target,number2)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number2)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 80" or msg.get("text") == "حالت ارام 80" and msg.get("author_object_guid") in admins:
							try:
								number3 = 80
								bot.setGroupTimer(target,number3)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number3)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت ارام 100" or msg.get("text") == "حالت آرام 100" and msg.get("author_object_guid") in admins:
							try:
								number4 = 100
								bot.setGroupTimer(target,number4)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number4)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 3600" or msg.get("text") == "حالت ارام 3600" and msg.get("author_object_guid") in admins:
							try:
								number5 = 3600
								bot.setGroupTimer(target,number5)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number5)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 300" or msg.get("text") == "حالت ارام 300" and msg.get("author_object_guid") in admins:
							try:
								number6 = 300
								bot.setGroupTimer(target,number6)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number6)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 7200" or msg.get("text") == "حالت ارام 7200" and msg.get("author_object_guid") in admins:
							try:
								number7 = 7200
								bot.setGroupTimer(target,number7)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number7)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "حالت آرام 18000" or msg.get("text") == "حالت ارام 1800" and msg.get("author_object_guid") in admins:
							try:
								number8 = 18000
								bot.setGroupTimer(target,number8)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number8)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))


						#test send image

						#image

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number = 0
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number1 = 0
								bot.setGroupTimer(target,number1)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number2 = 0
								bot.setGroupTimer(target,number2)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number3 = 0
								bot.setGroupTimer(target,number3)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number4 = 0
								bot.setGroupTimer(target,number4)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number5 = 0
								bot.setGroupTimer(target,number5)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number6 = 0
								bot.setGroupTimer(target,number6)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number7 = 0
								bot.setGroupTimer(target,number7)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins:
							try:
								number8 = 0
								bot.setGroupTimer(target,number8)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("اخطار") and msg.get("author_object_guid") in admins:
							try:
								mesagidhoshdar = msg.get("message_id")
								user = msg.get("text").split(" ")[1][1:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									alert(guid,user)

								else :
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))

							except IndexError:
								mesagidhoshdar = msg.get("reply_to_message_id")
								guid = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								if not guid in admins:
									alert(guid,user)
								else:
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))



						elif msg.get("text") == "قفل گروه" or msg.get("text") == "قفل کردن گپ" or msg.get("text") == "قفل"  and msg.get("author_object_guid") in admins :
							try:
								bot.setMembersAccess(target, ["AddMember"])
								bot.sendMessage(target, "🔒 گروه قفل شد", message_id=msg.get("message_id"))
							except:
								print("err lock GP")

						elif msg.get("text") == "بازکردن گروه" or msg.get("text") == "باز کردن گپ" or msg.get("text") == "باز" and msg.get("author_object_guid") in admins :
							try:
								bot.setMembersAccess(target, ["SendMessages","AddMember"])
								bot.sendMessage(target, "🔓 گروه اکنون باز است", message_id=msg.get("message_id"))
							except:
								print("err unlock GP")

					else:
						if msg.get("text") == "روشن" or msg.get("text") == "\start":
							try:
								if msg.get("author_object_guid") in admins:
								   sleeped = False
								   bot.sendMessage(target, "ربا‌ت با موفقیت روشن شد!", message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target, '❌ اجازه دسترسی به شما داده نشد',message_id=msg.get("message_id"))
							except:
								print('error one bot')

				elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
					name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
					data = msg['event_data']
					if data["type"]=="RemoveGroupMembers":
						try:
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"‼️ کاربر {user} با موفقیت از گروه حذف شد .\nساعت حذف کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}", message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							print("err rm member answer")

					elif data["type"]=="AddedGroupMembers":
						try:
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							p = Image.open('R.png')
							bot.sendPhoto(target, 'picture_newmember/R.png', p.size,caption=  f"هــای {user} عزیز 😘🌹 \n • به گـروه {name} خیـلی خوش اومدی 😍❤️ \nلطفا قوانین رو رعایت کن .\n\nساعت ورود کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}\n\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی!\nدوست داری ربات بسازی؟ بیا اینجا😍👇\nسازنده:\narianBOT\nآرین عباسی" , message_id=msg["message_id"])
							print(Fore.GREEN+" sended new AddMember photo")
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							try:
								user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
								p = Image.open('picture_newmember/R.png')
								bot.sendPhoto(target, 'picture_newmember/R.png', p.size,caption=  f"هــای {user} عزیز 😘🌹 \n • به گـروه {name} خیـلی خوش اومدی 😍❤️ \nلطفا قوانین رو رعایت کن .\n\nساعت ورود کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}\n\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی!\nدوست داری ربات بسازی؟ بیا اینجا😍👇\nسازنده:\narianBOT\nآرین عباسی" , message_id=msg["message_id"])
								print(Fore.GREEN+" sended new AddMember photo")
							except:
								print("err add group member")

					elif data["type"]=="LeaveGroup":
						try:
							user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
							bot.sendMessage(target, f"خدانگهدار {user} 👋 ", message_id=msg["message_id"])
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							try:
								user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
								bot.sendMessage(target, f"خدانگهدار {user} 👋 ", message_id=msg["message_id"])
							except:
								print("err lef")


					elif data["type"]=="JoinedGroupByLink":
						try:
							user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
							p = Image.open('R.png')
							bot.sendPhoto(target, 'picture_newmember/R.png', p.size,caption=  f"هــای {user} عزیز 😘🌹 \n • به گـروه {name} خیـلی خوش اومدی 😍❤️ \nلطفا قوانین رو رعایت کن .\n\nساعت ورود کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}\n\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی!\nدوست داری ربات بسازی؟ بیا اینجا😍👇\nسازنده:\narianBOT\nآرین عباسی" , message_id=msg["message_id"])
							print(Fore.GREEN+"sended new JoinedGroupByLink photo")
							# bot.deleteMessages(target, [msg["message_id"]])
						except:
							try:
								user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
								p = Image.open('picture_newmember/R.png')
								bot.sendPhoto(target, 'picture_newmember/R.png', p.size,caption=  f"هــای {user} عزیز 😘🌹 \n • به گـروه {name} خیـلی خوش اومدی 😍❤️ \nلطفا قوانین رو رعایت کن .\n\nساعت ورود کاربر: {time.localtime().tm_sec} : {time.localtime().tm_min} : {time.localtime().tm_hour}\n\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی!\nدوست داری ربات بسازی؟ بیا اینجا😍👇\nسازنده:\narianBOT\nآرین عباسی" , message_id=msg["message_id"])
								print(Fore.GREEN+"sended new JoinedGroupByLink photo")
							except:
								print("err answer join By link")

				else:
					if "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("message_id")])
						guid = msg.get("author_object_guid")
						user = bot.getUserInfo(guid)["data"]["user"]["username"]
						alert(guid,user,True)
						bot.deleteMessages(target, [msg.get("message_id")])

					else:
						if msg["type"] =="Sticker" and not msg.get("message_id") in answered and not msg.get("author_object_guid") in admins:
							if lock_Sticker == True:
								guid_st = msg.get("author_object_guid")
								user_st = bot.getUserInfo(guid_st)["data"]["user"]["username"]
								alert_sticker(guid_st,user_st)
								sleep(1)
								bot.deleteMessages(target, [msg.get("message_id")])
							else:
								pass

						else:
							if msg["file_inline"]["type"] =="Gif" and not msg.get("message_id") in answered and not msg.get("author_object_guid") in admins:
								if lock_GIF == True:
									guid_GF = msg.get("author_object_guid")
									user_GF = bot.getUserInfo(guid_GF)["data"]["user"]["username"]
									alert_GIF(guid_GF,user_GF)
									sleep(1)
									bot.deleteMessages(target, [msg.get("message_id")])
								else:
									pass


					continue
			except:
				continue
			answered.append(msg.get("message_id"))
	except:
		continue
