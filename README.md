# YaMDB

### _API resource for collect reviews on movies, books, music etc._

If you have an irresistible desire to read or watch something brand new,
and at the same time find out people's opinions regarding a title, our
super-cool API resource will save your time spent on searching for high-quality
content!

Visiting our website, you have a marvelous possibility to see reviews of
various books, films, music track etc. and find out their rating, genre,
category!

Moreover, if you are keen on sharing your opinion with other users and
influence their choice (you may have an influence on what your friend will
check out on Netflix this Friday, is it great?), then just register! It will
also help you to leave comments on the reviews of other respected users.

IMDB can leave you at any time, but reliable YaMDb will always be available

Check it out!

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
