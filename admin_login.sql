/*
Navicat MySQL Data Transfer

Source Server         : 1270.0.1
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : admin_login

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-04-21 17:42:36
*/

create database admin_login;
use admin_login;
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for adminlogin
-- ----------------------------
DROP TABLE IF EXISTS `adminlogin`;
CREATE TABLE `adminlogin` (
  `ID_admin` char(20) NOT NULL,
  `password` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of adminlogin
-- ----------------------------
INSERT INTO `adminlogin` VALUES ('1001', '0001');
INSERT INTO `adminlogin` VALUES ('1002', '0002');
