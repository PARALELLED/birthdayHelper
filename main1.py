import datetime
import schedule
import time
#from plyer import notification

# 定義生日日期
birthday = {
    "吳佳晏":"07-08",
    "藍玉彤":"01-08",
    "John": "05-20",
    "Emma": "08-15",
    "test1":"02-09",
    # 添加更多的生日...
}

def check_birthday():
    print("check_birthday start")
    today = datetime.date.today().strftime("%Y-%m-%d")
    today = today[5:]
    for name, bday in birthday.items():
        if today == bday:
            message = f"今天是{name}的生日！"
            # notification.notify(
            #     title="生日提醒",
            #     message=message,
            #     timeout=10
            # )
    return today

def job():
    # 每天 00:00 執行 (24小時)
    schedule.every().day.at("22:05").do(check_birthday)
    #print("開始執行")
    while True:
        schedule.run_pending()
        time.sleep(1)  # 每隔 60 秒檢查一次