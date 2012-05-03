test:
	DJANGO_SETTINGS_MODULE=sesame.tests.settings \
	django-admin.py test sesame

coverage:
	coverage erase
	DJANGO_SETTINGS_MODULE=sesame.tests.settings \
	coverage run --branch --source=sesame `which django-admin.py` test sesame
	coverage html

clean:
	find . -name '*.pyc' -delete
	rm -rf .coverage dist htmlcov MANIFEST
