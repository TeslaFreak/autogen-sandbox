from autogen import (
    AssistantAgent,
    UserProxyAgent,
    config_list_from_json,
    GroupChat,
    GroupChatManager,
)

# import api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
llm_config = {"config_list": config_list, "seed": 42, "request_timeout": 120}

# create user proxy agent
user_proxy = UserProxyAgent(
    name="user_proxy",
    system_message="A human admin who will give the idea and run the code provided by Coder",
    code_execution_config={"last_n_messages": 2, "work_dir": "autogen-output"},
    human_input_mode="ALWAYS",
)

coder = AssistantAgent(name="coder", llm_config=llm_config)

pm = AssistantAgent(
    name="product_manager",
    llm_config=llm_config,
    system_message="You will help break down the initial idea into a well scoped requirement for the coder; Do not involve in future conversations or error fixing",
)


# create groupchat
groupchat = GroupChat(agents=[user_proxy, coder, pm], messages=[])
manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# start conversation
user_proxy.initiate_chat(
    manager, message="Build a classic and basic pong game with two players in python"
)
