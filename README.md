# Customer Records Application

This project is a Python application that manages customer records using Flask and PostgreSQL. It provides a simple API to create, read, update, and delete customer information.

## Project Structure

```
customer-records-app
├── src
│   ├── app.py          # Entry point of the application
│   ├── db.py           # Database connection management
│   ├── models.py       # Data models for customer records
│   └── requirements.txt # Python dependencies
├── Dockerfile           # Instructions to build the Docker image
├── docker-compose.yml    # Service definitions for Docker
├── .dockerignore        # Files to ignore during Docker build
└── README.md           # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd customer-records-app
   ```

2. **Build the Docker image:**
   ```
   docker-compose build
   ```

3. **Run the application:**
   ```
   docker-compose up
   ```

4. **Access the API:**
   The application will be available at `http://localhost:5000`.

## Usage

- **Create a customer record:**
  - POST `/customers`
  
- **Get all customer records:**
  - GET `/customers`
  
- **Get a specific customer record:**
  - GET `/customers/<id>`
  
- **Update a customer record:**
  - PUT `/customers/<id>`
  
- **Delete a customer record:**
  - DELETE `/customers/<id>`

## Dependencies

The application requires the following Python packages:

- Flask
- psycopg2

These dependencies are listed in `src/requirements.txt`.

## License

This project is licensed under the MIT License.# apipython
