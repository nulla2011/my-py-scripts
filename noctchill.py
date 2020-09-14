import requests
import time
import ctypes
url='https://shinycolors.idolmaster.jp/idol/noctchill/'
url="https://starlit-season.idolmaster.jp/images/idol/ill/asahi-serizawa.png"
while (True):
	n=requests.get(url, allow_redirects=False)
	print (n.status_code)
	if (n.status_code==200):
		player = ctypes.windll.kernel32
		player.Beep(1000,800)
	time.sleep(120)