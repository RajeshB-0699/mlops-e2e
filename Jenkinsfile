pipeline {
    agent any

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
                    python -m venv menv
                    . menv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                    sh ''' 
                    . menv/bin/activate
                    pylint app.py train.py --output=pylint-report.txt --exit-zero
                    flake8 app.py train.py --ignore=E501,E302 --output-file=flake8-report.txt
                    black app.py train.py
                    '''
                }
            }
        }


        stage ('Pytest Tests') {
            steps {
                script {
                    echo 'Pytests test cases'
                    
                    sh ''' 
                    . menv/bin/activate
                    pytest tests/
                    '''
                }
            }
        }

        stage ('Trivy File System') {
            steps {
                script {
                    echo 'Scanning File System'
                    sh '''
                    . menv/bin/activate
                    trivy fs . --format table -o trivy-fs-report.html
                    '''
                }
            }
        }

        stage ('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Images'
                    echo 'Starting'
                    sh "docker build -t my-app-mlops-01"
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