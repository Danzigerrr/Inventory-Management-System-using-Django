# Inventory and Sales Management System

This is a Django-based web application designed to manage the inventory and sales for a small business that sells handmade crafts and art supplies. The application provides functionalities to track inventory levels, process sales, and generate reports.

## Features

- **Inventory Management**: Track stock levels, receive new inventory, and update inventory levels as items are sold.
- **Sales Processing**: Process sales in both the physical store and the online store, and automatically update inventory levels accordingly.
- **Reporting**: Generate reports on sales, inventory levels, and customer data, such as popular products and customer purchase histories.
- **User-Friendly Interface**: Easy-to-use interface for the business owner and employees.
- **Security**: Password-protected access and regular data backups.
- **Scalability**: Designed to accommodate future business growth.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Danzigerrr/Inventory-Management-System-using-Django.git
   cd inventory_management
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source source .venv/Scripts/activate

   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
    - Open your browser and go to `http://127.0.0.1:8000/`

## Usage

### Admin Interface

- Visit `http://127.0.0.1:8000/admin/` to access the Django admin interface.
- Log in with the superuser credentials.
- Manage products, inventory transactions, sales, and customer data through the admin interface.

### Main Application

- **Inventory Management**: Navigate to `/inventory/` to view and manage inventory.
- **Sales Management**: Navigate to `/sales/` to view and process sales.
- **Customer Management**: Navigate to `/customers/` to view and manage customer data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Stay in touch
Author - Krzysztof Nazar:
- [Linkedin](https://www.linkedin.com/in/krzysztofnazar/)
- [GitHub](https://github.com/Danzigerrr)


## License
This project is [MIT licensed](LICENSE)

