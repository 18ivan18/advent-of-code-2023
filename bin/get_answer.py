#!/usr/bin/env python3

from base import solutions_dir, path, day, level

import subprocess
import os


def get_answer(day: int, level: int, input: str = 'input.txt'):
    # Assuming your Python script is in the 'solutions' directory and follows a naming convention like 'day_01.py'
    script_path = f'{solutions_dir}/{day:02}'

    # Check if the script file exists
    if not os.path.exists(solutions_dir):
        print(f"Error: Solution script for day {day} not found.")

    # Execute the Python script using subprocess
    command = [f"{path}/run.sh", f"-d{path}/{script_path}", f"-i{input}"]
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


if __name__ == '__main__':
    print(get_answer(day, level))
