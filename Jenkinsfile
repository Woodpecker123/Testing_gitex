pipeline {
  agent any
  stages {
    
    // First stage: Print a message
    stage('Hello') {
      steps {
        echo 'Hi There please work'
      }
    }
     stage('Setup') {
            steps {
                script {
                    // Define variables
                    env.HOST = "http://sit.woodpecker.com"
                    env.USERNAME = "akash"
                    env.PASSWORD = "akash@2024"
                }
            }
        }
  
    stages {
        stage('Install Virtualenv') {
            steps {
                script {
                    // Update pip
                    sh 'pip3 install --upgrade pip'
                    
                    // Install virtualenv for the user
                    sh 'pip3 install --user virtualenv'
                    
                    // Optionally create and activate a virtual environment
                    // Uncomment the following lines if needed
                    // sh 'python3 -m venv myenv'
                    // sh 'source myenv/bin/activate'
                }
            }
        }
