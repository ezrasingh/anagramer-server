#!/usr/bin/python3
import os, redis

''' Check for Redis server else use localhost via Docker '''
REDIS_SERVER = os.getenv('REDIS_SERVER', 'redis://redis:6379')

''' Redis storage for caching Word-Anagram mappings with persistance '''
cache = redis.from_url(REDIS_SERVER)