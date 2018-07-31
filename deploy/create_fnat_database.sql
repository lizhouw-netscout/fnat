CREATE DATABASE IF NOT EXISTS fnat_base;

USE fnat_base;

CREATE TABLE IF NOT EXISTS fnat_execution(
    exec_id       BIGINT    NOT NULL PRIMARY KEY AUTO_INCREMENT,
    build_number  CHAR(100) NOT NULL,
    start_time    DATETIME  NOT NULL,
    serial_no     CHAR(20)  NOT NULL,
    config        SMALLINT  NOT NULL DEFAULT 0,
    log_location  CHAR(100) NOT NULL,
    logcat_status CHAR      NOT NULL DEFAULT 0,
    dmesg_status  CHAR      NOT NULL DEFAULT 0,
    serial_status CHAR      NOT NULL DEFAULT 0,
    hostname      CHAR(50));

CREATE TABLE IF NOT EXISTS fnat_case_result(
    record_id     BIGINT    NOT NULL PRIMARY KEY AUTO_INCREMENT,
    exec_id       BIGINT    NOT NULL,
    case_name     CHAR(80)  NOT NULL,
    purpose       TEXT,
    steps         TEXT,
    exp_result    TEXT,
    start_time    DATETIME  NOT NULL,
    end_time      DATETIME,
    logcat_fn     CHAR(100),
    dmesg_fn      CHAR(100),
    serial_fn     CHAR(100),
    verdict       CHAR      NOT NULL);

USE mysql;

UPDATE user SET Host = '%' WHERE user = 'root';
GRANT ALL on *.* to 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
flush privileges;
