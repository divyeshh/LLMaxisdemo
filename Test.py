# Variables

text ="Hey Lovely People"
a= 5
b= 10
c= 15

# Function
def summarize(text):
    result_text=text[:20]
    return result_text

summary=summarize(text)
#print(summary)


def addition(a ,c):
    result = a + c
    return result

def Sub(a ,c):
    result = a - c
    return result

c=30
a=20
result=addition(a,c)
#print (result)


d=50
e=25
result=addition(d,e)
substraction =Sub(d,e)
#print (result)
#print(substraction)

#List
my_list =[10,20,30,40] #0-3(4-1)
names =["ganesh","Ravi","Kiran","Lakshmi","Srujana"] #0-2(3-1)
mixed=[1,"Ganesh",3.5,True] #0-3(4-1)

#print(my_list)
#print(my_list[2])
#print(name[2])

#Dictionary (word-meaning)

my_dict ={
    "name":"Ganesh",
    "city": "Bangalore",
     "age": 20
}
#If statements
if my_dict["age"] >= 22:
    print("Ganesh is  Major")
else:
    print("Ganesh is  Minor") 

# Loops    
for name in names:
    print("Hi", name)


