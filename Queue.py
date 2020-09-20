#Implementation of queue

def enqueue(queue,item):
    queue.append(item)
def dequeue(queue):
    if len(queue)==0:
        print("Underflow")
    else:
        queue.pop(0)
def queuefront(queue):
    n=len(queue)
    if n==0:
        print("Underflow")
    else:
        print()
        print(queue[0])
def showqueue(queue):
    print()
    for i in range(len(queue)):
        print(queue[i],end=" ")   
queue=[]
while True:
    print("\n\n1 Insert\n2 Delete\n3 Show front\n4 Show queue\n5 Exit\n")
    ch=int(input("Enter your choice : "))
    if ch==1:
        item=int(input("Enter the item : "))
        enqueue(queue,item)
        print("\nSuccess")
    elif ch==2:
        dequeue(queue)
    elif ch==3:
        queuefront(queue)
    elif ch==4:
        showqueue(queue)
    else:
        print()
        print("Please enter a valid input")
else:
    print("Please enter a valid input")
