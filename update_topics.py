"""
课题信息管理脚本
用于更新蔡月明课题组内部平台的课题信息
"""

import json
import os
from datetime import datetime

class ProjectUpdater:
    def __init__(self):
        self.data_file = "topics_data.json"
        self.index_file = "index.html"
        self.topic_files = ["topic1.html", "topic2.html", "topic3.html", "topic4.html", "topic5.html"]
        self.backup_dir = "backups"
        
    def create_backup(self):
        """创建备份目录和备份文件"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"backup_{timestamp}"
        
        # 备份HTML文件
        all_html_files = [self.index_file] + self.topic_files
        for filename in all_html_files:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                backup_path = os.path.join(self.backup_dir, f"{backup_filename}_{filename}")
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
        
        print(f"已创建备份: {backup_filename}")
    
    def load_topics_data(self):
        """加载课题数据"""
        default_data = {
            "topics": [
                {
                    "id": "topic1",
                    "name": "皮肌炎的免疫发病机制研究",
                    "progress": "患者样本收集完成，正在进行免疫细胞分型",
                    "person_in_charge": "张三",
                    "start_time": "2025年",
                    "next_plan": "完成免疫细胞分析，探究关键通路分子",
                    "data_spec": "• 文件按 日期_患者编号_检测类型 命名<br>            • 每周三备份至课题组云盘<br>            • 患者临床信息匿名化处理，严格保密"
                },
                {
                    "id": "topic2",
                    "name": "类风湿关节炎免疫调控研究",
                    "progress": "动物模型构建完成，待检测",
                    "person_in_charge": "李四",
                    "start_time": "2025年",
                    "next_plan": "完成检测数据分析，开始药物干预实验",
                    "data_spec": "• 按动物/细胞数据分类存储<br>            • 每日备份实验数据<br>            • 绑定动物编号，避免混淆"
                },
                {
                    "id": "topic3",
                    "name": "单细胞多组学分析",
                    "progress": "数据已下机，正在分析",
                    "person_in_charge": "王五",
                    "start_time": "2025年",
                    "next_plan": "完成数据分析，准备初稿撰写",
                    "data_spec": "• 原始数据/结果/脚本分文件夹存储<br>            • 数据下机后立即双备份<br>            • 注释脚本版本和参数"
                },
                {
                    "id": "topic4",
                    "name": "天然免疫与炎症信号通路",
                    "progress": "Western 实验验证中",
                    "person_in_charge": "赵六",
                    "start_time": "2025年",
                    "next_plan": "完成WB验证，开始信号通路机制探究",
                    "data_spec": "• 原始图片禁止修改<br>            • 24小时内备份实验数据<br>            • 保留至少3次重复原始数据"
                },
                {
                    "id": "topic5",
                    "name": "临床转化与药物靶点研究",
                    "progress": "小分子筛选进行中",
                    "person_in_charge": "钱七",
                    "start_time": "2025年",
                    "next_plan": "完成筛选，验证候选药物效果",
                    "data_spec": "• 记录药物浓度和抑制率<br>            • 每周备份筛选数据<br>            • 标注药物信息，避免混淆"
                }
            ]
        }
        
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # 创建默认数据文件
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(default_data, f, ensure_ascii=False, indent=2)
            return default_data
    
    def update_html_files(self):
        """更新HTML文件"""
        topics_data = self.load_topics_data()
        
        # 更新index.html
        index_content = self.generate_index_html(topics_data['topics'])
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        # 更新每个课题的详情页
        for i, topic in enumerate(topics_data['topics']):
            topic_content = self.generate_topic_html(topic)
            with open(self.topic_files[i], 'w', encoding='utf-8') as f:
                f.write(topic_content)
        
        print("HTML文件已更新")
    
    def generate_index_html(self, topics):
        """生成index.html内容"""
        items_html = ""
        for topic in topics:
            items_html += f'    <div class="item"><a href="{topic["id"]}.html">{topic["name"]}</a></div>\n'
        
        html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>抗MDA5+皮肌炎免疫致病机制研究</title>
<style>
    *{{margin:0;padding:0;box-sizing:border-box;font-family:Microsoft YaHei}}
    body{{background:#f5f7fa}}
    header{{background:#004080;color:white;padding:20px 0;text-align:center}}
    .container{{max-width:700px;margin:40px auto;padding:0 15px}}
    .item{{background:white;padding:20px;border-radius:8px;margin-bottom:12px;box-shadow:0 1px 3px #00000010}}
    .item a{{color:#004080;font-size:16px;font-weight:bold;text-decoration:none}}
</style>
</head>
<body>
<header><h2>抗MDA5+皮肌炎免疫致病机制研究</h2></header>
<div class="container">
{items_html.rstrip()}
</div>
</body>
</html>"""
        return html_content
    
    def generate_topic_html(self, topic):
        """生成单个课题详情页内容"""
        # 为第一个课题（皮肌炎）添加特殊处理，包含网盘链接
        if topic["id"] == "topic1":
            extra_content = f'''
        <div class="line"><span class="label">研究内容：</span>{topic.get("research_content", "")}</div>

        <div class="line" style="margin-top:20px">
            <span class="label">细胞Marker库：</span>
            <a href="{topic.get("cell_marker_link", "")}" target="_blank" class="link">点击打开网盘（提取码：ame9）</a>
        </div>

        <div class="line">
            <span class="label">课题参考文献：</span>
            <a href="{topic.get("literature_link", "")}" target="_blank" class="link">点击打开网盘（提取码：qjdp）</a>
        </div>
 '''
        else:
            extra_content = ""
        
        html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{topic["name"]}</title>
