pipeline {
    agent any

    environment {
        // This forces Jenkins to look where Docker and Compose are usually installed
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${env.PATH}"
    }

    stages {
        stage('Clone') {
            steps {
                echo 'Source code pulled successfully.'
            }
        }

        stage('Pre-Flight Check') {
            steps {
                // This checks if the Docker engine is actually reachable
                sh 'docker info || echo "ERROR: Docker socket not reachable"'
                sh 'which docker-compose || echo "ERROR: docker-compose binary not found"'
            }
        }

      stage('Build & Deploy') {
            steps {
                // Use 'docker compose' (space) instead of 'docker-compose' (hyphen)
                // This uses the built-in plugin which usually avoids permission issues
                sh 'DOCKER_BUILDKIT=0 docker compose up -d --build'
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
                echo 'The new version (including API_3) is officially live!'
            }
        }
    }
}
