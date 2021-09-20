# Course 2 - Week 3 - Question 6
#Given a list fib = [0, 1], write a loop that appends the sum of the last two items in fib to the end of fib.  
#What is the value of the last item in fib after twenty iterations of this loop?  Enter the answer below as an integer.

#As a check, the value of the last item in fib after ten iterations is 89.

#Solution_1

fib = [0, 1]
def append_sum(fib):
    i = 0
    while i < 20:
        fib.append(fib[-2] + fib[-1])
        i += 1
    return fib

print(append_sum(fib))

#Solution_2

fib = [0, 1]
def append_sum(fib):
    for i in range(0,10):
        fib.append(fib[-1] + fib[-2])
    return fib

print(append_sum(fib))


