def f1(m,n):
    list1 = []
    list2 = []
    for i in range(n):
        list1.append('_')
    shape1 = "|".join(list1)
    print(shape1)
    for i in range(m):
        list2.append(shape1)
    shape2 = "*".join(list2)
    print(shape2)

def f2(n):
    number = n
    count = 0
    list3 = []
    while number:
        number = number//10
        count+=1
    for i in range(count-1,-1,-1):
        num = n//(10**i)
        list3.append(num%2)
    for e in list3:
        if e == 0:
            print(f"\N{black square}",end="")
        if e ==1:
            print(f"\N{white square}",end="")
    return ''


def f3(n):
    number = n
    count = 0
    list3 = []
    max_number = 0
    while number:
        list3.append(number%10)
        max_number = max(max_number,number%10)
        number = number//10

    if max_number !=0:
        for i in range(max_number+1,11,1):
            val = 0
            for e in range(len(list3)):
                val += list3[e]*(max_number+1)**e
            print(f"{n} is {val} in base {i}")
    else:
        for i in range(2,11,1):
            print(f"{n} is 0 in base {i}")
           
def f4(n,base):
    di = {}
    for i in range(n):
        di[i]=int2base(i,base)
    print(di)

def int2base(n,base):
    list_ib =[]
    if n:
        while n :
            code = n%base
            n = n//base
            list_ib.append(code)
    else:
        list_ib.append(0)
    return list_ib[::-1]
    
    

f4(5,2)

def f5(integaral_part,fractional_part):
    string = str(fractional_part)
    number = (integaral_part*(10**len(string))+fractional_part)/10**len(string)
    precision = 2 * len(string)

# 2. 然后，使用 str.format() 方法来应用这个动态的精度
#    第一个 {} 是数字的占位符，第二个 {} 是精度的占位符
    final = "{:.{}f}".format(number, precision)
    # final = f"{number:.10f}"
    print(final)
f5(123,11111111111)
def f6(L,key1):
    l1 =[]
    for i in range(len(L)):
        l1.append(L[i][key1[0]-1])
    
    L = sorted(L,key=l1) 

    print(L)

def f6(L: list[list[int]], K: list[int]) -> list[list[int]]:
    """
    根据一个“排序规则”列表 K，对一个由列表组成的列表 L 进行多级排序。

    Args:
        L: 一个列表，其元素也是列表，例如 [[3, 3], [0, 0]]。
        K: 一个由整数组成的列表，指定了排序的优先级。
           例如 [1, 2] 表示先按第1列排，再按第2列排。
           [2, 1] 表示先按第2列排，再按第1列排。
           注意：K 中的索引是基于 1 的，代码中需转换为基于 0 的索引。

    Returns:
        一个根据规则 K 排序后的新列表。
    """
    
    # 使用 sorted() 函数进行排序。关键在于 key 参数。
    # 我们用一个 lambda 函数来为 L 中的每个元素（item）动态生成一个排序“键”。
    # 这个“键”是一个元组，元组的元素顺序由 K 决定。
    # Python 会自动按元组的字典序进行排序。
    # 例如，当 K=[2, 1] 且 item=[3, 2] 时，生成的键是 (item[1], item[0]) -> (2, 3)
    
    # tuple(item[c - 1] for c in K) 是一个生成器表达式，
    # 它会根据 K 中的顺序高效地创建出排序键元组。
    
    sorted_list = sorted(L, key=lambda item: tuple(item[c - 1] for c in K))
    
    return sorted_list

# --- 运行示例 ---

# Test Case 1 from your screenshot
L1 = [[3], [0], [1], [0], [8], [4], [0], [4], [7]]
K1 = [1, 1]
print(f"输入 L: {L1}")
print(f"排序规则 K: {K1}")
print(f"输出: {f6(L1, K1)}\n")
# 预期输出: [[0], [0], [0], [1], [3], [4], [4], [7], [8]]

# Test Case 2 from your screenshot
L2 = [[3, 3], [0, 0], [0, 2], [0, 1], [1, 1], [3, 2]]
K2 = [1, 2]
print(f"输入 L: {L2}")
print(f"排序规则 K: {K2}")
print(f"输出: {f6(L2, K2)}\n")
# 预期输出: [[0, 0], [0, 1], [0, 2], [1, 1], [3, 2], [3, 3]]

# Test Case 3 from your screenshot
L3 = [[3, 3], [0, 0], [0, 2], [0, 1], [1, 1], [3, 2]]
K3 = [2, 1]
print(f"输入 L: {L3}")
print(f"排序规则 K: {K3}")
print(f"输出: {f6(L3, K3)}\n")
# 预期输出: [[0, 0], [0, 1], [1, 1], [0, 2], [3, 2], [3, 3]]
