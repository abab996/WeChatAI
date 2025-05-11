from openai import OpenAI
import time

client = OpenAI(
    api_key="f66bebfd48594ab1a012f426a936aba1.nekFESO7qWulHNkY",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
) 

def up_message(a, b, c):
    try:
        # 尝试兼容性更好的/v1/chat/completions路径
        completion = client.chat.completions.create(
            model="glm-4-flash-250414",  # 使用完整模型名称
            messages=[
                {"role": "system", "content": "现在你是一个判断用户是否在呼唤你的机器人，除了判断用户是否在呼叫你你不能回答任何别的内容。你可以在开头通过很多思考判断用户是否在呼唤你，但必须在信息末尾换行回复true或false，除此之外你不能在结尾回复任何其他内容。你需要根据用户的新问题和之前的对话判断用户是否在呼叫你。你可以根据判断之前的对话与用户新问题的话题相似度或者用户有没有对你很明显的称呼来判断用户是否在呼叫你，但如果用户只是回应你，而没有提出新的问题也回复发；flase，例如用户回复‘哦’，‘原来如此’，‘这样啊’，‘懂了’一系列的词语。以下是一些要求：1.你只必须且只在回答结尾换行，注意！一定要换行！！！（但不意味着你就可以不用先思考！）回复true或者false 2.如果你判断出用户在呼叫你那就回复true 3.如果你判断出用户没在呼叫你那就回复false 4.如果用户没有提出新的问题请忽略前面的要求回复flase 5.示例：我对你的提问（这是之前你的回复：所以1+1=2 这是用户新的提问：那2+2呢？ 请你判断用户是否在呼叫你） 你的回复（根据前文的提示，我回复了1+1=2，用户紧接着说了‘那2+2呢’。两个语句都是在讨论数学运算，所以很有可能用户是在呼叫我。再看用户的话中有‘那’，这个字一般用于继续追问，所以我应该回复true。\ntrue）；示例2：我对你的提问（这是之前你的回复：所以1+1=2 这是用户新的提问：他就是笨！ 请你判断用户是否在呼叫你） 你的回复（根据前文的提示，我回复了1+1=2，用户紧接着说了‘他就是笨！’。两个语句都没有逻辑上的联系，所以用户可能没在呼叫我。所以我应该回复false。\nfalse）"},
                {"role": "user", "content": '这是之前你的回复：' + str(a) + '这是用户新的提问：' + str(b) + '请你判断用户是否在呼叫你'}
            ],
        )
        out = completion.choices[0].message.content
        list_out = out.split('\n')  # 使用换行符分割字符串

        return list_out[-1], list_out, a, b

    except Exception as e:
        print(f"API调用失败: {str(e)}")
        print("建议检查：")
        print("1. 确保本地服务支持OpenAI兼容API")
        print("2. 确认服务是否运行在1234端口")
        print("3. 尝试使用curl测试API端点是否可用")

#print(up_message('9.9比9.11大', '谢谢你')) 

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