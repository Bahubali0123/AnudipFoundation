#looping through list
'''fruits=["apple","cherry","grapes"]
for fruit in fruits:
    print(fruit)
    
#looping through range
for i in range(5):
    print(i)
    
#looping through string
print("...............")    
word="india"
for letter in word:
    print(word) 

number=10
while number<=15:
    print(number)
    number+=1    
    
 #to control loop execution ==> Break,continue,else,pass
 #Break
for i in range(20): 
    if i==5:
        break;  
    print(i)
    
#Continue
for x in range(5): 
    if x==2:
        continue;  #it will skip 2 and print rest all
    print(x) 
    
#Else
age=1
if(age>=18):
    print("Eligible")
else:
    print("not eligible")
    
#pass
for x in range(5): 
    if x==2:
        pass;  #it is just place holder
    print(x) '''
    
#Functions
'''def function_name(parameter):
    function body        
          
def show():
    print("larning function")
show()
def add(a,b):
    return a+b
result=add(11,13)
print(result)             

#default parameter
def greet(name="guest"):
    print(f"Hello,{name}!")
greet("Bahu")
greet() 
 
def sum_all(*numbers):
    return sum(numbers)
print(sum_all(1,2,3,4,5))

print("keyword arguments")
def person_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
person_info(name="Bahu",age=21,city="bgm")'''