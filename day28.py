


## 1. ##
name, city = "John", "Paris"


## 2. ##
import operator
list = [(7,4,5), (2, 5), (3, 6)]
list.sort(key=operator.itemgetter(0))
print(list)
#Output = [(2, 5), (3, 6), (7, 4, 5)]
list.sort(key=operator.itemgetter(1))
print(list)
#Output = [(7, 4, 5), (2, 5), (3, 6)]


## 3. ##
for name in user_list:
  print('{} is a user'.format(name))


## 4. ##
new = "This" + "is" + "a" + "string"
new = " ".join(["This","is","a","string"])


