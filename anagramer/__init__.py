#!/usr/bin/python3
import os, redis

''' Check for Heroku RedisToGo add-on availability else use localhost via Docker '''
REDIS_SERVER = os.getenv('REDISTOGO', 'redis://redis:6379')

''' Redis storage for caching Word-Anagram mappings with persistance '''
cache = redis.from_url(REDIS_SERVER)