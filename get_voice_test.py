__author__ = 'junlingwang'
import urllib.request
import urllib.error


def get_url_list(web_content):
    url_list = []
    i = 0
    while i < len(web_content):
        if web_content[i] == 'h' and web_content[i+1] == 't' and web_content[i+3] == 'p':
            begin_index = i
            j = begin_index
            url = ''
            while web_content[j] != '"' and web_content[j] != '\\':
                url += web_content[j]
                j += 1
            i = j
            url_list.append(url)
        i += 1
    return url_list

def try_url(url_string):
    # resp=urllib.request.urlopen('http://dict.cn/associated')
    html = None
    try:
        resp = urllib.request.urlopen(url_string)
        html = resp.read()
    except ValueError:
        print('not open')
    except urllib.error.URLError:
        print('not open')

    # print(type(html))
    # print(str(html))
    if 'raɪ' in str(html):
        print('Great!')
        print(url_string)
    else:
        print('no no no!')
    return str(html)


original_string = 'http://www.oxfordlearnersdictionaries.com/spellcheck/english/?q=%CB%88ra%C9%AAtli'
try_url(original_string)
# url_list = get_url_list(content)
# for url in url_list:
#     try_url(url)

