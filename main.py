import random, time
import tabulate
import sys
print(sys.setrecursionlimit(5000))

def selection_sort(a):
    for i in range(len(a)):
        min_val = (a[i],i)
        for j in range(i+1, len(a)):
            if a[j] < min_val[0]:
                min_val = (a[j],j)

        a[i],a[min_val[1]] = min_val[0],a[i]
    return a

print(selection_sort([3,5,7,9,1,2,8,6,4]))


def qsort(a, pivot_fn):
    ## TO DO
    if not a: return []
    if len(a) == 1:
        return [a[0]]
    
    pivot = pivot_fn(a)
    left = [num for num in a if num < pivot]
    right = [num for num in a if num > pivot]
    return qsort(left,pivot_fn) + [pivot] +  qsort(right,pivot_fn)

def fixed(a):
    return a[0]

print(qsort([3,5,7,9,1,2,8,6,4], fixed))

def random_fn(a):
    return random.choice(a)

print(qsort([3,5,7,9,1,2,8,6,4], random_fn))

def qsort_fixed(a):
    return qsort(a, fixed)

def qsort_random(a):
    return qsort(a, random_fn)
    
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###


def compare_sort(sizes=[10,100, 200, 500, 800 , 1000,1200, 1500,1800, 2000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = qsort_fixed
    qsort_random_pivot = qsort_random
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            
            time_search(qsort_fixed_pivot, mylist),
            time_search(selection_sort, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot','ss', 'qsort-random-pivot','tim_sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
