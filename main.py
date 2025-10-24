def PrimeList(N):
    # 辅助函数：判断一个数是否为质数
    def is_prime(num):
        if num &lt; 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        # 检查从3到sqrt(num)的所有奇数
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    # 生成小于N的所有质数列表
    primes = [str(num) for num in range(2, N) if is_prime(num)]

    # 用空格连接并输出
    return ' '.join(primes)
