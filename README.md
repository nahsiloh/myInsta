# myInsta
myInsta is a Django application that allows users to upload photos. 
It serves as a personal album (login required) and a public photo journal.

## Quick Start
Installation Steps if you want to try it out

```
git clone https://github.com/nahsiloh/myInsta.git
cd myInsta
virtualenv venv
venv\Scripts\activate
pip install django
cd insta
pip install django-bootstrap4
pip install pillow
python manage.py migrate
python manage.py runserver
```

## Requirements
- Python==3.7.2
- Django==2.2.2
- django-bootstrap4==0.0.8
- Pillow==6.0.0


## Functions
1. User login and sign up 
2. CRUD functions for Albums and Images (Login Required)
3. Allows for public and private settings for images. Public images published on homepage.
