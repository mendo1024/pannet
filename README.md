# exercise 1
clone this repo on Ubuntu 18.04
cd Exercise1

docker build -t weather:dev .
docker run --rm -e OPENWEATHER_API_KEY="c09cfd8b571a86deaed5e5c4b578169e" -e CITY_NAME="Honolulu" weather:dev

