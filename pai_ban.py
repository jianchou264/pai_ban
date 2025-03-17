from datetime import datetime, timedelta
import requests
import os


# 定义人员列表
people = ["张三", "李四", "王五", "赵六", "孙七"]

# 获取当前日期
current_date = datetime.now()

# 找到下一个周三
days_until_wednesday = (2 - current_date.weekday() + 7) % 7
next_wednesday = current_date + timedelta(days=days_until_wednesday)

# 定义排班周期（每周三）
weeks_to_schedule = 20  # 假设排20周

# 存储排班结果的列表
schedule_list = []

# 排班逻辑
for week in range(weeks_to_schedule):
    # 计算当前周的周三日期
    current_wednesday = next_wednesday + timedelta(weeks=week)
    
    # 选择当前值班人员（轮流）
    current_person = people[week % len(people)]
    
    # 将结果添加到列表
    schedule_list.append((current_wednesday.strftime('%Y-%m-%d'), current_person))

# 获取前两个排班记录
first_schedule = schedule_list[0]  # 当前值班
second_schedule = schedule_list[1]  # 下周值班准备


# 获取前两个排班记录
first_schedule = schedule_list[0]  # 当前值班
second_schedule = schedule_list[1]  # 下周值班准备


# # 输出结果
# print(f"当前值班: 日期: {first_schedule[0]}, 值班人员: @{first_schedule[1]}")
# print(f"下周值班准备: 日期: {second_schedule[0]}, 值班人员: @{second_schedule[1]}")


# 钉钉机器人推送消息
def send_dingtalk_message(message):
    # 从环境变量中获取钉钉机器人的 access_token
    access_token = os.getenv("DINGTALK_ACCESS_TOKEN")
    if not access_token:
        print("未找到钉钉机器人的 access_token，请检查环境变量配置。")
        return
    
    # 钉钉机器人 Webhook URL
    webhook_url = f"https://oapi.dingtalk.com/robot/send?access_token=adf06e88371122cbbc200796e9c4fb9d04678c5e3ae5facb2a25f099e34a469b"
    
    # 消息内容
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    
    # 发送请求
    response = requests.post(webhook_url, json=data)
    if response.status_code == 200:
        print("消息推送成功！")
    else:
        print(f"消息推送失败，状态码: {response.status_code}, 响应内容: {response.text}")

# 构造推送消息
message = f"值班提醒：\n当前值班: 日期: {first_schedule[0]}, 值班人员: {first_schedule[1]}\n下周值班准备: 日期: {second_schedule[0]}, 值班人员: {second_schedule[1]}"

# 推送消息到钉钉
send_dingtalk_message(message)