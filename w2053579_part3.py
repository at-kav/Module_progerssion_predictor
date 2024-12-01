def create_textfile(data):
    file = open('input_data.txt','w')
    file.write('Part 3:\n')
    for item in data:
        file.write(f'{item}\n')
    file.close
