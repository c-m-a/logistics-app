# Logistics App

The Logistics App is a Django-based web application designed to manage packages, customers, and couriers for efficient logistics operations.

## Description

The Logistics App allows users to:

- Track packages through the delivery process.
- Manage customer information.
- Assign and track couriers for efficient delivery.

## Used Libraries

The Logistics App utilizes the following key libraries:

- Django 4.2.10: Web framework for building robust web applications.
- Django Rest Framework (DRF) 3.14.0: A powerful and flexible toolkit for building Web APIs.
- SQLite: Lightweight, built-in database for local development.

## Installation and Configuration for Local Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/logistics-app.git
   cd logistics-app
   ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

```bash
    python manage.py runserver
```

7. Access the app at http://localhost:8000

8. How to Test

Run the tests using:

```bash
python manage.py test
```

8. APIs

The Logistics App exposes the following APIs:

    Assign Courier to Package:
        Endpoint: /api/packages/<int:package_id>/assign_courier/<int:courier_id>/
        Method: PUT

    Mark Package as Delivered:
        Endpoint: /api/packages/<int:package_id>/mark_delivered/
        Method: PUT

9. How to Test with CURL Command

### Assign Courier to Package
```lbash
curl -X POST http://localhost:8000/api/packages/<pk>/assign_courier/<courier_id>/
```
###Deliver Package

```bash
curl -X POST http://localhost:8000/api/packages/<pk>/deliver_package/
```

Adjust the package and courier IDs accordingly.

10. Deploy to Heroku

a. Sign up for a Heroku account.
b. Install the Heroku CLI: Heroku CLI.
c. Log in to Heroku using the CLI:

    ```bash
    heroku login
    ```

### Create a Heroku app:

    ```bash
    heroku create your-logistics-app
    ```

### Add a PostgreSQL database to your Heroku app:

    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

### Set environment variables:

    ```bash
    heroku config:set DJANGO_SETTINGS_MODULE=logistics_app.settings.production
    heroku config:set SECRET_KEY=your-secret-key
    ```

### Deploy the app:

    ```bash
    git push heroku master
    ```

### Run migrations:

    ```bash
    heroku run python manage.py migrate
    ```
### Open the app in your browser:

    ```bash
        heroku open
    ```

11. Hope or Flo

Hope or Flo is a simple, free continuous deployment service for Heroku. Connect your GitHub repository to automatically deploy changes to Heroku whenever you push to the main branch.

