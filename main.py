from collections import deque
from math import inf


class info_class:
    k: int = 0
    x = "a"
    regex = ""

    def read(self):
        self.regex = input()
        self.x = input()
        self.k = int(input())

    def read_from_file(self, file_name):
        with open(file_name, 'r') as file:
            self.regex = file.readline()
            self.x = file.readline()
            self.k = int(file.readline())


info = info_class()


class object_stack:

    def __init__(self, char='#'):
        self.min_len_prefix = list()
        self.can_do_xk = list()
        for i in range(info.k + 1):
            self.min_len_prefix.append(inf)
            self.can_do_xk.append(False)
        if char != '#':
            self.min_len_prefix[0] = 1
        if char == info.x:
            self.min_len_prefix[1] = 1
            self.can_do_xk[1] = True


def do_plus(left: object_stack, right: object_stack) -> object_stack:
    current_object = object_stack()
    for i in range(info.k + 1):
        current_object.min_len_prefix[i] = min(left.min_len_prefix[i], right.min_len_prefix[i])
        current_object.can_do_xk[i] = left.can_do_xk[i] or right.can_do_xk[i]
    return current_object


def do_multiply(left: object_stack, right: object_stack) -> object_stack:
    current_object = object_stack()
    for i in range(info.k + 1):
        current_object.min_len_prefix[i] = left.min_len_prefix[i] + right.min_len_prefix[0]
        for j in range(i + 1):
            if left.can_do_xk[j]:
                current_object.min_len_prefix[i] = min(current_object.min_len_prefix[i],
                                                       j + right.min_len_prefix[i - j])
            if left.can_do_xk[j] and right.can_do_xk[i - j]:
                current_object.can_do_xk[i] = True
    return current_object


def do_Klini_star(obj: object_stack) -> object_stack:
    current_object = obj
    current_object.can_do_xk[0] = True
    current_object.min_len_prefix[0] = 0
    for i in range(info.k + 1):
        if current_object.can_do_xk[i]:
            for j in range(info.k + 1):
                if i + j > info.k:
                    break
                if current_object.can_do_xk[j]:
                    current_object.can_do_xk[i + j] = True
                    current_object.min_len_prefix[i + j] = i + j
    for i in range(info.k + 1):
        if current_object.can_do_xk[i]:
            for j in range(info.k + 1):
                if i + j > info.k:
                    break
                current_object.min_len_prefix[i + j] = min(current_object.min_len_prefix[i + j],
                                                           i + current_object.min_len_prefix[j])
    return current_object


def calculate(information: info_class) -> int:
    global info
    info = information
    help_buffer = deque()
    for c in information.regex:
        if c.isalpha():
            help_buffer.append(object_stack(c))
        else:
            if c == '+':
                second = help_buffer.pop()
                first = help_buffer.pop()
                help_buffer.append(do_plus(first, second))
            if c == '.':
                second = help_buffer.pop()
                first = help_buffer.pop()
                help_buffer.append(do_multiply(first, second))
            if c == '*':
                obj = help_buffer.pop()
                help_buffer.append(do_Klini_star(obj))
    res = help_buffer.pop()
    return res.min_len_prefix[info.k]
