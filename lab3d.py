#!/usr/bin/env python3

# Author ID: 148596190

import subprocess
import os

# def free_space():
#     p = subprocess.Popen(['df', '-h', '|', "grep'/$'", '|', 'awk', "'{print $4}'"], 
#                          stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output = p.communicate()
#     stdout = output[0].decode('utf-8').strip()
#     return stdout

def free_space():
    df_return = os.popen("df -h | grep '/$' | awk '{print $4}'")
    df_contents = df_return.read()
    return df_contents.strip()


if __name__ == "__main__":
    space = free_space()
    print(space)