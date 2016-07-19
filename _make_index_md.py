from __future__ import print_function, absolute_import
import os
import sys

# take yaml from urubu
sys.path.insert(0, os.path.abspath('urubu'))
import yaml

# read news directory
import glob
filenames = (
    filename for filename in glob.glob('news/*.md')
    if not filename.endswith('index.md'))


# read in header, text-body of the last 4 news
# https://stackoverflow.com/questions/25814568/is-it-possible-to-use-pyyaml-to-read-a-text-file-written-with-a-yaml-front-matt/25816324#25816324
def get_yaml(f):
    pointer = f.tell()
    if f.readline() != '---\n':
        f.seek(pointer)
        return None
    readline = iter(f.readline, '')
    readline = iter(readline.next, '---\n')
    return yaml.safe_load(''.join(readline))


def read_md(filename):
    # XXX: could use urubu as library and use its functions
    with open(filename) as f:
        header = get_yaml(f)
        body = f.read()
        # header, body = yaml.safe_load_all(f)
        return header, body


news = []
for filename in sorted(filenames, reverse=True)[:4]:
    header, body = read_md(filename)
    news.append({'header': header, 'body': body})


# write index.md based on _index.md
header, body = read_md('_index.md')
header['news'] = news
with open('index.md', 'w') as f:
    f.write('---\n')
    f.write(yaml.safe_dump(header))
    f.write('\n')
    f.write('---\n')
    f.write(body)
