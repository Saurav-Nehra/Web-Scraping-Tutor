import json
from pathlib import Path
from ..utils.config import RAW_DIR, OUTPUT_DIR
from ..transform.cleaner import strip_html




def issue_to_record(issue):
fields = issue.get('fields', {})
comments = []
# comments may be expanded as rendered fields or separate API calls - guard both
if 'comment' in fields and 'comments' in fields['comment']:
for c in fields['comment']['comments']:
comments.append({'author': c.get('author', {}).get('displayName'), 'body': strip_html(c.get('body')) , 'created': c.get('created')})
# fallback: check renderedFields or changelog (not exhaustive)
rec = {
'id': issue.get('id'),
'key': issue.get('key'),
'title': fields.get('summary'),
'project': fields.get('project', {}).get('key'),
'reporter': fields.get('reporter', {}).get('displayName') if fields.get('reporter') else None,
'assignee'
