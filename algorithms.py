idx = -1

def search(nums, n):
  i = 0
  while i < len(nums):
    if nums[i] == n:
      globals() [idx] = i
      return True
    i = i + 1
  return False


nums = [8, 4, 2, 1, 9, 5]
n = 2

search(nums, n)
print('Number ', n, ' found in the position: ', idx)
