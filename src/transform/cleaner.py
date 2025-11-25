import re




def strip_html(text):
if not text:
return ''
# strip simple HTML tags
cleaned = re.sub(r'<[^>]+>', '', text)
# convert multiple spaces/newlines
cleaned = re.sub(r'\s+', ' ', cleaned).strip()
return cleaned
