CREATE DATABASE bookstore;
CREATE USER bookstoreAdmin WITH PASSWORD 'bookstoreAdmin123';
GRANT ALL PRIVILEGES ON DATABASE bookstore TO bookstoreAdmin;
ALTER DATABASE bookstore OWNER TO bookstoreAdmin;