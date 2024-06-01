import os

os.environ["OPENAI_API_VERSION"] = "2024-05-13"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://ik-oai-eastus.openai.azure.com/"
os.environ["AZURE_OPENAI_API_KEY"] = "a72bf3d17ab74336915a78d15296b15d"


from langchain_openai import AzureOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_mistralai.chat_models import ChatMistralAI

# If api_key is not passed, default behavior is to use the `MISTRAL_API_KEY` environment variable.
chat = ChatMistralAI(api_key="QLrfXO2hbUYXoUtSqDXm0bGiwcOiSQmd")
messages = [
    SystemMessage(content="you are a bot, name Asa"),
    HumanMessage(content="knock knock")
    ]
reply = chat.invoke(messages)
print(reply)