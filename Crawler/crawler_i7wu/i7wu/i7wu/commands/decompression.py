__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import os
import zipfile
import traceback
import argparse

def find_path_file(specific_file_type,search_directory):

    result_path_filename = list()
    result_path_filename.extend([os.path.join(dirpath,filename) for dirpath,dirnames,filenames
                                 in os.walk(search_directory) for filename in filenames
                                 if os.path.splitext(filename)[1] == ('.' + specific_file_type)])
    return result_path_filename

def Decompression_rar(specific_file):

    cmd='unrar x "'+specific_file+'"'+' "'+os.path.split(specific_file)[0]+'"'
    os.system(cmd)


def Decompression_zip(specific_file):

    if zipfile.is_zipfile(specific_file):
        try:
            zipfile.ZipFile(specific_file).extractall(os.path.split(specific_file)[0])
        except Exception as err:
            traceback.print_exc()

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-d','--delsource',action='store_true',help='delete the source file(rar or zip)')
    args=parser.parse_args()

    path=os.path.abspath(os.path.dirname(__file__))+'/../i7wumedia/book_files'

    _rar=find_path_file('rar',path)
    for i in _rar:
        Decompression_rar(i)

    _zip=find_path_file('zip',path)
    for i in _zip:
        Decompression_rar(i)

    if args.delsource:
        _delete_rar=find_path_file('rar',path)
        _delete_zip=find_path_file('zip',path)
        for i in _delete_rar:
            os.remove(i)
        for i in _delete_zip:
            os.remove(i)