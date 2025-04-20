def getvalue(dict,key):
    try:
        return dict[key]
    except KeyError:
        print("key doesn't exist")  
getvalue({"arnav":"box","ravi":"chawal","shyam":"renji"},"shyam")