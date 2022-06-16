STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with',
]


def make_lowercase(file):
    lowercase = []
    for line in file.readlines():
        lowercase.append(line.lower())
    return lowercase


def remove_punctuations(file):
    removed_punctuations = []
    for line in file:
        removed_punct_line = line.replace(',', '').replace('.', '').replace('?', '')
        removed_punctuations.append(removed_punct_line)
    return removed_punctuations 


def add_to_dictionary(file):
    word_dictionary = {}
    words_list = []
    for line in file:
        for word in line.split():
            words_list.append(word)

    for word in words_list:
        word_dictionary[word] = words_list.count(word)
    return word_dictionary


def remove_stop_words(word_dict):
    print(word_dict)
    new_word_dict = word_dict.copy()
    for word_key in word_dict:
        if word_key in STOP_WORDS:
            del new_word_dict[word_key]
    return new_word_dict
    

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as open_file:
        lowercase = make_lowercase(open_file)
        removed_punctuation = remove_punctuations(lowercase)
        word_dict = add_to_dictionary(removed_punctuation)
        word_dict_values = remove_stop_words(word_dict)

        new_list = sorted(word_dict_values.items(), key=lambda x: x[1], reverse=True)
        for i in new_list:
            print(f"{i[0]:15} | {i[1]} {'*' * i[1]}")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()
    file = Path(args.file)

    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
