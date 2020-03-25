from math import sqrt

from scipy.stats import norm, t, chi2

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
