import requests
import time
import ctypes
url='https://shinycolors.idolmaster.jp/pc/static/voices/24_nichika/nichika_01.mp3'
while (True):
	n=requests.get(url, allow_redirects=False)
	print (n.status_code)
	if (n.status_code==200):
		player = ctypes.windll.kernel32
		player.Beep(1000,800)
	time.sleep(60)