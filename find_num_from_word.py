# part 1: letters to num map
def compute_letter_num_map():
	d = []
	d = {'A':1}
	for i in range(2,27):
		d[chr(65+i-1)] = d[chr(65+i-2)]*2 + i
	return d
	
def print_letter_to_num_map(d):
	for i in range(65,91):
		print chr(i),":",d[chr(i)]

#recursive
def find_lett_num_rec(lett):
	arr = [chr(i) for i in range(65,91)]
	if 	lett == arr[0]:
		return 1
	else:
		return 2*find_lett_num_rec(arr[arr.index(lett)-1]) + (arr.index(lett)+1)

def find_lett_num_DP(lett):
	return (compute_letter_num_map())[lett]
	
def print_letter_to_num_map_rec():
		for i in range(65,91):
			print chr(i),":",find_lett_num_rec(chr(i))
		
#part 2: letters to sum of letters in num	
def word_to_num_sum(d, word):
	if not word:
		return 0
	num_sum = 0
	for i in word:
		num_sum += d[i]
	return num_sum
	

#part 3: num to string
def num_to_string(num):
	res = []
	for i in range(0, (ord('Z')-ord('A'))+1):
		chr_num = find_lett_num_rec(chr(ord('Z') - i))
		div = num / chr_num
		if div:
			res.append(chr(ord('Z') - i))
			num -= (chr_num*div)
	return ''.join(res)


# calls	
print_letter_to_num_map(compute_letter_num_map())		
print_letter_to_num_map_rec()
print word_to_num_sum(compute_letter_num_map(),'GREP')
print num_to_string(word_to_num_sum(compute_letter_num_map(),'GREP'))	