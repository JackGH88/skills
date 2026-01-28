"""
简单的 Python 示例代码
"""


def greet(name):
    """问候函数"""
    return f"你好, {name}!"


def calculate_sum(a, b):
    """计算两个数的和"""
    return a + b


if __name__ == "__main__":
    # 示例使用
    print(greet("用户"))
    print(f"5 + 3 = {calculate_sum(5, 3)}")

    # 列表操作
    fruits = ["苹果", "香蕉", "橙子"]
    for fruit in fruits:
        print(f"水果: {fruit}")