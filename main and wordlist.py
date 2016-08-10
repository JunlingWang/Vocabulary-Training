__author__ = 'junlingwang'
import worditem
# import webbrowser
from worditem import get_word_item
# from fileprocessing import open_web_page
from worditem import WordItem
import random
from datetime import datetime


# def open_web_page(word_str):
#     webbrowser.open_new_tab("http://www.oxfordlearnersdictionaries.com/definition/english/" + word_str + "_1")


def read_file(file_name):  # returns a list sorted by score
    with open('/home/junlingwang/Desktop/Vocabulary training/'+file_name+'.txt', 'r') as word_file:
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
    with open('/home/junlingwang/Desktop/Vocabulary training/'+file_name+'.txt', 'w') as word_file:
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


def get_date_difference(word_item_to_get_date_difference):
    date_today = datetime.now()  # this is a datetime object, not str
    history_str = word_item_to_get_date_difference.history
    practice_list = history_str.split(';')
    last_practice_date_str = practice_list[0][0: -1]
    last_practice_year_int = int(last_practice_date_str[0: 4])
    last_practice_month_int = int(last_practice_date_str[5: 7])
    last_practice_day_int = int(last_practice_date_str[8: 10])
    date_difference = date_today - datetime(last_practice_year_int, last_practice_month_int, last_practice_day_int)
    if 'day' in str(date_difference):
        index_of_d = 0
        for i in str(date_difference):
            if i != 'd':
                index_of_d += 1
            else:
                break
        date_difference_int = int(str(date_difference)[0: index_of_d])
    else:
        date_difference_int = 0
    return date_difference_int


def get_daily_record(date_str, file_name=''):
    with open('/home/junlingwang/Desktop/Vocabulary training/'+file_name+'.txt', 'r') as word_file:
        lines = word_file.readlines()  # lines is a list of strings

    if len(lines) > 0 and date_str == lines[-1][0: 10]:
        last_line = lines[-1]
        times_str = last_line[11:]  # this is the string from 11th char to the relast one
        previous_exercise = int(times_str)
        return previous_exercise
    else:
        return 0


def write_daily_record(date_str='', practice_count=0, file_name=''):
    with open('/home/junlingwang/Desktop/Vocabulary training/'+file_name+'.txt', 'r') as word_file:
        lines = word_file.readlines()  # lines is a list of strings

    if len(lines) > 0 and date_str == lines[-1][0: 10]:
        last_line = lines[-1]
        times_str = last_line[11:]  # this is the string from 11th char to the relast one
        previous_exercise = int(times_str)
        practice_count += previous_exercise
        lines.remove(last_line)
    new_line = date_str+','+str(practice_count)+'\n'
    lines.append(new_line)
    with open('/home/junlingwang/Desktop/Vocabulary training/'+file_name+'.txt', 'w') as word_file:
        word_file.writelines(lines)
    return new_line[11:].strip()+' '


########################################
# main below


