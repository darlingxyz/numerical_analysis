import function as fun
import sympy as sp


x = sp.symbols('x')
# 设置原函数
list_x = [0, 0.2, 0.4, 0.6, 0.8, 1]
list_fx = [1, 2, 3, 4, 5, 6]
# 设置待预测的点
interpolation_x = 2
# 计算拉格朗日插值多项式
expression_lagrange = fun.get_expression_lagrange(list_fx, list_x)
# 计算该多项式在计算点的值
result_interpolation = fun.get_value_expression_lagrange(expression_lagrange, interpolation_x)

print("拉格朗日插值多项式：", expression_lagrange)
print("插值结果：", result_interpolation)
