invalids = ["N/A", "", "-"]
myDict = {"name":{"first":"Robert","middle":"","last":"Smith"},"age":25,"DOB":"-","hobbies":["running","coding","-",{"first":"Robert","middle":"","last":"Smith"}],"education":{"highschool":"N\/A","college":"Yale"}}

def valudation(value, invalids):
    for i in invalids:
        if value == i:
            return False
    return True

def recursive(value, invalids):
    if isinstance(value, dict):
        for k, v in list(value.items()):
            if not recursive(v,invalids):
                value.pop(k)
        return value
    elif isinstance(value, list):
        for i in list(value):
            if not recursive(i,invalids):
                value.remove(i)
        return value
    else:
        return valudation(value,invalids)

print(recursive(myDict, invalids))
