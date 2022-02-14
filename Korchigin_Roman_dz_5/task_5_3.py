tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Роман', 'Анатолий']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9Е']


def check_gen(tutors: list, klasses: list):
    #return ((tutor, klasses[i]) if i < len(klasses) else (tutor, None)
    #       for _, tutor in enumerate(tutors))
    for _, tutor in enumerate(tutors):
        if i < len(klasses):
            var = (tutor, klasses[i])
        else:
            var = (tutor, None)
        yield var

generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(type(generator))
# print(generator)

for i in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
