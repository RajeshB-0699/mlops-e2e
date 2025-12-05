pipeline {
    agent any
    
    environment {
        VENV_DIR
    }

    stages {
        
        stage ('Clone Repository') {
            steps {
                script {
                    echo 'Cloning Repo...'
                    checkout scmGit(branches: [[name: '*/Main']], extensions: [], userRemoteConfigs: [[credentialsId: 'e2e-mlops', url: 'https://github.com/RajeshB-0699/mlops-e2e.git']]) 
                }
            }
        }

        stage ('Lint and Tests') {
            steps {
                script {
                    echo 'Testing & Linting'
                    echo "Installing all deps"
                    sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
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