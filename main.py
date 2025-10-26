def isOdd(value):
    if isinstance(value,int) and not isinstance(value,bool):
        return value%2!=0
    else:
        return False
