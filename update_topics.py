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
        self.backup_dir = "backups"
        
    def create_backup(self):
        """创建备份目录和备份文件"""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"backup_{timestamp}"
        
        # 备份HTML文件
        topic_files = [
            filename for filename in os.listdir(".")
            if filename.startswith("topic") and filename.endswith(".html")
        ]
        all_html_files = [self.index_file] + topic_files
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
                    "name": "抗MDA5+皮肌炎免疫致病机制研究",
                    "progress": "课题设计完成，准备开展样本实验",
                    "person_in_charge": "蔡月明课题组",
                    "start_time": "2025年",
                    "research_content": "围绕抗MDA5+皮肌炎相关间质性肺病，解析免疫细胞失衡、单核-巨噬细胞动态转化及干扰素信号通路异常，挖掘诊疗标志物。",
                    "cell_marker_link": "https://pan.baidu.com/s/183EB-VMgmspOj_NOog3lBQ",
                    "literature_link": "https://pan.baidu.com/s/1bNwFLGickvwNl-JNGTrxEg?pwd=qjdp",
                    "next_plan": "建立临床队列，开展流式细胞分型与单细胞测序分析",
                    "data_spec": "• 细胞分型严格参照网盘Marker标准<br>            • 临床样本严格保密、去标识化使用<br>            • 课题研究统一依据文献库进展"
                },
                {
                    "id": "topic2",
                    "name": "抗MDA5抗体阳性皮肌炎相关间质性肺病患者感染发生率的Meta分析",
                    "progress": "已完成初步查重与候选文献初筛，待老师确认题目",
                    "person_in_charge": "蔡月明课题组",
                    "start_time": "2026年",
                    "research_content": "以王虹丽DM/PM-RP-ILD系统综述与Meta分析为主要方法模板，围绕抗MDA5抗体阳性皮肌炎相关间质性肺病患者的感染相关结局开展系统综述与比例Meta分析。",
                    "template_reference": "主要参考DM/PM-RP-ILD Meta文章的方法框架；SLE肠道菌群文章用于参考自身免疫病选题思路和Introduction写法。",
                    "literature_link": "https://pan.baidu.com/s/1x4JH5S-Dlo2O1u6PentQHg?pwd=9uni",
                    "literature_code": "9uni",
                    "outcomes": "总感染发生率、CMV再激活率、PJP/PCP发生率、真菌/曲霉感染率、严重感染率、感染相关死亡率。",
                    "next_plan": "等待老师确认题目后，整理PROSPERO注册方案，开展正式数据库检索、文献筛选、全文下载、数据提取和R软件比例Meta分析。",
                    "data_spec": "• 避免与已注册治疗策略Meta方向重复<br>            • 提取每篇研究的事件人数和总人数<br>            • 记录检索来源、纳排理由、质量评价和统计分析过程"
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
        for topic in topics_data['topics']:
            topic_content = self.generate_topic_html(topic)
            with open(f'{topic["id"]}.html', 'w', encoding='utf-8') as f:
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
        extra_parts = []

        if topic.get("research_content"):
            extra_parts.append(f'''
        <div class="line"><span class="label">研究内容：</span>{topic.get("research_content", "")}</div>
''')

        if topic.get("template_reference"):
            extra_parts.append(f'''
        <div class="line"><span class="label">模板参考：</span>{topic.get("template_reference", "")}</div>
''')

        if topic.get("outcomes"):
            extra_parts.append(f'''
        <div class="line"><span class="label">主要结局：</span>{topic.get("outcomes", "")}</div>
''')

        if topic.get("cell_marker_link"):
            extra_parts.append(f'''
        <div class="line" style="margin-top:20px">
            <span class="label">细胞Marker库：</span>
            <a href="{topic.get("cell_marker_link", "")}" target="_blank" class="link">点击打开网盘（提取码：ame9）</a>
        </div>
''')

        if topic.get("literature_link"):
            literature_code = topic.get("literature_code", "qjdp")
            extra_parts.append(f'''
        <div class="line">
            <span class="label">课题参考文献：</span>
            <a href="{topic.get("literature_link", "")}" target="_blank" class="link">点击打开网盘（提取码：{literature_code}）</a>
        </div>
''')

        extra_content = "".join(extra_parts)
        
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
