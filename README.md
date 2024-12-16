py --version

py -m venv .venv

code.

.venv\Scripts\activate.bat

python manage.py runserver

py manage.py migrate

py manage.py shell

>>> from news.models import News
>>> n = News()
>>> n.title = "Допомога UGB для UNBROKEN досягне 40 млн грн до кінця 2024 року"
>>> n.save()
>>> n.content = "UGB (оновлений Укргазбанк) продовжує системно підтримувати Національний реабілітаційний центр UNBROKEN (НЕЗЛАМНІ), де лікують та реабілітують військовослужбовців, ветеранів та українців, що постраждали внаслідок війни. "
>>> n.save()
>>> n.image_url = "https://img.tsn.ua/cached/361/tsn-135859377404ec64163c97d964721c31/thumbs/1036x648/90/79/ff3a43c14a7f3cfde426d70f9c7c7990.jpeg"
>>> n.save()
>>> News.objects.all().values() 

Global Database ---  filess.io
