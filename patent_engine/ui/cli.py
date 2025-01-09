# ui/cli.py
import argparse
from data_management.importer import import_patents_from_directory
from retrieval.search_engine import SearchEngine
from generation.prompt_manager import PromptManager
from generation.generator import PatentGenerator
from quality_control.checker import QualityChecker
import logging

def main():
    parser = argparse.ArgumentParser(description="专利库系统")
    parser.add_argument('--import', type=str, help="导入专利文件的目录")
    parser.add_argument('--search', type=str, help="搜索专利")
    parser.add_argument('--generate', type=str, help="生成新专利，提供主题")
    args = parser.parse_args()
    
    if args.import:
        import_patents_from_directory(args.import)
    
    if args.search:
        search_engine = SearchEngine()
        results = search_engine.search(args.search)
        for patent in results:
            print(f"标题: {patent.title}\n摘要: {patent.abstract}\n")
    
    if args.generate:
        search_engine = SearchEngine()
        prompt_manager = PromptManager()
        generator = PatentGenerator(prompt_manager, search_engine)
        checker = QualityChecker()
        
        user_input = args.generate
        generated = generator.generate_with_rag(user_input, top_k=5)
        
        if generated:
            is_valid = checker.run_all_checks(generated)
            if is_valid:
                print("生成的专利内容:\n", generated)
                # 可以选择保存到数据库或文件
            else:
                print("生成的专利内容不完整或格式不符合要求。")
        else:
            print("生成失败。")

if __name__ == "__main__":
    main()
