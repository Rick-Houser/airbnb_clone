CREATE USER 'airbnb_user_test'@'%' IDENTIFIED By '636881922Hazmat';

CREATE DATABASE airbnb_test
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON airbnb_test . * TO 'airbnb_user_test';

FLUSH PRIVILEGES;
