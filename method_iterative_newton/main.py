import setting
import function
import sympy as sp

# 设置迭代初始值
init_x = 0
# 设置方程表达式
x = sp.symbols('x')
func = sp.cos(x) - x
# 获取方程对象
equation = setting.Equation(func)
# 创建x值的队列
list_x = [init_x]
# 调用牛顿迭代法
function.method_iterative_newton(fx=equation.fx,
                                 diff_fx=equation.diff_fx,
                                 list_x=list_x,
                                 precision=equation.precision,
                                 precision_diff=equation.precision_diff,
                                 precision_value=10)  # 计算结果的有效数字设为10位
print("方程：", func)
print("迭代结果：", list_x)  # 简单打印计算结果


