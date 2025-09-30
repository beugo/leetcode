def solution(numbers):
    result = []
    for i in range(1, len(numbers) - 1):
        n = numbers[i]
        if numbers[i - 1] < n:
            if numbers[i + 1] < n:
                result.append(1)
            else:
                result.append(0)
        elif numbers[i + 1] > n:
            result.append(1)
        else:
            result.append(0)
    
    return result

'''
def solution(numbers):
    result = []
    for i in range(1, len(numbers)-1):
        left, n, right = numbers[i-1], numbers[i], numbers[i+1]
        result.append(1 if (left < n > right) or (left > n < right) else 0)
    return result
'''