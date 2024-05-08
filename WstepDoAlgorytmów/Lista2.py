import random
import time
import matplotlib.pyplot as plt
import math

# część 1 ------------------------------------------------------------------------------
# losowanie m n-elementowych list
n = 1000
m = 10
def generateRandomArrays(n, m):
    return [[random.randint(0, 1000) for _ in range(n)] for _ in range(m)]

def BubbleSort(lista):
    for i in range(len(lista)):  
        for j in range (0,len(lista)-i-1):  
            if (lista[j]>lista[j+1]):  
                temp=lista[j]  
                lista[j]=lista[j+1]  
                lista[j+1]=temp  
    return lista 

def InsertionSort(lista):
    for i in range(len(lista)):
        for j in range(0,i): 
            if (lista[i]<lista[j]):  
                temp=lista[i]  
                lista[i]=lista[j]  
                lista[j]=temp  

    return lista

def SelectionSort(lista):
    for i in range(len(lista)):  
        for j in range (i+1,len(lista)): 
            if (lista[i]>lista[j]):  
                temp=lista[i]  
                lista[i]=lista[j]  
                lista[j]=temp 
    return lista

test_cases = generateRandomArrays(n, m)
def testComplexity(index, test_cases):
    times = []
    for case in test_cases:
        start = time.perf_counter()
        if index==0:
            BubbleSort(case)
        elif index==1:
            InsertionSort(case)
        elif index==2:
            SelectionSort(case)
        wynik = time.perf_counter() - start
        times.append(wynik)
    return times

result_bubble = testComplexity(0, test_cases)
print("----- BUBBLE SORT -----")
print(f"Maksymalny czas to {max(result_bubble)}")
print(f"Minimalny czas to {min(result_bubble)}")
print(f"Średni czas to {round(sum(result_bubble)/len(result_bubble), 4)}")
result_insertion = testComplexity(1, test_cases)
print("----- INSERTION SORT -----")
print(f"Maksymalny czas to {max(result_insertion)}")
print(f"Minimalny czas to {min(result_insertion)}")
print(f"Średni czas to {round(sum(result_insertion)/len(result_insertion), 4)}")
result_selection = testComplexity(2, test_cases)
print("----- SELECTION SORT -----")
print(f"Maksymalny czas to {max(result_selection)}")
print(f"Minimalny czas to {min(result_selection)}")
print(f"Średni czas to {round(sum(result_selection)/len(result_selection), 4)}")
        
# część 2 ------------------------------------------------------------------------------
sizes = [10, 20, 50, 100, 200, 500, 1000]
test_cases = [[[random.randint(0, 1000) for _ in range(i)] for _ in range(10)] for i in sizes]

def testComplexity_10(algorithm, test_cases):
    result = []
    for size_tests in test_cases:
        times = []
        for test in size_tests:
            start_time = time.time()
            if algorithm == 0:
                BubbleSort(test)
            elif algorithm == 1:
                InsertionSort(test)
            elif algorithm == 2:
                SelectionSort(test)
            end_time = time.time()
            times.append(end_time - start_time)
        result.append(times)
    return result

result_bubble = [sum(times)/len(times) for times in testComplexity_10(0, test_cases)]
result_insertion = [sum(times)/len(times) for times in testComplexity_10(1, test_cases)]
result_selection = [sum(times)/len(times) for times in testComplexity_10(2, test_cases)]
max_bubble = [max(times) for times in testComplexity_10(0, test_cases)]
max_insertion = [max(times) for times in testComplexity_10(1, test_cases)]
max_selection = [max(times) for times in testComplexity_10(2, test_cases)]

plt.figure(figsize=(10, 6))
plt.plot(sizes, result_bubble, label='Bubble Sort - Average', marker='x')
plt.plot(sizes, result_insertion, label='Insertion Sort - Average', marker='x')
plt.plot(sizes, result_selection, label='Selection Sort - Average', marker='x')
plt.xlabel('Wielkość tablicy')
plt.ylabel('Czas [sekundy]')
plt.title('Zestawienie złożoności (średniej) czasowej różnych metod sortowania')
plt.legend()
plt.grid(True)
plt.xticks(sizes, labels=[str(size) for size in sizes])
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(sizes, max_bubble, label='Bubble Sort - Max', marker='x')
plt.plot(sizes, max_insertion, label='Insertion Sort - Max', marker='x')
plt.plot(sizes, max_selection, label='Selection Sort - Max', marker='x')
plt.xlabel('Wielkość tablicy')
plt.ylabel('Czas [sekudny]')
plt.title('Zestawienie złożoności (maksymalnej) czasowej różnych metod sortowania')
plt.legend()
plt.grid(True)
plt.xticks(sizes, labels=[str(size) for size in sizes])
plt.show()

