array = [3,3]
original_number = 6
# Know how to get the index of an element in an array
# Storing the numbers in a stack or list
stores = []
for i, x in enumerate(array):
  print(i)
  # I will take x(the current number in the array) and sum it up with each number in the array
  for y in array[i + 1:len(array)]:
    # check if the sum is equal to the original_number
    if x + y == original_number:
      # print(x)
      # print(y)
      # # If it is equal to the original number
      # print("iterted")
      stores.extend([array.index(x), array.index(y)])
  # stores.append(x)
print(stores)
