import threading
import time
import queue

lst = []
n = int(input("Enter number of elements : "))
lst = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

prime_list=[]
listo=[]
def check_prime(num):
     if num in [0,1]:
          pass
     else:
          x=0
          for j in range(2,num):

               if num%j==0:
                    x+=1
                    if x>0:return False
          return True

def threader():
     while True:
          value=q.get()
          result=check_prime(value)

          if result == True:
              print("\n",value, "is prime\n")
          else :
              print("\n",value, "is not prime\n")
          q.task_done()


q=queue.Queue()
for x in range(30):
     t=threading.Thread(target=threader)
    
     t.start()

for value in lst:
     q.put(value)
q.join() 
print('There are ', threading.active_count(), 'thread(s) running by now')