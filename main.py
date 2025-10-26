def PrimeList(N):
    if N <= 2:
        return ""
    
    # 创建标记数组，初始都认为是质数
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    
    # 埃拉托斯特尼筛法
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 将i的倍数标记为非质数
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集所有质数
    primes = []
    for i in range(2, N):
        if is_prime[i]:
            primes.append(str(i))
    
    # 用空格连接，自动处理了空格分隔
    return " ".join(primes)
