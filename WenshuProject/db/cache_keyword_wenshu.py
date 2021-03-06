#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
import redis

pl = platform.system()

if pl == "Linux":
    redis_obj = redis.Redis(host='127.0.0.1', port=6379, db=1)
else:
    redis_obj = redis.Redis(host='master', port=6379, db=1)
keys = ['债权', '查封', '冻结', '扣押', '拍卖', '变卖', '合同', '不动产', '继续履行', '变更', '驳回', '合同约定', '处分', '交付', '所有权', '第三人',
        '不履行', '清偿', '抵押', '程序合法', '担保', '土地使用权', '投资', '利息', '债权人', '和解协议', '法定期限', '给付', '动产', '强制措施', '租赁',
        '执行和解', '债务人', '财产保全', '利害关系人', '股权', '房屋买卖', '财产刑', '抵押权', '本案争议', '罚金', '管辖', '房地产开发企业', '建设工程', '债权转让',
        '贷款', '买卖合同', '分公司', '民间借贷', '迟延履行', '标的物', '风险责任', '法定代表人', '共有', '租金', '股份有限公司', '公证', '房屋所有权', '优先受偿权',
        '财产权', '保证', '婚姻', '返还', '保证金', '承诺', '个人财产', '夫妻关系', '借款合同', '担保物权', '强制性规定', '离婚', '夫妻共同财产', '建设用地',
        '不完全履行', '意思表示真实', '房屋租赁', '抵偿', '共同债务', '企业法人', '国有土地使用权', '不予受理', '和解', '拆迁', '案件受理费', '破产清算', '劳动争议',
        '催告', '继承人', '质押', '承租人', '房产证', '有价证券', '授权', '违约金', '共同财产', '变更登记', '最高法院', '高级法院', '中级法院', '基层法院',
        '最高人民法院', '北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省',
        '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省',
        '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区', '新疆维吾尔自治区高级人民法院生产建设兵团分院', '2018', '2017', '2016', '2015', '2014',
        '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001',
        '2000', '1999', '1998', '1997', '1996', '判决书', '裁定书', '调解书', '决定书', '通知书', '令']

redis_obj.sadd("wenshu_keys", *keys)
print("cache success.....")
