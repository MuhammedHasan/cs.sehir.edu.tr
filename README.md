#Installation

Create `virtual environment` and `activate` then

```
git clone https://github.com/MuhammedHasan/cs.sehir.edu.tr.git
cd cs.sehir.edu.tr
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json
python manage.py migrate # may it need
python manage.py runserver 8000
```

Update field whose values are '#' in settings.py 
