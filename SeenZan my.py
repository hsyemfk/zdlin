import rainbowtext, pyfiglet
from ar import info
print(rainbowtext.text(pyfiglet.figlet_format('A R  B O T')))
from rubika.client import Bot,clients
from json import loads,dumps
from requests import post
from colorama import Fore, Back , Style, init
import sys,time

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0./90)
from rubpy import Rubika
from re import findall
from time import sleep
import asyncio
# rubpy

bot = Rubika(info.auth)
channel_guid : str = info.guid

post_link: str = info.link_post

get_infos: list = [] # get post info
links = []


get_infos: list = [] # get post info
links = []

async def main():
	t: bool = False
	while(t != True):
		try:
			message_info: str = await bot.getLinkFromAppUrl(post_link)
			global get_infos
			get_infos.append(message_info['message_id'])
			get_infos.append(message_info['object_guid'])
			t: bool = True
		except:
			t: bool = False

	t: bool = False
	while(t!=True):
		try:
			messages : list = await bot.getMessagesInterval(channel_guid, await bot.getChannelLastMessageId(channel_guid))
			t:bool=True
		except:
			t:bool=False
	for msg in messages:
		try:
			msg = msg['text']
			group_link = findall(r"https://rubika.ir/joing/\w{32}", msg)
			for link in group_link:
				links.append(link)
		except: pass
	
	while(1):
		for link in links:
			sleep(0.5)
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
					group_guid:str= await bot.joinGroup(link)
					group_guid: str = group_guid.get('data').get('group').get('group_guid')
					t:bool=True
					count += 5
				except:
					t:bool=False
					count += 1
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
				#	await bot.sendMessage(group_guid, "تبلیغ")
					await bot.forwardMessages(get_infos[1], [get_infos[0]], group_guid)
					print(Fore.YELLOW+'   Sended Message to group  ')
					t:bool=True
					count+=5
				except:
					t:bool=False
					count+=1
			t:bool=False
			count:int=0
			limit:int=5
			while(count<5 and t!=True):
				try:
					await bot.leaveGroup(group_guid)
					t:bool=True
					count+=5
				except:
					t:bool=False
					count+=1

asyncio.run(main())