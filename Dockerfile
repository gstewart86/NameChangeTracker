FROM python

COPY .env .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3 hall_of_fame.py" ]