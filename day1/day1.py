"""
https://adventofcode.com/2021/about
Day 1: Sonar Sweep
"""


def day_1_task1(filename: str) -> None:
    """Count increased measurement"""
    with open(filename, encoding='utf-8') as file:
        data = [int(line.strip()) for line in file]
        inc = 0
        for i in range(len(data) - 1):
            if data[i] < data[i+1]:
                inc += 1
        print(f'input filename - {filename} increased measurement - {inc}')


def day_1_task2(filename: str) -> None:
    """Count increased measurement with 3-size window"""
    with open(filename, encoding='utf-8') as file:
        data = [int(line.strip()) for line in file]

    inc = 0
    i = 0
    w_size = 3
    while i < len(data) - w_size:
        w_1 = data[i: i + w_size]
        w_2 = data[i + 1: i + 1 + w_size]
        if sum(w_1) < sum(w_2) and len(w_2) == w_size:
            inc += 1
        i += 1

    print(f'input filename - {filename} increased measurement - {inc}')


if __name__ == '__main__':
    day_1_task1('test.txt')
    day_1_task1('input.txt')

    day_1_task2('test.txt')
    day_1_task2('input.txt')
