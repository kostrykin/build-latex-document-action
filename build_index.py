#!/usr/bin/env python

import glob
import os


filepaths = list()

for filepath in glob.glob('**/*', recursive=True):

    # Only accept files from sub-directories (only static files are top-level)
    if os.path.isfile(filepath) and '/' in filepath:
        filepaths.append(filepath)

html = """
<html>
<body>
<ul>
""" + '\n'.join(f'<li><a href="{filepath}">{filepath}</a></li>' for filepath in sorted(filepaths)) + """
</ul>
</body>
"""

with open('index.html', 'w') as fout:
    fout.write(html)
