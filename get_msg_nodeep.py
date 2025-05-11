from openai import OpenAI
import time

client = OpenAI(
    api_key="f66bebfd48594ab1a012f426a936aba1.nekFESO7qWulHNkY",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
) 

def up_message(a):
    try:
        # 尝试兼容性更好的/v1/chat/completions路径
        completion = client.chat.completions.create(
            model="glm-4-flash-250414",  # 使用完整模型名称
            messages=[
                {"role": "system", "content": "你是一个能帮助用户，并且能准确回答用户问题的助手。你会根据用户的问题，给出专业、准确、有见地的建议。"},
                {"role": "user", "content": a}
                
            ],
            tools = [{"type":"web_search","web_search":{"search_result":True,"search_engine":"search-std"}}],
            #stream=True
        )
        out = completion.choices[0].message.content
        return out

    except Exception as e:
        print(f"API调用失败: {str(e)}")
        print("建议检查：")
        print("1. 确保本地服务支持OpenAI兼容API")
        print("2. 确认服务是否运行在1234端口")
        print("3. 尝试使用curl测试API端点是否可用")





# from openai import OpenAI 

# client = OpenAI(
#     api_key="f66bebfd48594ab1a012f426a936aba1.nekFESO7qWulHNkY",
#     base_url="https://open.bigmodel.cn/api/paas/v4/"
# ) 

# completion = client.chat.completions.create(
#     model="glm-4-flash-250414",  
#     messages=[    
#         {"role": "system", "content": "你是一个AI"},    
#         {"role": "user", "content": "你好"} 
#     ],
#     top_p=0.7,
#     temperature=0.9
#  ) 
 
# print(completion.choices[0].message.content)




#pip install zhipuai 请先在终端进行安装

# from zhipuai import ZhipuAI

# client = ZhipuAI(api_key="f66bebfd48594ab1a012f426a936aba1.nekFESO7qWulHNkY")

# response = client.chat.completions.create(
#     model="glm-4-flash-250414",
#     messages=[
#         {
#             "role": "system",
#             "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。" 
#         },
#         {
#             "role": "user",
#             "content": "你好"
#         }
#     ],
#     top_p= 0.7,
#     temperature= 0.95,
#     max_tokens=8192,
#     tools = [{"type":"web_search","web_search":{"search_result":True,"search_engine":"search-std"}}],
#     stream=True
# )

# print(response)


# pip install zhipuai 请先在终端进行安装

# from zhipuai import ZhipuAI

# client = ZhipuAI(api_key="f66bebfd48594ab1a012f426a936aba1.nekFESO7qWulHNkY")

# response = client.chat.completions.create(
#     model="glm-4-flash-250414",
#     messages=[
#         {
#             "role": "system",
#             "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。" 
#         },
#         {
#             "role": "user",
#             "content": "哪吒2多久上映"
#         }
#     ],
#     top_p= 0.7,
#     temperature= 0.95,
#     max_tokens=8192,
#     tools = [{"type":"web_search","web_search":{"search_result":True,"search_engine":"search-std"}}],
#     stream=True
# )

# # Process the streaming response
# for chunk in response:
#     if chunk.choices[0].delta.content:
#         print(chunk.choices[0].delta.content, end="", flush=False)
# print(response)