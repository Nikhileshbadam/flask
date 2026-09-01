pipeline {
    agent any

    stages {
        stage('Checkout happend') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                echo 'GitHub webhook triggered Jenkins!'
                echo "Commit: ${env.GIT_COMMIT}"
                echo "Branch: ${env.GIT_BRANCH}"
            }
        }
    }
}
