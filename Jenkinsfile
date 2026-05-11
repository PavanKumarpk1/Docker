pipeline {
    agent any

    stages {
        stage('Deploy All Services') {
            steps {
                script {
                    echo 'Cleaning up old containers...'
                    // We use '|| true' so the pipeline doesn't fail if the containers don't exist yet
                    sh 'docker stop api_1 api_2 api_3 ui || true'
                    sh 'docker rm api_1 api_2 api_3 ui || true'

                    echo 'Building Images...'
                    sh 'DOCKER_BUILDKIT=0 docker build -t my-api-1 ./api_1'
                    sh 'DOCKER_BUILDKIT=0 docker build -t my-api-2 ./api_2'
                    sh 'DOCKER_BUILDKIT=0 docker build -t my-api-3 ./api_3'
                    sh 'DOCKER_BUILDKIT=0 docker build -t my-ui ./frontend'

                    echo 'Launching Containers...'
                    // Launching them individually to match your compose setup
                    sh 'docker run -d --name api_1 -p 8001:5000 -v shared_storage:/data my-api-1'
                    sh 'docker run -d --name api_2 -p 8002:5000 -v shared_storage:/data my-api-2'
                    sh 'docker run -d --name api_3 -p 8003:8003 my-api-3'
                    sh 'docker run -d --name ui -p 80:80 my-ui'
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
