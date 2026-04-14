pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "rushikesh2022bcs0151/wine-api:latest"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                apt update
                apt install -y python3 python3-venv python3-pip

                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate
                python3 scripts/train.py
                echo "Name: RUSHIKESH"
                echo "Roll No: 2022BCS0151"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_PASS')]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u rushikesh2022bcs0151 --password-stdin
                    docker push $DOCKER_IMAGE
                    '''
                }
            }
        }
    }
}
