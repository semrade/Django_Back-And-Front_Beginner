# Step 1: Set Up Django Project
1/Install Django:
```bash
pip install django
```
2/Create Django Project:
```
django-admin startproject your_project_name
```
3/Navigate to Project Directory:
```    
cd your_project_name
```
4/Create Django Apps:
```
python manage.py startapp resume
python manage.py startapp task
```
# Step 2: Configure Django Apps
-   Add the created apps to the `INSTALLED_APPS` list.
```python
INSTALLED_APPS = [
# other apps...
'resume',
'task',
]
```
# Step 3: Create Models and Migrate
1/Define Models:
-   In the `models.py` file of each app (`resume` and `task`), define your models.
2/Migrate Database
```
python manage.py makemigrations
python manage.py migrate
```
# Step 4: Create Django Views and Templates
1/Create Views:
-   Define views for each app in their respective `views.py` files.

2/Create Templates:
-   Create HTML templates in each app's `templates` directory.
# Step 5: Set Up React App
1/Install Node.js and npm:
-   Install Node.js and npm from  [Click Here](https://nodejs.org/en "Click Here").
  
2/Create React App:
```
npx create-react-app react_app
```
3/Navigate to React App Directory:
```
cd react_app
```
# Step 6: Connect React App with Django
1/Install Django-CORS-Headers:
-   Install the CORS headers package for Django.
```
pip install django-cors-headers
```
2/Configure Django Settings:
-   Add `corsheaders` to INSTALLED_APPS and `corsheaders.middleware.CorsMiddleware` to `MIDDLEWARE` in `settings.py`.
-   Set `corsheaders.middleware.CorsMiddleware` at the top of the `MIDDLEWARE` list.
  
3/Configure CORS Settings:
-   Add the following to `settings.py`:
```
CORS_ALLOWED_ORIGINS = [
"http://localhost:3000",  # or your React app's URL
]
```
# Step 7: Connect React Components
1/Update React App:
-   Update React components in the `src` directory to fetch data from Django backend.

2/Run React App:
```
npm start
```
# Step 8: Run Django Server
```
python manage.py runserver
```

Now, your Django project with two apps (`resume` and `task`) and a connected React app should be set up. Adjust the details according to your specific requirements and project structure.

# Step 9 Testing:
Now, when you run your Django development server (python manage.py runserver), you can access the following URLs:

-  Resume Education List: http://localhost:8000/resume/education-list/
-  Resume Experience List: http://localhost:8000/resume/experience-list/
-  Task List: http://localhost:8000/task/task-list/

Make sure to replace http://localhost:8000/ with your actual server address. If you are running the server locally, it will typically be http://localhost:8000/. Adjust the URLs and paths according to your project structure and preferences.

# step 10 Serialisation:

For now, the Django project uses HTML files to display the views, this is a normal behavior to display the views in the back in debug mode and check the server like I did in step 9.
To be able to work with React we have to serialize data from the Django project to the React app, React is a JavaScript language and it understands JSON files.

1/Create a JSON Serializer (serializers.py):
-  Create a serializer in `serializers.py` to handle the serialization of the `Experience` model to JSON

```python
# serializers.py in your Django app

from rest_framework import serializers
from .models import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'job_title', 'company', 'start_date', 'end_date', 'description', ...]
        # Include other fields as needed

```
reset_framwork needs to be installed.
Open a terminal or command prompt, navigate to your project's directory, and run the following command:
```
pip install djangorestframework

```

2/Create a JSON View (views.py):
-  Create a separate view that uses the serializer to return a JSON response.
```python
# views.py in your Django app

from django.http import JsonResponse
from .models import Experience
from .serializers import ExperienceSerializer

def experience_list_json(request):
    experiences = Experience.objects.all()
    serializer = ExperienceSerializer(experiences, many=True)
    return JsonResponse(serializer.data, safe=False)

```

3/Update URLs (urls.py):
-  Add a new URL pattern in urls.py to map to the JSON view.
```python
# urls.py in your Django app

from django.urls import path
from .views import experience_list, experience_list_json

urlpatterns = [
    # ... other URL patterns
    path('experience-list/', experience_list, name='experience-list'),
    path('experience-list-json/', experience_list_json, name='experience-list-json'),
]

```

Now, you can access the HTML-rendered view at 
`http://localhost:8000/resume/experience-list/` and the JSON view at 
`http://localhost:8000/resume/experience-list-json/`. 
The existing view remains unchanged, and you have a separate endpoint to retrieve the data in JSON format.

Please replace the ellipses (`...`) with the actual field names from your Experience model in the serializer.
Step 10 must be duplicated on the `task` and `Education` models.














  
