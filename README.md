# TOP101 - Movie and TV Show Recommendation Platform

Welcome to the TOP101 project! This web application provides recommendations for movies and TV shows, allowing users to create accounts, log in, view curated lists, and manage their favorites. Built with Django, TOP101 aims to deliver a seamless user experience with an intuitive interface and dynamic content.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Features

- **User Authentication**: Secure user registration, login, and logout functionality.
- **Favorites Management**: Add, view, and remove favorite movies and TV shows.
- **Curated Lists**: Browse recommended movies and TV shows.
- **User-Friendly Interface**: Intuitive navigation and interactive elements.

## Technologies Used

- **Django**: A high-level Python web framework.
- **SQLite**: Lightweight database for development.
- **HTML/CSS**: For structuring and styling web pages.
- **JavaScript**: For enhancing interactivity.

## Installation

To get a local copy up and running, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the repository**
   ```sh
   git clone https://github.com/busenursoker/TOP101.git
   cd TOP101
   ```

2. **Create a virtual environment**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server**
   ```sh
   set DJANGO_SETTINGS_MODULE=TOP101.settings
   python manage.py runserver
   ```

6. **Access the application**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### User Registration and Login

1. **Register**: Create a new account by providing a username, email, and password.
2. **Login**: Use your credentials to log in and access personalized features.

### Managing Favorites

1. **Add Favorites**: Browse movies and TV shows and add them to your favorites list.
2. **View Favorites**: Access your favorites list to see all your added movies and TV shows.
3. **Remove Favorites**: Update your favorites list by removing unwanted items.

### Browsing Content

1. **Movies Page**: View a curated list of recommended movies.
2. **TV Shows Page**: Explore a list of recommended TV shows.

## Project Structure

```plaintext
TOP101/
├── TOP101/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── app1/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.


Thank you for using TOP101! We hope you enjoy my platform. If you have any questions or feedback, feel free to contact us.
