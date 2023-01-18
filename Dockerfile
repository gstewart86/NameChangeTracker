FROM python

COPY .env .
COPY requirements/prod requirements
COPY src/ .

RUN pip install -r requirements

ENTRYPOINT [ "python3 ncr.py" ]