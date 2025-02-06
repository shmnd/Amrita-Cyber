
## Setup Instructions

1. Clone the repository:
 git clone https://github.com/yourusername/evaluation_project.git
 cd evaluation_project

2. Set up a virtual environment:
  python -m venv venv
  source venv/bin/activate

3.Install dependencies:
pip install -r requirements.txt

5.Run migrations:
  python manage.py makemigrations
  python manage.py migrate

6.Start the Django development server:
  python manage.py runserver

7.Start the Celery worker:
  celery -A evaluation_project worker --loglevel=info
