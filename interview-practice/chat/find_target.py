def find_target(arr, target):
    complements = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in complements:
            return [complements[complement], i]
        complements[num] = i

print(find_target([2, 7, 11, 15], 9))