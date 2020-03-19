import random, matplotlib.pyplot as plt
from stats.descriptive_stats import mean


def sample(num_of_samples, sample_sz):
    data = []
    # 遍历样本
    for _ in range(num_of_samples):
        # 从 0-1的均匀分布中抽取 sample_sz 的个体组成的样本,mean 计算样本均值
        data.append(mean([random.uniform(0.0, 1.0) for _ in range(sample_sz)]))
    return data


"""中心极限定理"""
if __name__ == '__main__':
    data = sample(1000, 40)
    plt.hist(data, bins="auto", rwidth=0.8)
    # 绘制均值线
    plt.axvline(x=mean(data), c="red")
    plt.show()
