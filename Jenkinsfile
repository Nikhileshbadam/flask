pipeline {
    agent any

    stages {
        stage('Checkout') {
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
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t nikhilesh000007/flask-app:${env.GIT_COMMIT} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub_cred',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login \
                            -u "$DOCKER_USERNAME" \
                            --password-stdin

                        docker push nikhilesh000007/flask-app:$GIT_COMMIT

                        docker logout
                    '''
                }
            }
        }
    }
}
