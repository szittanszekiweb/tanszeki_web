GH-PAGES = ${HOME}/dev/urubu-gh-pages/

all: build

build:
	python urubu build
	touch _build/.nojekyll

serve:
	python urubu serve

publish:
	git subtree push --prefix _build origin gh-pages
