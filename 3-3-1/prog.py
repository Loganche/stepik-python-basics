text = ''
with open ('in.txt', 'r') as file_in, open("out.txt", 'w') as file_out:
    text = file_in.readline()
    for i in range(len(text)):
        if '0' <= text[i] <= '9' and '0' <= text[i-1] <= '9':
            num = int(text[i-1] + text[i])
            l = str(text[i-2]) * (num - 1)
            file_out.write(l)
        elif '0' <= text[i] <= '9':
            num = int(text[i])
            l = str(text[i-1]) * (num)
            file_out.write(l)
        elif text[i] == len(text) - 1 and '0' <= text[i] <= '9':
            num = int(text[i])
            l = str(text[i-1]) * num
            file_out.write(l)
