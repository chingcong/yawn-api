#!/usr/bin/python3

from configs import configs
from healthcheck import HealthCheck

def health_redis():
    return True, "redis"

def health_db():
    return True, "database"

def application_data():
    return {
        "name": "yawn-tornado",
    }

health = HealthCheck(checkers=[health_redis, health_db])
health.add_section("application", application_data)
health.add_section("version", configs.version)
health.add_section("env", configs.env)