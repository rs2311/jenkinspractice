import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("-il","--input_line", help="-- input line")
args = parser.parse_args()

with open('file_update.txt', 'a') as file:
    file.write('\n')
    file.write(args.input_line)
