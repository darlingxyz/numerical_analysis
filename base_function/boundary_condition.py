class BoundaryCondition:
    def __init__(self,
                 list_x: list,  # 自变量的list
                 value,  # 该边界条件的值
                 list_rank: list,  # 各项的微分次数list
                 list_factor: list,  # 各项的系数
                 list_relation: list  # 各项与总表达式的关系（加减乘除）
                 ):
        self.list_x = list_x
        self.value = value
        self.list_rank = list_rank
        self.list_factor = list_factor
        self.list_relation = list_relation
