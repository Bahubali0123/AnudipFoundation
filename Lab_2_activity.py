#QN 1
number = int(input("Enter a number: "))               # Taking input from the user
result = "Even" if number % 2 == 0 else "Odd"    # Using a ternary operator to check even or odd
print(f"The number {number} is {result}.")      # Displaying the result

#QN 2
a=int(input("Enter a number"))#taking input for value a
b=int(input("Enter a number"))#taking input for value b
def swap(a,b):                #creating function
    return b,a
a,b= swap(a,b)                #swapping
print(a,b)

#QN 3
kilometer=float(input("Enter a kilometer"))  #taking input values for kilometers
convert=0.62137119                           #1 miles value
miles=kilometer*convert                      #calculation for miles
print(f"{kilometer} km in miles is",miles)  #printing values 

#QN 4
principle_amount=200
time=5
rate=5
si=principle_amount*time*rate/100
print(f"simple interest for this is:{si}")
