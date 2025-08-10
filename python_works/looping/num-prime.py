def is_prime(num_str):
    num = int(num_str)  

    if num <= 1:
        return False

    for number in range(2, num):
        if num % number == 0:
            return False

    return True
print(is_prime(3))
