CREATE DATABASE IF NOT EXISTS sqlhelper;
USE sqlhelper;

-- 系统信息表
CREATE TABLE IF NOT EXISTS system_management (
    id INT AUTO_INCREMENT PRIMARY KEY,
    system_name VARCHAR(255) NOT NULL UNIQUE,
    owner VARCHAR(255),
    description TEXT,
    created_at DATETIME,
    updated_at DATETIME
);

-- 数据库信息表
CREATE TABLE IF NOT EXISTS database_management (
    id INT AUTO_INCREMENT PRIMARY KEY,
    system_id INT NOT NULL,
    database_name VARCHAR(255) NOT NULL,
    creator VARCHAR(255) NOT NULL DEFAULT 'KILLIAN',
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    description VARCHAR(255),
    surf VARCHAR(255) NOT NULL,
    software VARCHAR(255) NOT NULL DEFAULT 'MYSQL',
    UNIQUE(system_id, database_name)
);

-- 数据表信息表
CREATE TABLE IF NOT EXISTS table_management (
    id INT AUTO_INCREMENT PRIMARY KEY,
    database_id INT NOT NULL,
    table_name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    creator VARCHAR(255) NOT NULL DEFAULT 'KILLIAN',
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    status VARCHAR(10) NOT NULL,
    UNIQUE(database_id, table_name)
);

-- 字段信息表
CREATE TABLE IF NOT EXISTS field_management (
    id INT AUTO_INCREMENT PRIMARY KEY,
    database_id INT NOT NULL,
    table_id INT NOT NULL,
    field_name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    type VARCHAR(50) NOT NULL,
    length INT UNSIGNED,
    creator VARCHAR(255) NOT NULL DEFAULT 'KILLIAN',
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    is_null ENUM('Y', 'N') NOT NULL,
    is_key ENUM('PRIMARY', 'FOREIGN', 'UNIQUE', '') DEFAULT '',
    default_value VARCHAR(50),
    UNIQUE(table_id, field_name)
);

-- 字段枚举值表
CREATE TABLE IF NOT EXISTS field_enum (
    id INT AUTO_INCREMENT PRIMARY KEY,
    field_id INT NOT NULL,
    enum_value VARCHAR(50) NOT NULL,
    enum_label VARCHAR(100),
    UNIQUE(field_id, enum_value)
);

-- 通用变更记录表
CREATE TABLE IF NOT EXISTS change_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    target_type ENUM('system', 'database', 'table', 'field') NOT NULL,
    target_id INT NOT NULL,
    action ENUM('create', 'update', 'delete') NOT NULL,
    description TEXT,
    performed_by VARCHAR(255),
    performed_at DATETIME NOT NULL
);