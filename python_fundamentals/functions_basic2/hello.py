
def countdown():
    new_arr = []
    for i in range(5, -1, -1):
        new_arr.append(i)
    return new_arr
#print(countdown())

def print_and_return():
    arr = [1,2]
    print(arr[0])
    return arr[len(arr)-1]
#print_and_return()

def first_plus_print():
    arr = [1,2,3,4]
    sum = (arr[0] + len(arr))
    return sum
#print(first_plus_print()) 

def values_greater_than_second():
    arr = [1,2,3,4,5]
    new_arr = [] #empty array
    greater = arr[1] #great will be 2
    count = 0
    for i in range(0, len(arr)): #goes through all of array arr
        if(arr[i] > greater): 
            new_arr.append(arr[i])
            count +=1
    return new_arr        
    #return none
#print(values_greater_than_second())

def this_length_that_value(num1,num2):
    new_arr = []
    if(num1 == num2):
        print("jinx")
    for i in range(0, num1):
        new_arr.append(num2)
    return new_arr
#print(this_length_that_value(5,5))




   





