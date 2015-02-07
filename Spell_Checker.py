__author__ = 'Wanchun Zhao'

# read text from a file
def read_text(file_name):
    in_file=open(file_name,"r")
    file_contents=in_file.readlines()
    in_file.close()
    return file_contents

# strip /r/n from every line of the text
def strip_line(list_of_items):
    for i in range(0,len(list_of_items)-1):
        list_of_items[i]=list_of_items[i].rstrip()
    return list_of_items

# split the text into words
def split_text(lines_of_text):
    list_of_words=list()
    for line in lines_of_text:
        line=line.rstrip()
        line=line.lower()
        line=line.replace(',','')
        line=line.replace('.','')
        line=line.replace('*','')
        line=line.replace('(','')
        line=line.replace(')','')
        words=line.split(' ')
        list_of_words.extend(words)
    return list_of_words

# check the spelling by comparing input words to items in dictionary
def check_spelling(misspelled_words,words_in_input,dictionary_items):
    for word in words_in_input:
        if word not in dictionary_items:
            if word in misspelled_words:
                misspelled_words[word]+=1
            else:
                misspelled_words[word]=1
    return misspelled_words

# print misspelled words and corresponding frequency
def print_misspelling(misspelled_words):
     for key in misspelled_words:
        print key, misspelled_words[key]

# replace markup signs in each word
def replace_markups(word):
    word=word.replace('&','&amp;')
    word=word.replace('"','&quot;')
    word=word.replace('<','&lt;')
    word=word.replace('>','&gt;')
    return word


def print_header():
    output_file = open("spelling_correction.html", "a")
    output_file.writelines("<html><head><title>Correction</title></head><body><br />")

def print_footer():
    output_file = open("spelling_correction.html", "a")
    output_file.writelines("</body></html>")

# create correction output
def create_output(input_contents,misspelled_words):

    output_file=open("spelling_correction.html","w")
    print_header()

    for line in input_contents:
        list_of_words= line.split()
        for word in list_of_words:
            # replace markup signs in word
            word=replace_markups(word)
            if word in misspelled_words:
                output_file.writelines("<u><b>" + word + "</b></u> ")
            else:
                output_file.writelines(word+" ")
    print_footer()
    output_file.close()


# main function
def main():
    # read the items in dictionary
    dictionary_items=read_text("dictionary.txt")
    dictionary_items=strip_line(dictionary_items)

    # read the words in input file
    input_contents=read_text("input.txt")
    input_words=split_text(input_contents)

    # check the spelling
    misspelled_words=dict()
    misspelled_words=check_spelling(misspelled_words,input_words,dictionary_items)

    # print misspelled words print misspelled words and corresponding frequency
    print_misspelling(misspelled_words)

    # create correction output
    create_output(input_contents,misspelled_words)


main()