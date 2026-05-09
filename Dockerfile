# starting environment
FROM python:3.11-slim
# working directory inside the container
WORKDIR /app

RUN pip install --no-cache-dir torch==2.3.0 --index-url https://download.pytorch.org/whl/cpu
# copying the requirements file to the container and installing the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# copying the rest of the application code to the container
COPY . .
# exposing the port that the application will run on
EXPOSE 8000
# command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
