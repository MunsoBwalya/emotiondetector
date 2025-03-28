#Find the maximum number of values in an array

array =[2,8,5,6]
max = array[0]

for num in array:
    if num > max:
        max= num

print(max)

#Find the maximum number index of values in an array
arrays =[2,8,4,5,6,7,12]
maxi = arrays[0]
index= 0
i = 0
for i in  range(len(arrays)):
    if arrays[i ]> maxi:
        maxi= arrays[i]
        index= i
        
#print(index)

nums = [0, 0, 1, 2, 2, 3]
k = 1  # Start tracking unique elements from index 1

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:  # Compare current and previous element
        nums[k] = nums[i]  # Place the unique element at index k
        k += 1  # Move k forward

#print(nums[:k])  # Print the first 'k' unique elements
#print(k)  # Print the length of the unique part
