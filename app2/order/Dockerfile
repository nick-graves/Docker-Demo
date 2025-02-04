FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install flask requests

EXPOSE 5002

CMD ["python", "order_service.py"]