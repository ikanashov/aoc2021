"""
https://adventofcode.com/2021/about
Day 1: Sonar Sweep
"""


def day_1_task1(filename: str):
    """Count increased measurement"""
    with open(filename, encoding='utf-8') as file:
        data = [int(line.strip()) for line in file]
        inc = 0
        for i in range(len(data) - 1):
            if data[i] < data[i+1]:
                inc += 1
        print(f'input filename - {filename} increased measurement - {inc}')


if __name__ == '__main__':
    day_1_task1('test.txt')
    day_1_task1('input.txt')
