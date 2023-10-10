from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# import api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
llm_config = {"config_list": config_list, "seed": 42, "request_timeout": 120}

# create user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy", code_execution_config={"work_dir": "autogen-output"}
)
# create assistant agent
assistant = AssistantAgent(
    name="assistant", llm_config={"model": "gpt-3.5-turbo", "config_list": config_list}
)


# start the conversation
user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVDA and TESLA stock price change YTD"
)
