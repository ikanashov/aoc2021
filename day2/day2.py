"""
https://adventofcode.com/2021/about
Day 2: Dive!
"""


def day_2_task1(filename: str) -> None:
    """Calculate submarine position part 1"""
    command_place = 0
    command_value = 1
    with open(filename, encoding='utf-8') as file:
        data = [(line.strip().split()[command_place], int(line.strip().split()[command_value])) for line in file]

        forward = 0
        depth = 0
        for i in range(len(data)):
            command = data[i][command_place]
            value = data[i][command_value]

            if command == 'forward':
                forward += value
            elif command == 'up':
                depth -= value
            elif command == 'down':
                depth += value

        print(f'input filename - {filename} forward - {forward} depth - {depth}  multiply {forward * depth}')


def day_2_task2(filename: str) -> None:
    """Calculate submarine position part 2"""
    command_place = 0
    command_value = 1
    with open(filename, encoding='utf-8') as file:
        data = [(line.strip().split()[command_place], int(line.strip().split()[command_value])) for line in file]

        forward = 0
        depth = 0
        aim = 0
        for i in range(len(data)):
            command = data[i][command_place]
            value = data[i][command_value]

            if command == 'forward':
                forward += value
                depth += aim * value
            elif command == 'up':
                aim -= value
            elif command == 'down':
                aim += value

        print(f'input filename - {filename}  forward - {forward}  aim - {aim}'
              f'  depth - {depth} multiply {forward * depth}')


if __name__ == '__main__':
    day_2_task1('test.txt')
    day_2_task1('input.txt')

    day_2_task2('test.txt')
    day_2_task2('input.txt')