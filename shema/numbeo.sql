/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 80029
 Source Host           : localhost:3306
 Source Schema         : numbeo

 Target Server Type    : MySQL
 Target Server Version : 80029
 File Encoding         : 65001

 Date: 22/11/2022 17:54:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for categories
-- ----------------------------
DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for cities
-- ----------------------------
DROP TABLE IF EXISTS `cities`;
CREATE TABLE `cities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `country_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for countries
-- ----------------------------
DROP TABLE IF EXISTS `countries`;
CREATE TABLE `countries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=235 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for currencies
-- ----------------------------
DROP TABLE IF EXISTS `currencies`;
CREATE TABLE `currencies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for date_updates
-- ----------------------------
DROP TABLE IF EXISTS `date_updates`;
CREATE TABLE `date_updates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `last_update` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for items
-- ----------------------------
DROP TABLE IF EXISTS `items`;
CREATE TABLE `items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for price_cities
-- ----------------------------
DROP TABLE IF EXISTS `price_cities`;
CREATE TABLE `price_cities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `price` float(10,2) DEFAULT NULL,
  `price_min` float(10,2) DEFAULT NULL,
  `price_max` float(10,2) DEFAULT NULL,
  `item_id` int DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  `city_id` int DEFAULT NULL,
  `currency_id` int DEFAULT NULL,
  `date_update_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Table structure for price_countries
-- ----------------------------
DROP TABLE IF EXISTS `price_countries`;
CREATE TABLE `price_countries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `price` float(10,2) DEFAULT NULL,
  `price_min` float(10,2) DEFAULT NULL,
  `price_max` float(10,2) DEFAULT NULL,
  `item_id` int DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  `country_id` int DEFAULT NULL,
  `currency_id` int DEFAULT NULL,
  `date_update_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb3;

SET FOREIGN_KEY_CHECKS = 1;
