pipeline {
    agent any

    stages {
        stage('pull') {
            steps {

            checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'd395f040-8080-4e8d-9eaa-7c6266134195', url: 'https://github.com/abbygo/Homework.git']]])

            }
        }
        stage('code check') {
            steps {

                script{
                    scannerHome=tool ''

                }
                withSonarQubeEnv(''){
                 sh "$(s)"
                }
            }
        }
    }

}
