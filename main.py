import sys


class MyCustomError(Exception):
    def __init__(self, value):
        if value:
            self.value = value
        else:
            self.value = None

    def __str__(self):
        if self.value:
            return self.value
        else:
            return 'MyCustomError has been raised'


class TestClass:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def bad_a(self):
        if self.__a > self.__b:
            raise MyCustomError("'A'>'B' by " + str(self.__a - self.__b))
        else:
            return False


def get_month_name(number_of_month):
    month = {1: "January", 2: "February", 3: "March", 4: "April",
             5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}
    try:
        return month[int(number_of_month)]
    except KeyError:
        print("The entered value is not a month number")
    except ValueError:
        print("The month number must be an integer from 1 to 12")


def is_uniquenumber_list(int_list):
    unique_number = []
    if type(int_list) != list:
        raise ValueError("The function accepts a list")
    try:
        [unique_number.append(float(i)) for i in int_list if i not in unique_number]
    except ValueError:
        print("The list should only contain numbers", file=sys.stderr)
    except Exception:
        print("Something wrong", file=sys.stderr)
    return len(int_list) == len(unique_number)


print(get_month_name(10))

lst = [10, "aaa", 3]
print(is_uniquenumber_list(lst))

test = TestClass(600, 500)
print(test.bad_a())
