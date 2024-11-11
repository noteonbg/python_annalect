def freaky(x):
    print("function is getting called",x)
    return True

#who decides the return type of freaky function
#what is input and what is its output if you assume you plan to pass it as input argument
#to some other function

x=[2,3]
#y=map(doubleit,x)
y =filter(freaky,x)
y=filter(lambda x:True,x)
print(list(y))




