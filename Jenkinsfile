
pipeline {
    agent any

    environment {
        SONARQUBE = 'SonarQube'
    }

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

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv("${SONARQUBE}") {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=ACEest-Fitness \
                            -Dsonar.projectName='ACEest Fitness' \
                            -Dsonar.sources=application \
                            -Dsonar.tests=tests \
                            -Dsonar.python.version=3.9 \
                            -Dsonar.sourceEncoding=UTF-8
                        """
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
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