<style>
    *{{margin:0;padding:0;box-sizing:border-box;font-family:Microsoft YaHei}}
    body{{background:#f5f7fa;line-height:1.7}}
    header{{background:#004080;color:white;padding:20px;text-align:center}}
    .back{{text-align:center;margin:15px 0}}
    .back a{{color:#004080;text-decoration:none}}
    .container{{max-width:700px;margin:0 auto 40px;padding:0 15px}}
    .box{{background:white;padding:30px;border-radius:8px;box-shadow:0 1px 3px #00000010}}
    .box h3{{color:#004080;margin-bottom:20px;font-size:20px}}
    .line{{margin:10px 0;font-size:15px}}
    .label{{font-weight:bold;width:100px;display:inline-block}}
    .notes{{background:#eef6ff;padding:12px 15px;border-radius:6px;margin-top:15px;font-size:14px}}
    .link{{color:#004080;font-weight:bold;text-decoration:underline}}
</style>
</head>
<body>
<header><h2>课题详情</h2></header>
<div class="back"><a href="index.html">← 返回课题总览</a></div>
<div class="container">
    <div class="box">
        <h3>{topic["name"]}</h3>
        <div class="line"><span class="label">当前进度：</span>{topic["progress"]}</div>
        <div class="line"><span class="label">负责人：</span>{topic["person_in_charge"]}</div>
        <div class="line"><span class="label">开始时间：</span>{topic["start_time"]}</div>
{extra_content}
        <div class="line"><span class="label">下一步计划：</span>{topic["next_plan"]}</div>
        <div class="notes">
            <strong>数据规范 & 注意事项：</strong><br>
            {topic["data_spec"]}
        </div>
    </div>
</div>
</body>
</html>"""
        return html_content

def main():
    updater = ProjectUpdater()
    
    print("蔡月明课题组内部平台 - 课题信息管理")
    print("1. 创建备份")
    print("2. 查看当前课题信息")
    print("3. 更新HTML文件")
    print("4. 退出")
    
    while True:
        choice = input("\n请选择操作 (1-4): ").strip()
        
        if choice == "1":
            updater.create_backup()
        elif choice == "2":
            data = updater.load_topics_data()
            print("\n当前课题信息:")
            for i, topic in enumerate(data['topics'], 1):
                print(f"{i}. {topic['name']}")
                print(f"   进度: {topic['progress']}")
                print(f"   负责人: {topic['person_in_charge']}")
                print(f"   下一步计划: {topic['next_plan']}\n")
        elif choice == "3":
            confirm = input("确定要更新HTML文件吗？(y/N): ").strip().lower()
            if confirm == 'y':
                updater.create_backup()
                updater.update_html_files()
                print("HTML文件已更新完成")
        elif choice == "4":
            print("退出程序")
            break
        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main()