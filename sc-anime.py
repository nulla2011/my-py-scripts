import requests

url_static = "https://campaign-shinycolors.idolmaster.jp/ssr2020/static/media/"


def is404(url):
    h = requests.head(url, allow_redirects=False)
    if (h.status_code == 404):
        return True
    else:
        return False


for n in range(1, 24):
    i = 1
    while True:
        url = f"{url_static}{str(n).zfill(2)}_{i}memory.mp4"
        if is404(url):
            break
        with open("list.txt", "a+") as f:
            f.write(url + "\n")
        i += 1
    i = 1
    while True:
        url = f"{url_static}{str(n).zfill(2)}_{i}staging.mp4"
        if is404(url):
            break
        with open("list.txt", "a+") as f:
            f.write(url + "\n")
        i += 1
