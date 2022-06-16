import os
import requests


def should_i_retry():
    while True:
        try:
            print('Do you want to start over? y/n', end=' ')
            input_data = input().strip().lower()
            return {'y': True, 'n': False}[input_data]

            # if input_data == 'y':
            #     return True
            # elif input_data == 'n':
            #     return False
            # else:
            #     raise Exception()
        except:
            print("That's not a valid answer.")


should_i_retry()

# while True:
#     print('Welcome to IsItDown.py!')
#     print('Please write a URL or URLs you want to check. (saperated by comma)')
#     input_data = input()
#     print('input_data', input_data)
