# 赤石小助手（astrbot_plugin_redstone）

这是一个适用于 [AstrBot](https://astrbot.app) 的插件，用于生成令人迷惑的“地狱笑话”。本插件调用 **硅基流动 API**，支持多种国产大语言模型。

## 🧠 功能简介

通过指令 `/来依托`，调用大模型自动生成荒诞、无厘头却结构完整的“地狱笑话”。

## 🚀 安装与使用

### 1. 添加插件

将插件代码放入插件文件夹。

### 2. 设置环境变量

你需要配置以下变量：

```bash
export SILICONFLOW_API_KEY=你的API密钥
export SILICONFLOW_MODEL=internlm/internlm2_5-7b-chat
export SILICONFLOW_API_URL=https://api.siliconflow.cn/v1
```

也可以通过 `.env` 文件配置。

## 🔧 指令说明

| 指令 | 描述                         |
|------|------------------------------|
| /来依托 | 生成中文地狱笑话（使用 LLM） |

## 💡 示例

```bash
/来依托
😈 地狱笑话出炉：
“ 拔舌地狱现已开通自助服务，舌钉可抵扣30%的业力。”
```

## 📦 依赖

- Python 3.8+

## 🙋‍♂️ 联系与支持

如有问题欢迎访问插件主页或提交 Issue：

🔗 [插件主页](https://github.com/oyxning/astrbot_plugin_redstone)  
📚 [AstrBot 文档](https://astrbot.app)

## 📝 License

MIT License