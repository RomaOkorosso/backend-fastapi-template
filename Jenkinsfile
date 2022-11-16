pipeline {
    agent any

    environment {
        PATH = "$PATH:/usr/local/bin"
    }

    stages {
        stage("Build dev") {
            when {
                branch 'master'
            }
            environment {
                BACKEND_PORT = '4000'
                POSTGRES_DATA = '/project/data/postgres/data'
                POSTGRES_PORT = '5432'
                BACKEND_ENV_ID = 'env-prod' // env-prod || env-dev
            }
            steps {
                buildBackend(BACKEND_ENV_ID)
                deployBackend()
            }
        }

        stage("Build stage-dev") {
            when {
                branch 'dev'
            }
            environment {
                BACKEND_PORT = '4001'
                POSTGRES_DATA = '/home/priority2030-backend/data/postgres-dev/data'
                POSTGRES_PORT = '5431'
                BACKEND_ENV_ID = 'env-dev' // env-prod || env-dev
            }
            steps {
                buildBackend(BACKEND_ENV_ID)
                deployBackend()
            }
        }
    }
}

def deployBackend() {
    echo "Stopping previous container..."
    sh "docker-compose down"
    echo "Deploying..."
    sh "docker-compose up -d"
    echo "Deployed!"
}

def buildBackend(envID) {
    withCredentials([
        file(credentialsId: envID, variable: 'ENV'),
    ]) {
        echo "Creating .env"
        sh "rm -f .env"
        sh "cp $ENV .env"
    }

    withCredentials([
        gitUsernamePassword(credentialsId: '33348f45-74d8-449e-b7e3-e93bbba3033d', gitToolName: 'git-tool')
    ]) {
        echo "Submodules update"
        sh 'cd submodules && git submodule init && git submodule update'
    }

    echo "Building..."
    sh "docker-compose build"
    echo "Built!"
}