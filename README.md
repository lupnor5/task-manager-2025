# Django Task Manager

A simple and elegant task management application built with Django and Bootstrap. This application allows users to create, read, update, and delete tasks through a user-friendly interface.

## Features

- Create new tasks
- View list of all tasks
- Update existing tasks
- Delete tasks
- Responsive design using Bootstrap
- Clean and intuitive user interface

## Technologies Used

- Python 3.13
- Django 5.1.5
- Bootstrap 5.3.2
- Bootstrap Icons

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd task-manager
```

2. Create and activate a virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages
```bash
pip install django
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to use the application.

## Project Structure

```
task-manager/
├── todo/                   # Main application directory
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   │   ├── todo/
│   │   │   ├── add.html
│   │   │   ├── home.html
│   │   │   ├── layout.html
│   │   │   └── update.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── myproject/             # Project configuration directory
├── manage.py
└── README.md
```

## Usage

1. **View Tasks**: Navigate to the home page to see all tasks
2. **Add Task**: Click the "Add New Task" button and fill in the task details
3. **Update Task**: Click the "Edit" button next to any task to modify it
4. **Delete Task**: Click the "Delete" button next to any task to remove it

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## Contact

Maria Guadalupe Ramirez Cruz - [lupnor5@gmail.com]

Project Link: [https://github.com/lupnor5/task-manager-2025]
