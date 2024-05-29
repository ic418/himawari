from datetime import datetime, timedelta

def date_iterator(start_date, days_back):
    # 将开始日期转换为datetime对象
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    
    # 计算结束日期
    end_date = start_date - timedelta(days=days_back)
    
    # 生成日期迭代器
    current_date = start_date
    while current_date >= end_date:
        yield current_date.strftime('%Y/%m-%d')
        current_date -= timedelta(days=1)

if __name__ == "__main__":
    start_date = '2024-01-03'  # 开始日期
    days_back = 99999  # 往回退的天数


    for date_str in date_iterator(start_date, days_back):
        print(date_str)