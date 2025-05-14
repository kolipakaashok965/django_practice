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
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    cd web_app_test
                    python manage.py test
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }
        
        stage('Run Docker Container') {
            steps {
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d -p 8000:8000 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}
                    sleep 10
                    curl http://localhost:8000/apiviews/info/
                '''
            }
        }
    }
    
    post {
        always {
            sh 'docker stop ${CONTAINER_NAME} || true'
            sh 'docker rm ${CONTAINER_NAME} || true'
            cleanWs()
        }
    }
} 