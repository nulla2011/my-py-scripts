# coding: utf-8
from requests_html import HTMLSession
import time
from win10toast import ToastNotifier
url="https://u2.dmhy.org/promotion.php?action=torrent&id=39679" #promotion page,now is
cookie=''
with open('cookies.ck','r') as f:
    cookie=f.read()
headers={
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,ja;q=0.5",
    "cookie":cookie,
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
while True:
    session = HTMLSession()
    print("getting HTML...")
    r = session.get(url,headers=headers)
    sel="body > table.mainouter > tr > td.outer > table > tr > td > h3:nth-child(5) > img"
    sel2="body > table.mainouter > tr > td.outer > table > tr > td > h3:nth-child(5) > b:nth-child(5)"
    results = r.html.find(sel)
    results2 = r.html.find(sel2)
    h=r.html.html
    toaster = ToastNotifier()
    if(r.html.xpath("/html/head/title",first=True).text=="Access Point :: U2"):
        print("COOKIE ERROR!")
        toaster.show_toast("COOKIE ERROR!","check your cookie",duration=120)
    else:
        isPromotion=True
        try:
            status=results[0].attrs.get('alt')
        except IndexError:
            print("NO PROMOTION")
            isPromotion=False
        if isPromotion:
            if(status==""):
                print("ERROR")
                toaster.show_toast("ERROR!","ERROR!!!!!!!!!!!",duration=120)
            elif(status=="FREE" or status=="2X Free"):
                print("FREE!")
                toaster.show_toast("FREE!","FREE!!!!!!!!!!!",duration=120)
            elif (status=="50%" or status=="2X 50%"):
                print("50%")
                toaster.show_toast("50%","50%!!!!!!!!!!!",duration=120)
            elif (status=="30%"):
                print("30%")
                toaster.show_toast("30%","30%!!!!!!!!!!!",duration=120)
            elif(status=="Promotion"):
                if len(results2)==0:
                    print("ERROR!")
                    toaster.show_toast("ERROR!","ERROR!!!!!!!!!!!",duration=120)
                elif(results2[0].text=="0.00X"):
                    print("SPECIAL FREE!")
                    toaster.show_toast("SPECIAL FREE!","SPECIAL FREE!!!!!!!!!!!",duration=120)
                elif(float(results2[0].text[0:4])<1):
                    print("OTHER PROMOTION")
            else:
                print("NO PROMOTION")
    time.sleep(1800)