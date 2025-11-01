# Windows键禁用器

这是一个使用PyQt5和keyboard库开发的Windows键禁用器程序，可以轻松地禁用和解锁Windows键。

## 功能特点

- 简洁的图形用户界面
- 一键禁用/解锁Windows键
- 实时状态显示
- 程序关闭时自动解锁Windows键
- 支持左Win键、右Win键和Command键

## 安装依赖

在运行程序之前，请确保安装所需的Python库：

```bash
pip install -r requirements.txt
```

或者手动安装：

```bash
pip install PyQt5==5.15.9
pip install keyboard==0.13.5
```

## 使用方法

1. 运行程序：
   ```bash
   python win_key_disabler.py
   ```

2. 点击"禁用Windows键"按钮来禁用Windows键
3. 再次点击按钮（此时显示为"解锁Windows键"）来解锁Windows键
4. 关闭程序时会自动解锁Windows键

## 注意事项

- 此程序需要以管理员权限运行才能正常工作
- 程序会阻止左Win键、右Win键和Command键
- 确保在关闭程序前解锁Windows键，或者让程序自动解锁

## 系统要求

- Windows操作系统
- Python 3.6或更高版本
- 管理员权限

## 文件说明

- `win_key_disabler.py` - 主程序文件
- `requirements.txt` - 依赖项列表
- `README.md` - 使用说明文档
