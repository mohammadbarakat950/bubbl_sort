def bubbl_sort(arr):
   n = len(arr)
   for i in rang(n):
      for j in rang(0, n-i-1):
         if arr [j] > arr [j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
   return arr

arr = [64,34,25,12,22,11,90]
sorted_arr = bubble_sort(arr)
print("sorted array is:", sorted_arr)