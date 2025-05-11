import threading
from wxauto import *
import time
import get_msg
import get_msg_nodeep
import pyautogui
import pyperclip
import decide

# 添加线程锁
conversation_lock = threading.Lock()

#--------------------------------
# 重点关注
#--------------------------------
# 初始化参数
self_name = ['白鲨想睡觉', '白鲨', '鲨鲨', '小鲨鱼']  # 替换为你的微信名
listen_list = ['renji', '好名字可以让你的朋友更容易记住你', 'Keitaro.🥑']  # 替换为你想要监听的用户名
group_mod = True  # 群聊模式，True为群聊，False为私聊
deep = True  # 深度模式，True为开启，False为关闭


# 初始化微信API
wx = WeChat()
wx.GetSessionList()
response = ''
for i in listen_list:
    wx.AddListenChat(who=i)
    print(f"已添加监听：{i}")

# 存储已处理的消息ID
processed_msg_ids = set()

def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    
# # 获取微信名
# def get_wechat_name():
#     friend_infos = wx.GetAllFriends()
#     return friend_infos[0]['NickName']

# print(get_wechat_name())
    
    
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
            print(f"{get_time()}监听出错: {str(e)}")
            time.sleep(0)


# 修改为使用字典存储每个会话的对话历史
conversation_history = {}

def listen_latest_messages_q():
    try:
        msgs = wx.GetListenMessage()
        active_chats = []
        
        for chat in msgs:
            one_msgs = msgs.get(chat)
            
            for msg in one_msgs:
                msg_id = f"{msg.sender}_{msg.content}"
                if msg.type == 'friend':
                    sender = msg.sender
                    print(f'<{sender.center(10, "-")}>：{msg.content}')
                    
                    # 初始化该聊天窗口的历史记录
                    if chat not in conversation_history:
                        conversation_history[chat] = ""
                    
                    # 检查是否被@或包含任一用户名
                    if '�' in msg.content or any(name in msg.content for name in self_name):
                        chat.SendMsg('思考中...')  # 先统一回复思考中
                        print(f"{get_time()} 你被@了！")
                        processed_msg_ids.add(msg_id)
                        cleaned_msg = msg.content
                        
                        for name in self_name:
                            cleaned_msg = cleaned_msg.replace(name, '').strip()
                        active_chats.append((chat, sender, cleaned_msg))
                    else:
                        c = decide.up_message(response, msg.content, self_name)
                        print(f"判断结果：{c}")
                        if c[0] == 'true':
                            chat.SendMsg('思考中...')  # 先统一回复思考中
                            print(f"{get_time()} 被判断为呼唤")
                            processed_msg_ids.add(msg_id)
                            active_chats.append((chat, sender, msg.content))
        
        # 按消息接收时间排序(最早的消息最先处理)
        active_chats.sort(key=lambda x: x[2])  
        return active_chats if active_chats else None
                    
    except Exception as e:
        print(f"{get_time()}监听出错: {str(e)}")
        time.sleep(0)

# 原代码中使用 str() 创建空字符串，这在语法上没问题，但通常更推荐直接使用空字符串字面量
qa = ""


# time.sleep(5)
# pyperclip.copy('running...')  # 修正拼写错误
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.press('enter')
print('启动...')
for i in listen_list:
    wx.ChatWith(i)
    pyperclip.copy('running...')  # 修正拼写错误
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
print('启动完成...')

while True:
    time.sleep(0)
    if group_mod:
        active_chats = listen_latest_messages_q()
    else:
        active_chats = [listen_latest_messages()]
    
    if active_chats is None:
        continue
        
    for chat_info in active_chats:
        if chat_info is None:
            continue
            
        chat, u_name, message = chat_info
        print(get_time(), '监听：', (u_name, message))
        
        if u_name != 'Self':
            print('用户名：', u_name)
            if deep:
                if group_mod:
                    response = '@' + u_name + ' ' + str(get_msg.up_message(message, self_name, conversation_history[chat], u_name))
                else:
                    response = str(get_msg.up_message(message, self_name, conversation_history[chat], u_name))
                
                # 修改对话历史更新逻辑
                MAX_HISTORY_LENGTH = 99999999999999999999999999999999999  # 保留最近10轮对话
                with conversation_lock:
                    conversation_history[chat] = f"{conversation_history[chat]}用户：{message} 你：{response}|"
                if len(conversation_history[chat].split('|')) > MAX_HISTORY_LENGTH:
                    # 保留最近MAX_HISTORY_LENGTH轮对话
                    conversation_history[chat] = '|'.join(conversation_history[chat].split('|')[-MAX_HISTORY_LENGTH:])
            else:
                # 类似处理非深度模式...
                pass
                
            print('回复：', response)
            print('记忆：', conversation_history)
            print('\n')
            pyperclip.copy(response)
            time.sleep(0)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
        else:
            print('It Self丄\n')
    
