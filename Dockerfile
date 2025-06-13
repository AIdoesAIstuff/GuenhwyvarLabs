FROM python:3.11-slim

WORKDIR /app

COPY entertainment_recommender/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY entertainment_recommender/ ./

EXPOSE 5000

CMD ["python", "app.py"]
