# Inventory Management System

## Team Members
- **Hadid Sukma Raganata** - A11.2022.14551
- **Setya Ardi Kurniawan** - A11.2022.14555
- **Alfath Tauhidillah** - A11.2022.14573

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)

## Overview
The **Inventory Management System** allows users to:
- Manage items, categories, and suppliers
- View and update inventory levels and prices
- Retrieve statistics on stock levels, values, and supplier contributions
- Monitor items that fall below a specified stock threshold

## Features
- **Dashboard**: Displays a summary of stock levels, total stock value, average price, and more.
- **Items Management**: CRUD operations (Create, Read, Update, Delete) for managing items.
- **Categories Management**: CRUD operations for managing item categories.
- **Suppliers Management**: CRUD operations for managing suppliers.

## Technologies
- **Django** - Web framework for Python to handle business logic and ORM operations.
- **PostgreSQL** - Database for storing inventory data (items, categories, suppliers, etc.).
- **Tailwind CSS** - Frontend styling for responsive and modern UI.
- **Docker** - Containerization for easy setup and deployment.

## Setup and Installation
### Prerequisites
- Docker installed on your machine

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/hadidsr/uts_pss.git
   cd uts_pss
   ```

2. **Build and Run Docker**
 Use Docker Compose to build and start the containers:
   ```bash
   docker compose up -d --build
   ```

3. **Apply Migrations**

    In a new terminal window, apply the migrations to set up the database tables:

- First, generate migrations
   ```bash
   docker exec web_uts_pss python manage.py makemigrations
   ```

- Then, apply the migrations
   ```bash
   docker exec web_uts_pss python manage.py migrate
   ```

4. **Restart the Docker Containers**

   After applying migrations, restart the Docker containers to ensure all changes are loaded correctly:
   ```bash
   docker compose restart
   ```

5. **Creating a Superuser (Admin Access)**

    To access the admin panel for create an admin inventory management, run the following command:
   ```bash
   docker exec -it web_uts_pss python manage.py createsuperuser
   ```

6. **Access the Application**

    - Visit the application by opening your browser and navigating to http://localhost:8000/.
    - **Note:** you can't manage any category, suppliers, and items before create an admin for inventory management

7. **Create Admin Inventory Management**

    - Select admin on the navigation bar
    - Log in using the superuser credentials you just created.
    - From the admin panel, you can manage admin for inventory management.
    
    After creating this admin, you will have full to features available in the application.