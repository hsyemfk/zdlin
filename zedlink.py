print("⚠️کاربران گرامی شما حق ویرایش یا ادیت سورس پایتون آرین بات را ندارید درصورت مشاهده آپدیت های سورس بنده دراختیار شما قرار نمی گیرد⚠️")



from rubika.client import Bot

#شناسه اکانت
bot = Bot("xffmaicbkrrlofhuysquscwmenjpriai")
#......
#شناسه گروه
target = "g0BbWVQ04efc221bc358b350870b9808"
#......


answer = []

def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me"]
	for i in links:
		if i in msg:
			return True

while (1):
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		v =  bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while(1):
			try:
				x = bot.getMessages(target,v)
				break
			except:continue

		for pay in x:
			try:
				if pay['type'] == 'Text' and not pay['message_id'] in answer:
					print("messages:" + "  " + pay['text'])
					if hasAds(pay.get("text")) and not pay.get("author_object_guid") in admins:
						bot.deleteMessages(target, [pay.get("message_id")])
						print("links pak shodand")
					else:pass
				else:
					if "forwarded_from" in pay.keys() and bot.getMessagesInfo(target, [pay.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not pay.get("author_object_guid") in admins:
						bot.deleteMessages(target, [pay.get("message_id")])
						print("forwards pak shodand")
					else:pass
			except:pass
			answer.append(pay['message_id'])
		else:pass
	except:pass