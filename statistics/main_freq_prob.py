import random, matplotlib.pyplot as plt


def toss():
    """模拟硬币的正反面"""
    return random.randint(0, 1)


if __name__ == '__main__':
    indices = [] # 定义抛硬币的次数
    freq = [] # 定义硬币正面朝上的频率
    for toss_num in range(10, 10001, 10):
        heads = 0
        for _ in range(toss_num):
            if toss() == 0:
                heads += 1
        freq.append(heads / toss_num)
        indices.append(toss_num)
    plt.plot(indices, freq)
    plt.show()
