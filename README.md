# Number Classification API

This is a simple Flask-based API that classifies a given number and returns interesting mathematical properties about it, along with a fun fact fetched from the [Numbers API](http://numbersapi.com/).

---

## Table of Contents
1. [Features](#features)
2. [API Endpoint](#api-endpoint)
3. [Example Requests](#example-requests)
4. [Response Format](#response-format)
5. [How to Run Locally](#how-to-run-locally)
6. [Deployment](#deployment)
7. [Technologies Used](#technologies-used)
8. [GitHub Repository](#github-repository)
9. [License](#license)

---

## Features
- Classifies a number based on its mathematical properties:
  - **Prime**: Whether the number is a prime number.
  - **Perfect**: Whether the number is a perfect number.
  - **Armstrong**: Whether the number is an Armstrong number (also known as a narcissistic number).
  - **Odd/Even**: Whether the number is odd or even.
  - **Digit Sum**: The sum of the digits of the number.
- Fetches a fun fact about the number from the Numbers API.
- Handles invalid inputs gracefully with appropriate error messages.

---

## API Endpoint
The API exposes a single endpoint:

### **GET** `/api/classify-number?number=<number>`
- **Query Parameter**:
  - `number`: The number to classify (must be a valid integer).
- **Response**:
  - Returns a JSON object with the number's properties and a fun fact.

---

## Example Requests

### Valid Input
**Request**:
GET /api/classify-number?number=371

**Response**:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number."
}
Invalid Input
Request:

GET /api/classify-number?number=abc
Response:

{
    "number": "abc",
    "error": true
}
Response Format
Success Response (200 OK)

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number."
}
Error Response (400 Bad Request)

{
    "number": "abc",
    "error": true
}

## How to Run Locally
Prerequisites
Python 3.x

Flask (pip install flask)

Requests (pip install requests)

Flask-CORS (pip install flask-cors)

Steps
Clone the repository:


git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
Install dependencies:

pip install -r requirements.txt
Run the Flask app:

python app.py
The API will be available at http://127.0.0.1:5000/api/classify-number.

Deployment
The API is deployed on Render and is publicly accessible. You can test it using the following URL:

Deployed API URL
https://number-classification-api.onrender.com/api/classify-number

Steps to Deploy on Render
Sign Up for Render :
Go to Render and sign up for an account if you haven’t already.
Create a New Web Service :
Click New + > Web Service .
Connect to GitHub :
Click Connect and authorize Render to access your GitHub account.
Select the repository number-classification-api.
Configure the Deployment :
Name : Optionally, you can give your service a name (e.g., number-classification-api).
Branch : Ensure the branch is set to main.
Region : Choose the region closest to you or your target audience.
Environment : Select Python 3 .
Build Command : Leave it blank (Render will automatically detect requirements.txt).
Start Command : Enter python app.py.
Environment Variables (Optional):
If you need any environment variables, you can add them here. For this project, you don’t need any.
Advanced Settings (Optional):
You can configure additional settings like auto-deploy, health checks, etc., if needed.
Create the Web Service :
Click Create Web Service .
Wait for Deployment :
Render will automatically build and deploy your application.
You can monitor the build process in the Render dashboard.
Access Your Deployed API :
Once the deployment is successful, Render will provide a public URL for your API.
It typically looks something like https://number-classification-api.onrender.com/api/classify-number.
Technologies Used
Python : The programming language used.
Flask : The web framework used to build the API.
Requests : Used to fetch fun facts from the Numbers API.
Flask-CORS : Handles Cross-Origin Resource Sharing (CORS).
Render : Platform for deploying the API.
GitHub Repository
The source code for this project is hosted on GitHub:
https://github.com/wawiramercy066/number-classification-api

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Mercy Wawira