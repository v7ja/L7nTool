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
	   type1 = (aa+bb+'.'+dd)
	   type2 = (bb+aa+dd+bb)
	   type3 = (aa+aa+aa+bb)
	   type4 = (aa+aa+bb+aa)
	   type5 = (aa+bb+aa+aa)
      type6 = (bb+aa+aa+aa)
      type7 = ('.'+aa+bb+bb)
      type8 = ('_'+aa+bb+bb)
      type9 = ('.'+bb+aa+bb)
type10 = ('_'+bb+aa+bb)
type11 = ('.'+bb+aa+dd)
type11 = (aa+bb+dd)
				type12 = (aa+'_'+aa+aa)
				type13 = (aa+aa+aa+aa)
				type14 = (bb+'.'+bb+dd)
				type15 = (bb+'_'+bb+dd)
				type16 = (aa+aa+bb+dd)
				type17 = (aa+bb+aa+bb)
				type18 = (aa+dd+dd+aa)
				type19 = (aa+bb+bb+aa)
				type20 = (aa+aa+bb+'_')
				type21 = (aa+aa+aa+'_')
				type22 = ('_'+aa+aa+'_')
				type23 = ('_'+bb+bb+'_')
				type24 = ('_'+aa+bb+'_')
				type25 = ('.'+aa+aa+'_')
				type26 = ('.'+bb+aa+'_')
				type27 = (aa+'_'+aa+'_')
				type28 = (aa+'.'+bb+'_')
				type29 = (aa+'.'+'.'+aa)
				type30 = (aa+'.'+'.'+bb)
				type31 = (bb+'.'+'.'+aa)
				type32 = (bb+'.'+'.'+bb)
				type33 = (aa+'.'+bb)
				type34 = (bb+'.'dd)
abd = (type1,type2,type3,type4,type5,type6,type7,type8,type9,type10,type11,type12,type13,type14,type15,type16,type17,type18,type19,type20,type21,type22,type23,type24,type25,type26,type27,type28,type29,type30,type31,type32,type33,type34)
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
