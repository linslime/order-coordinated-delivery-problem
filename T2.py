import pulp
import numpy as np


def assignment_problem(matrix_x, matrix_y):
    row_matrix_x = len(matrix_x)
    col_matrix_x = len(matrix_x[0])

    row_matrix_y = len(matrix_x)
    col_matrix_y = len(matrix_x[0])

    # 这里是将变量拉成一条直线，方便求解
    flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]

    # 这是说明了是求最大值：LpMaximize，如果需要求最小值：LpMinimize。
    m = pulp.LpProblem('task_name', sense=pulp.LpMaximize)
    print(type(pulp.LpProblem('task_name', sense=pulp.LpMaximize)))
    print(type(m))
    # 这里是mu和v2个决策变量的定义，是个矩阵形式，所以需要使用的dict这个函数，lowBound说明了下界大于等于0，和约束条件6对应
    # 这里的数据类型默认是浮点型，也可以换成Ingredients，cat=’Ingredients‘就是整数， cat=pulp.LpBinary这是离散型数据就是整数了。
    var_mu = pulp.LpVariable.dicts("mu", (range(row_matrix_x), range(col_matrix_x)), lowBound=0)
    var_vi = pulp.LpVariable.dicts("vi", (range(row_matrix_x), range(col_matrix_x)), lowBound=0)

    print(var_vi)

    # # 这里是6个变量，由于约束条件5中说明了上下届
    # rho1 = pulp.LpVariable('rho1', lowBound=0.15, upBound=0.18)
    # rho2 = pulp.LpVariable('rho2', lowBound=0.02, upBound=0.17)
    # rho3 = pulp.LpVariable('rho3', lowBound=0.15, upBound=0.33)
    # rho4 = pulp.LpVariable('rho4', lowBound=0.25, upBound=0.33)
    # rho5 = pulp.LpVariable('rho5', lowBound=0.08, upBound=0.17)
    # rho6 = pulp.LpVariable('rho6', lowBound=0.01, upBound=0.18)
    #
    # # 对应这求解最大值，即目标。pulp.lpDot相乘操作
    # m += pulp.lpDot(matrix_y.flatten(), flatten(var_mu))
    #
    # # 对应这约束条件1，pulp.lpSum当成求和用即可。
    # for j in range(row_matrix_x):
    #     m += (pulp.lpSum(var_vi[j][i] * matrix_x[j][i] for i in range(col_matrix_x)) == 1)
    #
    #     # 对应这约束条件2，看起来有点长。
    # for j in range(row_matrix_x):
    #     for k in range(row_matrix_x):
    #         m += (pulp.lpSum(var_mu[j][i] * matrix_y[k][i] for i in range(col_matrix_x)) - pulp.lpSum(
    #             var_vi[j][i] * matrix_x[k][i] for i in range(col_matrix_x)) <= 0.0)
    #
    # # 对应这约束条件3和4，为了方便就展开来写了。也可以改成上述的for循环。
    # m += (pulp.lpSum(var_mu[j][0] for j in range(row_matrix_x)) == rho1 * row_matrix_x)
    # m += (pulp.lpSum(var_mu[j][1] for j in range(row_matrix_x)) == rho2 * row_matrix_x)
    # m += (pulp.lpSum(var_mu[j][2] for j in range(row_matrix_x)) == rho3 * row_matrix_x)
    # m += (pulp.lpSum(var_mu[j][3] for j in range(row_matrix_x)) == rho4 * row_matrix_x)
    # m += (pulp.lpSum(var_mu[j][4] for j in range(row_matrix_x)) == rho5 * row_matrix_x)
    # m += (pulp.lpSum(var_mu[j][5] for j in range(row_matrix_x)) == rho6 * row_matrix_x)
    #
    # m += (pulp.lpSum(var_vi[j][0] for j in range(row_matrix_x)) == row_matrix_x * rho1 * 5)
    # m += (pulp.lpSum(var_vi[j][1] for j in range(row_matrix_x)) == row_matrix_x * rho2 * 5)
    # m += (pulp.lpSum(var_vi[j][2] for j in range(row_matrix_x)) == row_matrix_x * rho3 * 5)
    # m += (pulp.lpSum(var_vi[j][3] for j in range(row_matrix_x)) == row_matrix_x * rho4 * 5)
    # m += (pulp.lpSum(var_vi[j][4] for j in range(row_matrix_x)) == row_matrix_x * rho5 * 5)
    # m += (pulp.lpSum(var_vi[j][5] for j in range(row_matrix_x)) == row_matrix_x * rho6 * 5)
    #
    # # 求解目标，就这么简单。不用怀疑
    # m.solve()
    # # 可以打印出来各个约束条件，拆分开的很多，可以注释掉。
    # print(m)
    #
    # # 把求解的值，取出来的操作。
    # result_mu = [[pulp.value(var_mu[i][j]) for j in range(col_matrix_x)] for i in range(row_matrix_x)]
    # result_vi = [[pulp.value(var_vi[i][j]) for j in range(col_matrix_x)] for i in range(row_matrix_x)]
    # result_rho1 = pulp.value(rho1)
    # result_rho2 = pulp.value(rho2)
    # result_rho3 = pulp.value(rho3)
    # result_rho4 = pulp.value(rho4)
    # result_rho5 = pulp.value(rho5)
    # result_rho6 = pulp.value(rho6)
    #
    # return {'objective': pulp.value(m.objective), 'result_mu': result_mu, 'result_vi': result_vi}


# 构造数据，我们这里为了方便直接写0，自己进行替换即可。
matrix_x = np.zeros((1008, 6))
matrix_y = np.zeros((1008, 6))
# 输入数据求解，打印结果.
res = assignment_problem(matrix_x, matrix_y)
# print('{res["objective"]}')
# print(res['result_mu'])
