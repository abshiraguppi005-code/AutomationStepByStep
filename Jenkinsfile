pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
                            .venv\\Scripts\\python -m pytest -o addopts="--html=report1.html --self-contained-html" --headless
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html, reports/**/*.xml, screenshots/**/*', allowEmptyArchive: true
            junit allowEmptyResults: true
        }
    }
}
