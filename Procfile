% prepara el repositorio para su despliegue. 
release: sh -c 'cd grooving-server/Server && python manage.py makemigrations && python manage.py migrate && echo "from django.contrib.auth import get_user_model; User = get_user_model();\nif not User.objects.filter(email='"'"'admin@grooving.com'"'"').exists(): User.objects.create_superuser('"'"'admin@grooving.com'"'"', '"'"grooving'"'"')" | python3 ./manage.py shell'

% especifica el comando para lanzar Decide
web: sh -c 'cd grooving-server/Server && gunicorn Server.wsgi --log-file -'
