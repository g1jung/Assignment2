# merge_sort.py
def merge_sort(arr):
    """Return a new sorted list using merge sort (stable, O(n log n) time, O(n) space)."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    if i < len(left): merged.extend(left[i:])
    if j < len(right): merged.extend(right[j:])
    return merged
