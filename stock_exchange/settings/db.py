DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'stockexchange',
        'USER': 'stockexchangeuser',
        'PASSWORD': 'lolcat',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'TEST': {
            'CHARSET': 'UTF8',
            'NAME': 'travel-test'
        }
    }
}