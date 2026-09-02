pipeline {
    agent any

    stages {
        stage('Checkout happened') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'GitHub webhook triggered Jenkins!'
                echo "Commit: ${env.GIT_COMMIT}"
                echo "Branch: ${env.GIT_BRANCH}"

                sh 'docker --version'
                sh "docker build -t flask-app:${env.GIT_COMMIT} ."
            }
        }
    }
}
