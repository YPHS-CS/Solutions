import os
import shutil
import datetime

def move_files(source_dir):
    """
    将指定目录下的特定文件移动到另一个指定目录
    """
    
    filenames = os.listdir(source_dir)
    print('filenames', filenames)
    for filename in filenames:
        if filename.find('-') == -1:
            continue

        judge = filename.split('-')[0]
        print(filename)
        src_path = os.path.join(source_dir, filename)
        
        problem = filename.replace(f"{judge}-", "")
        problem_store_folder = f"./Solutions/{judge.upper()}/{os.path.splitext(problem)[0]}"
        if not os.path.exists(problem_store_folder):
           os.makedirs(problem_store_folder)
        dst_path = os.path.join(problem_store_folder, os.path.splitext(problem)[0]+f"-{len(os.listdir(problem_store_folder))}"+os.path.splitext(problem)[1])
        shutil.move(src_path, dst_path)
                
                
def update_readme(source_dir):
    Solutions = {}
    cnt_all = 0
    cnt = 0
    for folder in sorted(os.listdir(source_dir)):
        Solutions[folder] = []
        folder_path = os.path.join(source_dir, folder)
        for question in sorted(os.listdir(folder_path)):
            question_path = os.path.join(folder_path, question)
            Solutions[folder].append((question, f"https://github.com/YPHS-CS/Solutions/tree/main/Solutions/{folder}/{question}"))

            cnt_all += len(os.listdir(question_path))
            cnt += 1

    content = """
# Solutions

要互助這一個資料庫才可以好，不然現在看起來超弱的。
```
只能上傳在根目錄
檔案名稱應該如下才可以

平台名稱-題目編號.副檔名
如
ZEROJUDGE-a001.cpp
```

"""
    content += f"`總共完成了 {cnt} 個題目。`\n"
    content += f"`總共有 {cnt_all} 個解。`\n"
    for i in Solutions:
        content += f"### {i}\n"
        for j in Solutions[i]:
            content += f"[`{j[0]}`]({j[1]}) "
        content += "\n"

    content += f'\n###### Last Updated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    with open("README.md", 'w') as file:
        file.write(content)
if __name__ == "__main__":
    move_files(".")
    update_readme("./Solutions")
