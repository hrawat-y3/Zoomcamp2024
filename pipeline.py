print("\n\n HELLO IM HERE \n\n")

docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v ny_taxi_data:$(pwd)\var\lib\postgresql\data -p 5432 postgres:13

pgcli -h 172.17.0.2 -p 5432 -u root -d ny_taxi