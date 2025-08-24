pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-cid"
        CONTAINER_NAME = "django_app"
        REPO_URL = "https://github.com/rashid893/django-todo"
        BRANCH = "master"
        SONARQUBE_ENV = "MySonarQube"   // must match the SonarQube server name in Jenkins
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Run Container') {
            steps {
                sh """
                  docker rm -f ${CONTAINER_NAME} || true
                  docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh "docker exec ${CONTAINER_NAME} python manage.py test || true"
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    script {
                        def scannerHome = tool 'sonar-scanner'   // must match the name in Global Tool Config
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        always {
            sh "docker ps -a"
        }
        success {
            echo '✅ Pipeline + SonarQube scan completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
