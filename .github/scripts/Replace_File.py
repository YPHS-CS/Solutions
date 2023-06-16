import os
import shutil

def move_files(source_dir):
    """
    将指定目录下的特定文件移动到另一个指定目录
    """
    # 获取源目录下的所有文件名
    filenames = os.listdir(source_dir)
    print('filenames', filenames)
    for filename in filenames:
        # 判断是否是目标文件
        if "readme" not in filename.lower():
            # 构造源文件路径和目标文件路径
            
            mp = {"ZEROJUDGE":"ZeroJudge", "CODEFORCES":"CodeForces", "TIOJ":"TIOJ", "APCS":"APCS"}
            # 移动文件
            
            
            judge = None
            for name in mp:
              if name in filename:
                judge = name
            if judge == None:
                continue
            src_path = os.path.join(source_dir, filename)
            
            problem = filename.replace(f"{judge}-", "")
            problem_store_folder = f"./Solutions/{mp[judge]}/{os.path.splitext(problem)[0]}"

            if not os.path.exists(problem_store_folder):
               os.makedirs(problem_store_folder)

            dst_path = os.path.join(problem_store_folder, os.path.splitext(problem)[0]+f"-{len(os.listdir(problem_store_folder))}"+os.path.splitext(problem)[1])
            shutil.move(src_path, dst_path)
                

if __name__ == "__main__":
    # 设置源目录和目标目录
    source_dir = "."
    move_files(source_dir)
