cd data
python -m venv venv
pip install -r requirments.txt
cd ../parser
python -m venv venv
pip install -r requirments.txt
cd ..
START /b python data\manage.py runserver
START /b python parser\main.py