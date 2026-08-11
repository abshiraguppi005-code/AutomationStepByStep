pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python -m venv .venv
                            . .venv/bin/activate
                            python -m pip install --upgrade pip
                            python -m pip install -r requirements.txt
                            python -m playwright install --with-deps
                        '''
                    } else {
                        bat '''
                            python -m venv .venv
                            .venv\\Scripts\\python -m pip install --upgrade pip
                            .venv\\Scripts\\python -m pip install -r requirements.txt
                            .venv\\Scripts\\python -m playwright install --with-deps
                        '''
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . .venv/bin/activate
                            python -m pytest -o addopts="--html=report.html --self-contained-html" --headless --junitxml=reports/junit.xml
                        '''
                    } else {
                        bat '''
                            .venv\\Scripts\\python -m pytest -o addopts="--html=report.html --self-contained-html" --headless --junitxml=reports/junit.xml
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html, reports/**/*.xml, screenshots/**/*', allowEmptyArchive: true
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
        }
    }
}
