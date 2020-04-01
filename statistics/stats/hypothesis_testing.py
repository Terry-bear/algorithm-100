from math import sqrt

from scipy.stats import norm, t, chi2, f

from stats.descriptive_stats import mean, std, variance


def z_test(data1, data2=None, tail="both", mu=0, sigma1=1, sigma2=None):
    """
    z检验
    :param data1: 样本 1
    :param data2: 样本 2
    :param tail: 是否双尾检验， 默认是
    :param mu: μ值
    :param sigma1:
    :param sigma2:
    :return:
    """

    assert tail in ["both", "left", "right"], \
        'tail should be one of "both", "left", "right"'

    if data2 is None:
        # 样本均值
        mean_value = mean(data1)
        # 标准误
        se = sigma1 / sqrt(len(data1))
        z_value = (mean_value - mu) / se
    else:
        assert sigma2 is not None
        mean_diff = mean(data1) - mean(data2)
        se = sqrt(sigma1**2 / len(data1) + sigma2**2 / len(data2))
        z_value = (mean_diff - mu) / se

    if tail == "both":
        # 计算面积
        p = 2 * (1 - norm.cdf(abs(z_value)))
    elif tail == "left":
        p = norm.cdf(z_value)
    else:
        p = 1 - norm.cdf(z_value)
    return z_value, p


def t_test(data1, data2=None, tail="both", mu=0, equal=True):
    """
    t检验
    :param data1: 样本 1
    :param data2: 样本 2
    :param tail: 是否双尾检验， 默认是
    :param mu: μ值
    :param equal:
    :return:
    """
    assert tail in ["both", "left", "right"], \
        'tail should be one of "both", "left", "right"'

    if data2 is None:
        mean_val = mean(data1)
        se = std(data1) / sqrt(len(data1))
        t_val = (mean_val - mu) / se
        df = len(data1) - 1
    else:
        n1 = len(data1)
        n2 = len(data2)
        mean_diff = mean(data1) - mean(data2)
        sample1_var = variance(data1)
        sample2_var = variance(data2)

        if equal:
            sw = sqrt(((n1 - 1) * sample1_var + (n2 - 1) * sample2_var) / (n1 + n2 - 2))
            t_val = (mean_diff - mu) / (sw * sqrt(1/n1 + 1/n2))
            df = n1 + n2 - 2
        else:
            se = sqrt(sample1_var/n1 + sample2_var/n2)
            t_val = (mean_diff - mu) / se
            df_numerator = (sample1_var / n1 + sample2_var / n2) ** 2
            df_denominator = (sample1_var / n1) ** 2 / (n1 - 1) + (sample2_var / n2) ** 2 / (n2 - 1)
            df = df_numerator / df_denominator

    if tail == "both":
        p = 2 * (1 - t.cdf(abs(t_val), df))
    elif tail == "left":
        p = t.cdf(t_val, df)
    else:
        p = 1 - t.cdf(t_val, df)

    return t_val, df, p


def t_test_paired(data1, data2, tail="both", mu=0):
    data = [e1 - e2 for (e1, e2) in zip(data1, data2)]
    return t_test(data, tail=tail, mu=mu)


def chi2_test(data, tail="both", sigma2=1):
    """
    卡方分布
    :param data: 样本值
    :param tail: 尾类型
    :param sigma2: μ
    :return:
    """

    assert tail in ["both", "left", "right"], \
        'tail should be one of “both”, “left”, “right”'

    n = len(data)
    sample_var = variance(data)
    chi2_val = (n - 1)*sample_var/sigma2

    if tail == "both":
        p = 2 * min(1 - chi2.cdf(chi2_val, n-1), chi2.cdf(chi2_val, n-1))
    elif tail == "left":
        p = chi2.cdf(chi2_val, n-1)
    else:
        p = 1 - chi2.cdf(chi2_val, n-1)

    return chi2_val, n-1, p


def f_test(data1, data2, tail="both", ratio=1):
    """
    F 分布
    :param data1: 样本值 1
    :param data2: 样本值 2
    :param tail: 尾类型
    :param ratio:
    :return:
    """

    assert tail in ["both", "left", "right"], \
        'tail should be one of “both”, “left”, “right”'

    n1 = len(data1)
    n2 = len(data2)
    sample1_var = variance(data1)
    sample2_var = variance(data2)
    f_val = sample1_var/sample2_var/ratio
    df1 = n1 - 1
    df2 = n2 - 1

    if tail == "both":
        p = 2 * min(1 - f.cdf(f_val, df1, df2), f.cdf(f_val, df1, df2))
    elif tail == "left":
        p = f.cdf(f_val, df1, df2)
    else:
        p = 1 - f.cdf(f_val, df1, df2)

    return f_val, df1, df2, p
