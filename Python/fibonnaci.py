##########################
#   Prints the first N elements of Fibonacci sequence.
#   Starting with 0 and 1 (first two elements always presents). In the Fibonacci Sequence, the N+1 element is the sum of the N-1 and N element in the sequence.
#   For example, the third element(1) is the sum of the first one (0) and the second (1). The Fourth(2) is the sum of third one(1) and second(1).
#   Author: Rogelio Hernandez
#   Date: 06/Enero/2024
##########################

#Funcion Fibonacci: print the first N (limit) elements of the Fibonacci's sequence. This limit should be greater than 0.
def printFibonacci(limit):
    #Starting elements, always are the same
    a=0
    b=1
    #When ask for the first two (or one) elements of the sequence dont need more calculations than print the first elements
    if limit<3:
        print(a)
        if limit==2:
            print(b)
        return
    #Printing the elements two by two. If the "limit" element is odd, it wont print the last number, should print outside the cycle
    for i in range(int(limit/2)): 
        print(a)
        print(b)
        a=a+b   #N+1 element
        b=a+b   #N+2 element
    #if the number of elements are odd, print the last element apart
    if limit%2!=0:
        print(a)



maxLimit=0
#While the limit value are negative or zero, stay asking for the limit
while maxLimit<=0:
    maxLimit=int(input("Ingrese la cantidad de elementos que desea visualizar (mayor que cero): \n"))
printFibonacci(maxLimit)



