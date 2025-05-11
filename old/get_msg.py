from openai import OpenAI
import time

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",  # 确保添加/v1路径
    api_key="none"  # 本地服务通常不需要真实API密钥
)

def up_message(a):
    try:
        # 尝试兼容性更好的/v1/chat/completions路径
        response = client.chat.completions.create(
            model="qwen2.5-0.5b-instruct-q2_k.gguf",  # 使用完整模型名称
            messages=[
                {"role": "system", "content": "您是一个有帮助的助手"},
                {"role": "user", "content": a}
            ]
        )
        out = response.choices[0].message.content
        return out

    except Exception as e:
        print(f"API调用失败: {str(e)}")
        print("建议检查：")
        print("1. 确保本地服务支持OpenAI兼容API")
        print("2. 确认服务是否运行在1234端口")
        print("3. 尝试使用curl测试API端点是否可用")


