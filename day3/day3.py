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


def day_3_task2(filename: str) -> None:
    """Calculate life support rating of the submarine part 2"""
    with open(filename, encoding='utf-8') as file:
        # read and transpose data
        data = [[int(digit) for digit in line.strip()] for line in file]

        most_data = data.copy()
        most_transpose = list(map(list, zip(*most_data)))
        num_bits = len(most_transpose)
        column_num = 0
        while column_num < num_bits:
            column = most_transpose[column_num]
            most_bit = 1 if len(most_data) - sum(column) <= sum(column) else 0
            most_data = [
                line for line in most_data if line[column_num] == most_bit]
            most_transpose = list(map(list, zip(*most_data)))
            column_num += 1
            if len(most_data) == 1:
                column_num = num_bits

        least_data = data.copy()
        least_transpose = list(map(list, zip(*least_data)))
        num_bits = len(least_transpose)
        column_num = 0
        while column_num < num_bits:
            column = least_transpose[column_num]
            least_bit = 1 if len(least_data) - sum(column) > sum(column) else 0
            least_data = [
                line for line in least_data if line[column_num] == least_bit]
            least_transpose = list(map(list, zip(*least_data)))
            column_num += 1
            if len(least_data) == 1:
                column_num = num_bits

        o_rate = int('0b' + ''.join(list(map(str, most_data[0]))), 2)
        co2_rate = int('0b' + ''.join(list(map(str, least_data[0]))), 2)

        print(f'input filename - {filename} o_rate - {o_rate} '
              f'co2_rate - {co2_rate} '
              f'life support {o_rate * co2_rate}')


if __name__ == '__main__':
    day_3_task1('test.txt')
    day_3_task1('input.txt')

    day_3_task2('test.txt')
    day_3_task2('input.txt')
