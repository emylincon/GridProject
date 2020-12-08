import os
import random as r


def rename_files(folder):
    os.chdir(folder)
    files = os.listdir()
    for ind in range(len(files)):
        file = r.choice(files)
        files.remove(file)
        filename, ext = os.path.splitext(file)
        name = f'{ind}'.zfill(6)+ext
        os.rename(file, name)
    print('done!')


rename_files(fr'data\ready\train\nec')
