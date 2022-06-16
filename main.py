import os
import requests


def check_url(url):
    pass


def is_it_right_url(url):
    pass


def should_i_retry():
    while True:
        try:
            print('Do you want to start over? y/n', end=' ')
            return {'y': True, 'n': False}[input().strip().lower()]
        except:
            print("That's not a valid answer.")


while True:
    print('Welcome to IsItDown.py!')
    print('Please write a URL or URLs you want to check. (saperated by comma)')

    for input_url in [x.strip().lower() for x in input().split(',')]:
        check_url(input_url)

    if not should_i_retry():
        break
