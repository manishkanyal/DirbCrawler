#!/usr/bin/python3
""" 
*** DirbCrawler***
Author: Manish Kanyal
 
DirbCrawler is a python version of DirBuster which brute-forces and enumerates directories within a website. 
You can add your directory wordlist and by default a wordlist is also provided. 

You need python3 to run DirbCrawler
"""


#To check if all required modules are present or not
try:
	import sys
	import requests
	import argparse
	import os
	from requests.packages.urllib3.exceptions import InsecureRequestWarning
except:
	print("[-] Requirement not satisfied. For more info check requirement.txt")


#To determine python version running in your system
if sys.version_info < (3,0):
    print("[-] Sorry requires python 3.x")
    sys.exit(1)

# To Suppress SSL certificate warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Useragent headers used throughout the script
headers = {"User-Agent" : "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"}

#wordlist check
def wordlist_check(wordlist):
	try:
		path=os.path.exists(wordlist)
		if not path:
			print("[-] Sorry ! Wordlist doesn't exist at specified path ")
			sys.exit()
	except KeyboardInterrupt:
			print("\n[-] Keyboard Interrupt detected\n[-] Exiting now... ")	
			sys.exit()
	except:
		print("[-] Error detected\n[-] Exiting now... ")
		sys.exit()

#Used for increasing verbosity. We can verbose only for once	
def dprint(msg):
	if args.v:
		print(msg)


# directory brute forcing
def brute_forcing(domain,SSL,wordlist):
	host = requests.models.Response()
	wordlist_check(wordlist)
	word=open(wordlist,"r")
	line=word.readlines()
	if SSL=="TRUE":
		for l in line:
			url = "https://" + domain + "/" + l.strip()
			
			try:
				host=requests.get(url = url, headers = headers , verify = False)
			except requests.ConnectionError:
				print("[-] Connection Error occured\n[-] Exiting now...")
				sys.exit()
			except ConnectTimeout:
				print("[-] Connection Time Out \n[-] Exiting now...")
				sys.exit()
			except KeyboardInterrupt:
				print("\n[-] Keyboard Interrupt detected\n[-] Exiting now... ")	
				sys.exit()
			except:
				print("[-] Error occured\n[-] Exiting now...")
				sys.exit()
				
			if host.status_code==200:
				print("[+] {} Valid path found  :-  {}".format(host.status_code,url))
			else:
				dprint("[-] {} Path not found  :-  {}".format(host.status_code,url))
				
	else:
		for l in line:
			url = "http://" + domain + "/" + l.strip()
			
			try:
				host=requests.get(url=url,headers=headers)
			except requests.ConnectionError:
				print("[-] Connection Error occured\n[-] Exiting now...")
				sys.exit()
			except ConnectTimeout:
				print("[-] Connection Time Out \n[-] Exiting now...")
				sys.exit()
			except KeyboardInterrupt:
				print("\n[-] Keyboard Interrupt detected\n[-] Exiting now... ")	
				sys.exit()
			except:
				print("[-] Error occured\n[-] Exiting now...")
				sys.exit()
				
			if host.status_code==200:
				print("[+] {} Valid path found  :-  {}".format(host.status_code,url))
			else:
				dprint("[-] {} Path not found  :-  {}".format(host.status_code,url))
		
			
	
# Checking Url if it is valid or not
def url_check(domain,SSL,wordlist):
	print("[*] Checking RHOST........",end=" ")
	if SSL == "TRUE":
		url="https://"+domain
		
		try:
			rhost=requests.get(url=url,headers=headers , verify = False)
		except requests.ConnectionError:
			print("[-] Connection Error occured\n[-] Exiting now...")
			sys.exit()
		except ConnectTimeout:
			print("[-] Connection Time Out \n[-] Exiting now...")
			sys.exit()
		except InvalidURL:
			print("[-] Provided URL is invalid somehow\n[-] Exiting now...")
			sys.exit()
		except KeyboardInterrupt:
			print("\n[-] Keyboard Interrupt detected\n[-] Exiting now... ")	
			sys.exit()
		except:
			print("[-] Error occured\n[-] Exiting now...")
			sys.exit()
					
		if rhost.status_code==200:
			print("Done\n")
			brute_forcing(domain,SSL,wordlist)
		else:
			print("Fail")
			dprint("[-] Error: Cannot reach Host {}".format(domain))
			sys.exit()
			
	else:
		url = "http://" + domain
		
		try:
			rhost=requests.get(url=url,headers=headers)
		except requests.ConnectionError:		
			print("[-] Connection Error occured\n[-] Exiting now...")
			sys.exit()
		except ConnectTimeout:
				print("[-] Connection Time Out \n[-] Exiting now...")
				sys.exit()
		except InvalidURL:
			print("[-] Provided URL is invalid somehow\n[-] Exiting now...")
			sys.exit()
		except KeyboardInterrupt:
			print("\n[-] Keyboard Interrupt detected\n[-] Exiting now... ")	
			sys.exit()
		except:
			print("Error occured\n[-] Exiting now...")
			sys.exit()
			
			
		if rhost.status_code==200:
			print("Done\n")
			brute_forcing(url,SSL,wordlist)
		else:
			print("Fail")
			dprint("[-] Error: Cannot reach Host {}".format(domain))
			sys.exit()		
	
# Taking arguments	
def get_arguments():
	try:
		parser=argparse.ArgumentParser()
		parser.add_argument("-d","--domain",help="Specify domain name ")
		parser.add_argument("-w","--wordlist",help="Specify path of wordlist to use with extension",default="wordlist.txt")
		parser.add_argument("-s","--SSL",default="False",help="Specify SSL certificate is True or False . By default is False")
		parser.add_argument("-v" , help="Verbose output" , action="store_true")
		
		args=parser.parse_args()
		
		ssl=args.SSL.upper()
		if not args.domain:
			parser.error("[-] Specify domain name,for more information use --help option")
			sys.exit()
		elif ssl not in ["TRUE" , "FALSE"]:
			parser.error("[-] Invalid SSL parameter,for more information use --help option")
			sys.exit()
		else:
			return args
	except KeyboardInterrupt:
		print("\n[-] Keyboard Interrupt detected\n[-] Exiting now... ")	
		sys.exit()
	except:
		print("[-] Error detected...\n[-] Exting now...")   



def crawl():
	result=pyfiglet.figlet_format("dirbCrawler")
	print(result)
	print("[*] Input url in this form www.xyz.com")
	print("[*] Happy Hunting....\n")

                                                       
try:
	import pyfiglet
except:
	print("--------------------------------------------------------------------------------------------------\n\n\n")
	print("                        _ _      _      ____                    _           ")
	print("                     __| (_)_ __| |__  / ___|_ __ __ ___      _| | ___ _ __ ")
	print("                    / _` | | '__| '_ \| |   | '__/ _` \ \ /\ / / |/ _ \ '__|")
	print("                   | (_| | | |  | |_) | |___| | | (_| |\ V  V /| |  __/ |")   
	print("                    \__,_|_|_|  |_.__/ \____|_|  \__,_| \_/\_/ |_|\___|_| \n\n\n\n")
	print("--------------------------------------------------------------------------------------------------\n") 
	print("[*] Input url in like this www.xyz.com")
	print("[*] Happy Hunting....\n")
else:
	crawl()


#main function
if __name__=="__main__":	
	args=get_arguments()
	url_check(args.domain,args.SSL.upper(),args.wordlist)		

	
	
	
	
