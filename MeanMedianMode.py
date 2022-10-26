from collections import Counter

def mean(array):
    return sum(array) / len(array)

def median(array):
	return sorted(array)[int(len(array) / 2)] if len(array) % 2 == 1 else sum(sorted(array)[(int(len(array) / 2) - 1):(int(len(array) / 2) + 1)]) / 2
	
def mode(array):
    return [k for k, v in dict(Counter(sorted(array))).items() if v == max(list(dict(Counter(sorted(array))).values()))] if len([k for k, v in dict(Counter(sorted(array))).items() if v == max(list(dict(Counter(sorted(array))).values()))]) != len(array) else None

def data(array):
	# Return [Mean, Median, Mode(s)]
    return [sum(array) / len(array), sorted(array)[int(len(array) / 2)] if len(array) % 2 == 1 else sum(sorted(array)[(int(len(array) / 2) - 1):(int(len(array) / 2) + 1)]) / 2, [k for k, v in dict(Counter(sorted(array))).items() if v == max(list(dict(Counter(sorted(array))).values()))] if len([k for k, v in dict(Counter(sorted(array))).items() if v == max(list(dict(Counter(sorted(array))).values()))]) != len(array) else None, ]


w = [1, 2, 3, 4, 5] 
x = [1, 4, 4, 2, 4] 
y = [1, 2, 3, 4, 4, 5] 
z = [3, 1, 2, 2, 4, 1] 

print(data(w))
print(data(x))
print(data(y))
print(data(z))