all:
	echo 'Nothing to be done.'

collect:
	python manage.py collectstatic --noinput
	python manage.py render_base

prod_update:
	bash prod_update.sh
