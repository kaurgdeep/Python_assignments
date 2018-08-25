
def basic():
    for i in range(151):
        print(i)

def multiples_of_five():
    for i in range(5, 1000001):
        if(i % 5 == 0):
            print(i)

def counting():
    for i in range(1, 101):
        if(i % 10 == 0):
            print("coding")
            if(i % 5 == 0):
                print("Dojo")

def oddsum():  
    sum = 0 
    for i in range(1, 5000000):
        if(i % 2 != 0):
           sum = sum + i
           print(sum)

oddsum()

def countdown_by_fours():
    for i in range(2018, 1, -4):
        print(i)
countdown_by_fours()

def flexible_countdown():
    for i in range(2, 50, 3):
        print(i)
flexible_countdown()       

