"""
https://adventofcode.com/2021/about
Day 3: Binary Diagnostic
"""


def day_3_task1(filename: str) -> None:
    """Calculate the power consumption of the submarine part 1"""
    with open(filename, encoding='utf-8') as file:
        # read and transpose data
        data = [[int(digit) for digit in line.strip()] for line in file]
        transpose_data = list(map(list, zip(*data)))

        gamma = ['1' if len(data) - sum(column) < sum(column) else '0'
                 for column in transpose_data]
        epsilon = ['0' if digit == '1' else '1' for digit in gamma]

        gamma_rate = int('0b' + ''.join(gamma), 2)
        epsilon_rate = int('0b' + ''.join(epsilon), 2)

        print(f'input filename - {filename} gamma_rate - {gamma_rate} '
              f'epsilon_rate - {epsilon_rate} '
              f'power consumption {gamma_rate * epsilon_rate}')


if __name__ == '__main__':
    day_3_task1('test.txt')
    day_3_task1('input.txt')
