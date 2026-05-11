pipeline {
    agent any

    environment {
        // Adds common install locations to the PATH so Jenkins can find docker-compose
        PATH = "/usr/local/bin:/usr/bin:/bin:${env.PATH}"
    }

    stages {
        stage('Clone') {
            steps {
                echo 'Source code pulled successfully.'
            }
        }

        stage('Build & Deploy') {
            steps {
                script {
                    // Using 'sh' with the explicit path check
                    sh 'DOCKER_BUILDKIT=0 COMPOSE_DOCKER_CLI_BUILD=0 docker-compose up -d --build'
                }
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
                echo 'Deployment of API_1, API_2, and API_3 is complete!'
            }
        }
    }
}
