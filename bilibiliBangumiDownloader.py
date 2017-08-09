import os
import sys
import time

from automation.bilibiliBangumiAutomation import Parse


class bilibiliAnime:
    def __init__(self, serial, name, directory):
        self.serial = serial
        self.name = name
        self.directory = directory

    def create_directory(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        os.chdir(self.directory)

        if not os.path.exists(self.name):
            os.makedirs(self.name)
        os.chdir(self.name)
        print(os.getcwd())

    def download(self):
        data = Parse(self.serial)
        index = data.count()
        for src in data.key_url():
            # sys.argv = ['you-get', '--no-caption', src]
            # sys.argv = ['you-get', '--info', src]
            if not os.path.exists(str(index)):
                os.makedirs(str(index))
            os.chdir(str(index))
            try:
                # you_get.main()
                os.system("you-get --no-caption " + src)
            except:
                print("Exception, pending for 100 seconds")
                time.sleep(100)
                # you_get.main()
                os.system("you-get --no-caption " + src)
            os.chdir('..')
            index -= 1

    def start(self):
        self.create_directory()
        self.download()


if __name__ == '__main__':
    serial = sys.argv[1]
    name = sys.argv[2]

    directory = os.path.expanduser('~') + '\\Videos'
    bilibiliAnime(serial, name, directory).start()
