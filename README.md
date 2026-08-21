# CraftWorld Modifier

Craft The World 的桌面修改器正式版源代码。

## 运行

直接运行 `craft_web_v1.0.py`，或使用维护者提供的单文件 `CraftWorldModifier.exe`。

用户配置不会写入程序目录，而是保存到：

`%LOCALAPPDATA%\CraftWorldModifier\config\user_data.json`

因此更新或替换程序不会覆盖个人设置。

## 文件

- `craft_web_v1.0.py`：Python 后端与内存读写逻辑
- `ui_v1.0.html`：桌面界面
- `block_data.py`：方块与地图数据
- `item_translations.txt`：物品名称翻译数据
- `config/marks.json`：干净的默认配置模板，不包含用户数据

## 发布与更新

维护者使用构建目录中的脚本生成 EXE。程序启动后会检查内置的 GitHub Releases 更新地址；有新版本时只提示用户选择，不会强制更新。

