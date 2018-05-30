def solution(arr):
    """
    time complexity: O(N)
    space complexity: O(1)
    """
    if not arr:
        return 1
    
    #shifting all negative elements to left
    j = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    for i in range(j,len(arr)):
        if abs(arr[i]) - 1 < len(arr) - j and arr[abs(arr[i]) + j - 1] > 0:
            arr[abs(arr[i]) + j - 1] = -arr[abs(arr[i]) + j - 1]
    
    for i in range(j,len(arr)):
        if arr[i] > 0:
            return i - j + 1
    
    return len(arr) - j + 1

l1 = [3, 4, -1, 1]
print(solution(l1))

l1 = [1, 2, 0]
print(solution(l1))

l1 = [2, 5]
print(solution(l1))