import sys
import numpy as np


def get_max_row_in_column(matrix_a, j):
    """ 获取第j列中最大元素的所在行数
     此方法将被反复调用，所以每次运算时，不是从整个系数矩阵a中找最大行数，
     而是从可能已经做过几次消元的系数矩阵a的(j, j)子矩阵(尚未进行消元操作的部分)中寻找最大行数 """
    max_item = abs(matrix_a[j][j])
    max_row = j
    for i in list(range(j, matrix_a.shape[0])):
        if abs(matrix_a[i][j]) > abs(max_item):
            max_item = matrix_a[i][j]
            max_row = i
    return max_row


def swap_row_in_matrix_a(matrix_a, max_row, i):
    """ 在系数矩阵a中交换某两行的元素 """
    for j in (list(range(i, matrix_a.shape[1]))):
        temp = matrix_a[i][j]
        matrix_a[i][j] = matrix_a[max_row][j]
        matrix_a[max_row][j] = temp


def swap_row_in_matrix_b(matrix_b, max_row, i):
    """ 在值矩阵b中交换某两行的元素 """
    temp = matrix_b[i][0]
    matrix_b[i][0] = matrix_b[max_row][0]
    matrix_b[max_row][0] = temp


def method_elimination_gauss(matrix_a, matrix_b):
    """ 高斯消元法主循环 """
    for i in list(range(0, matrix_a.shape[0])):  # 逐行处理矩阵数据
        max_row = get_max_row_in_column(matrix_a, i)  # 在当前系数矩阵的(i, i)子矩阵中获取第一列中最大元素所在行数，准备进行交换
        swap_row_in_matrix_a(matrix_a, max_row, i)  # 将最大元素所在行数交换至(i, i)子矩阵的第一行
        swap_row_in_matrix_b(matrix_b, max_row, i)  # 同时交换值矩阵b的元素，使方程的系数与值保持对应关系

        for k in list(range(i + 1, matrix_a.shape[0])):
            if matrix_a[i][i] != 0:  # 此时从系数矩阵的(i, i)子矩阵中获取的[i][i]元素已经是该列中绝对值最大的数，若为0，则奇异
                scale_factor = (-matrix_a[k][i]/matrix_a[i][i])  # 计算接下来消元需要用到的比例因子
            else:
                print('该矩阵奇异，无法求解方程组')
                sys.exit(0)

            for j in list(range(i, matrix_a.shape[1])):
                matrix_a[k][j] = scale_factor * matrix_a[i][j] + matrix_a[k][j]  # 消元，高斯消元法的核心之处
            matrix_b[k][0] = scale_factor * matrix_b[i] + matrix_b[k][0]  # 对b进行同样的”消元“


def solve_equation(matrix_a, matrix_b):
    """ 求解消元后的上三角方程 """
    x = np.zeros((matrix_a.shape[0], 1))
    if matrix_a[-1][-1] != 0:
        x[-1] = matrix_b[-1] / matrix_a[-1][-1]
    else:  # 若此上三角方程的系数矩阵的最后一行最后一列元素为0，说明矩阵奇异，无数解
        print('该矩阵奇异，无法求解方程组')
        sys.exit(0)  # 强制退出

    for i in list(range(matrix_a.shape[0] - 2, -1, -1)):  # 从上三角方程最后一行开始解方程，倒着计算
        sum_a = 0
        for j in list(range(i + 1, matrix_a.shape[0])):
            sum_a += matrix_a[i][j] * x[j]
        x[i] = (matrix_b[i] - sum_a) / matrix_a[i][i]
    return x
