from stats.descriptive_stats import mean, std, variance
from stats.interval_est import mean_ci_est, var_ci_est

if __name__ == '__main__':
    # 18 岁月收入数据
    salary_18 = [1484, 785, 1598, 1366, 1716, 1020, 1716, 785, 3113, 1601]
    # 35 岁月收入数据
    salary_35 = [902, 4508, 3809, 3923, 4276, 2065, 1601, 553, 3345, 2182]

    # 点估计
    # 区间估计
    print("18-->mean:", mean(salary_18))
    print("18-->mean_ci_est:", mean_ci_est(salary_18, 0.05))
    print("35-->mean:", mean(salary_35))
    print("35-->mean_ci_est:", mean_ci_est(salary_35, 0.05))
    print(std(salary_18), variance(salary_18), var_ci_est(salary_18, 0.05))
    print(std(salary_35), variance(salary_35), var_ci_est(salary_35, 0.05))
