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
    stage('Prepare Python Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python -m venv venv'
                    // Activate the virtual environment and install requirements
                    sh '''
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }
    
  }
}
