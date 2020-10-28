#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kafka import KafkaProducer

bootstrap_servers = ['172.19.255.10:9092']
topicName = 'tt'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

producer.send(topicName, "Hi")