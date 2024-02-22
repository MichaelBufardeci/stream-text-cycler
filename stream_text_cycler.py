"""Reads lines from a file and writes one at a time to another file"""

from time import sleep

def main():
    '''reads lines from a file and writes one at a time to another file'''
    while True:
        with open("messages.txt", 'r', encoding="utf-8") as reader:
            lines = [line.strip() for line in reader.readlines()]
            for line in lines:
                update_message(line)
                sleep(60)

def update_message(message):
    '''overwrites file with input message'''
    with open("output.txt", 'w', encoding="utf-8") as writer:
        writer.seek(0)
        writer.write(message)
        writer.truncate()
        print(message)

if __name__ == "__main__":
    main()
