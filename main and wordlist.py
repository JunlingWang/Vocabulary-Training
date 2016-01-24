__author__ = 'junlingwang'
import worditem
from worditem import get_word_item
from worditem import WordItem
import random


def read_file(file_name):  # returns a list sorted by score
    with open('/home/junlingwang/Desktop/Vocabulary trainning/'+file_name+'.txt', 'r') as word_file:
        lines = word_file.readlines()  # lines is a list of strings
    word_list = []
    for line in lines:  # line is a string in lines
        word_list.append(get_word_item(line.strip()))  # strip(), delete blank characters including '\n'
    sorted_list = sorted(word_list, key=lambda item: item.score, reverse=True)  # word_list is not changed
    #  lambda function. Before the colon is parameter, after the colon is the result.
    # this lambda function is to sort the word list's item by their scores
    return sorted_list


def write_file(word_list, file_name):
    lines = []  # list of strings
    for item in word_list:
        lines.append(item.generate_str() + '\n')
    with open('/home/junlingwang/Desktop/Vocabulary trainning/'+file_name+'.txt', 'w') as word_file:
        word_file.writelines(lines)
        # each item of the list 'lines' occupies a line in the txt file


def add_word_item(word_list, new_word_item):
    match_count = 0
    i = 0
    while i < len(word_list):
        if word_list[i].word == new_word_item.word:
            word_list[i] = new_word_item
            match_count += 1
        i += 1
    if match_count == 0:
        word_list.append(new_word_item)


def random_machine(score):
    if score >= 11:
        return True
    elif score < 1:
        return False
    else:
        ratio_factor = 2 # the bigger the more false words chosen
        random_number = random.randint(1, (int(score)+ratio_factor)) # get random number from range i to int(score)
        if random_number == 1:
            return False
        else:
            return True


def divide_list(word_list):
    list_not_exercised = []
    list_all_correct = []
    list_fault = []
    for item in word_list:
        if item.score == -2:
            list_not_exercised.append(item)
        elif item.score == -1:
            list_all_correct.append(item)
        else:
            list_fault.append(item)
    return list_not_exercised, list_all_correct, list_fault
    # returns a tuple containing three lists

########################################
# main below


def main(file_name):
    sorted_word_list = read_file(file_name)  # read_file has the function of sorting items by scores
    list_not_exercised, list_all_correct, list_fault = divide_list(sorted_word_list)
    # divide_list() is a function defined previously
    not_exercised_count = 0
    all_correct_count = 0
    fault_count = 0
    word_to_practice = None
    i = 0  # prevents infinite loop
    while True:
        word_to_practice = None  # in case the same word appears repeatedly
        if len(list_fault) > fault_count:
            choose_fault = random_machine(list_fault[fault_count].score)
        else:
            choose_fault = False
        if choose_fault:
            word_to_practice = list_fault[fault_count]
            fault_count += 1
        else:
            choose_not_exercised = random_machine(10)
            # the ratio of all correct to not exercised is 1 to 11
            if choose_not_exercised and len(list_not_exercised) > not_exercised_count:
                word_to_practice = list_not_exercised[not_exercised_count]
                not_exercised_count += 1
                # print('Not exercised count is', not_exercised_count) # for test
            elif len(list_all_correct) > all_correct_count:
                word_to_practice = list_all_correct[all_correct_count]
                all_correct_count += 1
                # print('All correct count is ' , all_correct_count) # for test
            elif (len(list_not_exercised) <= not_exercised_count and len(list_fault) <= fault_count) or i >= len(sorted_word_list):
                print('Finished today!')
                break
            else:
                i += 1

        if word_to_practice is not None:
            print(word_to_practice.voice)
            print(word_to_practice.meaning)
            word_input = input('input word \n')

            if word_input == word_to_practice.word:
                result = 't'
                do_continue = input('Correct! Any Key continue, X quit R repeat\n')
            elif word_input == 'x' or word_input == 'X':
                break
            # if user types 'x' during practice it's not considered as wrong
            # but considered as that he wants to quit
            else:
                result = 'f'
                do_continue = input('Wrong! It should be:\n'+word_to_practice.word + '\n Any Key continue, X quit R repeat \n')
            word_to_practice.add_result(result)
            add_word_item(sorted_word_list, word_to_practice)
            print(do_continue)
            while len(do_continue) > 1 or do_continue == 'r':
                if len(do_continue) > 1:
                    for item in sorted_word_list:
                        if do_continue == item.word:
                            word_to_practice = item
                            print(word_to_practice.voice)
                            word_input = input('input word \n')
                            if word_input == word_to_practice.word:
                                result = 't'
                                do_continue = input('Correct! Any Key continue, X quit R repeat\n')
                            elif word_input == 'x' or word_input == 'X':
                                do_continue = word_input
                                break
                            # if user types 'x' during practice it's not considered as wrong
                            # but considered as that he wants to quit
                            else:
                                result = 'f'
                                do_continue = input('Wrong! It should be:\n'+word_to_practice.word + '\n Y continue, X quit R repeat \n')
                                word_to_practice.add_result(result)
                                add_word_item(sorted_word_list, word_to_practice)
                if do_continue == 'r':
                    print(word_to_practice.voice)
                    word_input = input('input word \n')
                    if word_input == word_to_practice.word:
                        result = 't'
                        do_continue = input('Correct! Any Key continue, X quit R repeat\n')
                    else:
                        result = 'f'
                        do_continue = input('Wrong! It should be:\n'+word_to_practice.word + '\n Y continue, X quit R repeat \n')
                        word_to_practice.add_result(result)
                        add_word_item(sorted_word_list, word_to_practice)
            if do_continue == 'x' or do_continue == 'X':
                break

    write_file(sorted_word_list, file_name)


#######################
# test below


def test_read_file():
    word_list = read_file('oxford3000')
    for word_item in word_list:
        print(word_item)
    print('\n')

    new_item = get_word_item('dgrtyhaha,/hhh/')
    # word_list[1] = new_item
    add_word_item(word_list, new_item)
    for word_item in word_list:
        print(word_item)
    # list_not_exercised, list_all_correct, list_fault = divide_list(word_list)
    #
    # for word_item in list_not_exercised:
    #     print(word_item)
    # print('\n')
    #
    # for word_item in list_all_correct:
    #     print(word_item)
    # print('\n')
    #
    # for word_item in list_fault:
    #     print(word_item)
    # print('\n')

    write_file(word_list, 'oxford3000')


if __name__ == '__main__':
    main('oxford3000+')
