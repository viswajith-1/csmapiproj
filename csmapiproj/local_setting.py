
# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'csmdb',
        'USER': 'root',
        'PASSWORD': 'sirilsiril',
        'HOST': 'localhost',    
        'PORT': '3306',
    }
}
