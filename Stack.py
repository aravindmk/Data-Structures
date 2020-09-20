class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,value):
        self.items.append(value)
    def pops(self):
        return self.items.pop()
    
s=stack()
while True:
    print("\n1 Push\n2 Pop\n3 Exit\n")
    ch=int(input("Enter your choice : "))
    if ch==1:
        value=int(input("Enter the item : "))
        s.push(value)
        print("\nSuccess :)")
    elif ch==2:
        if s.is_empty():
            print("Underflow")
        else:
            print("\nPopped item : ",s.pops())
    elif ch==4:
        exit()
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")
