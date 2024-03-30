# %% [markdown]
# ### 星穹小游戏：酒吧
# 
#     * 已实现随机挑选number层配料满足要求三个味觉的若干标准;s
#     * 已实现一杯饮料中有相同的配料的组合;
#     * 暂未实现去除饮料编号的重复;
# 

# %%
import random
import queue 
from itertools import combinations_with_replacement

i=0
j=0
number = int(4)
number_s = 2*number-1
q=queue.Queue()
result = []
# 定义模型类
class Model:
    def __init__(self, a=0, b=0, c=0,sn=0):
        self.a = a
        self.b = b
        self.c = c
        self.sn = sn

# 创建模型实例
models = [
    Model(a=2, b=2,sn=1), Model(a=1, b=-1,sn=2), Model(a=1, b=-2,sn=3),
    Model(a=-1, b=-1,sn=4), Model(a=-2, b=1,sn=5), Model(c=2, b=1,sn=6),
    Model(c=1, b=2,sn=7), Model(c=1, b=-1,sn=8), Model(c=-1, b=1,sn=9),
    Model(c=-1, b=0,sn=10)
]

# 检查组合是否满足条件
def check_combination(combination):
    sum_a = sum(model.a for model in combination)
    sum_b = sum(model.b for model in combination)
    sum_c = sum(model.c for model in combination)
    return sum_b == 1 and sum_c == 1

# 检查组合是否含有相同model
def check_combination_rpt(combination):
    sn_set = set()
    for model in combination:
        if model.sn in sn_set:
            return True
        else:
            sn_set.add(model.sn)


# 尝试随机组合模型
def find_combination(models):
    for _ in range(10000):  # 尝试次数
        combination = random.choices(models, k=number)
        if check_combination(combination) and check_combination_rpt(combination):
            yield combination
    return None

# 找到一个有效的组合
valid_combination = find_combination(models)

# 输出结果
# if valid_combination:
    # for i, model in enumerate(valid_combination, 1):
        # print(f"Model {i}: a={model.a},c={model.c} , b={model.b}")
# else:
    # print("没有找到满足条件的组合")

# 检查组合是否相同

def check_combination_rpt_sn(combined_sn,k):
    
    global j
    if(k==0):
        j+=1
        q.put(combined_sn)
        return False
    else:
        item_1 = (ord(char) for char in q.get())
        q.put(combined_sn)
        item_2 = (ord(char) for char in combined_sn)
        if item_1 == item_2:
            return True
        else:
            return False
    
        
combined_sn_set = set()


for combination in valid_combination:
    for model in combination:
        print(f"Model{getattr(model,'sn','Not available')}: a={getattr(model, 'a', 'Not available')}, c={getattr(model, 'c', 'Not available')}, b={model.b}")
        result.append(str((getattr(model,'sn','Not available'))))
        result.append(" ")
        i=i+1
        combined_sn ="".join(result[-number_s:])
        if(i%4 == 0):
            if check_combination_rpt_sn(combined_sn,j):
                continue
            combined_sn_set.add(combined_sn)
            print("结果为:"+combined_sn)
            print("-------分割线-------")







