FROM python:3.7.5-slim
ADD . /app
WORKDIR /app
RUN python -m pip install -r requirements.txt
# COPY headlines.py .
EXPOSE 8050
CMD ["python", "app.py"]