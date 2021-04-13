DROP DATABASE IF EXISTS  isy;
DROP USER IF EXISTS  sejong;
create user sejong identified WITH mysql_native_password  by 'sejong';
create database isy;
grant all privileges on isy.* to sejong with grant option;
commit;

USE isy;

CREATE TABLE EXAM (
  id INTEGER PRIMARY KEY,
  subject_name VARCHAR(20),
  start_date DATETIME,
  end_date DATETIME
);

CREATE TABLE STUDENT (
  id INTEGER PRIMARY KEY,
  name VARCHAR(20)
);

CREATE TABLE EXAM_STUDENT (
 exam_id INTEGER,
 student_id INTEGER,
 clipboard VARCHAR(255),
 accept_face BOOLEAN,
 accept_idcard BOOLEAN,
 PRIMARY KEY (exam_id, student_id),
 FOREIGN KEY (exam_id) REFERENCES EXAM(id),
 FOREIGN KEY (student_id) REFERENCES STUDENT(id)
);

CREATE TABLE IMAGE (
  id INTEGER PRIMARY KEY,
  student_id INTEGER,
  file VARCHAR(40),
  FOREIGN KEY (student_id) REFERENCES STUDENT(id)
);

CREATE TABLE LOG (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  exam_id INTEGER,
  student_id INTEGER,
  time DATETIME,
  error_type INTEGER,
  data VARCHAR(40),
  remarks VARCHAR(20),
  FOREIGN KEY (exam_id) REFERENCES EXAM(id),
  FOREIGN KEY (student_id) REFERENCES STUDENT(id)
);

CREATE TABLE TA (
	id INTEGER PRIMARY KEY,
    ta_id VARCHAR(11),
    pw_code INTEGER
);

CREATE TABLE EXAM_TA (
	exam_id INTEGER,
	ta_id INTEGER,
	PRIMARY KEY (exam_id, ta_id),
	FOREIGN KEY (exam_id) REFERENCES EXAM(id),
	FOREIGN KEY (ta_id) REFERENCES TA(id)
);

commit;