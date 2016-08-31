__author__ = 'junlingwang'

from datetime import datetime
MAXIMUM_ROUNDS = 5
NEVER_WRONG_ROUNDS =5


def get_score(history_str):
    date_today = datetime.now()  # this is a datetime object, not str
    practice_list = history_str.split(';')
    number_of_practice = 0
    i = 0
    while i < MAXIMUM_ROUNDS and i < len(practice_list):
        if practice_list[i][0] != '0':
            number_of_practice += 1
        i += 1

    number_of_correction = 0
    i = 0
    while i < MAXIMUM_ROUNDS and i < len(practice_list):
        if practice_list[i][-1] == 't':
            number_of_correction += 1
        i += 1

    number_of_false = 0
    i = 0
    while i < MAXIMUM_ROUNDS and i < len(practice_list):
        if practice_list[i][-1] == 'f':
            number_of_false += 1
        i += 1

    number_of_practice_since_last_fault = 0
    i = 0
    while i < MAXIMUM_ROUNDS and i < len(practice_list):
        if practice_list[i][-1] == 't':
            number_of_practice_since_last_fault += 1
            i += 1
        elif practice_list[i][-1] == 'n':
            break
        else:
            number_of_practice_since_last_fault += 1
            break
    #  the practices before the fault won't count
    #  this gives the words with faults higher priority than ones without fault

    if number_of_practice == 0:
        return -2
    elif (number_of_practice == MAXIMUM_ROUNDS and number_of_correction == MAXIMUM_ROUNDS) or(number_of_practice >=NEVER_WRONG_ROUNDS and number_of_correction == number_of_practice):
        return -1
    else:
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
        score = date_difference_int / pow(2, (number_of_practice_since_last_fault - 1))
        #  words with fault gets higher scores
        return score


class WordItem:
    def __init__(self, word='', voice='', meaning='', history='', score=-2, weight=0):
        self.word = word
        self.voice = voice
        self.meaning = meaning
        self.history = history
        self.score = score  # float format
        self.weight = weight  # int, the times of fault, or if no fault, can be manually set as 1
                                # used to determine how much the word tends to be fault

    def __str__(self):
        return self.word + ',' + self.voice + ',' + self.meaning + ',' + self.history + ',' + str(self.score) + ',' + str(self.weight)

    def get_info(self):
        return self.voice + ',' + self.meaning + ',' + self.history + ',' + str(self.score)

    def generate_str(self):
        return self.word + ',' + self.voice + ',' + self.meaning + ',' + self.history + ',' + str(self.score) + ',' + str(self.weight)
    
    def add_result(self, result='t'):
        if result != 't':
            result = 'f'
        date_today = datetime.now()  # this is a datetime object, not str
        practice_list = self.history.split(';')
        if len(practice_list) < MAXIMUM_ROUNDS:
            difference = MAXIMUM_ROUNDS - len(practice_list)
            i = 0
            while i < difference:
                practice_list.append('0001-01-01n')  # there is no ';' in the list item, ';' is used to split the string
                i += 1

        i = 1
        while i < MAXIMUM_ROUNDS:
            practice_list[MAXIMUM_ROUNDS - i] = practice_list[MAXIMUM_ROUNDS - (i + 1)]
            i += 1
        practice_list[0] = str(date_today)[0: 10] + result
        new_history = practice_list[0]
        j = 1
        while j < MAXIMUM_ROUNDS:
            new_history += ';' + practice_list[j]
            j += 1
        self.history = new_history
        self.score = get_score(new_history)
        if result == 'f':
            self.weight += 1


def get_word_item(word_str):
    wi = WordItem('')  # ('') must be there or __str__() method doesn't work. Don't know why.
    attributes_list = word_str.split(',')
    wi.word = attributes_list[0]
    wi.history = '0001-01-01n;' * (MAXIMUM_ROUNDS - 1) + '0001-01-01n'
    wi.weight = 0
    if len(attributes_list) >= 2:
        wi.voice = attributes_list[1]
    if len(attributes_list) >= 3:
        wi.meaning = attributes_list[2]
    if len(attributes_list) >= 4 and len(attributes_list[3]) > 0:
        wi.history = attributes_list[3]
    # print(word_str+'\n')  # for trouble shooting
    wi.score = get_score(wi.history)
    if len(attributes_list) >= 6 and len(attributes_list[5]) > 0:
        wi.weight = int(attributes_list[5])
    else:
        practice_list = (wi.history).split(';')
        number_of_false = 0
        i = 0
        while i < MAXIMUM_ROUNDS and i < len(practice_list):
            if practice_list[i][-1] == 'f':
                number_of_false += 1
            i += 1
            wi.weight = number_of_false
    return wi

#######################################
# test below


def test_word_item():
    w = WordItem('good')
    w.voice = 'gud'
    w.meaning = 'desirable'
    w.history = 'F'
    w.score = '265'
    print(w)
    print(w.word)
    print(w.get_info())


def test_get_word_item():
    word_str = 'cup,/kap/,container with handle,0000-00-00n;0000-00-00n;0000-00-00n;0000-00-00n;0000-00-00n,16,'
    wi = get_word_item(word_str)
    print(wi.word)
    print(wi.voice)
    print(wi.meaning)
    print(wi.history)
    print(wi.score)
    print(wi)
    # print(wi.generate_str())
    wi.add_result('t')
    print(wi)
    wi.add_result('t')
    print(wi)
    # print(word_str)


def test_get_score():
    history_str = '2015-11-23t;2014-02-03t;2013-01-02f;0000-00-00n;0000-00-00n,16'
    print(get_score(history_str))


if __name__ == '__main__':
    test_get_score()