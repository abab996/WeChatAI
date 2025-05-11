from wxauto import *
import time
import get_msg_copy
import get_msg_nodeep
import pyautogui
import pyperclip
import c_true

#--------------------------------
# 重点关注
#--------------------------------
# 初始化参数
self_name = ['白鲨想睡觉', '白鲨', '鲨鲨', '小鲨鱼']  # 替换为你的微信名
listen_list = ['renji', '好名字可以让你的朋友更容易记住你']  # 替换为你想要监听的用户名
group_mod = True  # 群聊模式，True为群聊，False为私聊
deep = True  # 深度模式，True为开启，False为关闭


# 初始化微信API
wx = WeChat()
wx.GetSessionList()
b = ''
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


def listen_latest_messages_q():
    try:
        msgs = wx.GetListenMessage()
        for chat in msgs:
            one_msgs = msgs.get(chat)   # 获取消息内容
            
            # 处理每条消息
            for msg in one_msgs:
                msg_id = f"{msg.sender}_{msg.content}"  # 定义msg_id
                if msg.type == 'friend':
                    sender = msg.sender
                    print(f'<{sender.center(10, "-")}>：{msg.content}')
                    
                    # 检查是否被@或包含任一用户名
                    if '�' in msg.content or any(name in msg.content for name in self_name):
                        chat.SendMsg('思考中...')
                        print(f"{get_time()} 你被@了！")
                        processed_msg_ids.add(msg_id)
                        # 去除所有可能的@用户名内容
                        cleaned_msg = msg.content
                        for name in self_name:
                            cleaned_msg = cleaned_msg.replace(name, '').strip()
                        return sender, cleaned_msg
                    else:
                        c = c_true.up_message(b, msg.content, self_name)
                        if c[0] == 'true':
                            chat.SendMsg('收到')  
                            print(f"{get_time()} 被判断为呼唤")
                            print('\n\n\n\n\n' + str(c))
                            processed_msg_ids.add(msg_id)
                            return sender, msg.content
                        else:
                            time.sleep(0)
                            return None
                
                elif msg.type == 'self':
                    print(f'<{msg.sender.center(10, "-")}>：{msg.content}')
                    return None
                    
    except Exception as e:
        print(f"{get_time()}监听出错: {str(e)}")
        time.sleep(0)

# 原代码中使用 str() 创建空字符串，这在语法上没问题，但通常更推荐直接使用空字符串字面量
qa = ""


time.sleep(5)
pyperclip.copy('running...')  # 修正拼写错误
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

while True:
    time.sleep(0)
    if group_mod:  # 如果是群聊模式
        a = listen_latest_messages_q()  # 调用群聊监听函数
    else:  # 如果是私聊模式
        a = listen_latest_messages()  # 调用私聊监听函数

    if a is None:  # 添加对None的检查
        continue
    print(get_time(), '监听：', a)
    if a[0] != 'Self':
        #wx.ChatWith(who=a[0])
        u_name = a[0]
        print('用户名：', u_name)
        if deep:  # 如果是深度模式，使用深度回复函数
            # pyperclip.copy('深度思考中...')
            # time.sleep(0)
            # pyautogui.hotkey('ctrl', 'v')
            # pyautogui.press('enter')
            if group_mod:  # 如果是群聊模式，使用群聊回复函数
                b = '@' + u_name + ' ' + get_msg_copy.up_message('这是之前的对话，如果本次恢复中无用可以忽略：' +
                    str(qa) + '\n用户名：' + u_name + '--------------------------------' +
                    '以下是新问题：' + str(a[1]), self_name)  # 使用+连接字符串
            else:  # 如果是私聊模式，使用私聊回复函数
                b = get_msg_copy.up_message('这是之前的对话，如果本次恢复中无用可以忽略：' +
                    str(qa) + '\n用户名：' + u_name + '--------------------------------' +
                    '以下是新问题：' + str(a[1]), self_name)  # 使用+连接字符串
            qa = str(qa) + '用户' + str(a[1]) + ' 你：' + str(b) + '|'
        else:  # 如果不是深度模式，使用普通回复函数
            # pyperclip.copy('思考中...')
            # time.sleep(0)
            # pyautogui.hotkey('ctrl', 'v')
            # pyautogui.press('enter')
            if group_mod:  # 如果是群聊模式，使用群聊回复函数
                b = '@' + u_name + ' \n' + get_msg_nodeep.up_message('这是之前的对话，如果本次恢复中无用可以忽略：' +
                    str(qa) + '\n用户名：' + u_name + '--------------------------------' +
                    '以下是新问题：' + str(a[1]))  # 使用+连接字符串
            else:  # 如果是私聊模式，使用私聊回复函数
                b = get_msg_nodeep.up_message('这是之前的对话，如果本次恢复中无用可以忽略：' +
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
        # b = main.up_message(a[1])  # 假设up_message函数接受一个消息作为参数并返回处理后的结果
        # print(b)
        # pyperclip.copy(b)
        # time.sleep(0)
        # pyautogui.hotkey('ctrl', 'v')
        # pyautogui.press('enter')
        print('It Self丄\n')
    
