pipeline {
  agent any
  stages {
    stage('Hello') {
      steps {
        echo 'Hi There please work'
      }
    }

    stage('Setup') {
      steps {
        script {
          env.HOST = "http://sit.woodpecker.com"
          env.USERNAME = "akash"
          env.PASSWORD = "akash@2024"
        }

      }
    }

  }
}