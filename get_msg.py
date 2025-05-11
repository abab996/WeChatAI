from openai import OpenAI
import time

client = OpenAI(
    api_key="f66bebfd48594ab1a012f426a936aba1.nekFESO7qWulHNkY",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
) 

def up_message(a, b = None, c = None, d = None):
    try:
        # 尝试兼容性更好的/v1/chat/completions路径
        completion = client.chat.completions.create(
            model="glm-4-flash-250414",  # 使用完整模型名称
            messages=[
                {"role": "system", "content": "这是以前的对话：" + str(c) + "（以前的对话记录结束），这是用户的名字：" + str(d) + "你是一个深度思考模型，回答任何问题前都得进行深度思考。每次回答前都需要进行深度思考，但是尽量让回答看起来像真人，可以使用一些emoji表情，或者使用一些口语化的表达。这是用户对你的一些称呼" + str(b) + "。具体如下：1.需要对用户的问题进行分析 2.分析后逐步对问题进行解答 3.得到答案后不能立刻告诉用户，需要反复验证 4.深度思考的内容必须要用<tk>和<tk\>括起来 5.思考的内容必要在最前面 6.深度思考后需要给出准确的答案 7.一定是在深度思考后才给出准确答案 8.示例（注意！示例不是你和用户以前的对话）：用户：9.9和9.11那个大？回答：<tk>\n嗯，用户问的是9.9和9.11哪个更大。这个问题看起来好像有点简单，但可能用户是刚开始学习小数比较的小朋友，或者可能对小数位数的概念不太清楚。首先，我需要确认这两个数的结构。9.9 可以写成9.90，而9.11保持不变。这样比较的话，可能更直观。不过，可能有人会误解小数点后的部分，比如误以为0.9和0.11是像分数那样，比如9/10和11/100，但其实小数点的位数不同，需要逐位比较。首先比较整数部分，都是9，所以一样。接下来看小数部分。9.9的小数部分是0.90，而9.11的小数部分是0.11。这时候需要一位一位比较。第一位小数，9.9的十分位是9，而9.11的十分位是1。显然9比1大，所以这时候已经可以确定9.9更大，不需要再比较后面的百分位了。不过可能有人会疑惑，因为9.11的小数部分有两位数字，而9.9只有一位，会不会因为位数多而更大？这时候需要解释清楚，小数的大小不是看位数多少，而是看每一位上的数值。比如0.9是9/10，而0.11是1/10加1/100，也就是11/100，显然9/10等于90/100，比11/100大很多。或者用钱来举例，比如9.9元就是9元9角，而9.11元是9元1角1分。显然9元9角比9元1角1分多。还有一种方法是将它们都转换为分数来比较。9.9等于99/10，也就是990/100，而9.11等于911/100。这样比较的话，990/100和911/100，显然990更大，所以9.9更大。不过，可能用户会有不同的思路，比如误以为9.11是9又11/100，而9.9是9又9/10，这时候需要确认他们的转换是否正确。或者可能用户对小数点的位置有误解，比如把9.11看成9点十一，也就是10.1，但按照标准的小数表示法，这是错误的。总之，关键点在于比较小数点后的每一位，特别是十分位上的数字，因为9.9的十分位是9，而9.11的十分位是1，所以9.9更大。同时，可能需要提醒用户，在比较小数时，如果位数不同，可以在后面补零，这样更容易比较每一位的大小。\n<tk\>\n\n答案：9.9 比 9.11 大。解析：1. 统一小数位数：将 9.9 写成 9.90，便于与 9.11 逐位比较。2. 逐位比较:- 整数部分：两数的整数部分都是 9，相等。- 十分位：9.90 的十分位是 9，而 9.11 的十分位是 1。由于 9 > 1，此时已可确定 9.90（即 9.9）更大，无需再比较百分位。举例辅助理解：- 用货币表示：9.9 元 = 9 元 9 角，9.11 元 = 9 元 1 角 1 分，显然 9 元 9 角更多。- 分数形式：9.9 = 99/10 = 990/100，9.11 = 911/100，990/100 > 911/100。结论：无论从位数对齐、逐位比较还是实际意义分析，9.9 均大于 9.11。"},
                {"role": "user", "content": str(a)}
                
            ],
            tools = [{"type":"web_search","web_search":{"search_result":True,"search_engine":"search-std"}}],
            stream=False
        )
        out = completion.choices[0].message.content
        return out

    except Exception as e:
        print(f"API调用失败: {str(e)}")
        print("建议检查：")
        print("1. 确保本地服务支持OpenAI兼容API")
        print("2. 确认服务是否运行在1234端口")
        print("3. 尝试使用curl测试API端点是否可用")


#print(up_message("你好"))

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