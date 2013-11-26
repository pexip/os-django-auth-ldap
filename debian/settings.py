DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testproject/test.db3'
    }
}
INSTALLED_APPS = ["django_auth_ldap",
                  "django.contrib.auth",
                  "django.contrib.contenttypes",
                  "django.contrib.admin",
                  "django.contrib.sites",
                  "django.contrib.sessions",
                  ]
SITE_ID = 1
ROOT_URLCONF = "testproject.urls"
SECRET_KEY = "1"
