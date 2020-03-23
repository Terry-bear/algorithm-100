import random
import matplotlib.pyplot as plt
from stats.descriptive_stats import mean, variance

if __name__ == '__main__':
    """相合性"""

    # 样本均值
    sample_means = []
    # 样本方差
    sample_vars = []
    # 样本容量
    indices = []

    for sz in range(20, 10001, 50):
        indices.append(sz)
        # 调用高斯分布
        sample = [random.gauss(0.0, 1.0) for _ in range(sz)]
        sample_means.append(mean(sample))
        sample_vars.append(variance(sample))

    plt.plot(indices, sample_means)
    plt.plot(indices, sample_vars)
    """结论，当样本越大时，样本均值逐渐趋向于样本方差,这就是相合性。"""
    plt.show()