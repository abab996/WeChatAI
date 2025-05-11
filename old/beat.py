from wxauto import WeChat
import time

wx = WeChat()

# 首先设置一个监听列表，列表元素为指定好友（或群聊）的昵称
listen_list = [
    'renji',
    '好名字可以让你的朋友更容易记住你'
]

# 然后调用`AddListenChat`方法添加监听对象，其中可选参数`savepic`为是否保存新消息图片
for i in listen_list:
    wx.AddListenChat(who=i)

wait = 0  # 设置3秒查看一次是否新消息
while True:
    try:
        msgs = wx.GetListenMessage()
        for chat in msgs:
            one_msgs = msgs.get(chat)   # 获取消息内容
            
            # 回复收到
            for msg in one_msgs:
                if msg.type == 'sys':
                    print(f'【系统消息】{msg.content}')
                
                elif msg.type == 'friend':
                    sender = msg.sender # 这里可以将msg.sender改为msg.sender_remark，获取备注名
                    print(f'<{sender.center(10, "-")}>：{msg.content}')
                    
                    # ！！！ 回复收到，此处为`chat`而不是`wx` ！！！
                    chat.SendMsg('收到')  
                    # 此处将msg.content传递给大模型，再由大模型返回的消息回复即可实现ai聊天
        
                elif msg.type == 'self':
                    print(f'<{msg.sender.center(10, "-")}>：{msg.content}')
                
                elif msg.type == 'time':
                    print(f'\n【时间消息】{msg.time}')
        
                elif msg.type == 'recall':
                    print(f'【撤回消息】{msg.content}')
        time.sleep(wait)
    except KeyboardInterrupt:
        print('Bye~')
        break
