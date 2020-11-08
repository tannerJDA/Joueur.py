all:
	make core
core:
	python3 -m compileall -x '.creer' ./

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

