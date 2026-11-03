# Bella Vista Cafe – Flask Web Application

**Course:** EGN 475 – Software Prototyping  
**Project:** Bella Vista Cafe  
**Developer:** Waqar Javed

## Project Overview

Bella Vista Cafe is a simple web application developed using Python and Flask as part of the EGN 475 Software Prototyping course.

The application demonstrates the fundamentals of web development using the Flask framework. It provides two basic web pages: a homepage that welcomes visitors and an About page that introduces the cafe.

## Technologies Used

- Python 3.12
- Flask 3.1.3
- Visual Studio Code
- Git and GitHub

## Application Features

The application includes two routes:

| Route | Description |
|---|---|
| `/` | Displays a welcome message: "Welcome to Bella Vista Cafe". |
| `/about` | Displays a short description of Bella Vista Cafe. |

## Project Structure

```text
egn475-cafe-javed/
│
├── .venv/          # Python virtual environment (not committed)
├── .gitignore      # Excludes unnecessary files
├── app.py          # Main Flask application
└── README.md       # Project documentation
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/iamwaqarjaved/egn475-cafe-javed.git
cd egn475-cafe-javed
```

### 2. Create a Virtual Environment

```bash
python3.12 -m venv .venv
```

### 3. Activate the Virtual Environment

**macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Flask

```bash
python -m pip install flask
```

### 5. Run the Application

```bash
python -m flask --app app run --debug
```

Open your browser and visit:

- Homepage: http://127.0.0.1:5000/
- About Page: http://127.0.0.1:5000/about

## Learning Objectives

This project demonstrates:

- Setting up a Python development environment.
- Creating and activating a Python virtual environment.
- Installing and using the Flask web framework.
- Creating URL routes and Python functions.
- Returning HTTP responses from Flask applications.
- Using Git for version control and GitHub for source code management.

## Author

**Waqar Javed**

EGN 475 – Software Prototyping