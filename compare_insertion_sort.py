import random
import matplotlib.pyplot as plt 

def insertion_sort(A,n):
    c=0
    s=0
    for i in range(1,n):
        key=A[i]
        j=i-1
        while(j>=0 and A[j]>key):
            c+=1
            A[j+1]=A[j]
            s=s+1
            j=j-1
        A[j+1]=key
        if(j>=0):
            c+=1
    print("sorted array is",A)
    return ([c,s])

def compare_pp(n):
    avgc=[]
    avgs=[]
    A=[]
    print("The size is ",n)
    print()
    print()
    for i in range(1,20):
        for x in range(n):
            A.append(random.randint(1,11))
        
        print("The numbers before sorting are",A)
        avg= insertion_sort(A,n)
        print("number of comparisons is",avg[0])
        print("number of shifts is",avg[1])        
        avgc.append(avg[0])
        avgs.append(avg[1])
        A=[]
    
    return ([round(sum(avgc)/n),round(sum(avgs)/n)])

def main():
    graph_c=[]
    graph_s=[]
    for i in range(1,10):
        a=compare_pp(i*10)
        graph_c.append(a[0])
        graph_s.append(a[1])
    
    plt.plot(range(10,100,10),graph_c)

    plt.xlabel('Number of items') 
    plt.ylabel('Number of comparisons') 

    plt.title('Comparison of keys with respect to numbers') 

    plt.show() 

    plt.plot(range(10,100,10),graph_s)
    
    
    plt.xlabel('Number of items') 
    plt.ylabel('Number of shifts') 

    plt.title('Shifting of keys with respect to numbers') 

    plt.show() 

        
        
        
