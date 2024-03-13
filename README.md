# Django Web App

## Functional Specification

### Overview

This web platform aims to connect customers to basic necessities and needs all at their convenience through services like online ordering, delivery or booking services.

### User Roles

1. _Guest User:_
   o Can browse products.
   o Can register or log in.
2. _Registered User(Customer):_
   o Inherits guest user privileges.
   o Can add/remove products to/from the shopping cart.
   o Can place orders.
3. _Registered User(Business):_
   o Inherits guest user privileges and registered user privileges for a customer.
   o Can setup, manage, and maintain online stores on the web platform.
4. _Admin User:_
   o Inherits registered user privileges.
   o Can add/update/remove products and also online stores
   o Can manage user accounts and orders

### Features

1. _Product Catalog:_
   o Display products with details.
   o Filter and search functionality.
2. _User Authentication:_
   o Registration and login.
   o Password reset functionality.
3. _Shopping Cart:_
   o Add/remove products.
   o Adjust quantities.
   o Calculate total price.
   o Rate products.
4. _Order Processing:_
   o Confirm order details.
   o Payment integration (e.g., Stripe).
   o Order confirmation and tracking.
5. _Admin Panel:_
   o Manage products.
   o View and process orders.
   o User management.

## Technological Specification

1.  _Backend:_
    o Django
    o Django REST Framework for APIs.
2.  _Frontend:_
    o HTML, CSS, JavaScript.
    o Bootstrap for responsive design.
3.  _Database:_
    o PostgreSQL or MySQL for data storage.
    • Authentication:
    o Django's built-in authentication system.
4.  _Misc:_
    o Payment Integration like: Stripe API
    o Email API like Sendgrid, Mailgun for email related tasks

## Development Methodology:

        o	Pair Programming: This involves collaboration on gitlab so as to ease tasks and ensure agile development and high quality code.
        o	Testing the platform: User acceptance testing to ensure platform functionality and stability.

## Evaluation Criteria:

        o	Ease of use of the platform
        o	Technical Implementation
        o	Deployment and Scalability
        o	Functionality
