pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/gurramsaiprakash1999-lang/devops-web-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t webapp:latest .'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    export PATH=$PATH:/usr/local/bin
                    minikube status || minikube start --driver=docker --force
                    kubectl apply -f k8s-deployment.yaml
                '''
            }
        }
    }
}
