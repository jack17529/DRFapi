# DRFapi

- This api is created using Python 3.8.10.
- You can get more information about the packages used please see the `requirements.txt`.
- Used core-api for generating docs.

# Directory Structure

```
.
├── base
│   ├── admin.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   ├── serializers.cpython-38.pyc
│   │   │   ├── urls.cpython-38.pyc
│   │   │   └── views.cpython-38.pyc
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-38.pyc
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── templates
│   │   └── base
│   │       ├── home.html
│   │       └── profile.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── DRFapi
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── LICENSE
├── manage.py
├── media
│   └── resumes
│       ├── 1
│       │   ├── contrast-resume2021-12-28_191619.031114.pdf
│       │   ├── images.2021-12-28_164934.459953.pdf
│       │   ├── images.2021-12-29_142837.269263.pdf
│       │   ├── modern_resume_template_word_free2021-12-28_185525.798568.pdf
│       │   ├── modern_resume_template_word_free2021-12-29_143433.073629.pdf
│       │   └── Professional-Resume-Template-Free-1000x7502021-12-28_164838.588032.pdf
│       ├── 2
│       │   ├── images.2021-12-28_192951.566237.pdf
│       │   ├── modern_resume_template_word_free2021-12-28_165504.263814.pdf
│       │   └── modern_resume_template_word_free2021-12-28_191106.354636.pdf
│       ├── 4
│       │   └── images.2021-12-28_193013.231428.pdf
│       └── 6
│           └── 3021542021-12-30_141545.056986.pdf
├── README.md
└── templates
    ├── main.html
    └── navbar.html
```

- `./base/api/` is the place where the code for the rest api is stored.
- `./base` is the app which I have created in the django. All the backend functionalities that I have implemented are present in this directory too.
- `./DRFapi` is the directory with all the server configrations.
- `.env` file can be used to run the server. For security reasons I have created it. A sample `.env` file would be.

.env
```
SECRET_KEY=django-insecure-xzhx-(m+e_0oj!y-b6418(3+4k9j$gtq8btb%&x2q=k^3_%sv*
DEBUG=True
DB_NAME=qratedb
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
```

# Usage

1. Create a python virtual environement to use the api.
2. Install from `requirements.txt` using `pip install -r requirements.txt`.
3. Create a user for it to access the api, it should be listed in the Django database. Since login, register and logout was not present in the points of the assignment I have not implemented them, but  creating users is very easy. First create a superuser using `python manage.py createsuperuser`. One can create the other two types of users too in the admin panel with isStaff and isActive permissions respectively.
4. Start the server using `python manage.py runserver`. Now you can create as many users as you like with permissions in the django admin panel present here `http://127.0.0.1:8000/admin/auth/user/`, by logging in as the superuser that you just created.
5. I also made a bit of frontend which you can see at the home page (`http://127.0.0.1:8000/`) but my main focus was satisfying REST api requirements.
6. You can test the api using Postman.

# API usage.

- NOTE: The api is made to be consumed from a frontend that is exposed to the internet, which is what I assumed from the information provided to me. A company should not store data of the candidates like resumes when they update their resume. It is actually a crime until a written notice is provided to the candidates which they agree on. It is not made to be exposed directly to public internet. The requirements need to be changed in order for me to make it usuable for public internet directly.

1. The docs are present at `http://127.0.0.1:8000/api/docs/`.
2. All the routes are available at `http://127.0.0.1:8000/api/` without any permissions. All the other routes needs a jwt token and IsAuthorized permission to access the route.

- GET Request
- Response
```
[
    "GET,POST       /api/profiles/",
    "GET,PUT,DELETE /api/profiles/:id",
    "GET,PUT,POST   /api/profiles/:id/resumes",
    "POST           /api/token/",
    "POST           /api/token/refresh"
]
```

- I have created a workflow for the requests to get a better hang of how to use the api.

3. I have implemented OAuth 2 using `simplejwt`. So one has to login and get a token from here `http://127.0.0.1:8000/api/token`. Then one can use the `access_token` with the `Authorization > Bearer token` with every request when interacting with the api.

- POST Request
```
{
    "username": "superuser",
    "password": "superuser"
}
```

