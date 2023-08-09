pipeline {
    agent any
    
    environment {
        DOCKER_HUB_USERNAME = credentials('docker-hub-username')
        DOCKER_HUB_PASSWORD = credentials('docker-hub-password')
        IMAGE_NAME = 'pizza-app'
        DOCKERHUB_REPO = 'nashpaz123/pizza-app'
    }

    stages {
        stage('Checkout') {
            steps {
                // play with checkout e.g several sources or fetch logic
            }
        }
		stage('unit test') {
            steps {
                // or other tests for the code or app
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', DOCKER_HUB_USERNAME, DOCKER_HUB_PASSWORD) {
                        def dockerImage = docker.build("${DOCKERHUB_REPO}:${env.BUILD_NUMBER}")
                        dockerImage.push()
                    }
                }
            }
        }
    }
    
    post {
	    succuss {
			sh """
			   docker tag "${DOCKERHUB_REPO}:${env.BUILD_NUMBER} "${DOCKERHUB_REPO}:latest
			   #and push. or set the successful tag in values/deployment yaml if integration tests were passed in CI
			"""}
        always {
            // Clean up after the build
            cleanWs()
        }
    }
}