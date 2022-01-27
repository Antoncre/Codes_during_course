from typing import Union
def multiply(*args: Union[float, int]):
    result = 1
    for arg in args:
        result *= arg
    return result
