pipeline {
    agent any

    stages {
        
        stage ('Clone Repository') {
            steps {
                script {
                    echo 'Cloning Repo...'
                }
            }
        }

        stage ('Lint and Tests') {
            steps {
                script {
                    echo 'Testing & Linting'
                }
            }
        }

        stage ('Trivy File System') {
            steps {
                script {
                    echo 'Scanning File System'
                }
            }
        }

        stage ('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Images'
                }
            }
        }

        stage ('Push Docker Image') {
            steps {
                script {
                    echo 'Pushing Docker Image to DockerHub'
                }
            }
        }

        stage ('Deploy') {
            steps {
                script {
                    echo 'Deploying to Production'
                }
            }
        }
    }
}