def main(file_name):
    sorted_word_list = read_file(file_name)  # read_file has the function of sorting items by scores
    list_not_exercised, list_all_correct, list_fault = divide_list(sorted_word_list)
    # divide_list() is a function defined previously
    print((len(sorted_word_list) - len(list_not_exercised)),'words has been practiced previously.')  # show how many words have been practised
    not_exercised_count = 0
    all_correct_count = 0
    fault_count = 0
    word_to_practice = None
    i = 0  # prevents infinite loop
    date_now = datetime.now()
    date_str = str(date_now)[0: 10]
    previous_exercise_count = get_daily_record(date_str, 'record')
    exercise_count = 0  # To count how many words are exercised.
    words_practiced_today = []
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
                print(write_daily_record(date_str, exercise_count, 'record')+"words have been exercised today.")
                break
            else:
                i += 1
        if word_to_practice in words_practiced_today or get_date_difference(word_to_practice) == 0:
            word_to_practice = None
        #  if the word has been practiced today, it will be filtered

        if word_to_practice is not None:
            words_practiced_today.append(word_to_practice)
            exercise_count += 1  # One more word is to be exercised
            print(word_to_practice.voice, previous_exercise_count, '+', exercise_count)
            if word_to_practice.meaning != '':
                print(word_to_practice.meaning)
            word_input = input('input word \n')

            if word_input == word_to_practice.word:
                result = 't'
                do_continue = input('Correct! Any Key continue, X quit R repeat M meaning I mark as important\n')
            elif word_input == 'x' or word_input == 'X':
                print(write_daily_record(date_str, exercise_count, 'record')+"words have been exercised today.")
                break
            # if user types 'x' during practice it's not considered as wrong
            # but considered as that he wants to quit
            else:
                result = 'f'
                do_continue = input('Wrong! It should be:\n'+word_to_practice.word + '\n Any Key continue, X quit R repeat M meaning I mark as important\n')
            word_to_practice.add_result(result)
            add_word_item(sorted_word_list, word_to_practice)
            while len(do_continue) > 1 or do_continue == 'r' or do_continue == 'm' or do_continue == 'i':
                if len(do_continue) > 1:
                    match_count = 0
                    for item in sorted_word_list:
                        if do_continue == item.word:
                            match_count += 1
                            word_to_practice = item
                            print(word_to_practice.voice)
                            print(word_to_practice.meaning)
                            word_input = input('input word \n')
                            if word_input == word_to_practice.word:
                                result = 't'
                                do_continue = input('Correct! Any Key continue, X quit R repeat M meaning I mark as important\n')
                            elif word_input == 'x' or word_input == 'X':
                                do_continue = word_input
                            # if user types 'x' during practice it's not considered as wrong
                            # but considered as that he wants to quit
                            else:
                                result = 'f'
                                do_continue = input('Wrong! It should be:\n'+word_to_practice.word + '\n Y continue, X quit R repeat I mark as important\n')
                                word_to_practice.add_result(result)
                                add_word_item(sorted_word_list, word_to_practice)
                            break
                    if match_count == 0:
                        break
                if do_continue == 'r':
                    print(word_to_practice.voice)
                    print(word_to_practice.meaning)
                    word_input = input('input word \n')
                    if word_input == word_to_practice.word:
                        do_continue = input('Correct! Any Key continue, X quit R repeat M meaning I mark as important\n')
                    else:
                        result = 'f'
                        do_continue = input('Wrong! It should be:\n'+word_to_practice.word + '\n Y continue, X quit R repeat I mark as important\n')
                        word_to_practice.add_result(result)
                        add_word_item(sorted_word_list, word_to_practice)
                if do_continue == 'm' or word_input == 'M':
                    meaning_input = input('Input the meaning')
                    if ',' in meaning_input or '/' in meaning_input:
                        print('No comma or slash in the meaning')
                        do_continue = input('Any Key continue, X quit R repeat M meaning I mark as important\n')

                    else:
                        word_to_practice.meaning = meaning_input
                        add_word_item(sorted_word_list, word_to_practice)
                        print(word_to_practice.meaning)
                        do_continue = input('Meaning has been saved. Any Key continue, X quit R repeat M meaning I mark as important\n')
                    # add the meaning of the item
                # if do_continue == 'c'or do_continue == 'C':
                #     open_web_page(word_to_practice.word)
                #     do_continue = input('Any Key continue, X quit R repeat M meaning I mark as important\n')
                if do_continue == 'i' or do_continue == 'I':
                    if word_to_practice.weight == 0:
                        word_to_practice.weight = 1
                    add_word_item(sorted_word_list, word_to_practice)
                    print('Current importance index is', word_to_practice.weight)
                    do_continue = input('Any Key continue, X quit R repeat M meaning I mark as important\n')
            if do_continue == 'x' or do_continue == 'X':
                print(write_daily_record(date_str, exercise_count, 'record')+"words have been exercised today.")
                break

    write_file(sorted_word_list, file_name)
    sorted_word_list = read_file(file_name)  # read_file has the function of sorting items by scores
    list_not_exercised, list_all_correct, list_fault = divide_list(sorted_word_list)
    # divide_list() is a function defined previously
    print((len(sorted_word_list) - len(list_not_exercised)),'words totally.')  # show how many words have been practised

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
    # main('newwords')
