# generation/prompt_manager.py
class PromptManager:
    def __init__(self):
        self.templates = {
            'initial_idea': (
                "请毕业于 Harvard 的麦肯锡咨询专家，揣摩我的观点，帮助我思考，提出有效的问题并完善这个点子。"
                "带有强的逻辑性，创造性，以及批判性思维。\n\n"
                "主题：{theme}\n核心问题：{core_problem}"
            ),
            'generate_innovations': (
                "请顶尖的 OpenAI prompt engineer 帮助我思考，提出有效的问题，并且挖掘新的专利点。\n\n"
                "思考步骤：{steps}\n请描述出三个创新点。"
            ),
            # 添加更多模板
            'generate_patent': (
                "请基于以下内容，撰写一份详细的专利文档，包括背景技术、发明内容、具体实施方式、权利要求等部分。\n\n"
                "相关专利内容：\n{related_patents}\n\n"
                "用户输入：\n{user_input}"
            )
        }
    
    def get_prompt(self, template_name, **kwargs):
        template = self.templates.get(template_name)
        if not template:
            raise ValueError(f"未知的模板名称: {template_name}")
        return template.format(**kwargs)
