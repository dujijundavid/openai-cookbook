import openai
import os
import logging
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定义使用的模型名称
MODEL_NAME = "gpt-4-mini"

def generate_completion(model, messages, max_tokens):
    """
    调用 OpenAI API 生成回复。

    :param model: 使用的模型名称
    :param messages: 消息列表，包含系统和用户消息
    :param max_tokens: 回复的最大长度
    :return: 模型生成的回复文本
    """
    try:
        response = openai.ChatCompletion.acreate(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            timeout=10  # 设置超时时间为10秒
        )
        content = response.choices[0].message['content'].strip()
        logging.info(f"模型 {model} 成功生成回复。")
        return content
    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API 调用失败: {e}")
        return None

def save_to_file(filename, content):
    """
    将内容保存到文件。

    :param filename: 文件名
    :param content: 要保存的内容
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.info(f"内容已成功保存到 {filename}")
    except IOError as e:
        logging.error(f"文件保存失败: {e}")

def step1_generate_initial_idea():
    step1_input = """
    目标：

    我需要你去帮助我构思并且梳理观点，它的主题是：

    -

    核心需要解决的问题：如何写专利，限制在100个token内。

    首先，请毕业于 Harvard 的麦肯锡咨询专家，揣摩我的观点，帮助我思考，提出有效的问题并完善这个点子。带有强的逻辑性，创造性，以及批判性思维。
    """
    step1_output = generate_completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "你是一个毕业于 Harvard 的麦肯锡咨询专家。"},
            {"role": "user", "content": step1_input}
        ],
        max_tokens=100
    )
    if step1_output:
        save_to_file("step1_output.txt", step1_output)
    return step1_output

def step2_generate_innovations():
    step2_input = """
    首先，请顶尖的 OpenAI prompt engineer 帮助我思考，提出有效的问题，并且挖掘新的专利点。

    不着急，think step by step，加入你的思考逻辑，描述出三个创新点。
    """
    step2_output = generate_completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "你是一个顶尖的 OpenAI prompt engineer。"},
            {"role": "user", "content": step2_input}
        ],
        max_tokens=1500
    )
    if step2_output:
        save_to_file("step2_output.txt", step2_output)
    return step2_output

def step3_answer_questions():
    step3_input = """
    1. 为了这项发明进行了哪些工作？
    2. 本发明解决了哪些技术问题？
    3. 知悉与本发明相关的背景知识或现有技术吗（例如专利文献、竞品等），其存在的缺点是什么？
    4. 问题的解决方案是什么？
    5. 本发明可以实现哪些有益效果和/或优势？
    6. 以简短摘要的形式用英文概括本发明的核心内容？
    """
    step3_output = generate_completion(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": step3_input}
        ],
        max_tokens=1500
    )
    if step3_output:
        save_to_file("step3_output.txt", step3_output)
    return step3_output

def step4_customize_patent(step3_content):
    step4_input = f"""
    针对以下问题解决方案：为 Mercedes Benz 写出定制化的专利，优化，加入 Mercedes 数据科学家和研究科学家的理解，技术负责人加入更多技术实现和算法的细节。将这部分进一步的细节公式化，模型化，以便专利不会被查出重复。

    问题解决方案：

    {step3_content}
    """
    step4_output = generate_completion(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": step4_input}
        ],
        max_tokens=1500
    )
    if step4_output:
        save_to_file("step4_output.txt", step4_output)
    return step4_output

def main():
    logging.info("开始执行专利生成流程。")

    # 步骤 1
    logging.info("执行步骤 1：生成初始想法。")
    step1_output = step1_generate_initial_idea()
    if not step1_output:
        logging.error("步骤 1 失败，终止流程。")
        return

    # 步骤 2
    logging.info("执行步骤 2：生成创新点。")
    step2_output = step2_generate_innovations()
    if not step2_output:
        logging.error("步骤 2 失败，终止流程。")
        return

    # 步骤 3
    logging.info("执行步骤 3：回答专利相关问题。")
    step3_output = step3_answer_questions()
    if not step3_output:
        logging.error("步骤 3 失败，终止流程。")
        return

    # 步骤 4
    logging.info("执行步骤 4：定制化专利撰写。")
    step4_output = step4_customize_patent(step3_output)
    if not step4_output:
        logging.error("步骤 4 失败，终止流程。")
        return

    logging.info("专利生成流程已完成。所有输出已保存到文件。")

if __name__ == "__main__":
    main()
