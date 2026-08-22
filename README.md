# 打造世界修改器 · CraftWorld Modifier

适用于 Steam 版 **Craft The World / 打造世界** 的 Windows 桌面修改器。它把常用的资源、成长、生物、物品、魔法、世界事件与地图操作整合在一个本地界面中，并尽量让每项写入具备范围检查、即时读回与可追溯的操作记录。

> 当前正式版本：**v1.0.0**。请始终先备份存档；游戏更新后，旧版定位结果可能需要重新验证。

![打造世界修改器主界面](docs/images/main-panel.png)

## 主要内容

- **基础功能**：金币、法力、经验、游戏时间与速度，以及红门倒计时和事件控制。
- **世界事件**：潘多拉盒子事件目录、下一事件安排、倒计时与队列控制。
- **生物管理**：矮人与已识别生物列表、状态与坐标读取、培养预设、装备预设和矮人生成。
- **物品与配方**：物品目录、常用物品、数量读取与已验证修改、配方编辑。
- **魔法与地图**：常用魔法参数、地图读取、标记和已验证的地图编辑工具。
- **离线存档与记录**：存档备份/校验/恢复入口，以及本次会话的操作记录与可撤销项目。

功能仅在游戏运行时使用；不会上传存档、游戏目录或个人配置。

## 使用 EXE

1. 前往仓库的 [Releases](../../releases) 下载 `CraftWorldModifier.exe`。
2. 启动游戏并进入存档，再运行修改器。
3. 点击“连接游戏”，确认顶部状态显示连接成功后再使用相应功能。
4. 首次启动会后台查询一次最新 Release，仅更新顶部版本文字；不会自动下载、替换或重启。

个人设置保存在：

`%LOCALAPPDATA%\CraftWorldModifier\config\user_data.json`

因此替换或更新 EXE 不会覆盖你的预设、地图标记和其它个人设置。

## 更新中心

- **立即检查**：重新读取 GitHub 最新 Release，不下载文件。
- **下载并校验**：下载新版本、核对文件大小和 SHA-256 后暂存。
- **应用并重启**：使用已暂存的更新包替换修改器 EXE 并重新打开。
- **关闭**：关闭更新窗口，不执行任何更新。

## 从源码运行

环境：Windows 10/11、Python 3.10+、Steam 版游戏。

```powershell
python -m pip install -r requirements.txt
python .\craft_web_v1.0.py
```

## 构建单文件 EXE

安装构建依赖后运行：

```powershell
python -m pip install -r requirements-build.txt
powershell -ExecutionPolicy Bypass -File .\build_release.ps1
```

输出文件为 `发布包\CraftWorldModifier.exe`。它会把界面、默认配置、方块数据与物品翻译数据打入一个 EXE；个人配置不会参与构建。

## 目录说明

- `craft_web_v1.0.py`：Python 后端、游戏读取/写入与更新逻辑。
- `ui_v1.0.html`：桌面界面。
- `block_data.py`、`item_translations.txt`：随程序读取的方块和名称数据。
- `config/marks.json`：不含个人数据的默认配置模板。
- `build_release.ps1`：构建单文件 EXE 的脚本。
- `docs/images/main-panel.png`：主界面截图。

## 使用提示

- 游戏或模组更新后，先在副本存档上确认读取和写入是否仍正常。
- 看到“定位失效”“版本不支持”或“游戏未确认该操作”时，不要把显示值当作实际写入结果。
- 对会改变世界、物品或生物的数据，优先使用操作记录中的已验证撤销项；重要存档请先使用“离线存档”备份。
