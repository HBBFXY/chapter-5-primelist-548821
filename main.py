def PrimeList(N):
    if N < 3:
        return ""
    
    primes = []
    for num in range(2, N):
        # 检查num是否为质数
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    
    return " ".join(primes)
