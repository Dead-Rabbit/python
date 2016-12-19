map = {'name':'wangzixiao','age':20}
while True:
    key = input("attribute=>")
    if not key :
        break
    try:
        record = map[key]
    except:
        print('No Attribute!')
    else:
        print("result=>",record)
