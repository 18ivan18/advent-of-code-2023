#!/usr/bin/env python3

import requests
from base import session_cookie, advent_of_code_base_url, year, day

# Submit the solution
url = f'{advent_of_code_base_url}/{year}/day/{day}/answer'
data = {'level': 1, 'answer': 2285}

headers = {'cookie': f'session={session_cookie}'}

response = requests.post(url, data=data, headers=headers)

# Print the response from the server
print(response.text)
