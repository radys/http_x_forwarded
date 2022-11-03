docker image build -t flask_docker .
docker run -p 5000:5000 -d --rm --name flask flask_docker
