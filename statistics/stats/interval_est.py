from math import sqrt

from scipy.stats import norm, t, chi2, f

from stats.descriptive_stats import mean, std, variance


def mean_ci_est(data, alpha, sigma=None):
    """ci-置信区间, est-均值置信区间"""
    n = len(data)
    sample_mean = mean(data)

    if sigma is None:
        #  方差未知
        s = std(data)
        se = s / sqrt(n)
        t_value = abs(t.ppf(alpha / 2, n - 1))
        return sample_mean - se * t_value, sample_mean + se * t_value
    else:
        #  方差已知
        se = sigma / sqrt(n)  # 标准误
        #  计算 Z 值
        z_value = abs(norm.ppf(alpha / 2))
        return sample_mean - se * z_value, sample_mean + se * z_value


def var_ci_est(data, alpha):
    """方差的置信区间"""
    n = len(data)
    s2 = variance(data)
    # 卡方分布
    chi2_lower_value = chi2.ppf(alpha / 2, n - 1)
    chi2_upper_value = chi2.ppf(1 - alpha / 2, n - 1)
    return (n - 1) * s2 / chi2_upper_value, (n - 1) * s2 / chi2_lower_value


def mean_diff_ci_t_est(data1, data2, alpha, equal=True):
    # 样本容量 1
    n1 = len(data1)
    # 样本容量 2
    n2 = len(data2)
    # 均值差
    mean_diff = mean(data1) - mean(data2)
    # 样本方差
    sample1_var = variance(data1)
    sample2_var = variance(data2)

    # 两个总体方差未知且相等，求均值差的置信区间
    if equal:
        # 联合标准差
        sw = sqrt(((n1 - 1) * sample1_var + (n2 - 1) * sample2_var) / (n1 + n2 - 2))
        t_value = abs(t.ppf(alpha / 2, n1 + n2 - 2))
        return mean_diff - sw * sqrt(1 / n1 + 1 / n2) * t_value, \
               mean_diff + sw * sqrt(1 / n1 + 1 / n2) * t_value

    # 两个总体方差未知且不等，求均值差的置信区间
    else:
        # 自由度
        # 分子
        df_numerator = (sample1_var / n1 + sample2_var / n2) ** 2
        # 分母
        df_denominator = (sample1_var / n1) ** 2 / (n1 - 1) + (sample2_var / n2) ** 2 / (n2 - 1)
        df = df_numerator / df_denominator
        t_value = abs(t.ppf(alpha / 2, df))
        return mean_diff - sqrt(sample1_var / n1 + sample2_var / n2) * t_value, \
               mean_diff + sqrt(sample1_var / n1 + sample2_var / n2) * t_value


def mean_diff_ci_z_est(data1, data2, alpha, sigma1, sigma2):
    # 样本容量 1
    n1 = len(data1)
    # 样本容量 2
    n2 = len(data2)
    # 均值差
    mean_diff = mean(data1) - mean(data2)
    z_value = abs(norm.ppf(alpha / 2))
    return mean_diff - sqrt(sigma1 ** 2 / n1 + sigma2 ** 2 / n2) * z_value, \
           mean_diff + sqrt(sigma1 ** 2 / n1 + sigma2 ** 2 / n2) * z_value


def var_ratio_ci_est(data1, data2, alpha):
    # 样本容量 1
    n1 = len(data1)
    # 样本容量 2
    n2 = len(data2)
    # 置信下限
    f_lower_value = f.ppf(alpha / 2, n1 - 1, n2 - 1)
    # 置信上限
    f_upper_value = f.ppf(1 - alpha / 2, n1 - 1, n2 - 1)
    # 方差比
    var_ratio = variance(data1) / variance(data2)
    return var_ratio / f_upper_value, var_ratio / f_lower_value
