FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 5001

CMD ["python", "user_service.py"]