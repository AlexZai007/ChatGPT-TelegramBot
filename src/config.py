from dataclasses import dataclass


@dataclass
class Config():
    """
    🧠 here is the config.

    telegram_token - telegram bot token, can be obtained from telegram bot father
    open_ai_token - chatgpt token, can be obtained from the chatgpt api website

    ⚡ EXAMPLE

    telegram_token: str = "5897272316:AAFI0FiR7I_0RzydOsadiyfgsdfDSAFSVA"
    open_ai_token: str = "sk-RPd5EeqIsdfgsdfr0xqQTALUFDGKJDFDSa"
    """

    #ТОКЕНЫ
    telegram_token: str = "-"
    open_ai_token: str = "-"











