/**
 * Owner: Ashok
 * Date: 2024-03-19
 */

pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'django-practice'
        CONTAINER_NAME = 'django-app'
        PYTHON_PATH = 'C:\\Users\\ashok\\IdeaProjects\\django_practice\\django_env\\Scripts\\python.exe'
        PIP_PATH = 'C:\\Users\\ashok\\IdeaProjects\\django_practice\\django_env\\Scripts\\pip.exe'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Check Docker') {
            steps {
                bat 'docker --version'
            }
        }
        
        stage('Setup Python') {
            steps {
                bat '''
                    "%PYTHON_PATH%" -m pip install --upgrade pip
                    "%PIP_PATH%" install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                bat '''
                    cd web_app_test
                    "%PYTHON_PATH%" manage.py test
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