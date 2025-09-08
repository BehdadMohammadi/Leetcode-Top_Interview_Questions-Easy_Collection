import math

n = 10


prime_list = []

for num in range(2, n):

    flag = 0

    sqrt_num = round(math.sqrt(num))

    for i in prime_list:
        if i > sqrt_num:
            break
        else:
            if num%i == 0:
                flag = 1
                break
    
    if flag == 0:
        prime_list.append(num)


print("Count is: " + str(len(prime_list)))




