def PrimeList(N):
    """
    返回小于N的所有质数，以空格分隔
    
    参数:
    N -- 整数，返回小于N的所有质数
    
    返回:
    字符串 -- 小于N的质数，以空格分隔
    """
    # 处理边界情况
    if N <= 2:
        return ""
    
    # 埃拉托斯特尼筛法
    is_prime = [True] * N
    is_prime[0] = False  # 0不是质数
    is_prime[1] = False  # 1不是质数
    
    # 筛法核心
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 标记i的所有倍数为非质数
            for j in range(i*i, N, i):
                is_prime[j] = False
    
    # 收集质数
    primes = []
    for num in range(2, N):
        if is_prime[num]:
            primes.append(str(num))
    
    # 用空格连接
    return " ".join(primes)

