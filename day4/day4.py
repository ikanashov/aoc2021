"""
https://adventofcode.com/2021/about
Day 4: Giant Squid
"""
from itertools import chain


def day_4_task1(filename: str) -> None:
    """Play bingo part 1"""
    with open(filename, encoding='utf-8') as file:
        numbers = list(map(int, file.readline().strip().split(',')))
        data = [list(map(int, line.strip().split()))
                for line in file if line.strip()]
        t_len = 5
        num_table = len(data) // t_len

        data_tuple = []
        for num in range(num_table):
            for row_num in range(t_len):
                data_tuple.append([data[row_num + num * t_len][col_num]
                                   for col_num in range(t_len)])
                data_tuple.append([data[col_num + num * t_len][row_num]
                                   for col_num in range(t_len)])

        be_numbers = []
        is_bingo = False
        for number in numbers:
            if is_bingo:
                break
            be_numbers.append(number)
            for num, line in enumerate(data_tuple):
                if not set(line) - set(be_numbers):
                    win_line = line
                    b_t_num = int((num / 2) / t_len)
                    bingo_table = chain.from_iterable(
                        data[b_t_num * t_len: (b_t_num * t_len) + t_len])
                    bingo_sum = sum(set(bingo_table) - set(be_numbers))
                    win_number = number
                    is_bingo = True
                    break

        print(f'input filename - {filename}\n'
              f'BINGO with number {win_number} in line num {num} '
              f'line is {win_line} on table_num = {b_t_num} '
              f'with sum unmarked = {bingo_sum} \n'
              f'final score is {bingo_sum * win_number}')


def day_4_task2(filename: str) -> None:
    """Play bingo part 2 (last win)"""
    with open(filename, encoding='utf-8') as file:
        numbers = list(map(int, file.readline().strip().split(',')))
        data = [list(map(int, line.strip().split()))
                for line in file if line.strip()]
        t_len = 5
        num_table = len(data) // t_len

        data_tuple = []
        for num in range(num_table):
            for row_num in range(t_len):
                data_tuple.append([data[row_num + num * t_len][col_num]
                                   for col_num in range(t_len)])
                data_tuple.append([data[col_num + num * t_len][row_num]
                                   for col_num in range(t_len)])

        be_numbers = []
        win_table: list[int] = []
        for number in numbers:
            if len(set(win_table)) == num_table:
                break
            be_numbers.append(number)
            for num, line in enumerate(data_tuple):
                if not set(line) - set(be_numbers):
                    win_line = line
                    b_t_num = int((num / 2) / t_len)
                    bingo_table = chain.from_iterable(
                        data[b_t_num * t_len: (b_t_num * t_len) + t_len])
                    bingo_sum = sum(set(bingo_table) - set(be_numbers))
                    win_number = number
                    win_table.append(b_t_num)
                    if len(set(win_table)) == num_table:
                        break

        print(f'input filename - {filename}\n'
              f'BINGO with number {win_number} in line num {num} '
              f'line is {win_line} on table_num = {b_t_num} '
              f'with sum unmarked = {bingo_sum} \n'
              f'final score is {bingo_sum * win_number}')


if __name__ == '__main__':
    day_4_task1('test.txt')
    day_4_task1('input.txt')

    day_4_task2('test.txt')
    day_4_task2('input.txt')
