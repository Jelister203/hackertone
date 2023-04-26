python -m venv data/venv
pip install -r data/requirements.txt
python -m venv parser/venv
pip install -r parser/requirements.txt

python data\manage.py migrate
START /b python data\manage.py runserver
START /b python parser\main.py