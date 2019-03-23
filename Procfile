release: sh -c 'cd grooving-server/Server && python3 manage.py makemigrations && python3 manage.py migrate'

web: sh -c 'gunicorn --chdir ./grooving-server/Server/ Server.wsgi --log-file -' 
