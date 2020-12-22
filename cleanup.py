import os


def scandirs(path):
    for root, dirs, files in os.walk(path):
        for currentFile in files:
            print("processing file: " + currentFile)
            exts = ('.srt', '.vtt')
            if currentFile.lower().endswith(exts):
                os.remove(os.path.join(root, currentFile))


scandirs("/Volumes/Local Disk/Python")
