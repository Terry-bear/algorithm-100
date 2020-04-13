from collections import Counter
from stats.descriptive_stats import frequency, mode, median, mean, covariance, cor
from stats.descriptive_stats import rng, quartile, variance, std
if __name__ == "__main__":
    # 测试频数
    data = [1, 2, 2, 3, 4, 3, 1, 5, 1]
    counter = Counter(data)
    print(counter.most_common())
    print(counter.most_common()[0][1])

    # 测试频率
    pl = frequency(data)
    print(pl)

    # 测试众数
    zs, zs_count = mode(data)
    print("zs", zs, zs_count)

    # 测试中位数
    data_zws1 = [1, 2, 3, 4]
    data_zws2 = [1, 2, 3, 4, 5]
    data_zws3 = [1, 2, 3, 4, 99]
    zws1 = median(data_zws1)
    zws2 = median(data_zws2)
    zws3 = median(data_zws3)
    print("zws", zws1, zws2, zws3)  # 再次认证中位数和极端值没有关联，是集中趋势

    # 测试均值
    data_jz = [1, 2, 3, 4, 5]
    jz = mean(data_jz)
    print("jz", jz)

    # 测试极差
    data_jc = [1, 2, 3, 999]
    jc = rng(data_jc)
    print("jc", jc)

    # 测试四分位数
    data_sfws = [1, 4, 2, 3, 5]
    sfws = quartile(data_sfws)
    print(sfws)

    # 测试方差
    data_fc = [1, 4, 2, 3, 5]
    fc = variance(data_fc)
    bzc = std(data_fc)
    print(fc, bzc)

    # 测试协方差,相关系数
    score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    happy = [1, 3, 2, 6, 4, 5, 8, 10, 9, 7]
    print(covariance(score, happy))
    print(cor(score, happy))
