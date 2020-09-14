ma=(2*3600+20*60+48)//2
with open("M:/mobile/bn.txt",'w') as f:
    for i in range(0,ma):
        if i<10:
            f.write("https://d3rlyceqcs08f.cloudfront.net/live/bnef_high_0000"+str(i)+".ts\n")
        else:
            if i<100:
                f.write("https://d3rlyceqcs08f.cloudfront.net/live/bnef_high_000"+str(i)+".ts\n")
            else:
                if i<1000:
                    f.write("https://d3rlyceqcs08f.cloudfront.net/live/bnef_high_00"+str(i)+".ts\n")
                else:
                    f.write("https://d3rlyceqcs08f.cloudfront.net/live/bnef_high_0"+str(i)+".ts\n")