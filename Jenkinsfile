pipeline {
    agent any

    stages {
        stage('Stop Existing') {
            steps {
                script {
                    // Stop and remove old containers to avoid "name already in use" errors
                    sh 'docker stop api_1 api_2 api_3 ui || true'
                    sh 'docker rm api_1 api_2 api_3 ui || true'
                }
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker build -t my-api-1 ./api_1'
                sh 'docker build -t my-api-2 ./api_2'
                sh 'docker build -t my-api-3 ./api_3'
                sh 'docker build -t my-ui ./frontend'
            }
        }

        stage('Run Containers') {
            steps {
                // api_1 & api_2 with shared volume
                sh 'docker run -d --name api_1 -p 8001:5000 -v shared_storage:/data my-api-1'
                sh 'docker run -d --name api_2 -p 8002:5000 -v shared_storage:/data my-api-2'
                
                // api_3 (The new one)
                sh 'docker run -d --name api_3 -p 8003:8003 my-api-3'
                
                // Frontend UI
                sh 'docker run -d --name ui -p 80:80 my-ui'
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
                echo 'Deployment finished without using Docker Compose!'
            }
        }
    }
}
