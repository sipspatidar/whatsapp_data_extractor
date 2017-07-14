import time
import re
import sqlite3
import datetime
import os
def list_Remove_Duplicates(x):
	return sorted(set(x))

def extract_link(msg):
	link = []
	for m in msg:
		m = m[0]
		result = re.findall( r'https://chat.whatsapp.com/.*\n', str(m))
		for m in result:
			link.append(m)
	return link
def write_into_file(link):
	fo = open(str(datetime.date.today())+str(int(time.time()))+".txt","a")
	i=0
	for invite_link in link:
		try:
			fo.write(invite_link)
			i=i+1
		except:
			print("Can't Write...")
	fo.close()
	print(str(i)+" Link Added")
def Main():
	aa = input("enter database name : ")
	conn = sqlite3.connect(aa)
	c = conn.cursor()
	offset = 0

	#c.execute("select data from messages where data like '%chat.whatsapp.com%' limit 100 offset "+str(offset)+"")
	c.execute("select data from messages where data like '%chat.whatsapp.com%'")
	msg = c.fetchall()
	#offset = offset + 100
	link = extract_link(msg)
	link = list_Remove_Duplicates(link)
	try:
		os.mkdir("links")
	except:
		print("links folder already exist")
	finally:
		os.chdir("links")
	write_into_file(link)

	print("Suceesfully File Created")
if __name__=='__main__':
	Main()