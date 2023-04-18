from PIL import Image
import os
import sys


class Colors:
    FAIL = '\033[91m'
    HEADER = '\033[95m'
    SUCCESS = '\033[92m'
    INFO = '\033[30m'
    BOLD= '\033[1m'
    NORMAL = '\033[0m'


extensions = Image.registered_extensions()
supported_extensions = {ex for ex, f in extensions.items() if f in Image.OPEN}


def check_if_supported_type(filename):
    for ext in supported_extensions:
        if filename.endswith(ext):
            return True
    return False


def resize_image(path, img_width, img_height):
    with Image.open(path) as img:
        if img.size == (img_width, img_height):
            return
        _resized = img.resize((img_width, img_height))
        _resized.save(path)


def resize_images(dirname, img_width, img_height):
    _files = os.listdir(dirname)

    for _file in _files:
        if check_if_supported_type(_file):
            resize_image(dirname + "/" + _file, img_width, img_height)


def show_help():
    valid_format = """%s(Resize all images in a directory) %s
\t$ python resize.py {width} {height} {directory}
\t$ python resize.py {size} {directory}
%s(Resize a specific file)%s
\t$ python resize.py {width} {height} {filename}
\t$ python resize.py {size} {filename}
%s(Resize a collection of files)%s
\t$ python resize.py {width} {height} {filename1} {filename2}
\t$ python resize.py {size} {filename1} {filename2}""" % (Colors.HEADER, Colors.INFO, Colors.HEADER, Colors.INFO, Colors.HEADER, Colors.INFO)

    print(Colors.BOLD + "Please enter your command in the following format: " + Colors.NORMAL + "\n" + valid_format)


if sys.argv[1] == "help":
    show_help()
else:

    match len(sys.argv):
        case 0:
            print("Invalid arguments, enter `python resize.py help` for further help")
        case 1:
            print("Invalid arguments, enter `python resize.py help` for further help")
        case 2:
            print("Invalid arguments, enter `python resize.py help` for further help")
        case 3:
            size = int(sys.argv[1])
            arg = sys.argv[2]

            direc = False
            file = False
            if os.path.isdir(arg):
                direc = arg
            elif os.path.isfile(arg):
                file = arg
            if direc:
                resize_images(direc, size, size)
            elif file:
                resize_image(file, size, size)
        case 4:

            if isinstance(sys.argv[2], int):
                width = int(sys.argv[1])
                height = int(sys.argv[2])
            else:
                size = int(sys.argv[1])

            files = []

            if size:
                for count in range(2, len(sys.argv)):
                    arg = sys.argv[count]
                    if os.path.isdir(arg):
                        print("Invalid arguments: only enter files, not directories, if providing a list")
                    elif os.path.isfile(arg):
                        files.append(arg)

                for file in files:
                    resize_image(file, size, size)
            else:
                arg = sys.argv[3]
                if os.path.isdir(arg):
                    direc = arg
                elif os.path.isfile(arg):
                    file = arg
                if direc:
                    resize_images(direc, width, height)
                elif file:
                    resize_image(file, width, height)
        case _:
            width = False
            size = False
            if isinstance(sys.argv[2], int):
                width = int(sys.argv[1])
                height = int(sys.argv[2])
            else:
                size = int(sys.argv[1])

            files = []

            if size:
                start = 2
            elif width:
                start = 3

            for count in range(start, len(sys.argv)):
                arg = sys.argv[count]
                if os.path.isdir(arg):
                    print("Invalid arguments: only enter files, not directories, if providing a list")
                elif os.path.isfile(arg):
                    files.append(arg)

            if files:
                for file in files:
                    if width:
                        resize_image(file, width, height)
                    elif size:
                        resize_image(file, size, size)


# python resize.py {width} {height} {directory}
# python resize.py {width/height} {directory}

# python resize.py {width} {height} {filename}
# python resize.py {width/height} {filename}

# python resize.py {width} {height} {filename1} {filename2} ...
# python resize.py {width/height} {filename1} {filename2} ...
