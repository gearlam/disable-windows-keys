@echo off
chcp 65001 >nul
echo ========================================
echo Windows键禁用器 - 一键打包工具
echo ========================================
echo.

echo 正在检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误：未找到Python环境，请先安装Python
    pause
    exit /b 1
)

echo Python环境检查通过
echo.

echo 正在检查依赖库...
python -c "import PyQt5, keyboard" >nul 2>&1
if errorlevel 1 (
    echo 正在安装依赖库...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo 错误：依赖库安装失败
        pause
        exit /b 1
    )
)

echo 依赖库检查通过
echo.

echo 正在检查PyInstaller...
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo 正在安装PyInstaller...
    pip install pyinstaller
    if errorlevel 1 (
        echo 错误：PyInstaller安装失败
        pause
        exit /b 1
    )
)

echo PyInstaller检查通过
echo.

echo 开始打包程序...
python build_exe.py

echo.
echo ========================================
echo 打包完成！
echo ========================================
echo.
echo 可执行文件位置：
echo - 当前目录：Windows键禁用器.exe
echo - 构建目录：dist\Windows键禁用器.exe
echo.
echo 注意事项：
echo 1. 程序需要以管理员权限运行
echo 2. 首次运行可能被防病毒软件误报
echo 3. 程序会自动处理Windows键的禁用和解锁
echo.
pause