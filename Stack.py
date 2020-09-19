#Implementation of stack data structure

def push(stack,item):
    stack.append(item)
def pops(stack):
    if len(stack)==0:
        print("Underflow")
    else:
        stack.pop()
def showtop(stack):
    n=len(stack)
    if n==0:
        print("Underflow")
    else:
        print()
        print(stack[n-1])
def showstack(stack):
    print()
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
def errmsg():
    print("Sorry, the process did not complete successfully")
        
stack=[]
while True:
    print("\n1 Push\n2 Pop\n3 Show top\n4 Show stack\n5 Exit\n")
    ch=int(input("Enter your choice : "))
    if ch==1:
        item=int(input("Enter the item : "))
        push(stack,item)
        print("\nSuccess")
    elif ch==2:
        pops(stack)
    elif ch==3:
        showtop(stack)
    elif ch==4:
        showstack(stack)
    else:
        print()
        print("Please enter a valid input")
else:
    print("Please enter a valid input")
