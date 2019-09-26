import pack
import send
import configparser
import argparse
import pathlib
from collections import namedtuple

def main():
    My_email = namedtuple('My_email' , 'fromaddr password toaddr filepath ')
    config = configparser.ConfigParser()
    parser = argparse.ArgumentParser()
    parser.add_argument('-d',type=bool)
    args = parser.parse_args()
    current_dir = pathlib.Path.cwd()
    config.read(str(current_dir)+'\config.ini')
    print(str(current_dir)+'config.ini')
    my_emal = My_email(fromaddr = config['EMAIL']['username'],
                       password = config['EMAIL']['userpassword'],
                       toaddr= config['EMAIL']['username'],
                       filepath= pack.main(str(current_dir)))
    print(my_emal)
    send.main(my_emal)


if __name__ == '__main__':
    main()

