def maxSubArray(arr):
	size = len(arr)
	curr_sum = 0
	max_yet = arr[0]
	st = 0
	end = 0
	poi = 0
	for i in range(0,size):
		curr_sum = curr_sum + arr[i]

		if(max_yet < curr_sum):
			max_yet = curr_sum
			st = poi 
			end = i

		if (curr_sum < i):
			curr_sum = 0
			poi = i + 1

	print("Maximum sum of the Subarray = ",max_yet)
	print("Start Index of the Array = ",st)
	print("End Index of the Array = ",end)

arr =[13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
maxSubArray(arr)