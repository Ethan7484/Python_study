
# def search(dirname):
#     print(dirname)

# search("D:/Study/Python_study/Jump to Python/")


# import os

# def search(dirname):
#     filenames = os.listdir(dirname)
#     for filename in filenames:
#         full_filename = os.path.join(dirname, filename)
#         print(full_filename)

# search("D:/Study/Python_study/Jump to Python/")


# import os

# def search(dirname):
#     filenames = os.listdir(dirname)
#     for filename in filenames:
#         full_filename = os.path.join(dirname, filename)
#         ext = os.path.splitext(full_filename)[-1]
#         if ext == '.py':
#             print(full_filename)

# search("D:/Study/Python_study/Jump to Python")

# import os

# def search(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]
#                 if ext == '.py':
#                     print(full_filename)
#     except PermissionError:
#         pass

# search("D:/Study/Python_study/Jump to Python")

import os



for (path, dir, files) in os.walk("D:/Study/Python_study/Jump to Python"):
    for filenmame in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))

