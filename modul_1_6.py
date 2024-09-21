my_dict={"car":2, "bike":1, "train":5}
print(my_dict)
print(my_dict.get("car"))
print(my_dict.get("metro", "Такого ключа нет"))
my_dict.update({'helicopter':4, 'tram':10})
print(my_dict)
a=my_dict.pop('helicopter')
print(a)
print(my_dict)

my_set={3,3,5, "cat",'dog','cat',(1,2,3)}
print(my_set)
my_set.update({"rabbit", 7})
print(my_set)
my_set.remove("cat")
print(my_set)

