from urllib.request import urlopen

def words():
    with urlopen('http://bothellrobotics.com/programs') as programs:
        program_words = []
        for line in programs:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                program_words.append(word)

    for word in program_words:
        print(word)

if(__name__ == '__main__'):
    words()
