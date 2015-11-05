__author__ = 'xiaocong'

# -*- coding:utf-8 -*-

import os
import zipfile
import traceback
import argparse
import shutil

def Compress_zip(raw_dir):

    target_zipfile=raw_dir+'.zip'
    cmd='zip -r -j "'+target_zipfile+'" '+'"'+raw_dir+'"'
    os.system(cmd)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-d','--delsource',action='store_true',help='delete the source directory')
    args=parser.parse_args()

    path=os.path.abspath(os.path.dirname(__file__))+'/../i7wumedia/book_files'
    compress_paths=[]
    for i in os.listdir(path):
        compress_paths.extend([os.path.join(path,i,j) for j in os.listdir(os.path.join(path,i))])

    for i in compress_paths:
        Compress_zip(i)

    if args.delsource:
        for i in compress_paths:
            shutil.rmtree(i,True)

