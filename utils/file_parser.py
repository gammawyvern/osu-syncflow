from typing import Dict, List
import re

def get_sections(file_content: str) -> Dict[str, List[str]]:
    sections: Dict[str, List[str]] = {}
    section_header_pattern = re.compile(r'^\[(.*)\]$')
    
    current_section = ""
    sections[current_section] = []

    for line in file_content.splitlines():
        stripped = line.strip()
        if not stripped:
            continue  

        match = section_header_pattern.match(stripped)
        if match:
            current_section = match.group(1)
            sections.setdefault(current_section, [])
        else:
            sections[current_section].append(stripped)

    return sections

