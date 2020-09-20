class queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def enqueue(self,value):
        self.items.append(value)
    def dequeue(self):
        return self.items.pop(0)
    
s=queue()
while True:
    print("\n1 Put\n2 Get\n3 Exit\n")
    ch=int(input("Enter your choice : "))
    if ch==1:
        value=int(input("Enter the item : "))
        s.enqueue(value)
        print("\nSuccess :)")
    elif ch==2:
        if s.is_empty():
            print("Underflow")
        else:
            print("\nPopped item : ",s.dequeue())
    elif ch==4:
        exit()
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")
