import time
def binary_search(l, e):
    """Assumes l is sorted in ascending order."""
    def bin_search(l, e, low, high):
        if high == low:
            return l[low] == e
        mid = (low + high) // 2
        if l[mid] == e:
            return True
        elif l[mid] > e:
            if low == mid:
                return False
            else:
                return bin_search(l, e, low, mid - 1)
        else:
            return bin_search(l, e, mid + 1, high)
            
    if not l:
        return False
    return bin_search(l, e, 0, len(l) - 1)

def sel_sort(l):
    """Sorts list in place in ascending order."""
    suffix_start = 0
    while suffix_start != len(l):
        for i in range(suffix_start, len(l)):
            if l[i] < l[suffix_start]:
                l[suffix_start], l[i] = l[i], l[suffix_start]
        suffix_start += 1
    return l

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # THESE LOOPS MUST BE OUTSIDE THE MAIN WHILE LOOP
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(l, compare=lambda x, y: x < y):
    """Returns a new sorted list."""    
    if len(l) < 2:
        return l[:]
    else:
        middle = len(l) // 2
        left = merge_sort(l[:middle], compare)
        right = merge_sort(l[middle:], compare)
        return merge(left, right, compare)

# --- Test Code ---
if __name__ == "__main__":
    test_list = [5, 2, 9, 1, 5, 6]
    print(f"Selection Sort: {sel_sort(test_list.copy())}")
    print(f"Merge Sort: {merge_sort(test_list)}")
    print(f"Is 9 in sorted list? {binary_search(sorted(test_list), 9)}")

def is_subset(l1,l2):
    """Assumes l1 and l2 are list.
    return true if each element in l1 is also in l2 and false otherwise"""
    for e in l1:
        matched=False
        for e2 in l2:
            if e==e2:
                matched=True
                break
        if not matched:
                return False
    return True
l1=[1,2,3,4]
l2=[4,3,2]
print(is_subset(l1,l2))

start=time.perf_counter()
def count_ways(n, steps, memo={}):
    if n == 0:
        return 1 #dont move
    if n < 0:
        return 0  # Can't reach a negative step0
    if n in memo:
        return memo[n]

    count = 0
    for step in steps:
        ways = count_ways(n-step, steps, memo)
        count += ways

    memo[n] = count
    return count

n = 100
steps = (1, 2)
print(count_ways(n, steps))
start=time.perf_counter()
end=time.perf_counter()
print(end-start)