from pathlib import Path


#path = Path('pi_digits.txt')
path = Path(__file__).with_name("pi_digits.txt")

contents = path.read_text()
#print(contents.rstrip())
lines = contents.splitlines()
pi_lines = ''
for line in lines:
   # print(line.rstrip())
   pi_lines += line.rstrip()

print(pi_lines)
print(len(pi_lines))