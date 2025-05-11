from openai import OpenAI

client = OpenAI(
    api_key="f66bebfd48594ab1a012f426a936aba1.nekFESO7qWulHNkY",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

def up_message(a):
    try:
        completion = client.chat.completions.create(
            model="glm-4-flash-250414",
            messages=[
                {"role": "system", "content": "你是一个可以上网的模型..."},
                {"role": "user", "content": a}
            ],
            tools=[{"type":"web_search","web_search":{"search_result":True,"search_engine":"search-std"}}],
            stream=False  // 改为非流式模式
        )
        
        if completion.choices[0].message.tool_calls:
            # 处理工具调用
            return "已触发搜索功能，请稍等..."
        return completion.choices[0].message.content

    except Exception as e:
        print(f"API调用失败: {str(e)}")
        return "抱歉，AI服务暂时不可用"

print(up_message("现在几点"))

# 处理流式响应
full_response = ""
for chunk in completion:
    if chunk.choices[0].delta.content:
        full_response += chunk.choices[0].delta.content


print(up_message("现在几点"))
