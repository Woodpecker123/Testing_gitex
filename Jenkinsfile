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
   stage('Install virtualenv') {
            steps {
                sh 'pip3 install virtualenv'
                sh 'virtualenv -p python3 venv'  // Install virtualenv
            }
        }

            
  }
}
