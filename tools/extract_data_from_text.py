import re

class ExtractDataFromText():
    def extract_data_from_text(self, text, pattern):
        matches = re.findall(pattern, text, flags=re.DOTALL | re.IGNORECASE)
        
        if matches:
            data = matches[0].strip()
            return data
        else:
            return None

    def extract_all_data_from_the_text(self, text, pattern):
        matches = re.findall(pattern, text, flags=re.DOTALL | re.IGNORECASE)
        
        if matches:
            data = [match.strip() for match in matches]
            return data
        else:
            return []