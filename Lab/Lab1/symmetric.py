import threading
# 1 thread
a=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    temp = int(input("Enter number:"))
    a.append(temp)

for i in range(0, n):
    counter = 0
    for j in range(1,a[i]+1):

        if a[i] % j == 0:
            counter += 1
    if counter == 2:
        print(a[i],"is a prime")

    else:
        print(a[i],"is not a prime") 
print("_______________________________")
def CheckSymetricNumber(n):
    temp = n
    new_num = 0
    while temp!= 0:
        late_num = temp % 10
        new_num = new_num*10 + late_num
        temp //= 10
    if new_num == n:
        return True
    else: return False
def PrintSymetricNummber(a):
    for i in range (0, len(a)):
        if(CheckSymetricNumber(a[i])==True):
            print(str(a[i])+" is symetric number")
        else: print (str(a[i])+" is not symetric number")

PrintSymetricNummber(a)
print('There are ', threading.active_count(), 'thread(s) running by now') 

# 31 threads
# lst = []
# n = int(input("Enter number of elements : "))
# lst = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

# prime_list=[]
# listo=[]
# def check_prime(num):
#      if num in [0,1]:
#           pass
#      else:
#           x=0
#           for j in range(2,num):

#                if num%j==0:
#                     x+=1
#                     if x>0:return False
#           return True

# def threader():
#      while True:
#           value=q.get()
#           result=check_prime(value)

#           if result == True:
#               print("\n",value, "is prime\n")
#           else :
#               print("\n",value, "is not prime\n")
#           q.task_done()


# q=queue.Queue()
# for x in range(30):
#      t=threading.Thread(target=threader)
    
#      t.start()

# for value in lst:
#      q.put(value)
# q.join() 
# print('There are ', threading.active_count(), 'thread(s) running by now')