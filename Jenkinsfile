pipeline {
    agent any

    environment {
        VENV = "venv"
        APP = "app.main:app"
        PORT = "8000"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/battudinesh/Jenkins.git'
            }
        }

        stage('Setup Virtual Env') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Stop Old FastAPI') {
            steps {
                bat '''
                for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do taskkill /PID %%a /F
                '''
            }
        }

        stage('Start FastAPI') {
            steps {
                bat '''
                start cmd /k "venv\\Scripts\\uvicorn app.main:app --host 0.0.0.0 --port 8000"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ FastAPI deployed successfully"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}
