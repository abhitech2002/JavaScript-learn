## To create new app
- `py manage.py startapp myworld`

## Making recognize new app

- Open Setting.py file and search installed apps
- Add the app name in array of installed apps

## Create new apps url

- Create urls.py file in app folders
- Include the Path in the urls.py
- `path('', views.learn, name='learn'),`
- Then in the project's urls.py include the app's urls file
- `path('world/', include('world.urls')),`
- Now for the app's url it become `http://localhost:8000/world/`

## To install tailwind cssin django
- Install the tailwind css through pip `pip install django-tailwind` & `pip install django-tailwind[reload]`
- `py manage.py tailwind init` For tailwind initializaition
- `py manage.py tailwind install` For tailwind installation [Note: First set the path of node js in setting.py]
- `NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"`
- After above setting, visit the `theme` templates in `theme` folder and open base.html file
- In this copy the Jinja layout and paste in the `layout.html` file
- Now add the tailwind class in the `index.html` file
- After this start the open 2 terminal in which you will start the django and tailwind
- Open second termianl and `py manage.py tailwind start` run this command
- After running the command restart the django and visit the output on browser
- For production change the command to the `py manage.py tailwind build`
- To make `django-tailwind-reload` work properly we have to include some commands in the `settings.py`
- In installed apps add `'django_browser_reload'` and in middleware add `django_browser_reload.middleware.BrowserReloadMiddleware`

## Creating super user
- `py manage.py createsuperuser` to create super user in Django
- `py manage.py changepassword userName` to change the passeword

## Models
- `class className(models.model):` to define the model 
- `MEDIA_URL = '/media/',  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`
- Import `from django.conf import settings, from django.conf.urls.static import static` in projects urls.py file to recognize as a Media 
- `+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` add after urls pattern array
- `py manage.py makemigrations appName` To create Migration
- `py manage.py migrate` to migrate it