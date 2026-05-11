pipeline {
    agent any

    stages {
        stage('Checkout & Clean') {
            steps {
                // 1. Wipe the old folder and pull fresh code from Git
                cleanWs()
                checkout scm
            }
        }

        stage('Build Images') {
            steps {
                script {
                    echo 'Building fresh images from Git...'
                    // --no-cache forces Docker to ignore old saved layers
                    sh 'docker build --no-cache -t my-api-1 ./api_1'
                    sh 'docker build --no-cache -t my-api-2 ./api_2'
                    sh 'docker build --no-cache -t my-api-3 ./api_3'
                    sh 'docker build --no-cache -t my-ui ./frontend'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Force cleaning old containers...'
                    sh 'docker rm -f ui api_1 api_2 api_3 || true'

                    echo 'Launching fresh Containers...'
                    sh 'docker run -d --name api_1 -p 8001:5000 my-api-1'
                    sh 'docker run -d --name api_2 -p 8002:5000 my-api-2'
                    sh 'docker run -d --name api_3 -p 8003:8003 my-api-3'
                    sh 'docker run -d --name ui -p 80:80 my-ui'
                }
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
