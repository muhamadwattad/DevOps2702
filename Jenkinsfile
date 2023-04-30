properties([pipelineTriggers([githubPush()])])
node{
    stage("clone"){
        git branch: 'my-branch', url: 'https://github.com/muhamadwattad/DevOps2702'
    }
    stage("execute"){
        bat "dir"
        bat "python disk_resizer.py"
    }
}
