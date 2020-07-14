### Django url shortener

#### Deploy localy

```shell script
git clone https://github.com/thestics/url_shortener.git shortener

cd shortener
python3 -m venv
source venv/bin/activate
pip3 install -r requirements.txt
gunicorn url_shortener.wsgi:application -b 0.0.0.0:8000
```