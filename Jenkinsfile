pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/battudinesh/Jenkins.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building FastAPI project...'
            }
        }
    }
}
