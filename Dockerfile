# 1. Use an official, lightweight Python image as the base
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements file first (this helps with Docker caching)
COPY requirements.txt .

# 4. Install the Python dependencies
# --no-cache-dir keeps the image size small
RUN pip install --no-cache-dir -r requirements.txt

# (Optional but recommended) Install Gunicorn explicitly if it's not in your requirements.txt
RUN pip install gunicorn uvicorn

# 5. Copy the rest of your application code and your ML model into the container
COPY . .

# 6. Tell Docker which port the container will listen on
EXPOSE 8000

# 7. Start the app using Gunicorn with Uvicorn workers to handle multiple concurrent users
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app:app", "--bind", "0.0.0.0:8000"]