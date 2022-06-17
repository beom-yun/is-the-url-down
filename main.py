import os
import requests


def check_url(url):
    if is_it_valid_url(url):
        try:
            if not ('http://' in url or 'https://' in url):
                url = 'http://' + url
            if requests.get(url).status_code != 200:
                raise Exception()
            print(f'{url} is up!')
        except:
            print(f'{url} is down!')
    else:
        print(f'{url} is not a valid URL.')


def is_it_valid_url(url):
    return True if '.' in url.replace('www.', '') else False


def should_i_retry():
    while True:
        try:
            print('Do you want to start over? y/n', end=' ')
            return {'y': True, 'n': False}[input().strip().lower()]
        except:
            print("That's not a valid answer.")


while True:
    os.system('clear')
    print('Welcome to IsItDown.py!')
    print('Please write a URL or URLs you want to check. (saperated by comma)')

    for input_url in [x.strip().lower() for x in input().split(',')]:
        check_url(input_url)

    if not should_i_retry():
        print('Bye!')
        break
