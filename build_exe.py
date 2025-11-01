#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows键禁用器打包脚本
使用PyInstaller将程序打包成可执行文件
"""

import os
import sys
import subprocess
import shutil

def build_executable():
    """构建可执行文件"""
    print("开始打包Windows键禁用器...")
    
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_script = os.path.join(current_dir, "win_key_disabler.py")
    
    # 检查主程序文件是否存在
    if not os.path.exists(main_script):
        print(f"错误：找不到主程序文件 {main_script}")
        return False
    
    # PyInstaller命令参数
    # --onefile: 打包成单个可执行文件
    # --windowed: 无控制台窗口（适用于GUI程序）
    # --name: 指定可执行文件名称
    # --icon: 指定图标（如果有的话）
    # --add-data: 添加额外数据文件
    # --clean: 清理临时文件
    # --noconfirm: 不询问确认
    
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "Windows键禁用器",
        "--clean",
        "--noconfirm",
        main_script
    ]
    
    print("执行命令:", " ".join(cmd))
    
    try:
        # 执行打包命令
        result = subprocess.run(cmd, cwd=current_dir, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("打包成功！")
            print(result.stdout)
            
            # 检查输出目录
            dist_dir = os.path.join(current_dir, "dist")
            exe_file = os.path.join(dist_dir, "Windows键禁用器.exe")
            
            if os.path.exists(exe_file):
                print(f"可执行文件已生成: {exe_file}")
                print(f"文件大小: {os.path.getsize(exe_file) / 1024 / 1024:.2f} MB")
                
                # 询问是否复制到当前目录
                target_file = os.path.join(current_dir, "Windows键禁用器.exe")
                if os.path.exists(target_file):
                    os.remove(target_file)
                
                shutil.copy2(exe_file, target_file)
                print(f"可执行文件已复制到: {target_file}")
                
                return True
            else:
                print("错误：找不到生成的可执行文件")
                return False
        else:
            print("打包失败！")
            print("错误输出:", result.stderr)
            return False
            
    except Exception as e:
        print(f"打包过程中发生错误: {str(e)}")
        return False

if __name__ == "__main__":
    success = build_executable()
    if success:
        print("\n打包完成！")
        print("注意事项：")
        print("1. 程序需要以管理员权限运行才能正常工作")
        print("2. 首次运行时可能会被防病毒软件误报，请添加信任")
        print("3. 程序会自动处理Windows键的禁用和解锁")
    else:
        print("\n打包失败，请检查错误信息")
        sys.exit(1)