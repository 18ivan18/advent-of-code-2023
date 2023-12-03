#!/usr/bin/env python3

import requests
from base import bcolors, get_answer, session_cookie, advent_of_code_base_url, year, day, level

# Submit the solution
url = f'{advent_of_code_base_url}/{year}/day/{day}/answer'
data = {'level': level, 'answer': get_answer(day, level)}

headers = {'cookie': f'session={session_cookie}'}

print(f"Submitting{day=} {level=}")
response = requests.post(url, data=data, headers=headers, allow_redirects=True)

if response.text.find("Did you already complete it") != -1:
    print(f"{bcolors.BOLD}{day=} {level=} is already completed.{bcolors.ENDC}")

if response.text.find("not the right answer") != -1:
    print(f"{bcolors.FAIL}{day=} {level=} Wrong Answer.{bcolors.ENDC}")

if response.text.find("too recently") != -1:
    print(f"{bcolors.FAIL}Submitted too recently.{bcolors.ENDC}")
