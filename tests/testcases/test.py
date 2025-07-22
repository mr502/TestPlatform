from typing import Union

var_1 : int = 1
var_2 : int = 2

var1 = 1 # type:int

# 混合类型注解
my_list: list[Union[int,str]] = [1,2,3,"1"]
# 对形参进行注解
def test_func(x:int,y : int):
    return x + y

# 对返回值进行注解
def test_func2(data: list) -> list:
    return data