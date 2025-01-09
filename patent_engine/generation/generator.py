# generation/generator.py
import openai
from config.config import Config
import logging

openai.api_key = Config.OPENAI_API_KEY

class PatentGenerator:
    def __init__(self, prompt_manager):
        self.prompt_manager = prompt_manager
    
    def generate(self, prompt, max_tokens=1500):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # 使用更强大的模型
                messages=[
                    {"role": "system", "content": "你是一个专业的专利撰写助手。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.7,
                timeout=20
            )
            content = response.choices[0].message.content.strip()
            logging.info("专利生成成功。")
            return content
        except openai.APIError as e:
            logging.error(f"OpenAI API 调用失败: {e}")
            return None
