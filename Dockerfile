# 1. Use official Python base image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory
WORKDIR /app

# 4. Install dependencies
#COPY requirements.txt .
RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
RUN pip install django

# 5. Copy all project files
COPY . .

# 6. Expose port
EXPOSE 8000

# 7. Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
