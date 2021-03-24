import requests

averages = []
counter = 0
value01 = 0
value02 = 0
value03 = 0

with open('in.txt', 'r', encoding='utf-8') as in_f_obj:

    for line in in_f_obj:
        line = line.rstrip().split(';')
        student_average = round(
            ((int(line[1]) + int(line[2]) + int(line[3])) / 3), 9)
        averages.append(student_average)
        value01 += int(line[1])
        value02 += int(line[2])
        value03 += int(line[3])
        counter += 1

with open('out.txt', 'w') as out_f_obj:

    for _ in averages:
        out_f_obj.write(str(_) + '\n')

    average_math = round(value01 / counter, 9)
    average_phys = round(value02 / counter, 9)
    average_rus = round(value03 / counter, 9)

    out_f_obj.write(str(average_math) + ' ' +
                    str(average_phys) + ' ' +
                    str(average_rus))
