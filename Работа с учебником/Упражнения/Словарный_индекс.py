def get_words(lines):
    count = 0
    indexes = {}

    for line in lines:
        words = line.split(' ')
        for word in words:
            if word in indexes:
                indexes[word].add(count + 1)
            else:
                indexes[word] = set([count + 1])

        count += 1

    return indexes
def input_file(w_dict):
    with open('Index.txt', 'a', encoding='utf-8')as file:
        for key in w_dict:
            file.write(f'{key}: ')
            for value in w_dict[key]:
                file.write(str(value) + ' ')
            file.write('\n')






def main():

    with open('Kennedy.txt', 'r', encoding='utf-8')as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip('\n:,.')

    w_dict = get_words(lines)

    input_file(w_dict)




if __name__ == '__main__':
    main()