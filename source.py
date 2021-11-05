from collections import deque
from math import inf


class InputData:
    __instance = None

    def __init__(self):
        prefix_len: int = 0
        prefix_symbol = "a"
        regex = ""

    @staticmethod
    def getinstance():
        if InputData.__instance is None:
            InputData.__instance = InputData()
        return InputData.__instance

    def read(self):
        self.regex = input()
        self.prefix_symbol = input()
        self.prefix_len = int(input())

    def read_from_file(self, file_name):
        with open(file_name, 'r') as file:
            self.regex = file.readline()
            self.prefix_symbol = file.readline()
            self.prefix_len = int(file.readline())


class ObjectStack:
    __eps = '#'

    def __init__(self, char=__eps):
        self.min_len_prefix = list()
        self.can_do_xk = list()
        for i in range(InputData().getinstance().prefix_len + 1):
            self.min_len_prefix.append(inf)
            self.can_do_xk.append(False)
        if char != ObjectStack.__eps:
            self.min_len_prefix[0] = 1
        if char == InputData().getinstance().prefix_symbol:
            self.min_len_prefix[1] = 1
            self.can_do_xk[1] = True


def do_plus(left: ObjectStack, right: ObjectStack) -> ObjectStack:
    current_object = ObjectStack()
    for i in range(InputData().getinstance().prefix_len + 1):
        current_object.min_len_prefix[i] = min(left.min_len_prefix[i], right.min_len_prefix[i])
        current_object.can_do_xk[i] = left.can_do_xk[i] or right.can_do_xk[i]
    return current_object


def do_multiply(left: ObjectStack, right: ObjectStack) -> ObjectStack:
    current_object = ObjectStack()
    for i in range(InputData().getinstance().prefix_len + 1):
        current_object.min_len_prefix[i] = left.min_len_prefix[i] + right.min_len_prefix[0]
        for j in range(i + 1):
            if left.can_do_xk[j]:
                current_object.min_len_prefix[i] = min(current_object.min_len_prefix[i],
                                                       j + right.min_len_prefix[i - j])
            if left.can_do_xk[j] and right.can_do_xk[i - j]:
                current_object.can_do_xk[i] = True
    return current_object


def do_Klini_star(obj: ObjectStack) -> ObjectStack:
    current_object = obj
    current_object.can_do_xk[0] = True
    current_object.min_len_prefix[0] = 0
    for i in range(InputData().getinstance().prefix_len + 1):
        if current_object.can_do_xk[i]:
            for j in range(InputData().getinstance().prefix_len + 1):
                if i + j > InputData().getinstance().prefix_len:
                    break
                if current_object.can_do_xk[j]:
                    current_object.can_do_xk[i + j] = True
                    current_object.min_len_prefix[i + j] = i + j
    for i in range(InputData().getinstance().prefix_len + 1):
        if current_object.can_do_xk[i]:
            for j in range(InputData().getinstance().prefix_len + 1):
                if i + j > InputData().getinstance().prefix_len:
                    break
                current_object.min_len_prefix[i + j] = min(current_object.min_len_prefix[i + j],
                                                           i + current_object.min_len_prefix[j])
    return current_object


def calculate_min_len_word_with_prefix() -> int:
    help_buffer = deque()
    for symbol in InputData().getinstance().regex:
        if symbol.isalpha():
            help_buffer.append(ObjectStack(symbol))
        else:
            if symbol == '+':
                right_operand = help_buffer.pop()
                left_operand = help_buffer.pop()
                help_buffer.append(do_plus(left_operand, right_operand))
            if symbol == '.':
                right_operand = help_buffer.pop()
                left_operand = help_buffer.pop()
                help_buffer.append(do_multiply(left_operand, right_operand))
            if symbol == '*':
                obj = help_buffer.pop()
                help_buffer.append(do_Klini_star(obj))
    object_stack_for_regex = help_buffer.pop()
    return object_stack_for_regex.min_len_prefix[InputData().getinstance().prefix_len]
