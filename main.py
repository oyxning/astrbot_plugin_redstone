from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import aiohttp
import os

@register(
    "astrbot_plugin_redstone",
    "LumineStory",
    "自动生成理解不了但中文的地狱笑话（使用硅基流动 API）",
    "1.0.0",
    "https://github.com/oyxning/astrbot_plugin_redstone"
)
class ChiShiXiaoZhuShou(Star):
    def __init__(self, context: Context):
        super().__init__(context)

        # —— 请设置你的硅基流动 API 信息 —— #
        self.api_base = os.getenv("SILICONFLOW_API_URL", "https://api.siliconflow.cn/v1")
        self.api_key = os.getenv("SILICONFLOW_API_KEY", "你的硅基流动API_KEY")
        self.model = os.getenv("SILICONFLOW_MODEL", "deepseek-ai/DeepSeek-V3")
        # ======================================== #

    @filter.command("来依托")
    async def yituo_handler(self, event: AstrMessageEvent):
        logger.info(f"[赤石小助手] 收到 /来依托，用户：{event.get_sender_id()}")

        prompt = (
            "请用中文生成一段“地狱笑话”"
            "要荒诞、无厘头、让人想笑，但是必须要让用户看得懂。"
        )

        url = f"{self.api_base}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300,
            "temperature": 0.8,
            "stream": False
        }

        try:
            async with aiohttp.ClientSession() as session:
                resp = await session.post(url, headers=headers, json=payload)
                if resp.status != 200:
                    text = await resp.text()
                    raise RuntimeError(f"API 返回码 {resp.status}, 内容：{text}")
                data = await resp.json()
                content = data["choices"][0]["message"]["content"].strip()

            if not content:
                raise ValueError("硅基流动返回内容为空")

            yield event.plain_result(f"😈 地狱笑话出炉（来自硅基流动）：\n{content}")

        except Exception as e:
            logger.error(f"[赤石小助手] 调用硅基流动 API 失败：{e}")
            yield event.plain_result("❌ 调用硅基流动 API 失败，请检查 KEY 或域名是否正确。")

    async def terminate(self):
        logger.info("赤石小助手插件已终止。")
