import sys


def main(start_1: int, finish_1: int):
    file_name = 'bakery.csv'
    with open(file_name, 'r', encoding='utf-8') as price_list:
        line = price_list.readline()
        line_count = 1
        while (line_count <= finish_1) or (finish_1 == 0 and line):
            if line_count >= start_1:
                print(line.strip())
            line = price_list.readline()
            line_count += 1


if __name__ == '__main__':

    if len(sys.argv) == 1:
        exit(main(1, 0))
    elif len(sys.argv) == 2:
        prog, start = sys.argv
        exit(main(int(start), 0))
    elif len(sys.argv) == 3:
        prog, start, finish = sys.argv
        exit(main(int(start), int(finish)))
    else:
        print("Ожидались параметры вывода")
