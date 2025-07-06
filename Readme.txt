Little Lemon Restaurant API and Web Application
================================================

This Django project implements the web application and REST API for Little Lemon Restaurant.

The project includes:
- Static HTML content pages
- A booking system
- Menu management
- Authentication with tokens

------------------------------------------------------------
Project Setup Instructions
------------------------------------------------------------

1. Install dependencies:
   pip install -r requirements.txt

2. Run migrations:
   python manage.py migrate

3. Create a superuser:
   python manage.py createsuperuser

4. Start the server:
   python manage.py runserver

------------------------------------------------------------
Authentication
------------------------------------------------------------

Use the following endpoint to obtain a token for authenticated API calls:

POST /api-token-auth/

Request Body (JSON):
{
  "username": "<your_username>",
  "password": "<your_password>"
}

The response will contain your token:
{
  "token": "<your_token>"
}

Use this token in the Authorization header for API requests:

Authorization: Token <your_token>

------------------------------------------------------------
Available URL Paths
------------------------------------------------------------

The project includes two main apps:

------------------------------------------------------------
Restaurant App (Web views)
------------------------------------------------------------

GET /
  - Home page

GET /about/
  - About page

GET /book/
  - Booking page (form)

GET /reservations/
  - List of reservations

GET /menu/
  - Menu page

GET /menu_item/<pk>/
  - Details of a single menu item

GET /bookings/
  - Booking records

POST /api-token-auth/
  - Obtain authentication token

------------------------------------------------------------
API App (API endpoints)
------------------------------------------------------------

POST /assign-manager/
  - Assign a user as manager

POST /add-category/
  - Add a new category

POST /add-menu-item/
  - Add a new menu item

GET  /menu-items/
  - List all menu items

GET  /categories/
  - List all categories

POST /cart/add/
  - Add items to the cart

GET  /cart/
  - View cart contents

POST /order/place/
  - Place an order

GET  /my-orders/
  - List orders of the logged-in user

POST /assign-delivery-crew/
  - Assign a delivery crew member

POST /assign-order/
  - Assign an order to delivery crew

GET  /delivery-orders/
  - List orders assigned to delivery crew

POST /update-order-status/
  - Update the status of an order

------------------------------------------------------------
How to Test
------------------------------------------------------------

1. Start the Django server:
   python manage.py runserver

2. Use a REST client like Postman or Insomnia to test the API endpoints.

3. For web pages, access them via your browser:
   http://127.0.0.1:8000/

4. Remember to include the Authorization header for protected endpoints:
   Authorization: Token <your_token>

------------------------------------------------------------

Thank you for reviewing this project!
