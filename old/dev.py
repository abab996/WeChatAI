# pip install zhipuai 请先在终端进行安装

from zhipuai import ZhipuAI

client = ZhipuAI(api_key="f66bebfd48594ab1a012f426a936aba1.nekFESO7qWulHNkY")

response = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {
            "role": "system",
            "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。" 
        },
        {
            "role": "user",
            "content": "今天天气"
        }
    ],
    top_p= 0.7,
    temperature= 0.95,
    max_tokens=1024,
    tools = [{"type":"web_search","web_search":{"search_result":True,"search_engine":"search-std"}}],
    stream=True
)
for trunk in response:
    print(trunk)