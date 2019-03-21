# Env
Ubuntu server 18.04 vm:
```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install git ansible prips
mkdir exercise && cd exercise
git clone https://github.com/mendo1024/pannet.git
```
# Exercies 1
```
cd pannet/exercise1/ansible
ansible-playbook weather.yml
cd ../../..
sudo docker build -t weather:dev .
sudo docker run --rm -e OPENWEATHER_API_KEY="c09cfd8b571a86deaed5e5c4b578169e" -e CITY_NAME="Honolulu" weather:dev
sudo grep openweather /var/log/syslog
```
# Exercise 2
```
cd pannet/exercise2
chmod 0700 scanner
./scanner 192.168.1.204 192.168.1.206
or
./scanner 192.168.1.204
```
