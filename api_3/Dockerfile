FROM python:3.9-slim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Ensure the database file exists and has permissions
RUN touch db.json && chmod 666 db.json
EXPOSE 8003
CMD ["python", "main.py"]
