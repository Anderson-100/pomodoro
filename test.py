lines = []
with open('custom_settings/test.txt') as file:
  for line in file:
    lines.append(line[:len(line)-1])
    print(line)

print(lines)