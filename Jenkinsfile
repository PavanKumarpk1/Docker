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
                    // This block finds where docker-compose is and uses it directly
                    def composePath = sh(script: "which docker-compose || echo '/usr/local/bin/docker-compose'", returnStdout: true).trim()
                    echo "Using docker-compose located at: ${composePath}"
                    
                    sh "DOCKER_BUILDKIT=0 COMPOSE_DOCKER_CLI_BUILD=0 ${composePath} up -d --build"
                }
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
                echo 'API_3 and the rest of the stack are now running!'
            }
        }
    }
}
