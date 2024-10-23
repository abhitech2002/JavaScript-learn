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