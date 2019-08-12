'''
Problem statement:
You have to do insertion sort on 20 samples of size 10.
Count the number of comparisons in 1 sample of size 10.
Count the number of shifts in 1 sample of size 10.

Now do it for all 20 samples. 
Find the average time of comparisons for all 20 samples
Find the average time of shifts for all 20 samples. 


Now do the above for 20 samples of size 20,30,40,....,100

Now you must have a list of average time for comparisons and average time of shifts for each size 10,20,30,..,100

Plot both the lines in a graph
No. of comparisons/shifts versus number of elements.
'''


import random
import matplotlib.pyplot as plt #this library has been imported to make plots



def insertion_sort(A,n):
    '''
    This function named insertion_sort(A,n) takes an array A consisting
    of n elements.
    Input:
    A: array to be sorted via insertion sort
    n: number of elements in array
    Output:
    A tuple consisting of number of comparisons(c) and number of shifts(s).
    '''
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

def create_sample_and_sort(n):
    '''
    This function create_sample_and_sort(n) takes an input n of the sample size
    and creates a sample of size n. The function calls insertion sort function
    and recieves a tuple consisting of number of comparisons and shifts in a
    variable named avg.

    Input:
    n: Sample size
    Output:
    A tuple consisting of average number of comparisons and shifts of 20 samples of
    a sample size
    '''
    avgc=[] 
    avgs=[]
    A=[]
    print("The size is ",n)
    print()
    print()
    for i in range(1,20):
        for x in range(n):
            A.append(random.randint(1,1000))
        
        print("The numbers before sorting are",A)
        avg= insertion_sort(A,n)
        print("number of comparisons is",avg[0])
        print("number of shifts is",avg[1])        
        avgc.append(avg[0]) 
        avgs.append(avg[1])
        A=[]
    
    return ([round(sum(avgc)/n),round(sum(avgs)/n)])

def main():
    '''
    The main function of the program to show graph of average comparisons/shifts versus sample size.
    '''
    graph_c=[] #Stores a list of number of average comparisons for different sample sizes 
    graph_s=[] #Stores a list of number of average shifts for different sample sizes 
    
    for i in range(1,10):
        a=create_sample_and_sort(i*10)
        graph_c.append(a[0])
        graph_s.append(a[1])
    
    plt.plot(range(10,100,10),graph_c, color='green', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12,label="Comparisons")



    plt.plot(range(10,100,10),graph_s, color='yellow', linewidth = 3, 
         marker='o', markerfacecolor='red', markersize=12,label="Shifts")
    
    
    plt.xlabel('Number of items') 
    plt.ylabel('Number of operations')
    plt.legend()
    plt.title('Shifting of keys with respect to numbers') 
    plt.show() 

        
        
        
if __name__== '__main__':
    main()
