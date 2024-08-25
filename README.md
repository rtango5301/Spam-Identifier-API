# Spam-Identifier-API

This is a Django REST API that allows users to register contacts and check whether they are associated with spam. The API is designed to be simple and efficient, providing endpoints for contact registration and spam checking based on phone numbers and names.

## Features

- **Contact Registration**: Register contacts with attributes like name, phone number, email, and a count of spam reports.
- **Spam Checking**: Check if a contact is associated with spam based on the number of spam reports.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/spam-identifier-api.git
   cd spam-identifier-api

2. **Create a virtual env**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Run the development server**:
   ```bash
   python manage.py runserver


## Usage

You can interact with the API using tools like 'curl' , Postman, or directly from your browser.

1. **Register a new contact**:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/register/ -d "name=John Doe&phone=1234567890&email=john@example.com"

3. **Check if a contact is spam by phone**:
   ```bash
   curl http://127.0.0.1:8000/api/search/phone/?phone=1234567890

   
5. **Check if a contact is spam by name**:
   ```bash
   curl http://127.0.0.1:8000/api/search/name/?name=John%20Doe


## Project Structure 

1. spam_identifier/ : Main project directory containing settings and URL configuration.
2. api/ : Contains the models, views, and URL patterns for the API.
3. requirements.txt : Lists all the dependencies required by the project.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes.

   

