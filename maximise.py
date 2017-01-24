def maximise(arr,rep):
	for i in range(len(arr)):
		if arr[i] < max(rep):
			arr[i] = max(rep)
			rep.remove(max(rep))
			
	return arr		
	
print maximise([3,1,4,5,6],[1,9,5,2,3])	