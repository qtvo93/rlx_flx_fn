FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port number the app runs on
EXPOSE 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "main.py"]
