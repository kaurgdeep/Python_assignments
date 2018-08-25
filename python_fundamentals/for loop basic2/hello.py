
#1.Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". 
#Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def biggie_size():
    arr = [-1, 2, -5]
    for i in range(0, len(arr)):
        if(arr[i] > 0):
            arr[i] = "big"
    return arr 
#print(biggie_size()) 
#2.Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it. 
 #(Note that zero is not considered to b a positive number).
def count_positives():
    arr = [-1,1,1,1,1,1]
    count = 0
    for i in range(0, len(arr)-1):
        if(arr[i] > 0):
            count = count + 1
    arr[len(arr)-1] = count
    return arr
#print(count_positives())

#3.SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array. 
 #For example sumTotal([1,2,3,4]) should return 10
def sum_total():
    arr = [1,2,3,4]
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum 
#print(sum_total())

#4.Average - Create a function that takes an array as an argument and returns the average of all the values in the array.
  #For example multiples([1,2,3,4]) should return 2.5
def average():
    arr = [1,2,3,4]
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
        avg = sum/len(arr)
    return avg    
#print(average())


#5.Length - Create a function that takes an array as an argument and returns the length of the array.  
#For example length([1,2,3,4]) should return 4
def length():
    arr = [1,2,3,4]
    len(arr)
    return len(arr)
#print(length())
 
#6.Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.
#For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum():
    arr = [1,2,3,4]
    min = arr[1]
    for i in range(0, len(arr)):
        if(arr[i] < min):
            min = arr[i]
        return min   
#print(minimum())

#7.Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false. 
 #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.
def maximum():
    arr = [1,2,3,4]
    if(len(arr) == 0):
        return "false"
    
    max = arr[0]
    for i in range(0, len(arr)):
        if(arr[i] > max):
            max = arr[i]
    return max   
#print(maximum())

#8.UltimateAnalyze - Create a function that takes an array as
 #an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
'''
def dic():
    my_dict = {'a':2, 'b':5, 'c':3, 'd':8, 'e':3}
    maxValKey = max(my_dict, key=my_dict.get)
    minValKey = min(my_dict, key=my_dict.get)
    return maxValKey,minValKey #(we are getting max,min values from dict)
print(dic())
'''
   
def get_dict():
    dict = {}
    arr = [1,2,3,4]
    max = 0
    min = 0
    avg = 0
    sum = 0
    len(arr)
    for i in range(0, len(arr)):
        sum += arr[i]
        avg = sum/len(arr)

        if(arr[i] > max):
            max = arr[i]
        if(arr[i] < min):
            min = arr[i]
    dict["max"] = max
    dict["min"] = min
    dict["avg"] = avg
    dict["sum"] = sum
    dict["len(arr)"] = len(arr)            #(print(dict["max"]),#print(dict["min"])this is another way to print seperately)
    return dict            
#print(get_dict())


#9. ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array. 
 #For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverse_list():
    arr = [1,2,3,4]
    reverse_arr = arr[::-1]
    return reverse_arr

    for i in reversed(arr):
        print(i)
    return arr    
#print(reverse_list())




