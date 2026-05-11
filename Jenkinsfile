pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Source code pulled successfully.'
            }
        }

        stage('Build & Deploy') {
            steps {
                script {
                    // We switch to 'docker compose' (no hyphen) 
                    // This uses the Docker CLI plugin which is standard in modern Docker installs
                    sh 'DOCKER_BUILDKIT=0 docker compose up -d --build'
                }
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
                echo 'Deployment successful using Docker Compose V2!'
            }
        }
    }
}
