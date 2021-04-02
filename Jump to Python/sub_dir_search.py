
# def search(dirname):
#     print(dirname)

# search("D:/Study/Python_study/Jump to Python/")


import sys

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print(full_filename)

search("D:/Study/Python_study/Jump to Python/")
