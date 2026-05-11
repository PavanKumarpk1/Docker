pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                // Jenkins handles the 'checkout' automatically if using SCM mode
                echo 'Source code pulled successfully.'
            }
        }

        stage('Build & Deploy') {
            steps {
                // This builds your image and starts the container on the VM
                sh 'DOCKER_BUILDKIT=0 COMPOSE_DOCKER_CLI_BUILD=0 docker-compose up -d --build'
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
                echo 'The new version is officially live!'
            }
        }
    }
}
