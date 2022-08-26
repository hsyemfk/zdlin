print("⚠️کاربران گرامی شما حق ویرایش یا ادیت سورس پایتون آرین بات را ندارید درصورت مشاهده آپدیت های سورس بنده دراختیار شما قرار نمی گیرد⚠️")


from requests import get
from re import findall
import os
import glob
from libraryArsein.Arsein import Robot_Rubika
import requests
import json
from json import loads , dumps
import time
from time import sleep
import random
import urllib.request
import io
from random import choice,randint
from PIL import Image

#staticvariable
answered,sleeped,blacklist,alerts,lock_fosh = [] , False , [] , [] , False


def my_auth():
	while(1):
		try:
			with open(f"AppName.json", "r") as file:
				jget = json.load(file)
				s = jget["data"]["auth"]
				Bot.registerDevice(s)
				return s

		except:continue

def delete_fosh(fosh):
	saveData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in fosh:
			saveData = [True, i]
			break
		else: continue
	return saveData

def hasAds(PY):
	links = ["http://","https://",".ir",".com",".org",".net",".me"]
	for TAB in links:
		if TAB in PY:
			return True

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


#شناسه اکانت
bot = Robot_Rubika("htvtmtmsvwazhdxzcvdbzmhomtceeppd")
#......
#شناسه گروه
target = "g0Bb18B06f7c85e83c00d8b62fc2a4ac"
#......
#شناسه کانال
channell = "c0s8Q60cff0af820f01376b4b2ca3563"



