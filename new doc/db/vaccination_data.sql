USE vaccination;
CREATE TABLE status (
  name CHAR(15) PRIMARY KEY,
  regno INT,
  status CHAR(3)
);
INSERT INTO student (name, regno, status) VALUES ('Magesh', 12345, 'Yes');
INSERT INTO student (name, regno, status) VALUES ('Mathesh', 123546, 'No');