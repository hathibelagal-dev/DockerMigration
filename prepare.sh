sudo docker rmi v2x:latest
sudo docker rmi v2xlarge:latest

cd docker/small
sudo docker build --tag v2x .

cd ../large
sudo docker build --tag v2xlarge .

sudo docker run -d --name v2x v2x:latest
sudo docker run -d --name v2xlarge v2xlarge:latest

