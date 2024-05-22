# BookStore Project

Welcome to the BookStore project! This project is a web application built with Django, designed to provide a comprehensive platform for managing a bookstore. Users can browse, review, and purchase books, as well as manage their shopping carts.

## Table of Contents

- [Project Overview](#project-overview)
- [Database](#database)
- [Features](#features)
- [User Operations](#user-operations)
- [Installation](#installation)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The BookStore project is a Django-based web application that allows users to browse books, add reviews, manage a shopping cart, and complete purchases. The project aims to provide a seamless and user-friendly experience for both customers and administrators.

## Database

The project uses a relational database (e.g., PostgreSQL, MySQL, SQLite) to store the following entities:

- **User**: Standard Django user model for authentication.
- **Book**: Stores information about books including title, author, description, price, and publication date.
- **UserProfileInfo**: Extends the user model to store additional profile information like portfolio site and profile picture.
- **Review**: Stores user reviews for books.
- **CartItem**: Stores items that users add to their shopping cart.

## Features

- **User Registration and Authentication**: Users can register, log in, and log out.
- **Book Management**: Users can add, edit, and delete books.
- **Review System**: Authenticated users can add reviews to books.
- **Shopping Cart**: Users can add books to a shopping cart and proceed to checkout.
- **Search Functionality**: Users can search for books by title, author, or keyword.

## User Operations

### Registration

Users can register by providing a username, email, and password. Upon successful registration, users are redirected to the login page.

### Login

Registered users can log in using their username and password. Upon successful login, users are redirected to the home page.

### Book Browsing

Users can browse books listed on the home page. Each book detail page displays the book information and reviews.

### Adding Reviews

Authenticated users can add reviews to books. The review form is available on each book detail page.

### Shopping Cart

Users can add books to their shopping cart. The cart displays the selected books, their quantities, and the total price. Users can remove items from the cart or proceed to checkout.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone <project link>
    cd project
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Screenshots

### Home Page
![Home Page](https://github.com/Olcaytp/Django-Bookstore-Project/blob/main/assets/home-1.png)
![Home Page](https://github.com/Olcaytp/Django-Bookstore-Project/blob/main/assets/home-2.png)

### Book Detail Page
![Book Detail Page](https://github.com/Olcaytp/Django-Bookstore-Project/blob/main/assets/detail-1.png)

### Shopping Cart
![Shopping Cart](https://github.com/Olcaytp/Django-Bookstore-Project/blob/main/assets/shopping-cart.png)

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to update tests as appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Notes for Me

There are a few things to add to this project

- after purchase completion mail will be sent to users email
- at navbar cart items number can be set
- adding book image may be good option
