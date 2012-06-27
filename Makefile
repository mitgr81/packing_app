PIP_EXEC?=pip

python_deps:
	@sudo ${PIP_EXEC} install -U nose python-rest-client pika pyyaml pybrightcove

clean:
	@printf "Cleaning up files that are already in .gitignore... "
	@for pattern in `cat .gitignore`; do find . -name "$$pattern" -delete; done
	@echo "OK!"

py_unit: clean
	@echo "Running python unit tests without printing (use py_stds if you want it)..."
	@cd python && nosetests --verbosity=2

py_stds: clean
	@echo "Running python unit tests with printing (use py_unit if you don't want it)..."
	@cd python && nosetests -s --verbosity=2

unit: py_unit
