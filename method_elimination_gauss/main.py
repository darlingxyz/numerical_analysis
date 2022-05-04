import numpy as np
import function as fun


# 为保证程序的连续性，一下两个矩阵均采用numpy库的矩阵形式输入，而不以数组形式输入
# 方程的系数矩阵a
matrix_a = np.array([[0.4096, 0.1234, 0.3678, 0.2943],
                     [0.2246, 0.3872, 0.4015, 0.1129],
                     [0.3645, 0.1920, 0.3781, 0.0643],
                     [0.1784, 0.4002, 0.2786, 0.3927]])
# 方程的值矩阵b
matrix_b = np.array([[1.1951],
                    [1.1262],
                    [0.9989],
                    [1.2499]])

# 输出结果
print("原系数矩阵a:")
print(matrix_a, "\n")
print("原值矩阵b:")
print(matrix_b, "\n")
fun.method_elimination_gauss(matrix_a, matrix_b)
print("消元后的系数矩阵a")
print(matrix_a, "\n")
print("消元后的值矩阵b")
print(matrix_b, "\n")
print("最终求解结果:")
print(fun.solve_equation(matrix_a, matrix_b))
