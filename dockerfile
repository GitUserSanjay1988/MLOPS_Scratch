FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y curl

WORKDIR /Users/sanjaypc/DSML-Oct-22/MLOPs/MLOPS/Flask_CICD/flask_working

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY classifier.pkl ./
COPY Loan_app.py ./
COPY dockerfile ./

COPY . .

CMD ["python","-m","flask","--app","Loan_app","run","--host=0.0.0.0"]