while(1):
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		name_admins = [i["first_name"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]

		while(1):
			try:
				messages = bot.getChatsUpdate()
				break
			except:
				continue

		for x in messages:
			try:
				if x['last_message']['type'] == "Text" and x["abs_object"]["type"] == "User" or x['object_guid'] == target:
					if not x['last_message']['message_id'] in answered:
						print("messages:" +" "+"[" + x['object_guid'] +"]" + ">>>" + " " + "(" + x['last_message']['text']+ ")"  + "\n")
						msg = x["last_message"]
						if msg.get("text").startswith("عجب"):
							try:
								bot.sendMessage(x['object_guid'], "مش رجب 😓", message_id=msg.get("message_id"))
							except:print('error restart bot')

						elif msg.get("text").startswith("خوبی") or msg.get("text").startswith("خبی"):
							try:
								bot.sendMessage(x['object_guid'], "تو چطوری؟🤪", message_id=msg.get("message_id"))
							except:print("err answer hay")

						elif msg.get("text").startswith("خش") or msg.get("text").startswith("خوشم") :
							try:
								bot.sendMessage(x['object_guid'], "همچنین عشقم😍🌹", message_id=msg.get("message_id"))
							except:print("err moharefe")

						elif msg.get("text").startswith("بوسم کن") or msg.get("text").startswith("بوس بده"):
							try:
								bot.sendMessage(x['object_guid'], "💋🙈", message_id=msg.get("message_id"))
							except:print("err bose")

						elif msg.get("text").startswith("🚶"):
							try:
								bot.sendMessage(x['object_guid'], "به این زودی میری🧐", message_id=msg.get("message_id"))
							except:print("ejab error")

						elif msg.get("text").startswith("ربات") or msg.get("text").startswith("بات") or msg.get("text").startswith("رباط") or msg.get("text").startswith("باط"):
							try:
								rew = ["⛑️\n😁\n👔🌻\n👖🖱 \n در خدمتم","🧢\n😆\n🥋🌷\n👖🖱\nجان ربات 😁","👒\n😍\n🧥🌼\n👖 \n جون ربات گفتن 😍","🎩\n😎\n🥋💐\n👖\n⚽️\n جان کاری داشتید","🎓\n🙂\n🧥\n👖\n⚽️ \nجونم ربات بفرمایید 😍","🪖\n🤓\n👔\n👖\nجونم بفرمایید 🤩","⛑️\n😁\n👔🌻\n👖🖱 \n امری داری آدمین من","⛑️\n🙄\n👔🌻\n👖🖱 \n هاچیه","⛑️\n😌\n👔🌻\n👖🖱 \n چیه عشقم؟","⛑️\n🤒\n👔🌻\n👖🖱 \n صدام کردی عمر من؟","⛑️\n😯\n👔🌻\n👖🖱 \n به به وجودم صدام کرده",]
								renn= choice(rew)
								bot.sendMessage(x['object_guid'], f"{renn}", message_id=msg.get("message_id"))
							except:print("error robot")

						elif msg.get("text") == "منشن":
							try:
								msg_ide = bot.getMessagesInfo(x['object_guid'], [x['last_message']['message_id']])[0]
								if 'reply_to_message_id' in msg_ide.keys():
									GAPE = bot.getGroupInfo(target)["data"]["group"]["group_title"]
									guidu = bot.getMessagesInfo(target, [msg_ide.get("reply_to_message_id")])[0]["author_object_guid"]
									useru = bot.getUserInfo(guidu)["data"]["user"]["first_name"]
									caption =  f"{useru}"
									if not guidu in admins:
										bot.sendMessage(x['object_guid'],f"کاربر {caption} نام شما هایپر شد" , metadata=[{"from_index": 6,"length": len(caption),"type":"MentionText","mention_text_object_guid":guidu}], message_id=msg.get("message_id"))
									else:bot.sendMessage(x['object_guid'], f"کاربر {caption} نام شما هایپر شد", metadata=[{"from_index": 6,"length": len(caption),"type":"MentionText","mention_text_object_guid":guidu}], message_id=msg.get("message_id"))
							except:print('hiper karbar')

						elif msg.get("text").startswith("بپرس"):
							try:
								file = open("plays_arianbot/bepors.txt").read().split("\n")
								read = list(file)
								bot.sendMessage(x['object_guid'],choice(read), message_id=msg.get("message_id"))
							except:
								print("err bepors")

						elif hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								mesagidhoshdar = msg.get("message_id")
								guid = msg.get("author_object_guid")
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								alert(guid,user,True)
								bot.deleteMessages(target, [msg.get("message_id")])
							except:print("ejab links")

						elif msg.get("text") == "لیست آدمین ها" or msg.get("text") == "لیست ادمین ها" and x['object_guid'] == target:
							try:
								GAP = bot.getGroupInfo(target)["data"]["group"]["group_title"]
								for x in name_admins:
									open("admins.txt","a+",encoding='utf-8').write(str("AD:" + " " + x + "\n"))
									get_admins = open("admins.txt","r",encoding='utf-8').read()
								bot.sendMessage(target, f"لیست آدمین های گروه {GAP} به شرح زیر است:\n\n{get_admins}", message_id=msg.get("message_id"))
								os.remove('admins.txt')
							except:
								print("get admins in GAP")

						elif msg.get("text").startswith("قلب"):
							try:
								matn_r = ["hello","arianbot","robot"]
								galb = ["💜","💙","💚"]
								my_id = bot.sendMessage(target,choice(matn_r), message_id=msg.get("message_id"))
								get_id = my_id["data"]["message_update"]
								get__ID = get_id["message_id"]
								sleep(5)
								bot.editMessage(x['object_guid'],choice(galb),get__ID)
							except:
								print("err edit")


						elif msg.get("text").startswith("قفل فحش روشن") and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								lock_fosh = True
								bot.sendMessage(target, "با موفقیت قفل فحش روشن شد ✅", message_id=msg.get("message_id"))
							except:
								print("err lock fosh")

						elif msg.get("text").startswith("قفل فحش خاموش") and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								lock_fosh = False
								bot.sendMessage(target, "با موفقیت قفل فحش خاموش شد ✅", message_id=msg.get("message_id"))
							except:
								print("err unlock fosh")

						elif delete_fosh(msg.get("text"))[0] and not msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								if lock_fosh == True:
									print("yek ahmagh fohsh dad")
									bot.deleteMessages(target, [str(msg.get("message_id"))])
									print("fohsh pak shod")
								else:pass
							except:
								print("err del fohsh Bug")

						elif msg.get("text") == "قفل گروه" or msg.get("text") == "قفل کردن گپ" or msg.get("text") == "قفل"  and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								bot.setMembersAccess(target, ["AddMember"])
								bot.sendMessage(target, "🔒 گروه قفل شد", message_id=msg.get("message_id"))
							except:
								print("err lock GP")

						elif msg.get("text") == "بازکردن گروه" or msg.get("text") == "باز کردن گپ" or msg.get("text") == "باز" and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								bot.setMembersAccess(target, ["SendMessages","AddMember"])
								bot.sendMessage(target, "🔓 گروه اکنون باز است", message_id=msg.get("message_id"))
							except:
								print("err unlock GP")

						elif msg.get("text") == "حالت ارام" and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								number = 30
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای " +str(number)+ "ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						elif msg.get("text") == "برداشتن حالت آرام" or msg.get("text") == "برداشتن حالت ارام" and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								number = 0
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "لطفا دستور رو صحیح وارد کنید!", message_id=msg.get("message_id"))


						elif msg.get("text") == "برداشتن سنجاق" and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								msg_ide = bot.getMessagesInfo(x['object_guid'], [x['last_message']['message_id']])[0]
								if 'reply_to_message_id' in msg_ide.keys():
									bot.sendMessage(target, "پیام مورد نظر از سنجاق برداشته شد!", message_id=msg_ide.get("reply_to_message_id"))
									bot.unpin(target, msg_ide["reply_to_message_id"])
								else:pass
							except:
								print("err unpin")

						elif msg.get("text") == "سنجاق" and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								msg_ide = bot.getMessagesInfo(x['object_guid'], [x['last_message']['message_id']])[0]
								if 'reply_to_message_id' in msg_ide.keys():
									bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg_ide.get("reply_to_message_id"))
									bot.pin(target, msg_ide["reply_to_message_id"])
								else:pass
							except:
								print("err pin")


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
									bot.sendMessage(x['object_guid'], str(rules), message_id=msg.get("message_id"))
								else:
									bot.sendMessage(x['object_guid'],f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
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
										bot.sendMessage(x['object_guid'], str(rules), message_id=msg.get("message_id"))
									else:
										bot.sendMessage(x['object_guid'],f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
								except:
									print("err dastorat")

						elif msg.get("text").startswith("ارتقا") and msg.get("author_object_guid") in admins and x['object_guid'] == target:
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
								msg_ide = bot.getMessagesInfo(x['object_guid'], [x['last_message']['message_id']])[0]
								if 'reply_to_message_id' in msg_ide.keys():
									guidzz = bot.getMessagesInfo(target, [msg_ide.get("reply_to_message_id")])[0]["author_object_guid"]
									userz = bot.getUserInfo(guidzz)["data"]["chat"]["abs_object"]["object_guid"]
									textwaa = bot.getUserInfo(userz)["data"]["user"]["first_name"]
									if not userz in admins:
										bot.setGroupAdmin(target,userz)
										bot.sendMessage(target, f"کاربر {textwaa} با موفقیت آدمین شد", message_id=msg.get("message_id"))
									else:bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
								else:pass
							except:print('error setadmin')
							

						elif msg.get("text").startswith("تنزیل") and msg.get("author_object_guid") in admins and x['object_guid'] == target:
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
								msg_ide = bot.getMessagesInfo(x['object_guid'], [x['last_message']['message_id']])[0]
								if 'reply_to_message_id' in msg_ide.keys():
									guidzVz = bot.getMessagesInfo(target, [msg_ide.get("reply_to_message_id")])[0]["author_object_guid"]
									userVz = bot.getUserInfo(guidzVz)["data"]["chat"]["abs_object"]["object_guid"]
									textwaa = bot.getUserInfo(userVz)["data"]["user"]["first_name"]
									if  userVz in admins:
										bot.deleteGroupAdmin(target,userVz)
										bot.sendMessage(target, f"کاربر {textwaa} با موفقیت از آدمین بودن برکنار شد", message_id=msg.get("message_id"))
									else:bot.sendMessage(target, "❌ کاربر گرامی متاسفانه خطایی رخ داده است", message_id=msg.get("message_id"))
								else:pass
							except:print('error setdeletadmin')


						elif msg.get("text").startswith("جوک") or msg.get("text").startswith("jok") or msg.get("text").startswith("!jok"):
							try:
								response = get("https://api.codebazan.ir/jok/").text
								bot.sendMessage(x['object_guid'], response,message_id=msg.get("message_id"))
							except:pass

						elif msg.get("text").startswith("عید"):
							try:
								responser = urllib.request.urlopen(f"https://api.codebazan.ir/new-year/")
								parsing = json.load(responser)
								al = [parsing["day"]]
								bot.sendMessage(x['object_guid'], "روز های مانده به عید 🌺\n"+"day: "+"".join(al)).text
							except:pass

						elif msg.get("text").startswith("پسورد"):
							try:
								response = get(f"http://api.codebazan.ir/password/?length={msg['text'].split()[1]}").text
								bot.sendMessage(x['object_guid'], response,message_id=msg.get("message_id"))
							except:pass

						elif msg.get("text").startswith("بیو") or msg.get("text").startswith("bio") or msg.get("text").startswith("!bio"):
							try:
								response = get("https://api.codebazan.ir/bio/").text
								bot.sendMessage(x['object_guid'], response,message_id=msg.get("message_id"))
							except:pass

						elif msg.get("text").startswith("داستان") or msg.get("text").startswith("!dastan"):
							try:
								response = get("http://api.codebazan.ir/dastan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:pass

						elif msg.get("text").startswith("دانستنی متن"):
							try:
								response = get("http://api.codebazan.ir/danestani/").text
								bot.sendMessage(x['object_guid'], response,message_id=msg.get("message_id"))
							except:pass

						elif msg.get("text").startswith("بن") and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									bot.banGroupMember(x['object_guid'], guid)
								else:bot.sendMessage(x['object_guid'], "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))

							except IndexError:
								msg_ide = bot.getMessagesInfo(x['object_guid'], [x['last_message']['message_id']])[0]
								if 'reply_to_message_id' in msg_ide.keys():
								 	getguidkr = bot.getMessagesInfo(target, [msg_ide.get("reply_to_message_id")])[0]["author_object_guid"]
								 	bot.banGroupMember(target, bot.getMessagesInfo(target, [msg_ide.get("reply_to_message_id")])[0]["author_object_guid"])
								else:pass
							except:bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("ازاد") and msg.get("author_object_guid") in admins and x['object_guid'] == target:
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									usernamep = bot.getUserInfo(guid)["data"]["user"]["first_name"]
									bot.unbanGroupMember(x['object_guid'], guid)
									bot.sendMessage(target,   f"کاربر {usernamep} با موفقیت آزاد شد", message_id=msg.get("message_id"))
								else:bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))

							except IndexError:
								msg_ide = bot.getMessagesInfo(x['object_guid'], [x['last_message']['message_id']])[0]
								if 'reply_to_message_id' in msg_ide.keys():
								 	getguidkr = bot.getMessagesInfo(target, [msg_ide.get("reply_to_message_id")])[0]["author_object_guid"]
								 	username = bot.getUserInfo(getguidkr)["data"]["user"]["first_name"]
								 	bot.unbanGroupMember(target, bot.getMessagesInfo(target, [msg_ide.get("reply_to_message_id")])[0]["author_object_guid"])
								 	bot.sendMessage(target,   f"کاربر {username} با موفقیت آزاد شد", message_id=msg.get("message_id"))
								else:pass
							except:bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))


						elif msg.get("text").startswith("افزودن") and x['object_guid'] == target:
							try:
								guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
								if guid in blacklist:
									if msg.get("author_object_guid") in admins:
										alerts.remove(guid)
										alerts.remove(guid)
										alerts.remove(guid)
										blacklist.remove(guid)

										bot.invite(target, [guid])
									else:bot.sendMessage(target, "❌ کاربر محدود میباشد", message_id=msg.get("message_id"))
								else:bot.invite(target, [guid])
							except IndexError:bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
							except:bot.sendMessage(target, "❌ دستور اشتباه", message_id=msg.get("message_id"))


						elif msg.get("text") == '1 عضو جدید به گروه افزوده شد.' and x['object_guid'] == target:
							try:
								Group = bot.getGroupInfo(x['object_guid'])["data"]["group"]["group_title"]
								bot.sendMessage(x['object_guid'], f"خوش آمدی کاربر گرامی انشالله از گروه {Group} لذت ببری😍❤️", message_id=msg.get("message_id"))
							except:print("err add group member")

						elif msg.get("text") == 'یک عضو گروه را ترک کرد.' and x['object_guid'] == target:
							try:
								bot.sendMessage(x['object_guid'], "یک عضو بی مصرف گروه را ترک کرد 😿💔", message_id=msg.get("message_id"))
							except:print("err lef")

						elif msg.get("text") == '1 عضو از گروه حذف شد.' and x['object_guid'] == target:
							try:
								bot.sendMessage(x['object_guid'], "یک عضو بی مصرف از گروه حذف شد 😎👐", message_id=msg.get("message_id"))
							except:print("err rm member answer")

						elif msg.get("text") == 'یک عضو از طریق لینک به گروه افزوده شد.' and x['object_guid'] == target:
							try:
								Group = bot.getGroupInfo(x['object_guid'])["data"]["group"]["group_title"]
								bot.sendMessage(x['object_guid'], f"خوش آمدی کاربر گرامی انشالله از گروه {Group} لذت ببری😍❤️", message_id=msg.get("message_id"))
							except:print("err answer join By link")

					else:pass
				else:
					if "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins and x['object_guid'] == target:
						bot.deleteMessages(target, [msg.get("message_id")])
						guid = msg.get("author_object_guid")
						user = bot.getUserInfo(guid)["data"]["user"]["username"]
						alert(guid,user,True)
						bot.deleteMessages(target, [msg.get("message_id")])
					else:pass
			except:pass
			answered.append(x['last_message']['message_id'])
	except:continue