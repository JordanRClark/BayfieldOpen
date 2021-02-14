FROM python:3.8

RUN python -m pip install --upgrade pip

COPY bayfieldopen/requirements/base.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .
