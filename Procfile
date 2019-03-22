% prepara el repositorio para su despliegue. 
CI1-Configuration: sh -c 'cd grooving-project/Server && python manage.py makemigrations && python manage.py migrate && echo "from django.contrib.auth import get_user_model; User = get_user_model();\nif not User.objects.filter(email='"'"'admin@grooving.com'"'"').exists(): User.objects.create_superuser('"'"'admin@grooving.com'"'"', '"'"grooving'"'"')" | python3 ./manage.py shell'

% especifica el comando para lanzar Decide
web: sh -c 'cd grooving-project/Server && gunicorn decide.wsgi --log-file -'
