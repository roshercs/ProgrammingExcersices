##########################
#   Printing numbers from A to B. If the k number is multiple of 3 prints "fizz" instead (in this implementation number and fizz), else if is multiple of 5 prints 
#   "buzz". If the k number is multiple of 3 and 5 at the same, prints fizzbuzz
#   Author: Rogelio Hernandez
#   Date: 06/January/2024
##########################

#Library and variables to count the ejecution time of functions
import time
timeClasic=0
timeMemory=0
timeSolution=0

#Classic implementation of fizzbuzz problem. In each cycle, in each if structure made the module operation
def fizzbuzz(a,b):
    global timeClasic
    startTime=time.time()
    for i in range(a,b):
        if i%3==0 and i%5==0:
            print(str(i)+": fizzbuzz")
        elif i%3==0:
            print(str(i)+": fizz")
        elif i%5==0:
            print(str(i)+": buzz")
        else:
            print(i)
    endTime=time.time()
    timeClasic=endTime-startTime
    print("Tiempo total version clasica: ", timeClasic," segundos")
# Implementation of fizzbuzz problem with "Memory". In each cycle, make the module operation once, in each if structure evaluate if is 0 or 1, like true and false.
#Less operation for cycle should decrease time of ejecution, but it just come relevant to a big number of cycles
def fizzbuzzMemmory(a,b):
    global timeMemory
    startTime=time.time()
    for i in range(a,b):
        #If i%3==0 is multiple of 3, if i%5==0 is multiple of 5, not operation convert 0 in 1, so if structure take it like True. Others values wont be 1 with the not operation
        io=not(i%3)
        il=not(i%5) 
        if io and il:
            print(str(i)+": fizzbuzz")
        elif io:    #Multiple of 3
            print(str(i)+": fizz")
        elif il:    #Multiple of 4
            print(str(i)+": buzz")
        else:
            print(i)
    endTime=time.time()
    timeMemory=endTime-startTime
    print("Tiempo total version con memoria: ", timeMemory," segundos")

#Version made by mouredev, similar idea of memory's version, except that use other operation instead the "not"
def fizzbuzzSolution(a,b):
    global timeSolution
    startTime=time.time()
    for i in range(a,b):
        io=i%3 == 0
        il=i%5 == 0
        if io and il:
            print(str(i)+": fizzbuzz")
        elif io:
            print(str(i)+": fizz")
        elif il:
            print(str(i)+": buzz")
        else:
            print(i)
    endTime=time.time()
    timeSolution=endTime-startTime
    print("Tiempo total version solucion: ", timeSolution," segundos")


fizzbuzz(1,100001)
fizzbuzzMemmory(1,100001)
fizzbuzzSolution(1,100001)
print("Tiempo total version clasica: ", timeClasic," segundos")
print("Tiempo total version con memoria: ", timeMemory," segundos")
print("Tiempo total version solucion: ", timeSolution," segundos")

#Evaluates if there is a difference of time between the three versions. For bigger range, the classic version, and memory's version become faster (even classic's time is a bit less in differents cases)
if  timeClasic>timeMemory:
    if timeMemory>timeSolution:
        print("Version Solucion Mejor")
    else:
        print("Version con memoria mejor")
elif timeClasic>timeSolution:
    print("Version Solucion Mejor")
else:
    print("Version clasica mejor")