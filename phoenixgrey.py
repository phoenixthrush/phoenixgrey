# MIT License

# Copyright (c) 2022 Phoenixthrush UwU

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def main():
    system('cls')
    print('\033[96mWelcome to \'Phoenixgrey\' v.1.0\033[00m\n')
    print('\033[31mThis tool is made by phoenixthrush!\033[00m')
    print('\033[31mThe language is made by grey!\033[00m\n')

    response = input('\033[95mDo you wanna write or read a text?\033[00m \033[31m[\033[00m\033[34mw\033[00m\033[96m|\033[00m\033[92mr\033[00m\033[31m]\033[00m ').lower()
    if response == 'w':
        write()
    elif response == 'r':
        read()
    else:
        system('cls')
        main()

def write():
    system('cls')
    message = input('\033[31mPlease "Enter" your message: \033[00m')
    encoded = ''
    for char in message:
        if char == 'a' or char == 'A':
            encoded += 'ä'
        elif char == 'b' or char == 'B':
            encoded += 'v'
        elif char == 'c' or char == 'C':
            encoded += 'x'
        elif char == 'd' or char == 'D':
            encoded += 's'
        elif char == 'e' or char == 'E':
            encoded += 'w'
        elif char == 'f' or char == 'F':
            encoded += 'd'
        elif char == 'g' or char == 'G':
            encoded += 'f'
        elif char == 'h' or char == 'H':
            encoded += 'g'
        elif char == 'i' or char == 'I':
            encoded += 'u'
        elif char == 'j' or char == 'J':
            encoded += 'h'
        elif char == 'k' or char == 'K':
            encoded += 'j'
        elif char == 'l' or char == 'L':
            encoded += 'k'
        elif char == 'm' or char == 'M':
            encoded += 'y'
        elif char == 'n' or char == 'N':
            encoded += 'b'
        elif char == 'o' or char == 'O':
            encoded += 'i'
        elif char == 'p' or char == 'P':
            encoded += 'o'
        elif char == 'q' or char == 'Q':
            encoded += 'ü'
        elif char == 'r' or char == 'R':
            encoded += 'e'
        elif char == 's' or char == 'S':
            encoded += 'a'
        elif char == 't' or char == 'T':
            encoded += 'r'
        elif char == 'u' or char == 'U':
            encoded += 'z'
        elif char == 'v' or char == 'V':
            encoded += 'c'
        elif char == 'w' or char == 'W':
            encoded += 'q'
        elif char == 'x' or char == 'X':
            encoded += 'y'
        elif char == 'y' or char == 'Y':
            encoded += 'm'
        elif char == 'z' or char == 'Z':
            encoded += 't'
        elif char == 'ü' or char == 'Ü':
            encoded += 'p'
        elif char == 'ö' or char == 'Ö':
            encoded += 'l'
        elif char == 'ä' or char == 'Ä':
            encoded += 'ö'
        else:
            encoded += char

    print()
    addToClipBoard(encoded)
    print('\033[34mWritten message...\033[00m\n')
    print(f'\033[36m{encoded}\033[00m\n')
    input('\033[31mPress "Enter" to exit!\033[00m\n')

def read():
    system('cls')
    message = input('\033[31mPlease "Enter" your message: \033[00m')
    encoded = ''
    for char in message:
        if char == 'a' or char == 'A':
            encoded += 's'
        elif char == 'b' or char == 'B':
            encoded += 'n'
        elif char == 'c' or char == 'C':
            encoded += 'v'
        elif char == 'd' or char == 'D':
            encoded += 'f'
        elif char == 'e' or char == 'E':
            encoded += 'r'
        elif char == 'f' or char == 'F':
            encoded += 'g'
        elif char == 'g' or char == 'G':
            encoded += 'h'
        elif char == 'h' or char == 'H':
            encoded += 'j'
        elif char == 'i' or char == 'I':
            encoded += 'o'
        elif char == 'j' or char == 'J':
            encoded += 'k'
        elif char == 'k' or char == 'K':
            encoded += 'l'
        elif char == 'l' or char == 'L':
            encoded += 'ö'
        elif char == 'm' or char == 'M':
            encoded += 'y'
        elif char == 'n' or char == 'N':
            encoded += 'm'
        elif char == 'o' or char == 'O':
            encoded += 'p'
        elif char == 'p' or char == 'P':
            encoded += 'ü'
        elif char == 'q' or char == 'Q':
            encoded += 'w'
        elif char == 'r' or char == 'R':
            encoded += 't'
        elif char == 's' or char == 'S':
            encoded += 'd'
        elif char == 't' or char == 'T':
            encoded += 'z'
        elif char == 'u' or char == 'U':
            encoded += 'i'
        elif char == 'v' or char == 'V':
            encoded += 'b'
        elif char == 'w' or char == 'W':
            encoded += 'e'
        elif char == 'x' or char == 'X':
            encoded += 'c'
        elif char == 'y' or char == 'Y':
            encoded += 'm'
        elif char == 'z' or char == 'Z':
            encoded += 'u'
        elif char == 'ü' or char == 'Ü':
            encoded += 'q'
        elif char == 'ö' or char == 'Ö':
            encoded += 'ä'
        elif char == 'ä' or char == 'Ä':
            encoded += 'a'
        else:
            encoded += char

    print()
    addToClipBoard(encoded)
    print('\033[92mReaded message...\033[00m\n')
    print(f'\033[36m{encoded}\033[00m\n')
    input('\033[31mPress "Enter" to exit!\033[00m\n')

def addToClipBoard(text):
    system(f'echo {text.strip()}| clip')

if __name__ == '__main__':
    from os import system

    main()