import os

program = []
__all__ = ['program']
directoy = os.listdir(os.curdir + "\Programs")

for file in directoy:
    if file[0] != '_':
        program.append(file[:-3])
