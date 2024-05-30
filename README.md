# Udyog Sarathi

**Udyog Sarathi** is a Django-based web application designed to serve as a comprehensive job and training portal specifically tailored for persons with disabilities. The platform aims to bridge the gap between job seekers with disabilities and potential employers, as well as provide necessary training resources to enhance their employability.



## Features

- **User Registration and Authentication**: Secure registration and login system for job seekers and employers.
- **Job Listings**: Employers can post job openings, and job seekers can browse and apply for jobs.
- **Training Resources**: Access to various training programs and resources to improve skills and employability.
- **Profile Management**: Users can create and manage their profiles, including personal information, skills, and experience.
- **Accessibility Features**: Designed with accessibility in mind to cater to the specific needs of users with disabilities.


## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (or any other preferred database)
- Virtualenv (for virtual environment management)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/udyog-sarathi.git
   cd udyog-sarathi
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**:
   - Ensure PostgreSQL is installed and running.
   - Create a database and a user with the appropriate permissions.
   - Update the database settings in `udyog_sarathi/settings.py`.

5. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Configuration

- **Settings**:
  - Update `udyog_sarathi/settings.py` with your specific configurations such as `DATABASES`, `EMAIL_BACKEND`, and other necessary settings.
  
- **Environment Variables**:
  - Use a `.env` file or set environment variables for sensitive information such as `SECRET_KEY`, `DATABASE_URL`, and email service credentials.

## Usage

- **Admin Interface**:
  - Accessible at `http://127.0.0.1:8000/admin/`.
  - Use the superuser credentials to log in and manage the application.

- **Job Seekers**:
  - Register and create a profile.
  - Browse and apply for jobs.
  - Access training resources.

- **Employers**:
  - Register and create a company profile.
  - Post job openings and manage applications.

## Project Structure

```
udyog-sarathi/
├── manage.py
├── udyog_sarathi/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── apps/
│   ├── accounts/
│   ├── jobs/
│   ├── training/
│   ├── ...
├── templates/
├── static/
├── media/
└── requirements.txt
```

- **manage.py**: Django's command-line utility for administrative tasks.
- **udyog_sarathi/**: Main project directory containing settings and configuration files.
- **apps/**: Directory containing Django apps for different functionalities.
- **templates/**: HTML templates for rendering the web pages.
- **static/**: Static files such as CSS, JavaScript, and images.
- **media/**: Uploaded media files.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

