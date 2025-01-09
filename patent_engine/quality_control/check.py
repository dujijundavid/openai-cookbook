# quality_control/checker.py
import re
import logging

class QualityChecker:
    def __init__(self):
        pass
    
    def check_completeness(self, patent_text):
        # 检查是否包含必要部分
        required_sections = ['背景技术', '发明内容', '具体实施方式', '权利要求']
        missing_sections = [section for section in required_sections if section not in patent_text]
        if missing_sections:
            logging.warning(f"缺失部分: {', '.join(missing_sections)}")
            return False, missing_sections
        return True, []
    
    def check_consistency(self, patent_text):
        # 检查标题与摘要是否一致（简单示例）
        title_match = re.search(r'专利标题:\s*(.*)', patent_text)
        abstract_match = re.search(r'摘要:\s*(.*)', patent_text)
        if title_match and abstract_match:
            title = title_match.group(1).strip()
            abstract = abstract_match.group(1).strip()
            if title.lower() not in abstract.lower():
                logging.warning("标题在摘要中未充分体现。")
                return False, ["标题与摘要不一致"]
        return True, []
    
    def check_format(self, patent_text):
        # 检查格式，如段落编号
        return True, []
    
    def run_all_checks(self, patent_text):
        completeness, missing = self.check_completeness(patent_text)
        consistency, _ = self.check_consistency(patent_text)
        format_ok, _ = self.check_format(patent_text)
        return completeness and consistency and format_ok