- Response
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MTAxMDAyNSwiaWF0IjoxNjQwOTIzNjI1LCJqdGkiOiI3MjQzMjhjNzhmYTI0YWI2YjgzNmJiZGQ1Nzk0MjkxMyIsInVzZXJfaWQiOjF9.Dhm1GkYT5gXTjdYIOkKipPXGtraMvFo8T4jqYN2Xos0",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwOTIzOTI1LCJpYXQiOjE2NDA5MjM2MjUsImp0aSI6ImYzZDFkZmNlYjc4MjRhYWI5Y2EwZjYyYmI3OTc4ZTYxIiwidXNlcl9pZCI6MX0.vFNdZ7dwLJ25D2SNn50jUlX9xGpAE3WA1eZQJ4BBZS0"
}
```

- One can do a POST request at `http://127.0.0.1:8000/api/token/refresh` to referesh the token using the refresh token provided above.

4. `http://127.0.0.1:8000/api/profiles`

- GET Request
- Response
```
[
    {
        "id": 1,
        "is_deleted": false,
        "name": "Shivam Sharma",
        "summary": "Backend Engineer",
        "updated": "2021-12-28T16:30:27.206622Z",
        "created": "2021-12-28T16:30:27.206650Z"
    },
    {
        "id": 4,
        "is_deleted": false,
        "name": "Rishi Raj Rahul",
        "summary": "co founder",
        "updated": "2021-12-28T19:15:15.202789Z",
        "created": "2021-12-28T19:15:15.202820Z"
    }
]
```

- POST Request
```
{
    "name": "Shivam Sharma",
    "summary": "DevOps Engineer"
}
```
- Response
```
{
    "id": 7,
    "is_deleted": false,
    "name": "Shivam Sharma",
    "summary": "DevOps Engineer",
    "updated": "2021-12-31T04:16:11.033761Z",
    "created": "2021-12-31T04:16:11.033787Z"
}
```

5. `http://127.0.0.1:8000/api/profiles/7`

- GET Request
- Response
```
{
    "id": 7,
    "is_deleted": false,
    "name": "Shivam Sharma",
    "summary": "DevOps Engineer",
    "updated": "2021-12-31T04:16:11.033761Z",
    "created": "2021-12-31T04:16:11.033787Z"
}
```

6. `http://127.0.0.1:8000/api/profiles/7/resumes`

- POST Request and Response
- ![](pics/post-resume-request-response.png)

- GET Request
- Response
```
[
    {
        "id": 15,
        "file": "/media/resumes/7/images.2021-12-31_042104.301667.pdf",
        "updated": "2021-12-31T04:21:04.302430Z",
        "created": "2021-12-31T04:21:04.302447Z",
        "profile": 7
    }
]
```

- All the resumes of this profile will be stored in `/media/resumes/7/` folder. The resumes include date and time at the end telling the order of the resumes uploaded.

- PUT Request and Response
![](pics/put-request-response.png)

7. `http://127.0.0.1:8000/api/profiles/7`

- PUT Request

```
{
    "name": "Shivam Sharma",
    "summary": "CTO"
}
```

- Response

```
{
    "id": 7,
    "is_deleted": false,
    "name": "Shivam Sharma",
    "summary": "CTO",
    "updated": "2021-12-31T05:59:45.760274Z",
    "created": "2021-12-31T04:16:11.033787Z"
}
```

- DELETE Request
- Response 404

8. The resumes for the profile will be soft deleted too on `http://127.0.0.1:8000/api/profiles/7/resumes`

- GET Request
- Response 404

# What more can I do

1. Filtering, sorting, paging(limiting the feilds per page) and field selection.
2. Versioning in the path.
3. Using SSL/TLS, a.k.a. using https everywhere. (security)
4. Hiding the database schema in the api endpoints (security)
5. One can put the business core logic in a `services` folder instead of in `models` or `views`.
6. Explaining that other endpoints that are available at the current endpoint.
7. Rate limiting. (scalability)
8. API Client which provide the standard for using the api to it's consumers, with different languages.
9.  Writing test cases for the api. (probably the first thing I'll do if I have more time)
10. Making different settings files for development and production.
11. Creating images and deploy it on a cloud service like ECS Fargate or EKS so that it can scale smoothly in production.