# część 3 ------------------------------------------------------------------------------
def BubbleSortNaive(lista):
    for _ in range(len(lista)):  
        for j in range (0,len(lista)-1):  
            if (lista[j]>lista[j+1]):  
                temp=lista[j]  
                lista[j]=lista[j+1]  
                lista[j+1]=temp  
    return lista 

def BubbleSortModified(lista):
    for i in range(len(lista)):  
        error = 0
        for j in range (0,len(lista)-1-i):  
            if (lista[j]>lista[j+1]):  
                error += 1
                temp=lista[j]  
                lista[j]=lista[j+1]  
                lista[j+1]=temp  
        if error == 0:
            return lista
    return lista 

# zrobiłem zestawienie jak z poprzedniego przykłądu
sizes = [10, 20, 50, 100, 200, 500]
test_cases = [[[random.randint(0, 1000) for _ in range(i)] for _ in range(10)] for i in sizes]

def testComplexity_10(algorithm, test_cases):
    result = []
    for size_tests in test_cases:
        times = []
        for test in size_tests:
            start_time = time.time()
            if algorithm == 0:
                BubbleSort(test)
            elif algorithm == 1:
                BubbleSortNaive(test)
            elif algorithm == 2:
                BubbleSortModified(test)
            end_time = time.time()
            times.append(end_time - start_time)
        result.append(times)
    return result

result_bubble = [sum(times)/len(times) for times in testComplexity_10(0, test_cases)]
result_bubble_naive = [sum(times)/len(times) for times in testComplexity_10(1, test_cases)]
result_bubble_mod = [sum(times)/len(times) for times in testComplexity_10(2, test_cases)]
max_bubble = [max(times) for times in testComplexity_10(0, test_cases)]
max_bubble_naive = [max(times) for times in testComplexity_10(1, test_cases)]
max_bubble_mod = [max(times) for times in testComplexity_10(2, test_cases)]

plt.figure(figsize=(10, 6))
plt.plot(sizes, result_bubble, label='Bubble Sort - Average', marker='x')
plt.plot(sizes, result_bubble_naive, label='Bubble Sort Naive- Average', marker='x')
plt.plot(sizes, result_bubble_mod, label='Bubble Sort Mod - Average', marker='x')
plt.xlabel('Wielkość tablicy')
plt.ylabel('Czas [sekudny]')
plt.title('Zestawienie złożoności (maksymalnej) czasowej różnych metod sortowania bąbelkowego')
plt.legend()
plt.grid(True)
plt.xticks(sizes, labels=[str(size) for size in sizes])
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(sizes, max_bubble, label='Bubble Sort - Max', marker='x')
plt.plot(sizes, max_bubble_naive, label='Bubble Sort Naive - Max', marker='x')
plt.plot(sizes, max_bubble_mod, label='Buble Sort Mod - Max', marker='x')
plt.xlabel('Wielkość tablicy')
plt.ylabel('Czas [sekudny]')
plt.title('Zestawienie złożoności (maksymalnej) czasowej różnych metod sortowania bąbelkowego')
plt.legend()
plt.grid(True)
plt.xticks(sizes, labels=[str(size) for size in sizes])
plt.show()

# część 4 ------------------------------------------------------------------------------
sizes = [10, 100, 1000]
test_cases = [[random.randint(0, 1000) for _ in range(i)] for i in sizes]
bubble = testComplexity(0, test_cases)
insert = testComplexity(1, test_cases)
select = testComplexity(2, test_cases)
print()
print("część 4")
print("----- BUBBLE SORT -----")
for i in range(len(sizes)):
    print(f"{sizes[i]:<6}|{bubble[i]:<10.6f}|{(sizes[i]*math.log(sizes[i]))/bubble[i]:<10.2f}")
print("----- INSERTION SORT -----")
for i in range(len(sizes)):
    print(f"{sizes[i]:<6}|{insert[i]:<10.6f}|{(sizes[i]*math.log(sizes[i]))/insert[i]:<10.2f}")
print("----- SELECTION SORT -----")
for i in range(len(sizes)):
    print(f"{sizes[i]:<6}|{select[i]:<10.6f}|{(sizes[i]*math.log(sizes[i]))/select[i]:<10.2f}")
