import math

def PrimeList(N):
    """
    找出小于给定整数 N 的所有质数，并以空格分隔的字符串形式返回。

    参数:
    N (int): 一个整数。

    返回:
    str: 小于 N 的所有质数，以空格分隔的字符串。
    """
    # 处理 N 小于 2 的情况，此时没有质数
    if N <= 2:
        return ""

    # 辅助函数：判断一个数是否为质数
    def is_prime(num):
        """
        判断一个数是否为质数。

        参数:
        num (int): 一个整数。

        返回:
        bool: 如果 num 是质数，返回 True；否则返回 False。
        """
        # 小于 2 的数不是质数
        if num < 2:
            return False
        # 2 是最小的质数
        if num == 2:
            return True
        # 偶数（除 2 外）不是质数
        if num % 2 == 0:
            return False
        # 检查从 3 到 sqrt(num) 的所有奇数
        # 使用 math.isqrt 避免浮点数精度问题
        for i in range(3, math.isqrt(num) + 1, 2):
            if num % i == 0:
                return False
        return True

    # 生成小于 N 的所有质数列表
    primes = [str(num) for num in range(2, N) if is_prime(num)]
    # 用空格连接并输出
    return ' '.join(primes)


