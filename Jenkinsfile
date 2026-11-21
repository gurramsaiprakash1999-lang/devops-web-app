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
                    export KUBECONFIG=/var/lib/jenkins/.kube/config
                    export PATH=$PATH:/usr/local/bin
                    minikube image load webapp:latest
                    kubectl apply -f k8s-deployment.yaml
                    kubectl rollout status deployment/webapp-deployment --timeout=60s
                    pkill -f "port-forward" || true
                    nohup kubectl port-forward --address 0.0.0.0 service/webapp-service 30300:5000 > /dev/null 2>&1 &
                '''
            }
        }
    }
}
