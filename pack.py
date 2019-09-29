import os
import tarfile
import datetime

def tardir(path, file_name):
    with tarfile.open(file_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))



def main(tarf_path):
    file_name = tarf_path+'\\'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'.tar'
    tardir(tarf_path, file_name)
    print(type(file_name))
    return file_name

if __name__ == '__main':
    main(tarf_path)