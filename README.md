# Image Compression Web Application

A modern web application for compressing images using Django and Flask, with a beautiful UI powered by Tailwind CSS.

## Features

- Drag and drop image upload
- File selection upload
- Paste image support (Ctrl+V or right-click)
- Automatic image compression
- Before/After size comparison
- Download compressed images
- Modern, responsive UI with Tailwind CSS

## Project Structure

```
.
├── frontend/              # Django application
│   ├── compress/         # Django app
│   ├── static/          # Static files
│   └── templates/       # HTML templates
├── backend/             # Flask microservice
│   └── api/            # API endpoints
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Django:
   ```bash
   cd frontend
   python manage.py migrate
   python manage.py runserver
   ```

4. Set up Flask backend:
   ```bash
   cd backend
   python app.py
   ```

5. Access the application:
   - Frontend: http://localhost:8000
   - Backend API: http://localhost:5000

## Development

- Django frontend runs on port 8000
- Flask backend runs on port 5000
- Tailwind CSS is used for styling
- Image compression is handled by Pillow

## Technologies Used

- Django 5.0.2
- Flask 3.0.2
- Tailwind CSS
- Pillow (PIL)
- Python 3.8+ 