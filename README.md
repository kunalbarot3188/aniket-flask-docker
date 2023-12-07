# VaseCom Flask App with MySQL

This repository contains a Flask web application (VaseCom) that interacts with a MySQL database using Docker. Follow the steps below to set up and run the application manually.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Aniket-d-d/ak-flask-docker.git
   cd ak-flask-docker
   ```

2. **Build the Docker Images:**
Build the Docker images for the Flask app and MySQL server.
   ```
   docker build -t vasecom-app:v1 .
   ```
3. **Create the network:**
Create a common docker network for both the containers to inetract.
   ```
   docker network create vasecom_network
   ```
4. **Run the MySQL Container:**
Start a MySQL container with the required environment variables.
   ```
   docker run -d --network vasecom_network --name mysql-server -e MYSQL_ROOT_USER=root -e MYSQL_ROOT_PASSWORD=AK@1234 -e MYSQL_DATABASE=akusers mysql:latest
   ```
5. **Run the Flask App Container:**
Start the Flask app container and link it to the MySQL container.
   ```
   docker run -d --name vasecom-appv1 --network vasecom_network -p 5000:5000 vasecom-app:v1
   ```
6. **Access the App:**
Open your web browser and visit http://VM_IP:5000 to access the Flask app.

7. **Stop and Clean Up:**
   ```
   docker stop vasecom-appv1 mysql-server
   docker rm vasecom-appv1 mysql-server
   ```


## Important Note

- **Functionality:** This site is designed for study purposes, and not all pages are fully functional.
- **Data Storage:** The only operational feature is the sign-up page, which stores user data in a MySQL database.
- **Viewing Data:** After signing up, you can view the stored user data on the "Ordered" page, accessible by clicking the "Place Order" button on the cart page.

Feel free to explore and study the codebase. If you encounter any issues or have questions, please don't hesitate to reach out.


      
