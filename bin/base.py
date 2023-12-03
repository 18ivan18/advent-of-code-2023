import json
import os
import subprocess
import sys

advent_of_code_base_url = 'https://adventofcode.com'
solutions_dir = 'solutions'


def today() -> int:
    days = [int(x) for x in os.listdir(solutions_dir)]
    days.append(0)
    return sorted(days)[-1]


env = json.load(open('.env' if os.path.exists('.env') else '.env.sample'))
session_cookie = env['session']
year = env['year']
day = int(sys.argv[1]) if len(sys.argv) > 1 else today()
level = int(sys.argv[2]) if len(sys.argv) > 2 else 1
day_str = f"{day:02}"
path = os.path.dirname(__file__)


def get_answer(day: int, level: int):
    # Assuming your Python script is in the 'solutions' directory and follows a naming convention like 'day_01.py'
    script_path = f'{solutions_dir}/{day:02}'

    # Check if the script file exists
    if not os.path.exists(solutions_dir):
        print(f"Error: Solution script for day {day} not found.")

    # Execute the Python script using subprocess
    command = [f"{path}/bin/run.sh", f"-d{path}/{script_path}"]
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Wait for the process to complete
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        # Successfully executed
        return stdout.splitlines()[level - 1]
    else:
        # An error occurred
        print(f"Error: Execution failed for day {day}, level {level}.")
        print("Error output:", stderr)
        return None


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(get_answer(day, level))
