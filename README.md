**Automated UI Testing with Python, Selenium, Pytest, Docker, and Allure.**

Prerequisites
Ensure you have the following installed before running the tests:  
✔ Python 3.10+  
Note: You may need to install or configure the Python interpreter if it's not already installed. You can download it from python.org.  
✔ Docker & Docker Compose  
✔ Allure Commandline (Install via Scoop on Windows: scoop install allure)  

**1. Clone the Repository**
To get started, clone the repository to your local machine:
```bash
git clone https://github.com/valeriu-birladeanu/Python_Selenium.git 
```

**2. Change to the Project Directory**
After cloning, change the current directory to the project folder:
```bash
cd Python_Selenium-demo_qa
```

**3. Create & Activate Virtual Environment**
Create and activate a virtual environment:
```bash
python -m venv venv
```
Activate the environment:  
✔ For Windows:  
```bash
.\venv\Scripts\activate
```
✔ For macOS/Linux:  
```bash
source venv/bin/activate
```
Note: If the python command doesn't work, try using python3 instead, especially on macOS/Linux.

**4. Install the required dependencies from requirements.txt:**
```bash
pip install -r requirements.txt
```

**5. Run Tests with Docker Compose**
To build the Docker image and execute the automated tests inside a container, run:
```bash
docker-compose up
```
This command will:  
✔ Build the Docker image based on the Dockerfile and docker-compose.yml.  
✔ Start a container and run the automated tests.  
Note: Ensure that Docker and Docker Compose are installed on your machine before running this command.  

**6. Generate and View Allure Report**
After the tests have been executed, you can generate and view the Allure report using the following command:
```bash
allure serve allure-results
```
This will open a browser with the detailed test report.
Note: Ensure that the allure-results directory exists and contains test execution data before running this command.