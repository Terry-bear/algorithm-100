import random
import matplotlib.pyplot as plt
from collections import Counter

if __name__ == '__main__':
    # scatter plot
    # random.seed(666)
    # x = [random.randint(0, 100) for _ in range(100)]
    # y = [random.randint(0, 100) for _ in range(100)]
    # plt.scatter(x, y)
    # plt.show()

    # line plot
    # plt.plot(x)
    # plt.show()

    # bar plot
    # data = [3, 3, 4, 1, 4, 5, 6, 7, 2, 3, 5, 3, 1, 5]
    # counter = Counter(data)
    # x = [point[0] for point in counter.most_common()]
    # y = [point[1] for point in counter.most_common()]
    # plt.bar(x, y)
    # plt.show()

    # histogram
    # data = [random.randint(1, 100) for _ in range(1000)]
    # plt.hist(data, rwidth=0.8, color="#f0f", density=True)
    # plt.show()

    # box plot
    data = [random.randint(1, 100) for _ in range(1000)]
    plt.boxplot(data)
    plt.show()