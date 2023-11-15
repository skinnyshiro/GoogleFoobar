def solution(n, b):
    #n is Minion ID
    #b is base
    #k is length
    z_array = []
    repetition = -1 #Flag for breaking loop
    n_string = str(n)
    while repetition < 0:             
        k = len(n_string)
        digits = list(n_string)
        sorted_digits = sorted(digits)
        x = ''.join(sorted_digits[::-1])
        x_base10 = int(x,b)
        y = ''.join(sorted_digits)
        y_base10 = int(y,b)
        z_base10 = x_base10 - y_base10
        z = base10_to_base_b(z_base10,b)
        while len(z) != k:
            z = '0' + z
        z_array.append(z)
        #print(f'X: {x}\nY: {y}\nZ Array: {z_array}')
        #z_array = solution(z,b,z_array,count-1)
        repetition = first_repeated_element(z_array)
        n_string = z
        
    
    if repetition == 0:
        repetition = 1

    return repetition
    
def base10_to_base_b(n,b):
    result = ""
    while n > 0:
        n, remainder = divmod(n,b)
        result = str(remainder) + result
    return result

def first_repeated_element(z_array):
    k = len(z_array)
    for i in range(k):
        for j in range(i+1,k):
            if z_array[i]==z_array[j]:
                #print(f'Repetition at Indices: {i} {j}')
                return j - i
    #print('No Repitition')
    return -1

#print(solution("1211",10))
print(solution("210022",3))

#print(base10_to_base_b(64,3))

