### Project Name
# The Movie Reviews Center
#### Author
### Stephen Ndele

## Description
The movie review center is platform that allows users post the movies they have watched and give their reviews and rating. Users can also give review to other people's posts and rate them as well.
## Live Link (feel free to experiment all features)
[View Site](https://moviereviewscenter.herokuapp.com/)


## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running 

   ```bash
   git clone https://github.com/stephenndele/movie-reviews.git
   ```
 or download a zip file of the project from github
 

Navigate to the project directory
```bash
cd movie-reviews
```

##### 2. Create a virtual environment
 Install `Virtualenv` 

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```

##### 3. Create a database or you can use sqlite provided by django framework
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```your db``` 
   ```prettier
   $ CREATE DATABASE your db
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python3 manage.py makemigrations moviereviews
```

 
then run the command below;

 ```bash
 python3 manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine, 

    python3 manage.py runserver

### Running Tests
>To run tests;

    python3 manage.py test

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap


## User stories
>As a user of the application I should be able to:

- [X] View different movies posted by other users.
- [X] Click on the article movie read more and read more details of the movie.
- [X] Can sign up to the application. 
- [X] Can sign in to the application.
- [X] Can also create a movie  and post for others to see
- [X] Can sign out of the application.
- [X] Can add review and rating to movie
- [X] Can edit review but his review only





## Bugs
There are no know bugs at the moment

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2019 Victor
 
## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## Contacts
Reach me on:
>Email:  stephenndele093@gmail.com