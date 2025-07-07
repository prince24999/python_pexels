# print('Hello, World!')
# a = [1, 2, 3, 4, 3/2]
# print(a)

# def add(x, y):
#     return x + y

# tup1 = 1,2,3
# tup1 += (4, 5, 6)
# print(tup1)

# import pandas as pd
# print('Pandas version:', pd.__version__)

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6]
# })

# lst = [1, 2, 3, 4, 5]

# s = ''.join(str(i) for i in lst)
# s1 = ''.join(map(str, lst))
# print(s)  # Output: '12345'
# print(s1)  # Output: '12345'
# Both s and s1 should be the same
# The join method is used to concatenate the elements of the list into a single string.

# troi_mua = False

# if troi_mua:
#     {print("Mưa")}

# else:
#     {print("Không mưa")}
# The above code checks if it is raining and prints 'Mua' if it is, otherwise it prints 'Khong mua'.

# for _ in range(10):
#     print("Hello, World!")

# s = input("Enter a string: ")
# while s!= 'q':
#     print(f"You entered: {s}")
#     s = input("Enter a string (or 'q' to quit): ")

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# # Kết quả: 0 1 2

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# # Kết quả: 0 1 2 4

# lst = {"a": 1, "b": 2, "c": 3}
# # lst = [1, 2, 3, 4, 5]
# # for key, value in lst.items():
# #     print(key, value)
# # The above code iterates over a dictionary and prints each key-value pair.
# # If you want to iterate over a list, you can use:
# # for index, value in enumerate(lst):
# #     print(index, value)
# # This will print the index and value of each element in the list.

# new_lst = [val ** 2 for val in lst.values()]
# print(new_lst)

# d = {"a": 1, "b": 2, "c": 3}
# for idx, (key, value) in enumerate(d.items()):
#     print(idx, key, value)

# new_lst = [val * 2 for val in d.values()]
# print(new_lst)
# Kết quả:
# 0 a 1
# 1 b 2
# 2 c 3

# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# for x, y in zip(a, b):
#     print(x, y)
# Kết quả:
# 1 a
# 2 b
# 3 c

def my_func(msg):
    print(msg)

my_func("Hello, World!")

def calculate_stats(operation, *numbers, round_result=False, **options):
    """
    Hàm thực hiện các phép toán trên nhiều số:
    - operation: 'sum' hoặc 'mean'
    - *numbers: danh sách số truyền vào
    - round_result: nếu True thì làm tròn kết quả
    - **options: các tuỳ chọn khác (ví dụ: 'digits' cho số chữ số làm tròn)
    """
    if not numbers:
        return None

    if operation == 'sum':
        result = sum(numbers)
    elif operation == 'mean':
        result = sum(numbers) / len(numbers)
    else:
        raise ValueError("Chỉ hỗ trợ 'sum' hoặc 'mean'")

    if round_result:
        digits = options.get('digits', 2)
        result = round(result, digits)

    return result

# Ví dụ sử dụng:
print(calculate_stats('sum', 1, 2, 3, 4, 5))  # 15
print(calculate_stats('mean', 1, 2, 3, 4, 5, round_result=True, digits=3))  # 3.0