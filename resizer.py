from PIL import Image, UnidentifiedImageError
import os
import sys


class Colors:
    FAIL = '\033[91m'
    HEADER = '\033[95m'
    SUCCESS = '\033[92m'
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
    try :    
        with Image.open(path) as img:
            if img_width.endswith("%"):
                img_width = int(img_width[:-1])
                img_width = img_width * img.size[0] // 100
            else:
                img_width = int(img_width)
            if img_height.endswith("%"):
                img_height = int(img_height[:-1])
                img_height = img_height * img.size[1] // 100
            else:
                img_height = int(img_height)
            if img.size == (img_width, img_height):
                return
            _resized = img.resize((img_width, img_height))
            _resized.save(path)
        print(Colors.SUCCESS + "Successfully resized " + path + " to size: %dx%d"%(img_width, img_height) + Colors.NORMAL)
    except FileNotFoundError as e:
        print(Colors.FAIL + "File not found: " + path + Colors.NORMAL)
    except UnidentifiedImageError as e:
        print(Colors.FAIL + "Invalid file: " + path + Colors.NORMAL)
    except TypeError as e:
        print(Colors.FAIL + "Invalid arguments, enter `python resizer.py help` for further help" + Colors.NORMAL)

def resize_images(dirname, img_width, img_height):
    _files = os.listdir(dirname)

    for _file in _files:
        if check_if_supported_type(_file):
            resize_image(dirname + "/" + _file, img_width, img_height)

    print(Colors.SUCCESS + "Successfully resized all images in " + dirname + Colors.NORMAL)


def show_help():
    valid_format = """%s(Resize all images in a directory) %s
\t$ python resizer.py {width} {height} {directory}
\t$ python resizer.py {size} {directory}
%s(Resize a specific file)%s
\t$ python resizer.py {width} {height} {filename}
\t$ python resizer.py {size} {filename}
%s(Resize a collection of files)%s
\t$ python resizer.py {width} {height} {filename1} {filename2}
\t$ python resizer.py {size} {filename1} {filename2}""" % (Colors.HEADER, Colors.NORMAL, Colors.HEADER, Colors.NORMAL, Colors.HEADER, Colors.NORMAL)

    print(Colors.BOLD + "Please enter your command in the following format: " + Colors.NORMAL + "\n" + valid_format)
    print(Colors.HEADER + "\n\nThe supported image types are: " + Colors.NORMAL + "\n\t" + ", ".join(supported_extensions))
    print(Colors.HEADER + "\n\nPlease note that the {size, width, height} arguments can be either a percentage (ending with '%') or a number representing the number of pixels for the axis.\n" + Colors.NORMAL)
    print(Colors.NORMAL + "Example: " + Colors.NORMAL + "\n\t$ python resizer.py 50% 50% /home/user/Pictures   # will resize all images in the directory to 50% of their original size")
    print(Colors.NORMAL + "Example: " + Colors.NORMAL + "\n\t$ python resizer.py 256 128 /home/user/Pictures   # will resize all images in the directory to 256x128 pixels\n")
if sys.argv[1] == "help":
    show_help()
else:
    match len(sys.argv):
        case 0:
            print(Colors.FAIL + "Invalid arguments, enter `python resizer.py help` for further help" + Colors.NORMAL)
        case 1:
            print(Colors.FAIL + "Invalid arguments, enter `python resizer.py help` for further help" + Colors.NORMAL)
        case 2:
            print(Colors.FAIL + "Invalid arguments, enter `python resizer.py help` for further help" + Colors.NORMAL)
        case 3:
            size = sys.argv[1]
            arg = sys.argv[2]

            if size.endswith("%"):
                if not size[:-1].isdigit():
                    print(Colors.FAIL + "Invalid arguments, enter `python resizer.py help` for further help" + Colors.NORMAL)
                    exit(-1)
            elif not size.isdigit():
                print(Colors.FAIL + "Invalid arguments, enter `python resizer.py help` for further help" + Colors.NORMAL)
                exit(-1)

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
            size = False
            if sys.argv[2][:-1].isdigit():
                width = sys.argv[1]
                height = sys.argv[2]
            else:
                size = sys.argv[1]

            files = []

            if size:
                for count in range(2, len(sys.argv)):
                    arg = sys.argv[count]
                    if os.path.isdir(arg):
                        print(Colors.FAIL + "Invalid arguments: only enter files, not directories, if providing a list" + Colors.NORMAL)
                    elif os.path.isfile(arg):
                        files.append(arg)

                for file in files:
                    resize_image(file, size, size)
            else:
                direc = False
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
            if sys.argv[2][:-1].isdigit():
                width = sys.argv[1]
                height = sys.argv[2]
            else:
                size = sys.argv[1]

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

            else:
                print(Colors.FAIL + "Invalid arguments, enter `python resizer.py help` for further help" + Colors.NORMAL)

