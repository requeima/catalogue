# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import argparse
from config import config
import os
import requests
from clean_arxiv import is_arxiv
import clean
import catalogue
import update_bibliography
import shutil


def main(args):
    # set up directory structure
    save_path = config['resource_path']
    if args.folder:
        save_path = os.path.join(save_path, args.folder)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    temp_folder = os.path.join(save_path, 'temp_folder_for_file')
    os.makedirs(temp_folder)

    # download and save file
    temp_name = (args.query.split('/'))[-1]
    if temp_name[-4:] != '.pdf':
        temp_name += '.pdf'
    url = os.path.join('https://arxiv.org/pdf/', temp_name)
    r = requests.get(url, allow_redirects=True)
    open(os.path.join(temp_folder, temp_name), 'wb').write(r.content)

    # run cleanup script
    args.files = filter(is_arxiv, catalogue.utils.list_files('.pdf'))
    clean.main(args)
    # update bibtex
    update_bibliography.main(None)

    # rename folder
    print(save_path)
    file = catalogue.bin.find(temp_folder)
    # this is pretty horrible
    file = list(catalogue.utils.file_filter(file, ['.pdf']))[0].split('/')[-1][:-4]
    print(file)
    new_folder_name = os.path.join(save_path, file)
    print(new_folder_name)
    shutil.move(temp_folder, new_folder_name)


if __name__ == '__main__':
    desc = 'Get arXiv file and generate directory.'
    parser = argparse.ArgumentParser(prog='getfile.py', description=desc)
    parser.add_argument('--folder', help='put document in particular subfolder',
                        action='store', default=None)
    parser.add_argument('query', nargs='?', help='query to search for')
    main(parser.parse_args())

