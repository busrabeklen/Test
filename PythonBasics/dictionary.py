

dic ={'name' : 'Busra' , 'age': 29 , 'location': 'MD', 6 :'Hello world'}

print(dic['age'])
print(dic[6])

dic ['location'] = "DC" #update
print(dic)

dic["abc"] = 8 #add new key value
print(dic)

for info in dic: #print keys only
    print(info)

for key, value in dic.items(): #prints key value
    print(f"key name : {key}")
    print(f"value name : {value}")

for value in dic.values(): #prints all values
    print(f"column value: {value}")



