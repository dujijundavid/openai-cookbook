# data_management/importer.py
import os
from .database import Patent, get_session
from .parser import parse_patent_file
import uuid
import logging

def import_patents_from_directory(directory_path):
    session = get_session()
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf') or filename.endswith('.docx'):
            file_path = os.path.join(directory_path, filename)
            try:
                patent_data = parse_patent_file(file_path)
                patent = Patent(
                    id=str(uuid.uuid4()),
                    title=patent_data['title'],
                    abstract=patent_data['abstract'],
                    claims=patent_data['claims'],
                    description=patent_data['description'],
                    filing_date=patent_data.get('filing_date'),
                    inventor=patent_data.get('inventor'),
                    ipc_class=patent_data.get('ipc_class')
                )
                session.add(patent)
                logging.info(f"成功导入专利: {patent.title}")
            except Exception as e:
                logging.error(f"导入失败 {filename}: {e}")
    session.commit()
    session.close()
