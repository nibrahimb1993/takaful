FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info postgresql-client gettext \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py compilemessages

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
