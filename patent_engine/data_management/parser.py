# data_management/parser.py
import textract
import re

def parse_patent_file(file_path):
    # 使用 textract 提取文本
    text = textract.process(file_path).decode('utf-8')
    # 实现专利文本的解析逻辑，提取标题、摘要、权利要求等
    patent_data = {
        'title': extract_title(text),
        'abstract': extract_abstract(text),
        'claims': extract_claims(text),
        'description': extract_description(text),
        'filing_date': extract_filing_date(text),
        'inventor': extract_inventor(text),
        'ipc_class': extract_ipc_class(text)
    }
    return patent_data

def extract_title(text):
    match = re.search(r'Title:\s*(.*)', text)
    return match.group(1).strip() if match else "示例标题"

def extract_abstract(text):
    match = re.search(r'Abstract:\s*([\s\S]*?)\n\n', text)
    return match.group(1).strip() if match else "示例摘要"

def extract_claims(text):
    match = re.search(r'Claims:\s*([\s\S]*?)\n\n', text)
    return match.group(1).strip() if match else "示例权利要求"

def extract_description(text):
    match = re.search(r'Description:\s*([\s\S]*?)\n\n', text)
    return match.group(1).strip() if match else "示例描述"

def extract_filing_date(text):
    match = re.search(r'Filing Date:\s*(\d{4}-\d{2}-\d{2})', text)
    return match.group(1) if match else None

def extract_inventor(text):
    match = re.search(r'Inventor:\s*(.*)', text)
    return match.group(1).strip() if match else "示例发明人"

def extract_ipc_class(text):
    match = re.search(r'IPC Class:\s*(.*)', text)
    return match.group(1).strip() if match else "示例分类号"
