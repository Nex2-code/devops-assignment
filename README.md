# devops-assignment

## Python Flask, Hello World 

.env file is for testing and practice purpose. Better practice is to add .env into your machine directly Dont save it in repository.
Dockerfile uses alpine:python as base (it uses less space) runs app.py on route localhost port 80. Prints Hello, World + the text mentioned in env

Example: .env [WORD=hiii] , Output: [Hello,World hiii]

The workflow check and linit [using codeQL and linit(python black,flake8)] the code whenever the code is pushed to master or merged And it starts the Docker build to upload the image to Amazon ECR.
Image is pulled into Amazon ECS on EC2 get deployed.
