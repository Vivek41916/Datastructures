class node:
    def __init__(s,data):
        s.data=data
        s.next=None
class sll:
    def __init__(s):
        s.head=None
    def print_ll(s):
        if s.head:
            t=s.head
            while(t):
                print(t.data,end='->')
                t=t.next
            print()
        else:
            print("empty linked list")
    def add_begin(s):
        n=node(int(input("enter the data of node:")))
        n.next=s.head
        s.head=n
    def add_end(s):
        n=node(int(input("enter the data of node:")))
        if(s.head==None):
            s.head=n
        else:
            t=s.head
            while(t.next):
                t=t.next
            t.next=n
    def add_pos(s):
        p=int(input("enter position"))
        try:
            if(p):
                t=s.head
                while(p-1):
                    t=t.next
                    p-=1
                n=node(int(input("enter the data of node:")))
                n.next=t.next
                t.next=n
            else:
                s.add_begin()
        except:
            s.add_end()
    def del_begin(s):
        t=s.head
        s.head=t.next
    def del_end(s):
        t=s.head
        while(t.next.next):
            t=t.next
        t.next=None
    def del_mid(s):
        p=int(input("enter position to delete the data:"))
        try:
            if p:
                t=s.head
                while(p-1):
                    t=t.next
                    p-=1
                t.next=t.next.next
            else:
                s.del_begin()
        except:
            s.del_end()
    def search(s):
        k=int(input("enter the data to search:"))
        t=s.head
        c=0
        while(t):
            if(t.data==k):
                print("available at "+str(c)+" position")
                break
            c+=1
            t=t.next
        else:
            print("not available")
ll=sll()
while(True):
    print("1.add element at begining\n2.add element at the end\n3.add element at a position\n4.delete at beginning\n5.delete at end\n6.delete at a position\n7.search an element\n8.print the linked list\n0.stop\n")
    c=int(input("enter your choice :"))
    d={0: 'break',1:'ll.add_begin()',2:'ll.add_end()',3:'ll.add_pos()',4:'ll.del_begin()',5:'ll.del_end()',6:'ll.del_mid()',7:'ll.search()',8:'ll.print_ll()'}
    eval(d[c])
