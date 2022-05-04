import sympy as sp


class Equation:
    def __init__(self, fx):
        """ 初始化方程的性质 """
        self.precision = 1e-6  # 初始化计算精度
        self.precision_diff = 1e-3  # 初始化导数最小值，以判断是否接近0
        self.x = sp.symbols('x')
        self.fx = fx  # 接收传入的方程的函数表达式
        self.diff_fx = sp.diff(self.fx, self.x)  # 生成方程的导数表达式

