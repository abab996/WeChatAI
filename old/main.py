from wxauto import *
import time
import get_msg
import pyautogui
import pyperclip

wx = WeChat()
wx.GetSessionList()

# 存储已处理的消息ID
processed_msg_ids = set()

def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def listen_latest_messages():
        try:
            msgs = wx.GetAllMessage()
            if msgs:
                latest_msg = msgs[-1]
                msg_id = f"{latest_msg[0]}_{latest_msg[1]}"  # 创建唯一消息ID
                
                if msg_id not in processed_msg_ids:
                    #print(f'新消息: {latest_msg[0]} : {latest_msg[1]}')
                    processed_msg_ids.add(msg_id)
                    return latest_msg[0], latest_msg[1]
            
            time.sleep(0)  # 每秒检查一次
            
        except Exception as e:
            print(f"监听出错: {str(e)}")
            time.sleep(0)


def listen_latest_messages_q():
        try:
            msgs = wx.GetAllMessage()
            if msgs:
                latest_msg = msgs[-1]
                msg_id = f"{latest_msg[0]}_{latest_msg[1]}"  # 创建唯一消息ID
                
                if msg_id not in processed_msg_ids:
                    # 检查是否被@（包含@符号或特定昵称）
                    if '@' in latest_msg[1] or '白鲨想睡觉' in latest_msg[1]:
                        print(f"{get_time()} 你被@了！")
                        processed_msg_ids.add(msg_id)
                        # 去除"@白鲨想睡觉"的内容
                        cleaned_msg = latest_msg[1].replace('@白鲨想睡觉', '').strip()
                        return latest_msg[0], cleaned_msg
        except Exception as e:
            print(f"{get_time()}监听出错: {str(e)}")
            time.sleep(0)

time.sleep(5)
pyperclip.copy('服务启动')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

qa = ""

while True:
    time.sleep(0)
    #a = listen_latest_messages() #私聊用这个
    a = listen_latest_messages_q() #群聊用这个
    if a is None:  # 添加对None的检查
        continue
    print(get_time(), '监听：', a)
    if a[0] != 'Self':
        u_name = a[0]
        print('用户名：', u_name)
        b = get_msg.up_message('这是之前的对话，如果本次恢复中无用可以忽略：' +
            str(qa) + '\n用户名：' + u_name + '--------------------------------' +
            '以下是新问题：' + str(a[1]))  # 使用+连接字符串
        qa = str(qa) + '用户' + str(a[1]) + ' 你：' + str(b) + '|'

        print('回复：', b)
        print('记忆：', qa)
        print('\n')
        pyperclip.copy(b)
        time.sleep(0)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    else:
        print('It Self丄\n')
    
