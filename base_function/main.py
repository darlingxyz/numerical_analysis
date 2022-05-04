from boundary_condition import BoundaryCondition
import base_expression as be

# 设置边界条件1
boundary_1 = BoundaryCondition(list_x=[0, 1],  # 设置边界条件的自变量
                               value=7,  # 设置边界条件的值
                               list_rank=[0, 0],  # 设置边界条件中各项的阶数
                               list_factor=[1, 2],  # 设置边界条件中各项的系数
                               list_relation=["add", "tim"])  # 设置边界条件中各项的关系
# 设置边界条件2
boundary_2 = BoundaryCondition(list_x=[0, 2],
                               value=-1,
                               list_rank=[1, 2],
                               list_factor=[1, -1],
                               list_relation=["add", "add"])

result = be.get_approximate_expression([boundary_1, boundary_2])
print("插值出的多项式表达式", result)
