# YaMDB

### _API resource for collect reviews on movies, books, music etc._

![Powered by TEAM 22, Python and DRF](https://i.yapx.ru/TywCz.png)

## 1. Technologies:

    - Python 3.8
    - Django 3.0
    - Djangorestframework 3.12.4    

## 2. How to launch:

#### Clone repository:

```sh
 git clone https://github.com/kozarezov/api_yamdb.git
 ```

#### Create and activate Virtual Environment:

```sh
python -m venv env
 ```

```sh
source env/bin/activate
 ```

#### Install requirements from _requirements.txt_:

```sh
python -m pip install --upgrade pip
 ```

```sh
pip install -r requirements.txt
 ```

#### Make migrations:

```sh
python manage.py migrate
 ```

#### Launch developer server:

```sh
python manage.py runserver
 ```

## 3. API documentation:

#### Go to Redoc documentation on localhost:

```sh
http://127.0.0.1:8000/redoc/
 ```

## 4. Requests examples:

#### Authorization:

**POST:** `/api/v1/auth/signup/` - to signup for new user

#### Actions with titles:

**GET:** `/api/v1/titles/` - to get all titles list

**POST:** `/api/v1/titles/` - to add a title

**PATCH:** `/api/v1/titles/{titles_id}/` - to update your title

**DELETE:** `/api/v1/titles/{titles_id}/` - to delete your title

#### Actions with reviews / comments:

**POST:** `/api/v1/titles/{title_id}/reviews/ ` - to create a review

**GET:** `/api/v1/titles/{title_id}/reviews/ ` - to get a title's reviews

## 5. Created by Team_22:

Denis Kozarezov [GitHub](https://github.com/kozarezov)

Irina Savenko [GitHub](https://github.com/Savi-rina)

Alexey Shemyakin [GitHub](https://github.com/Pomor29)
