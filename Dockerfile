FROM joyzoursky/python-chromedriver:3.8

COPY . /bootcamp_selenium_bdd_framework

WORKDIR /bootcamp_selenium_bdd_framework

RUN pip3 install pipenv
