
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv jenkins-venv
                    jenkins-venv/bin/python -m pip install --upgrade pip
                    jenkins-venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh 'jenkins-venv/bin/python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-fitness:jenkins .'
            }
        }
    }

    post {
        always {
            echo 'ACEest Fitness CI/CD pipeline completed'
        }
    }
}
