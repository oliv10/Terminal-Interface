import os

program = []

directoy = os.listdir(os.curdir + "\Programs")

print(directoy)

for file in directoy:
    if file[0] != '_':
        program.append(file[:-3])
