FROM python:3.8-buster

# $DELETE_BEGIN
COPY api api
COPY taxifaremodel taxifaremodel
COPY model.joblib model.joblib
COPY requirements.txt requirements.txt
# $DELETE_END

# $CHALLENGIFY_BEGIN
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# $CHALLENGIFY_END

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
