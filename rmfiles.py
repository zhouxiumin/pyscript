#! usr/bin/python
# coding=utf-8
import os.path


def remove_file_with_prefix(prefix, targetdir):
    for f in os.listdir(targetdir):
        target_file = os.path.join(targetdir, f)
        if os.path.isfile(target_file) and target_file.find(prefix) > 0:
            print target_file
            os.remove(target_file)
        if os.path.isdir(target_file):
            remove_file_with_prefix(prefix,target_file)


if __name__ == '__main__':
    print 'rm file with prefix'
    remove_file_with_prefix("._", "./")