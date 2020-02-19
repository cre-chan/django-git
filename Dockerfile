FROM python:3

# django uwsgiをインストール
RUN pip install django uwsgi
COPY requirements.txt requirements.txt

# あらゆる依存をインストール
RUN pip install -r requirements.txt

WORKDIR /server/django-git


# データベースを遷移し、静的ファイルを収集
# RUN python manage.py migrate \
#     && python manage.py collectstatic

# プログラムが作動するには/tmp/gitディレクトリが必要で、匿名ボリュームをつける
VOLUME /tmp/git/

# containerの8000番ポートで待ち受け
EXPOSE 8000

# CMD uwsgi uwsgi.ini