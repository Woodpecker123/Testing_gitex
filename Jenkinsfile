pipeline {
  agent any
  stages {
    
    // First stage: Print a message
    stage('Hello') {
      steps {
        echo 'Hi There please work'
      }
    }

    // Second stage: Run a Python script
    stage('Run Python Script') {
      steps {
        script {
          // Run the Python script using Python 3
          sh 'python3 score1.py'
        }
      }
    }
    
  }
}
