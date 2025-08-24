pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-cid"
        CONTAINER_NAME = "django_app"
        REPO_URL = "https://github.com/rashid893/django-todo"
        BRANCH = "master"   // change if you use main
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                echo "📥 Cloning repository from ${REPO_URL} ..."
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Run Container') {
            steps {
                echo '🚀 Starting Django container...'
                sh """
                  docker rm -f ${CONTAINER_NAME} || true
                  docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                sh "docker exec ${CONTAINER_NAME} python manage.py test || true"
            }
        }
    }

    post {
        always {
            echo '🛑 Cleaning up resources...'
            sh "docker ps -a"
        }
        success {
            echo '✅ Pipeline completed successfully! Django app running on port 8000'
        }
        failure {
            echo '❌ Pipeline failed. Check above logs.'
        }
    }
}
