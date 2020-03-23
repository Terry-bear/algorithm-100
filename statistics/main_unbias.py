import random
import matplotlib.pyplot as plt

from stats.descriptive_stats import mean, variance


def variance_bias(data):
    """无偏性方差"""
    n = len(data)
    if n <= 1:
        return None

    mean_value = mean(data)
    return sum((e - mean_value) ** 2 for e in data) / n


def sample(num_of_samples, sample_sz, var):
    data = []
    # 遍历样本
    for _ in range(num_of_samples):
        # 从 0-1的均匀分布中抽取 sample_sz 的个体组成的样本,mean 计算样本均值
        data.append(var([random.uniform(0.0, 1.0) for _ in range(sample_sz)]))
    return data


if __name__ == '__main__':
    """有偏"""
    data1 = sample(1000, 40, variance_bias)
    plt.hist(data1, bins="auto", rwidth=0.8)
    # 样本方差均值 实验值
    plt.axvline(x=mean(data1), c="000")
    # 总体方差均值 (b-a)^2/12  0.0, 1.0 理论值
    plt.axvline(x=1 / 12, c="red")
    print("bias: ", mean(data1), 1/12)
    plt.show()

    """无偏"""
    data2 = sample(1000, 40, variance)
    plt.hist(data1, bins="auto", rwidth=0.8)
    # 样本方差均值 实验值
    plt.axvline(x=mean(data2), c="000")
    # 总体方差均值 (b-a)^2/12  0.0, 1.0 理论值
    plt.axvline(x=1 / 12, c="red")
    print("un_bias: ", mean(data2), 1 / 12)
    plt.show()