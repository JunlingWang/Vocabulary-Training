__author__ = 'junlingwang'

from datetime import datetime

# s = '  12,4      dfg/  '
# print(s.split(','))
# print(s[0: -1])
# print(pow(2, 0.5))

# print(str(datetime.now()))
# print(datetime.now() - datetime(2015, 1, 3))

# str_list1 = ['123', 'f', '156t']
# print (str_list1[-1][0: -1])
# a = 3.88
# l = []
# short = s.strip()
# str_list = short.split(',' and '')
# # formatted_string = str_list[0]
# i = 1
# j = 1
# while i < len(str_list):
#     if str_list[i] != '':
#         if j == 1:
#             if str_list[i][0] != '/':
#                 formatted_string += ',/' + str_list[i]
#             else:
#                 formatted_string += ',' + str_list[i]
#             if str_list[i][-1] != '/':
#                 formatted_string += '/'
#             j += 1
#         else:
#             formatted_string += ',' + str_list[i]
#     i += 1
# # print(short)
# import urllib.request
# # resp=urllib.request.urlopen('http://dict.cn/associated')
# resp=urllib.request.urlopen('http://www.oxfordlearnersdictionaries.com/definition/american_english/associated?q=associated')
# html=resp.read()
# print(type(html))
# print(str(html))
# if 'send' in str(html):
#     print('True')
# if '联合的' in str(html):
#     print('Great!')
# else:
#     print('no no no!')

# string = 'good"and"bad'
# i = 0
# while i < len(string):
#     if string[i] == '"':
#         print(string[i+1])
#     i += 1

# b = 1
# a = b
# b += 1

a = '1ef'*0 + '0'
b = a*3

print(b)