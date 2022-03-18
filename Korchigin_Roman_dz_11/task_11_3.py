class OnlyNumber(Exception):
    def __init__(self, *args):
        super().__init__(*args)


if __name__ == "__main__":
    list_number = []
    while True:
        try:
            i = input()
            if i == "stop":
                break
            elif not i.isdigit():
                raise OnlyNumber()
            else:
                list_number.append(int(i))
        except OnlyNumber:
            print("Вы вводите не число")

    print(*list_number)
