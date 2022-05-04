import sympy as sp
# 设置全局精度变量，控制每次赋值运算的有效位数
precision_value = 5


def get_basic_approximate_expression(condition_num):
    """ 生成底层的近似u函数，传入已知边界条件个数，n个边界条件生成的插值函数最高n次 """
    expression_u = 0
    for i in list(range(condition_num + 1)):  # 基于边界条件个数n，循环生成n个多项式基函数
        index = "a" + str(i)
        item = sp.symbols('%s' % index)
        x = sp.symbols('x')
        expression_u += item * x ** i
    return expression_u


def get_expression_from_boundary(expression, rank):
    """ 从边界条件充实底层近似函数 """
    temp_expression = expression
    if rank != 0:  # 微分次数不为0时，进行循环微分
        for _ in list(range(rank)):
            temp_expression = sp.diff(temp_expression, 'x')
    return temp_expression


def get_equation_from_boundary(expression, value_x, precision=precision_value):
    """ 从边界条件获取仅含系数a的方程 """
    return expression.subs('x', value_x, n=precision)


def get_factor_relation(list_equation, list_value):
    """ 解方程，获取a系数之间的关系 """
    if len(list_equation) == len(list_value):  # 长度一致说明传入的格式正确
        num_list = []  # 用来存储未知数个数
        for equation in list_equation:
            string_equation = str(equation)  # 将方程组转化为字符形式
            num_list.append(string_equation.count('a'))  # 获取字符形式方程中未知数的个数，依次判断每个方程的未知数个数
        item_num = max(num_list)  # 只需知道未知数个数的最大值，因为只用来作循环的判断条件
        list_unknown_num = []  # 用来存储待消元的未知数
        complete_equation_list = []
        n = len(list_equation) + 1  # n个方程说明实际有n+1个未知数
        from_num = n - item_num  # 用来判断，是否有未知数在之前的代值过程中被消掉了
        # 如果最大值已经小于未知数个数，说明方程是可解的！
        if n - item_num == 0:
            for i in list(range(n)):
                index = "a" + str(i)
                list_unknown_num.append(index)
        elif n - item_num > 0:
            for i in list(range(from_num, n)):  # 此处还存在瑕疵，存在一个很强的假定条件：最后的an没有被消掉
                index = "a" + str(i)
                list_unknown_num.append(index)
        for j in list(range(len(list_equation))):
            temp = list_equation[j] - list_value[j]
            complete_equation_list.append(temp)
        return sp.solve(complete_equation_list, list_unknown_num)


def get_upper_approximate_expression(factor_relation, basis_expression):
    """ 插值出近似解的多项式表达式 """
    high_expression = basis_expression
    string_equation = str(high_expression)
    item_num = string_equation.count('a')  # 获取底层近似函数中未知数的个数
    list_index = []  # 存储全部ai数列符号
    list_result_key = []
    for i in list(range(item_num)):
        list_index.append("a" + str(i))
    for key in factor_relation:
        list_result_key.append(str(key))
    for index in list_index:
        # 将表达式替换为用一个a表示
        if index in list_result_key:
            sym = sp.symbols(index)
            high_expression = high_expression.subs({sym: factor_relation[sym]})
        # 需要将剩余的未知数置为1时，请取消注释
        # elif len(list_index) - len(list_result_key) == 1:  # 将其赋为1
        #     high_expression = high_expression.evalf(subs={index: 1})
        # else:
        #     high_expression = high_expression.evalf(subs={index: 0})
    return high_expression


def get_approximate_expression(list_boundary_condition):
    """ 主函数，集成运算后返回最终的多项式表达式 """
    list_equation = []
    list_value = []
    basic_approximate_expression = get_basic_approximate_expression(len(list_boundary_condition))
    for boundary in list_boundary_condition:
        # 把边界条件的值放到统一的list中
        list_value.append(boundary.value)
        # 获取此边界条件的项数
        item_num = len(boundary.list_x)
        equation = 0
        for i in list(range(item_num)):
            expression = get_expression_from_boundary(basic_approximate_expression,
                                                      rank=boundary.list_rank[i])
            temp_equation = get_equation_from_boundary(expression=expression, value_x=boundary.list_x[i])
            # 拼接到此边界条件的大方程中去
            if boundary.list_relation[i] == "add":  # 加法标记符，执行加法
                equation = equation + boundary.list_factor[i] * temp_equation
            elif boundary.list_relation[i] == "sub":  # 减法标记符，执行减法
                equation = equation - boundary.list_factor[i] * temp_equation
            elif boundary.list_relation[i] == "tim":  # 乘法法标记符，执行乘法
                equation = equation * boundary.list_factor[i] * temp_equation
            elif boundary.list_relation[i] == "div":  # 除法标记符，执行除法
                equation = equation / boundary.list_factor[i] * temp_equation
        list_equation.append(equation)  # 执行一次循环后，将处理好的方程保存到方程list中
    factor_relation = get_factor_relation(list_equation, list_value)
    return get_upper_approximate_expression(factor_relation, basis_expression=basic_approximate_expression)
