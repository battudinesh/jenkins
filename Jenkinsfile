pipeline {
    agent any

    environment {
        VENV_PATH = "${WORKSPACE}\\venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/battudinesh/Jenkins.git'
            }
        }

        stage('Setup Python') {
            steps {
                script {
                    if (!fileExists("${VENV_PATH}\\Scripts\\activate")) {
                        bat "python -m venv ${VENV_PATH}"
                    }
                    bat """
                        ${VENV_PATH}\\Scripts\\pip install --upgrade pip
                        ${VENV_PATH}\\Scripts\\pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat "${VENV_PATH}\\Scripts\\pytest tests\\"
            }
        }

        stage('Start FastAPI (Optional)') {
            steps {
                bat "start cmd /c ${VENV_PATH}\\Scripts\\python -m uvicorn main:app --port 8000 --reload"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully ✅'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
