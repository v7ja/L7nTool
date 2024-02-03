try:
	import requests
	import random
	import threading
	import pyfiglet
except:
	
	os.system('pip install requests')
	os.system('pip install random')
	os.system('pip install threading')
	os.system('pip install pyfiglet')

O = '\033[2;36m'
Le = pyfiglet.figlet_format(' climed [:] ')
print(O+Le)

a = 'qwertyuiopasdfghjklzxcvbnm1234567890'
b = 'qwertyuiopasdfghjklzxcvbnm1234567890'
id = input("\033[2;33m<<<\033[2;34mEnter Id\033[2;33m>>>\033[2;32m :\033[2;31m ")
token = input("\033[2;33m<<<\033[2;34mEnter Bot Token \033[2;33m>>> \033[2;32m:\033[2;31m ")
sessionid = input("EnTeR sEssioniD : ")
def Lev ():

	hea = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'user-agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html',
        'Cookie': 'sessionid='+sessionid,
    }
	while True:
	   aa = str("".join(random.choice(a)for x in range(1)))
	   bb = str("".join(random.choice(b)for x in range(1)))
	   dd = str("".join(random.choice(a)for x in range(1)))
	   c1 = (aa+bb+'.'+dd)
	   c2 = (bb+aa+dd+bb)
	   c3 = (aa+aa+aa+bb)
	   c4 = (aa+aa+bb+aa)
	   c5 = (aa+bb+aa+aa)
    c6 = (bb+aa+aa+aa)
    c7 = ('.'+aa+bb+bb)
    c8 = ('_'+aa+bb+bb)
    c9 = ('.'+bb+aa+bb)
    c10 = ('_'+bb+aa+bb)
    c11 = (aa+bb+dd)
				c12 = (aa+'_'+aa+aa)
				c13 = (aa+aa+aa+aa)
		  c14 = (bb+'.'+bb+dd)
				c15 = (bb+'_'+bb+dd)
			 c16 = (aa+aa+bb+dd)
			 c17 = (aa+bb+aa+bb)
			 c18 = (aa+dd+dd+aa)
				c19 = (aa+bb+bb+aa)
				c20 = (aa+aa+bb+'_')
		  c21 = (aa+aa+aa+'_')
				c22 = ('_'+aa+aa+'_')
				c23 = ('_'+bb+bb+'_')
				c24 = ('_'+aa+bb+'_')
			 c25 = ('.'+aa+aa+'_')
			 c26 = ('.'+bb+aa+'_')
				c27 = (aa+'_'+aa+'_')
				c28 = (aa+'.'+bb+'_')
				c29 = (aa+'.'+'.'+aa)
				c30 = (aa+'.'+'.'+bb)
				c31 = (bb+'.'+'.'+aa)
				c32 = (bb+'.'+'.'+bb)
				c33 = (aa+'.'+bb)
				c34 = (bb+'.'dd)
abd = (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34)
	   user = random.choice(abd)
	   tiko = f'https://www.tiktok.com/api/user/detail/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.32&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F109.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7193110014067459586&device_platform=web_pc&focus_state=true&from_page=user&history_len=10&is_fullscreen=false&is_page_visible=true&language=ar&os=mac&priority_region=&referer=&region=SA&screen_height=900&screen_width=1440tz_name=Asia%2FRiyadh&uniqueId={user}&verifyFp=verify_ldvov399_du9goymx_OHxC_4RTw_AEjU_Dth4CFGFw3lR&webcast_language=ar&msToken=f7RQRFGwBsu3WXbrhdLVX9gDRSynM_O_C7U9SX6WNqZqmb0QEsNO6H3dJ10pMAxt24bmyb2eMNPzUpr8w8-6Wx-xAawe1R6vbD6HZdDoWTPL4VOHo6ebwjHadXlUoyhG9ovbpBnhHipd_EWG&X-Bogus=DFSzswVY9D0ANeIIShUJbR/F6qHH&_signature=_02B4Z6wo00001xH2Y0gAAIDCaTiITAKYgosR9mfAAKeo28'
	   reqsnd = requests.get(tiko, headers=hea).text
	   if '"statusCode":10221,' in reqsnd:
	           print(f'{user} uSeR is Available!')
	           requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text="""cHecker v3.7 Tik 
hunt : {user}
Situation : Done"""")
	   else:
	   	print(f'{user} uSeR is NoT Available')
Threads=[] 
for t in range(2):
    x = threading.Thread(target=Lev)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
