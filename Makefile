GH-PAGES = ${HOME}/dev/urubu-gh-pages/

all: build

build:
	python2 _make_index_md.py
	python2 urubu build
	touch _build/.nojekyll
	rm index.md

serve:
	python2 urubu serve

publish:
	git subtree push --prefix _build origin gh-pages
