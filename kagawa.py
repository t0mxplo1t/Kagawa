import urllib,json,ipaddress

from urllib import request
from ipaddress import IPv4Address,IPv6Address

url = "http://ip-api.com/json/"

def banner():
	print("""
\033[1;32m ____  __.
\033[1;32m|    |/ _|____     _________  __  _  _______
\033[1;0m|      < \__  \   / ___\__  \ \ \/ \/ /\__  \ 
\033[1;0m|    |  \ / __ \_/ /_/  > __ \_\     /  / __ \_
\033[1;33m|____|__ (____  /\___  (____  / \/\_/  (____  /
\033[1;33m        \/    \//_____/     \/              \/
\033[0m+-----------------------------------------+
| \033[1;32mMr. Tom\033[0m | \033[1;32mhttps://github.com/14sept2002\033[0m |
+-----------------------------------------+""")
banner()

def result():
	print("\033[32mTracking\033[0m",extract['status'])
	print("\033[32mIP\033[0m",extract['query'])
	print("\033[32mCountry\033[0m",extract['country'])
	print("\033[32mCountry code\033[0m",extract['countryCode'])
	print("\033[32mRegion\033[0m",extract['region'])
	print("\033[32mRegion name\033[0m",extract['regionName'])
	print("\033[32mCity\033[0m",extract['city'])
	print("\033[32mZIP code\033[0m",extract['zip'])
	print("\033[32mLatitude\033[0m",extract['lat'])
	print("\033[32mLongitude\033[0m",extract['lon'])
	print("\033[32mTime zone\033[0m",extract['timezone'])
	print("\033[32mISP\033[0m",extract['isp'])
	print("\033[32mOrg\033[0m",extract['org'])
	print("\033[32mASN\033[0m",extract['as'])

try:
	choice = input("""
+---------------------------------+
| \033[41m>>> Choice <<<\033[0m                  |
+---------------------------------+
| \033[32mA.\033[0m | \033[32mIPv4 \033[33m[192.168.xxx.xxx]\033[0m     |
| \033[32mB.\033[0m | \033[32mIPv6 \033[33m[2000:abcd:4000:efgh]\033[0m |
+---------------------------------+
\033[41mEnter your choice [A/B]\033[0m """)

	if choice == "A":
		x = input("\n\033[33mIP \033[0m: ")
		ip_four = IPv4Address(x)
		open = request.urlopen(url+x)
		r = open.read()
		extract = json.loads(r)

		print(x)
		print("\033[32mPublic IP\033[0m", ip_four.is_global)
		print("\033[32mPrivate IP\033[0m", ip_four.is_private)
		print("\033[32mVersion\033[0m", ip_four.version)
		print("\033[32mBit\033[0m", ip_four.max_prefixlen)
		result()

	elif choice == "B":
		y = input("\n\033[33mIP \033[0m: ")
		ip_six = IPv6Address(y)
		open = request.urlopen(url+y)
		r = open.read()
		extract = json.loads(r)

		print(y)
		print("\033[32mPublic IP\033[0m", ip_six.is_global)
		print("\033[32mPrivate IP\033[0m", ip_six.is_private)
		print("\033[32mVersion\033[0m", ip_six.version)
		print("\033[32mBit\033[0m", ip_six.max_prefixlen)
		result()

	else:
		print("\033[32mNo options available!")

except KeyboardInterrupt:
	print("\033[32mThanks for using!")

except EOFError:
	print("\033[32mI understand!")
