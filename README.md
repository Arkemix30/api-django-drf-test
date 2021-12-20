# Spot Test with Django

## Solutions Implemented 💡

* _An endpoint to provide a search lookup within the tracks (at least by name, but is open to any suggestions)_
    * Solution: Created a `ListAPIView` to get a list of all tracks that matches with the query parameters in the url. In this case you can filter by `name` and `artistName`. Using Raw SQL queries
    *Endpoint example: `/api/tracks/?name={name}`
* _An endpoint that would allow to get the top 50 popularity tracks._
    * Solution: Created another `ListAPIView` class to get the list of most popular tracks, order by `rank` field. Using Raw SQL queries
    * Endpoint example: `/api/tracks/most_popular`
* _An endpoint to remove a track, using a given identifier (defined by you)_
    * Solution: Created a `RetrieveUpdateDestroyAPIView` that you can delete a track using the DELETE http method, passing the `id` of the track.
    * You need to register and be logged in to remove or update a track. `/api/auth/register` or `/api/auth/login/`
    * Endpoint example: `api/tracks/{id}/`
* _An endpoint to add new tracks using ORM._
    * Solution: Created a `CreateAPIView` that recieves the data, deserialize it and save it if data is valid.
    * You need to register and be logged in to create a track.
    * Endpoint example: `api/tracks/create/`

- Extra: There's an entire CRUD for Genres model, you can access at the endpoint: `api/genres/`
    * You need to register and be logged in.

#### Bonus:
- ✔ _Use a Database (suggested: SQLite), instead of the JSON File_
- ✔ _Add authentication API endpoint(s) with Django Rest Framework (DRF)_
    * Created an endpoint: `api/auth/register/` using a Serializer with the default Django Auth User Model, that receives `username`, `first_name`, `last_name`, `password`, `re_password` (for confirmation). It validates if both password matches. And then saves it into the database.
    * To _login_, you can use the endpoint: `/api/auth/login` with you created user.
- ✔ _Use SQL instead of ORM only for SELECT queries._
    * Using Raw Queries
- ✔ _Create an endpoint to return the tracks grouped by genres_
    * Created a `ListAPIView` class that filters against the URL, using the Django ORM filters by genre name.
    * Endpoint example:  `api/tracks/genre/{genre}/`

## Project's Folder Structure
```bash
.
├── api             # DRF app folder
    ├── auth
        ├── serializers.py
        └── views.py
    ├── genres
        ├── models.py
        ├── serializers.py
        └── views.py
    ├── migrations
    ├── tracks
        ├── models.py
        ├── serializers.py
        └── views.py
    ├── admin.py
    ├── apps.py
    └── urls.py
├── spot_test       # Django project's folder
├── manage.py
├── poetry.toml     # build configs
├── pyproject.toml  # build configs
└── README.md
```

## How to run the code 🏃‍♂️
### Installation 🔧

You will need to install [Poetry](https://python-poetry.org/) to install project's dependencies

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```

Locate where Poetry is installed

```bash
whereis poetry
```

Copy and replace poetry's path to this line and added it at the end of the `.bashrc` file

```bash
export PATH="$HOME/.poetry/bin:$PATH"
```

## Installing project's dependencies 📚

Enter into project's root folder and run:

```bash
poetry install
```
It should create a `.venv` folder, generating a virtual enviroment with all project's dependencies

## How to run locally ⚙️

* Clone the repository
```bash
$ git clone https://github.com/Arkemix30/spot-test.git
```

* To run the project, you need to activate the virtual environment.
For that, you can run this command:
```bash
$ poetry shell
```

* You have to migrate the model's schema into database, run the next commands:
```bash
$ python manage.py makemigrations && python manage.py migrate
```
(if you have problems, run the commands separately)

* Then, you should run the following command to insert the dummy data.
```bash
$ python manage.py loaddata genres_data.json
$ python manage.py loaddata tracks_data.json
```
* And finally, to run the server:
```bash
$ python manage.py runserver
```

## Built with 🛠️

* [Django](https://www.djangoproject.com/) - The framework used
* [Django Rest Framework](https://www.django-rest-framework.org/) - The framework used for RESTful API


## Authors ✒️

* **Enmanuel Silva** - [Arkemix](https://github.com/Arkemix30)

---
⌨️ with ❤️ by [Arkemix30](https://github.com/Arkemix) 😊
