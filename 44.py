def arrfinder():
    arr = ["hi","test","other","ok","ive rand out of names"]
    find = input("What arr do you want to find?")
    try:
        print("The index is "+str(arr.index(find)))
    except:
        print("Not found")
arrfinder()