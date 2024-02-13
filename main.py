def summarize(x: int, y: int) -> int:
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def get_dict():
    return {'name': 'Ivan', 'age': 29, 'city': 'Moscow'}


# a = ['Milk', 'Eggs', 'Milk', 'Meat', 'Bread', 'Milk', 'Spam', 'Butter', 'Sugar']
def get_most_popular(items: list) -> str:
    list_ = []
    for i in set(items):
        list_.append([i, items.count(i)])
    list_.sort(key=lambda x:x[1], reverse=1)
    return list_[0]
# Milk


# x = 10
# y = 20
# expected = 30
# res = summarize(x, y)
# assert res == expected

# x = 14
# y = 24
# expected = 40
# res = summarize(x, y)
# assert res > expected

# 1. Операции сравнения
# 2. is, is not
# key1 = "phone"
# value1 = None
#
# dict1 = get_dict()
# value = dict1.get(key1)
# assert value is value1

# 3. in / not in
# 4. is None, is not None
# 5. isinstance(), issubclass()
# 6. isdigit(), isalpha(), islower(), isupper()

SOME_NUMBER = 40
