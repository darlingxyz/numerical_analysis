import function as fun
import sympy as sp


x = sp.symbols('x')
# 设置原函数
fx = 1/(1+x**2)
# 给定区间及等分次数，获取对应x列表
list_x = fun.get_list_x(-5, 5, 5)
# 设置待计算的点
interpolation_x = 0
# 获取拉格朗日插值多项式
expression_lagrange = fun.get_expression_lagrange(fx, list_x)
# 计算该多项式在计算点的值
result_interpolation = fun.get_value_expression_lagrange(expression_lagrange, interpolation_x)
result_true = fun.get_value_fx(fx, interpolation_x)

print("原始表达式：", fx)
print("拉格朗日插值多项式：", expression_lagrange)
print("插值结果：", result_interpolation)
print("真值结果：", result_true)
