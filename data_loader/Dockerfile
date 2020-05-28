FROM python:3.7.5-slim
ADD . /myapp
WORKDIR /myapp
RUN python -m pip install -r requirements.txt
# COPY headlines.py .
CMD ["python", "data_loader.py"]