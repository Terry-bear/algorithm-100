from collections import Counter
from math import sqrt


# 集中趋势
def frequency(data):
    """频率"""
    counter = Counter(data)
    ret = []
    for point in counter.most_common():
        ret.append((point[0], point[1] / len(data)))
    return ret


def mode(data):
    """众数"""
    counter = Counter(data)
    if counter.most_common()[0][1] == 1:
        return None, None

    count = counter.most_common()[0][1]
    ret = []
    for point in counter.most_common():
        if point[1] == count:
            ret.append(point[0])
        else:
            break
    return ret, count


def median(data):
    """中位数"""
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]

    return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


def mean(data):
    """均值"""
    return sum(data) / len(data)


# 离散趋势
def rng(data):
    """极差"""
    return max(data) - min(data)


def quartile(data):
    """四分位数"""
    n = len(data)
    q1, q2, q3 = None, None, None
    if n >= 4:
        sorted_data = sorted(data)
        q2 = median(sorted_data)
        if n % 2 == 1:
            q1 = median(sorted_data[:n // 2])
            q3 = median(sorted_data[n // 2 + 1:])
        else:
            q1 = median(sorted_data[:n // 2])
            q3 = median(sorted_data[n // 2:])
    return q1, q2, q3


def variance(data):
    """方差"""
    n = len(data)
    if n <= 1:
        return None

    mean_value = mean(data)
    return sum((e - mean_value) ** 2 for e in data) / (n - 1)


def std(data):
    """标准差"""
    return sqrt(variance(data))


def covariance(data1, data2):
    """协方差"""
    assert len(data1) == len(data2)

    n = len(data1)
    assert n > 1

    mean_data1 = mean(data1)
    mean_data2 = mean(data2)
    return sum((e1 - mean_data1)*(e2 - mean_data2) for e1, e2 in zip(data1, data2))/(n-1)


def cor(data1, data2):
    """相关系数"""
    return covariance(data1, data2) / (std(data1)*std(data2))
