from requests_html import HTMLSession
url="https://idollist.idolmaster-official.jp/search"
a765=[]
cg=[]
ml=[]
sm=[]
sc=[]
other=[]
session = HTMLSession()
r=session.get(url)
idol=r.html.xpath("//*[@id=\"search\"]/div[2]/div[5]/ul/li")
for elem in idol:
    link=elem.find("a",first=True).links
    #id=link.split('/',4)
    print(link)
    try:
        className=elem.attrs['class'][2]
        if className=='imas':
            pass
        elif className=='deremas':
            pass
    except IndexError:
        print("other")