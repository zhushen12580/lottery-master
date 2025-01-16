import pandas as pd
import json

# 读取Excel文件
df = pd.read_excel('members.xlsx', header=None)  # 假设文件名为members.xlsx，没有表头

# 转换为指定格式
members = []
for _, row in df.iterrows():
    member = {
        "phone": row[0],  # 第一列是部门
        "name": row[1]    # 第二列是姓名
    }
    members.append(member)

# 生成JavaScript代码
js_code = "var member = " + json.dumps(members, ensure_ascii=False, indent=2)

# 写入到js文件
with open('member.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("转换完成！数据已写入 member.js 文件")