pipeline {
    agent any

    environment {
        IMAGE_NAME = 'nikhilesh000007/flask-app'
        DEPLOY_REPO = 'https://github.com/Nikhileshbadam/manifest.git'
    }

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
                sh """
                    docker build -t ${IMAGE_NAME}:${GIT_COMMIT} .
                """
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

                        docker push "$IMAGE_NAME:$GIT_COMMIT"

                        docker logout
                    '''
                }
            }
        }

        stage('Update Kubernetes Manifest') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'github_cred_manifest',
                        usernameVariable: 'GITHUB_USERNAME',
                        passwordVariable: 'GITHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        rm -rf deployment-repo

                        git clone https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/Nikhileshbadam/manifest.git deployment-repo

                        cd deployment-repo

                        git config user.name "Nikhileshbadam"
                        git config user.email "nikhilbadam24@gmail.com"

                        sed -i "s|image: nikhilesh000007/flask-app:.*|image: nikhilesh000007/flask-app:${GIT_COMMIT}|" deploy.yaml

                        echo "Updated deploy.yaml:"
                        cat deploy.yaml

                        git add deploy.yaml

                        git diff --cached --quiet || git commit -m "Update flask-app image to ${GIT_COMMIT}"

                        git push origin HEAD
                    '''
                }
            }
        }
    }
}
