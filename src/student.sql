/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50647
 Source Host           : 127.0.0.1:3306
 Source Schema         : student

 Target Server Type    : MySQL
 Target Server Version : 50647
 File Encoding         : 65001

 Date: 02/04/2020 20:46:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for info
-- ----------------------------
DROP TABLE IF EXISTS `info`;
CREATE TABLE `info`  (
  `sno` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `college` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `clazz` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`sno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of info
-- ----------------------------
INSERT INTO `info` VALUES (1, '张三', '女', '信息科学技术学院', '计科181');
INSERT INTO `info` VALUES (1001, 'a', '男', 'a', 'a');
INSERT INTO `info` VALUES (1002, 'b', '男', 'b', 'b');
INSERT INTO `info` VALUES (1003, 'c', '男', 'c', 'c');
INSERT INTO `info` VALUES (1004, 'd', '女', 'd', 'd');
INSERT INTO `info` VALUES (1005, 'e', '男', 'e', 'e');
INSERT INTO `info` VALUES (1006, 'f', '女', 'f', 'f');
INSERT INTO `info` VALUES (1007, 'g', '男', 'g', 'g');
INSERT INTO `info` VALUES (1008, 'h', '男', 'h', 'h');
INSERT INTO `info` VALUES (1009, 'i', '男', 'i', 'i');
INSERT INTO `info` VALUES (1010, 'j', '女', 'j', 'j');
INSERT INTO `info` VALUES (1011, 'k', '女', 'k', 'k');
INSERT INTO `info` VALUES (1012, 'l', '男', 'l', 'l');
INSERT INTO `info` VALUES (1013, 'm', '男', 'm', 'm');
INSERT INTO `info` VALUES (1014, 'n', '男', 'n', 'n');
INSERT INTO `info` VALUES (1015, 'o', '女', 'o', 'o');
INSERT INTO `info` VALUES (1016, 'p', '男', 'p', 'p');
INSERT INTO `info` VALUES (1017, 'q', '女', 'q', 'q');
INSERT INTO `info` VALUES (1018, 'r', '女', 'r', 'r');
INSERT INTO `info` VALUES (1019, 's', '女', 's', 's');
INSERT INTO `info` VALUES (1020, 't', '女', 't', 't');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`uid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'admin', '123456');

SET FOREIGN_KEY_CHECKS = 1;
