-- create user
CREATE User IF NOT EXISTS 'sammy'@'localhost';
SET PASSWORD FOR 'sammy'@'localhost'="password";
GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost';
FLUSH PRIVILEGES;
