class queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def enqueue(self,value):
        self.items.append(value)
    def dequeue(self):
        return self.items.pop(0)
    
q=queue()
while True:
    print("\n1 Put\n2 Get\n3 Exit\n")
    ch=int(input("Enter your choice : "))
    if ch==1:
        value=int(input("Enter the item : "))
        q.enqueue(value)
        print("\nSuccess :)")
    elif ch==2:
        if q.is_empty():
            print("Underflow")
        else:
            print("\nPopped item : ",q.dequeue())
    elif ch==4:
        exit()
    else:
        print("Please enter a valid input")
else:
    print("Please enter a valid input")
