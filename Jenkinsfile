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
                    kubectl rollout restart deployment/webapp-deployment
                    kubectl rollout status deployment/webapp-deployment --timeout=60s
                    pkill -f "port-forward" || true
                    nohup kubectl port-forward --address 0.0.0.0 service/webapp-service 30300:5000 > /dev/null 2>&1 &
                '''
            }
        }
    }
    post {
        always {
            withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                sh '''
                    COMMIT_HASH=$(git rev-parse HEAD)
                    
                    for CONTEXT in "default" "continuous-integration/jenkins" "continuous-integration/jenkins/branch" "ci/jenkins/build-status"; do
                      curl -s -X POST \
                        -H "Authorization: Bearer $GITHUB_TOKEN" \
                        -H "Accept: application/vnd.github.v3+json" \
                        https://api.github.com/repos/gurramsaiprakash1999-lang/devops-web-app/statuses/$COMMIT_HASH \
                        -d "{\\"state\\": \\"success\\", \\"target_url\\": \\"http://44.200.158.91:8080\\", \\"description\\": \\"Cloud Hub Application Deployed\\", \\"context\\": \\"$CONTEXT\\"}"
                    done
                '''
            }
        }
    }
}
