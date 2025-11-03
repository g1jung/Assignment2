# quick_sort.py
def quick_sort_first_pivot(arr):
    """Functional quicksort using first element as pivot (shows worst cases)."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less  = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort_first_pivot(less) + [pivot] + quick_sort_first_pivot(greater)

import random
def quick_sort_random(arr):
    """Randomized-pivot quicksort (expected O(n log n), mitigates sorted worst case)."""
    if len(arr) <= 1:
        return arr
    p = random.choice(arr)
    less   = [x for x in arr if x < p]
    equal  = [x for x in arr if x == p]
    greater= [x for x in arr if x > p]
    return quick_sort_random(less) + equal + quick_sort_random(greater)
