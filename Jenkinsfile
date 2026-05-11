pipeline {
    agent any

    stages {
        stage('Deploy All Services') {
            steps {
                script {
                    echo 'Force cleaning old containers...'
                    sh 'docker rm -f ui api_1 api_2 api_3 || true'

                    echo 'Launching Containers...'
                    sh 'docker run -d --name api_1 -p 8001:5000 my-api-1'
                    sh 'docker run -d --name api_2 -p 8002:5000 my-api-2'
                    
                    // THIS IS THE MISSING LINE:
                    sh 'docker run -d --name api_3 -p 8003:8003 my-api-3'
                    
                    sh 'docker run -d --name ui -p 80:80 my-ui'
                }
            }
        }
        }

        stage('Final Verification') {
            steps {
                sh 'docker ps'
                echo 'All services, including the new API_3, are now running!'
            }
        }
    }
}
