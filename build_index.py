#!/usr/bin/env python

import glob
import os


filepaths = list()

for filepath in glob.glob('**/*', recursive=True):
    if os.path.isfile(filepath) and filepath != 'index.html':
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
