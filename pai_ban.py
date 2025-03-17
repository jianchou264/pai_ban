from datetime import datetime, timedelta

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

# 输出结果
print(f"当前值班: 日期: {first_schedule[0]}, 值班人员: @{first_schedule[1]}")
print(f"下周值班准备: 日期: {second_schedule[0]}, 值班人员: @{second_schedule[1]}")