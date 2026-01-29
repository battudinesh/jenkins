pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/battudinesh/Jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        // stage('Stop Old FastAPI') {
        //     steps {
        //         bat '''
        //         netstat -ano | findstr :8000 > pid.txt
        //         if %errorlevel%==0 (
        //             for /f "tokens=5" %%a in (pid.txt) do taskkill /PID %%a /F
        //         ) else (
        //             echo FastAPI not running
        //         )
        //         '''
        //     }
        // }

        stage('Start FastAPI') {
            steps {
                bat '''
                start "" cmd /c "venv\\Scripts\\uvicorn main:app --host 0.0.0.0 --port 8000"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Auto-deploy successful"
        }
        failure {
            echo "❌ Auto-deploy failed"
        }
    }
}
