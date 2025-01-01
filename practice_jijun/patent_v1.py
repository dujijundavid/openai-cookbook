import openai

# 设置API密钥
# Step 1: 使用gpt-4-mini
step1_input = """
目标：

我需要你去帮助我构思并且梳理观点，它的主题是：

-

核心需要解决的问题：如何写专利，限制在100个token内。

首先，请毕业于Harvard的麦肯锡咨询专家，揣摩我的观点，帮助我思考，提出有效的问题并完善这个点子。带有强的逻辑性，创造性，以及批判性思维。
"""

response_step1 = openai.Completion.create(
  engine="gpt-4-mini",
  prompt=step1_input,
  max_tokens=100
)

step1_output = response_step1.choices[0].text.strip()

# Step 2: 使用gpt-4o
step2_input = """
首先，请顶尖的OpenAI prompt engineer帮助我思考，提出有效的问题，并且挖掘新的专利点。

不着急，think step by step, 加入你的思考逻辑，描述出三个创新点。
"""

response_step2 = openai.Completion.create(
  engine="gpt-4o",
  prompt=step2_input,
  max_tokens=1500
)

step2_output = response_step2.choices[0].text.strip()

# Step 3: 使用gpt-4-mini
step3_input = """
1. 为了这项发明进行了哪些工作？
2. 本发明解决了哪些技术问题？
3. 知悉与本发明相关的背景知识或现有技术吗（例如专利文献、竞品等），其存在的缺点是什么？
4. 问题的解决方案是什么？
5. 本发明可以实现哪些有益效果和/或优势？
6. 以简短摘要的形式用英文概括本发明的核心内容？
"""

response_step3 = openai.Completion.create(
  engine="gpt-4-mini",
  prompt=step3_input,
  max_tokens=1500
)

step3_output = response_step3.choices[0].text.strip()

# Step 4: 使用gpt-4o
step4_input = f"""
针对以下问题解决方案：为Mercedes Benz写出customized patent，优化，加入Mercedes data scientist和research scientist的理解，Tech Lead加入更多技术实现和算法的细节。将这部分进一步的细节公式化，模型化，以便patent不会被查出重复。

问题解决方案：

{step3_output}
"""

response_step4 = openai.Completion.create(
  engine="gpt-4o",
  prompt=step4_input,
  max_tokens=1500
)

step4_output = response_step4.choices[0].text.strip()

# 保存到文件
with open('basic_information.txt', 'w', encoding='utf-8') as f:
    f.write(step3_output)

with open('technical_details.txt', 'w', encoding='utf-8') as f:
    f.write(step4_output)