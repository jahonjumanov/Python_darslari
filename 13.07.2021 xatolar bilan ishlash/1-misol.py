try:
    n=int(input("Son kiriting:"))
    if n<0:
        raise Exception()
except:
    print("xato")
else:
    print("xato yo'q")