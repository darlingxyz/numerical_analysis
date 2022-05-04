import sympy as sp


def get_list_x_and_h(a,  # 区间起始点
                     b,  # 区间结束点
                     n   # n是划分的次数
                     ):
    """ 获取步长及计算区间 """
    list_x = []
    h = abs(a - b) / n
    for i in list(range(0, n + 1)):
        list_x.append(a + i * h)
    return list_x, h  # h是步长


def get_k(fx,  # 方程表达式
          x,
          y,
          precision_value=5):  # 计算结果保留的有效数字
    """ 计算k值 """
    return fx.evalf(subs={'x': x, 'y': y}, n=precision_value)


def method_runge_kutta(fx,  # 方程表达式
                       list_fx,  # 存储fx值的list
                       a, b, n):
    """ 主循环进行计算 """
    list_x, h = get_list_x_and_h(a, b, n)
    i = 0
    while i < n:
        k1 = get_k(fx, list_x[i], list_fx[i])
        k2 = get_k(fx, list_x[i] + h / 2, list_fx[i] + h / 2 * k1)
        k3 = get_k(fx, list_x[i] + h / 2, list_fx[i] + h / 2 * k2)
        k4 = get_k(fx, list_x[i] + h, list_fx[i] + h * k3)

        value_fx = list_fx[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        list_fx.append(value_fx)
        i += 1


# 设置方程表达式
x, y = sp.symbols('x, y')
fx = sp.sin(x) + y
# 设置迭代初始值
init_fx = -1
list_fx = [init_fx]
# 调用四阶荣格库塔方法
method_runge_kutta(fx=fx,
                   list_fx=list_fx,
                   a=0,
                   b=1,
                   n=5)
# 简单打印迭代结果
print("方程：", fx)
print("迭代结果：", list_fx)

