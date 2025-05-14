/**
 * Owner: Ashok
 * Date: 2024-03-19
 */

pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'django-practice'
        CONTAINER_NAME = 'django-app'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                bat '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                bat '''
                    cd web_app_test
                    python manage.py test
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }
        
        stage('Run Docker Container') {
            steps {
                bat '''
                    docker stop %CONTAINER_NAME% || exit 0
                    docker rm %CONTAINER_NAME% || exit 0
                    docker run -d -p 8000:8000 --name %CONTAINER_NAME% %DOCKER_IMAGE%
                    timeout /t 10
                    curl http://localhost:8000/apiviews/info/
                '''
            }
        }
    }
    
    post {
        always {
            bat 'docker stop %CONTAINER_NAME% || exit 0'
            bat 'docker rm %CONTAINER_NAME% || exit 0'
            cleanWs()
        }
    }
} 