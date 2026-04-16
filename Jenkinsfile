pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/nikhilkrtpm3-hash/pytest_project'
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest -v'
            }
        }
    }
}