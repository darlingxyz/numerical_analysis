def get_value_fx(fx, x, precision_value):
    """ 计算函数值 """
    return fx.evalf(subs={'x': x}, n=precision_value)  # n指定保留的有效数字


def get_value_fx_diff(diff_fx, x, precision_value):
    """ 计算导数值 """
    return diff_fx.evalf(subs={'x': x}, n=precision_value)  # n指定保留的有效数字


def get_new_x(fx,
              diff_fx,
              x,
              precision_value,
              descent_factor
              ):
    """ 迭代一次，计算新一个X的值，即X(k+1) """
    value_fx = get_value_fx(fx, x, precision_value)  # 获取函数值
    value_fx_diff = get_value_fx_diff(diff_fx, x, precision_value)  # 获取导数值
    return x - descent_factor * (value_fx / value_fx_diff)  # 带入牛顿迭代的表达式，并返回计算出的X(k+1)


def fx_diff_close_to_0(value_fx_diff, precision_diff):
    """ 判断导数值是否接近0 """
    if abs(value_fx_diff) < precision_diff:
        return True
    else:
        return False


def precision_requirement_meet(precision, list_x):
    """ 判断X的精度是否满足要求 """
    if len(list_x) == 1:
        return False
    difference = abs(list_x[-1] - list_x[-2])
    if difference < precision:
        return True
    else:
        return False


def method_iterative_newton(fx,
                            diff_fx,
                            list_x,
                            precision,
                            precision_diff,
                            precision_value=5,  # 结果有效数字默认保留5位
                            descent_factor=1  # 下山因子默认为1
                            ):
    """ 主循环进行计算 """
    while not precision_requirement_meet(precision, list_x):  # 当未满足精度时，进行一次迭代
        value_fx_diff = get_value_fx_diff(diff_fx, list_x[-1], precision_value)  # 为随后的判断，需单独计算一次导数值
        if fx_diff_close_to_0(value_fx_diff, precision_diff):  # 如果导数接近0.则终止计算
            print('导数接近0，结束计算，最终结果可能不满足精度要求\n')
            return
        list_x.append(get_new_x(fx=fx,
                                diff_fx=diff_fx,
                                precision_value=precision_value,
                                x=list_x[-1],
                                descent_factor=descent_factor))  # 将结果追加到x列表中进行保存


