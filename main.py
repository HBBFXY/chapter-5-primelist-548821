def PrimeList(N):
    if N <= 2:
        return ""
    primes = []
    for num in range(2, N):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return " ".join(primes)

# 测试示例
# print(PrimeList(10))  # 输出：2 3 5 7
