def PrimeList(N):
    # 处理特殊情况，小于2的数没有质数
    if N <= 2:
        return ""
    # 存储质数的列表
    primes = []
    # 遍历2到N-1的所有整数
    for num in range(2, N):
        # 假设当前数是质数
        is_prime = True
        # 检查是否能被2到其平方根之间的数整除
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        # 如果是质数，加入列表
        if is_prime:
            primes.append(str(num))
    # 以空格分隔输出，末尾无空格
    return " ".join(primes)
