string LABEL = 'jenkins-' + org.apache.commons.lang.RandomStringUtils.random(9, true, true)

pipeline {
    agent {
        kubernetes {
            label LABEL
            defaultContainer 'jnlp'
            yamlFile "jenkins.yaml"
        }
    }
    stages {
        stage('Run tests and code checks') {
            when { not { tag '*' } }
            steps {
                container('py35') {
                    sh "cp -r /jenkins-config/.config /home/jenkins/"
                    sh "cp -r /jenkins-config/.pypirc /home/jenkins/"

                    sh "tox -e py35"
                    publishHTML (target: [
                        allowMissing: false,
                        reportDir: 'coveragedir',
                        reportFiles: 'index.html',
                        reportName: 'HTML Coverage report'
                    ])
                    cobertura (
                        coberturaReportFile: 'coverage.xml',
                        autoUpdateHealth: false,
                        autoUpdateStability: false,
                        failUnhealthy: false,
                        failUnstable: false,
                        lineCoverageTargets: '80, 0, 0',
                        maxNumberOfBuilds: 0,
                        onlyStable: false,
                        sourceEncoding: 'ASCII',
                        zoomCoverageChart: false
                    )
                    junit 'pytest.xml'
                }
            }
        }
        stage('Deploy') {
            when { tag '*' }
            steps {
                container('py35-light') {
                    sh "cp -r /jenkins-config/.config /home/jenkins/"
                    sh "cp -r /jenkins-config/.pypirc /home/jenkins/"
                    script {
                        env.PYPI_VERSION = sh(script: "grep \"^\\s\\+version \\?= \\?\" setup.py | sed -e \"s/.*version \\?= \\?['\\\"]\\(.\\+\\)['\\\"].*/\\1/\"", returnStdout: true).trim()
                    }
                    sh "python3 setup.py sdist upload -r pypicloud"
                }
            }
        }
    }
    post {
        always {
            script {
                env.GIT_SHORT_COMMIT = env.GIT_COMMIT.substring(0, 8)
                env.GIT_MESSAGE = sh(returnStdout: true, script: "git log --format=%B -n 1 ${env.GIT_COMMIT}")
                env.GIT_AUTHOR = sh(returnStdout: true, script: "git show -s --format=\"%aN\" ${env.GIT_COMMIT}")
                switch ( currentBuild.currentResult ) {
                    case "SUCCESS":
                        env.COLOR = "#859900"
                        break
                    case "UNSTABLE":
                        env.COLOR = "#cb4b16"
                        break
                    case "FAILURE":
                        env.COLOR = "#dc322f"
                        break
                }
            }
            slackSend channel: '#jenkins', color: "${env.COLOR}", failOnError: true, message: "<${env.BUILD_URL}|${env.JOB_NAME}> [build ${env.BUILD_NUMBER}] - ${currentBuild.currentResult}\nCommit ${env.GIT_SHORT_COMMIT} by ${env.GIT_AUTHOR}\n${env.GIT_MESSAGE}"
        }
    }
}
