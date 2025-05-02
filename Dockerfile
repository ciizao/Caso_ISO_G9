FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080
ENV GOOGLE_API_KEY=AIzaSyBKjSTsJSq1m86927ij_gBQ1t2vEikRx40

CMD ["python", "app.py"]
