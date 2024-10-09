import os
import json
import environ
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables 
if os.getenv("APP_ENV"):
    logger.info("Loaded environment variables from system.")
else:
    from dotenv import load_dotenv
    load_dotenv(".env")
    logger.info("Loaded environment variables from .env file.")

@environ.config(prefix="APP", frozen=True)
class Config:

    @environ.config
    class Server:
        grace_period = environ.var(0)
        max_workers = environ.var(100)
        host = environ.var()
        port = environ.var()

    @environ.config
    class DB:
        name = environ.var("name")
        host = environ.var("host")
        port = environ.var("port")
        username = environ.var("username")
        password = environ.var("password")
        replicaset = environ.var("replicaset")
        collections = environ.var("collections") 
        
    env = environ.var()
    version = environ.var()
    server = environ.group(Server)
    db = environ.group(DB)

# Create the config instance
try:
    configs = environ.to_config(Config, environ={
        "APP_ENV": os.environ.get("YAWN_ENV"),
        "APP_VERSION": os.environ.get("YAWN_VERSION"),
        "APP_SERVER_HOST": os.environ.get("YAWN_SERVER_HOST"),
        "APP_SERVER_PORT": os.environ.get("YAWN_SERVER_PORT"),
        "APP_DB_NAME": os.environ.get("YAWN_DB_NAME"),
        "APP_DB_HOST": os.environ.get("YAWN_DB_HOST"),
        "APP_DB_PORT": os.environ.get("YAWN_DB_PORT"),
        "APP_DB_USERNAME": os.environ.get("YAWN_DB_USERNAME"),
        "APP_DB_PASSWORD": os.environ.get("YAWN_DB_PASSWORD"),
        "APP_DB_REPLICASET": os.environ.get("YAWN_DB_REPLICASET"),
        "APP_DB_COLLECTIONS": os.environ.get("YAWN_DB_COLLECTIONS"),
    })
    logger.info("Configuration loaded successfully.")
except Exception as e:
    logger.error(f"Failed to load configuration: {e}")
    
# Log the loaded configuration for debugging
logger.info(json.dumps({
    "env": configs.env,
    "version": configs.version,
    "server": {
        "host": configs.server.host,
        "port": configs.server.port
    },
    "db": {
        "name": configs.db.name,
        "host": configs.db.host,
        "port": configs.db.port
    }
}, indent=4))
