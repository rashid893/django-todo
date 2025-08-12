# 1. Use official Python base image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory
WORKDIR /app

# 4. Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Install Python dependencies
RUN pip install --upgrade pip
RUN pip install django psycopg2-binary

# 6. Copy all project files
COPY . .

# 7. Expose port
EXPOSE 8000

# 8. Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]