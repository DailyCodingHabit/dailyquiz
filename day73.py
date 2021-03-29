  
# call by value
string = "Daily"
def test(string):
      
    string = "DailyCoding"
    print("Inside:", string)
    
test(string)
print("Outside:", string)
# Output
# Inside: DailyCoding
# Outside: Daily




# call by reference
def add_more(list):
    list.append(10)
    print("Inside 2:", list)

mylist = [2,4,6,8]

add_more(mylist)
print("Outside 2:", mylist)
# Output
# Inside 2: [2, 4, 6, 8, 10]
# Outside 2: [2, 4, 6, 8, 10]




