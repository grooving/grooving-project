ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'grooving',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
