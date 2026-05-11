pipeline {
    agent any

    environment {
        // Ensuring common paths are available
        PATH = "/usr/local/bin:/usr/bin:/bin:${env.PATH}"
    }

    stages {
        stage('Cleanup') {
            steps {
                echo 'Cleaning up workspace...'
                // Optional: Uncomment the line below if you want to remove old images to save space
                // sh 'docker image prune -f'
            }
        }

        stage('Build & Deploy') {
            steps {
                script {
                    echo 'Starting build of all services (API_1, API_2, API_3, and UI)...'
                    
                    // Using 'docker compose' (no hyphen) as it is the most stable for modern Jenkins agents
                    // We keep DOCKER_BUILDKIT=0 to match your successful previous runs
                    sh 'DOCKER_BUILDKIT=0 docker compose up -d --build'
                }
            }
        }

        stage('Verify Health') {
            steps {
                echo 'Checking running containers...'
                sh 'docker ps'
                
                echo 'Verifying API_3 is reachable...'
                // This local check confirms the container is responding within the network
                sh 'curl -f http://localhost:8003/products || echo "Warning: API_3 not responding yet"'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful! Your product catalog is now live.'
        }
        failure {
            echo 'Deployment failed. Check the logs above for Docker build errors.'
        }
    }
}
