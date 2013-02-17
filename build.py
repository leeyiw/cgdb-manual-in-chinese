#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, markdown, codecs, re

index = 'summary.md'
index_target = 'cgdb-manual-in-chinese.html'
mode = 'full'
exclude = ['README.md']
is_meta_gen = False

def build(f):
    global is_meta_gen

    root, ext = os.path.splitext(f)
    if mode == 'full':
        target = index_target
    else:
        target = root + '.html'

    if os.path.exists(target):
        if mode == 'apart' or (mode == 'full' and is_meta_gen == False):
            os.remove(target)

    md = codecs.open(f, 'r', 'utf-8')
    content = md.read()
    html_content = markdown.markdown(content)
    html = codecs.open(target, 'a', 'utf-8', 'xmlcharrefreplace')
    html_content = re.sub('md', 'html', html_content)
    if mode == 'apart' or (mode == 'full' and is_meta_gen == False):
        html.write('<meta charset="utf-8">\n')
        is_meta_gen = True
    html.write(html_content)

def main():
    global mode

    argc = len(sys.argv)
    if argc > 2:
        sys.exit(2)
    elif argc == 2:
        if sys.argv[1] != 'full' and sys.argv[1] != 'apart':
            sys.exit(2)
        else:
            mode = sys.argv[1]

    build(index)
    filelist = os.listdir('.')
    filelist.sort()
    for i, f in enumerate(filelist):
        if f in exclude or f == index:
            continue
        root, ext = os.path.splitext(f)
        if ext == '.md':
            build(f)

if __name__ == '__main__':
    main()
