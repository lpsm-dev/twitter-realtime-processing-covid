# -*- coding: utf-8 -*-

from settings.cli import CLIArguments
from settings.config import Config
from settings.log import Log
from tools.os import OS
from tools.yml import YML

# ==============================================================================
# GLOBAL
# ==============================================================================

MAX_RETRIES = 50

config, args, yml = Config(), CLIArguments().args, YML().get_content()

twitter_consumer_key = config.get_env("TWITTER_CONSUMER_KEY")
twitter_consumer_secret = config.get_env("TWITTER_CONSUMER_SECRET")
twitter_access_token = config.get_env("TWITTER_ACCESS_TOKEN")
twitter_access_token_secret = config.get_env("TWITTER_ACCESS_TOKEN_SECRET")

twitter_consumer_key = twitter_consumer_key if twitter_consumer_key else yml[
    "twitter"]["consumer"]["key"]
twitter_consumer_secret = twitter_consumer_secret if twitter_consumer_secret else yml[
    "twitter"]["consumer"]["secret"]
twitter_access_token = twitter_access_token if twitter_access_token else yml[
    "twitter"]["access"]["token"]
twitter_access_token_secret = twitter_access_token_secret if twitter_access_token_secret else yml[
    "twitter"]["access"]["secret"]

log_path = config.get_env("LOG_PATH") if config.get_env(
    "LOG_PATH") else "/var/log/code"
log_file = config.get_env("LOG_FILE") if config.get_env(
    "LOG_FILE") else "file.log"
log_level = config.get_env("LOG_LEVEL") if config.get_env(
    "LOG_LEVEL") else "DEBUG"
logger_name = config.get_env("LOGGER_NAME") if config.get_env(
    "LOGGER_NAME") else "Twitter Realtime Processing"

logger = Log(log_path, log_file, log_level, logger_name).logger

realtime, version = args["realtime"].capitalize(), args["version"]

broker = config.get_env("KAFKA_BROKER_URL") if config.get_env(
    "KAFKA_BROKER_URL") else "kafka:9092"
tweets_topic = config.get_env("KAFKA_TOPIC") if config.get_env(
    "KAFKA_TOPIC") else "dados-tweets"
