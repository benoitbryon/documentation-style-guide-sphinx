ROOT_DIR=$(PWD)

install:
	cd ${ROOT_DIR}
	mkdir -p lib/buildout
	wget http://svn.zope.org/*checkout*/zc.buildout/tags/1.5.2/bootstrap/bootstrap.py?content-type=text%2Fplain -O lib/buildout/bootstrap.py
	python lib/buildout/bootstrap.py --distribute
	bin/buildout -N

uninstall:
	rm -r ${ROOT_DIR}/bin ${ROOT_DIR}/lib

tests:
	${ROOT_DIR}/bin/lettuce

documentation-build:
	cd ${ROOT_DIR}/docs; make clean html

README-build:
	cd ${ROOT_DIR}
	mkdir -p docs/_build/README
	bin/rst2 html README.rst > docs/_build/README/README.html
