import random
import pyperclip
while True:
    n = input("input char number: ")
    st = ''
    rang = "9FFF"
    for i in range(0, int(n)):
        l = random.randint(0, int(rang, 16))
        st += chr(l)
    print(st)
    pyperclip.copy(st)
    print("copy success")
