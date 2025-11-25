import json
from pathlib import Path

def generate_tasks(jsonl_in, jsonl_out=None):
    """
    Read a JSONL corpus produced by jsonl_converter and create a simple
    derived task file (summarization placeholder).
    """
    jsonl_in = Path(jsonl_in)
    if not jsonl_in.exists():
        raise FileNotFoundError(f"Input file not found: {jsonl_in}")

    jsonl_out = Path(jsonl_out or jsonl_in.parent / (jsonl_in.stem + '_tasks.jsonl'))
    with jsonl_in.open('r', encoding='utf-8') as inf, jsonl_out.open('w', encoding='utf-8') as outf:
        for line in inf:
            obj = json.loads(line)
            text = (obj.get('title') or '') + '\n\n' + (obj.get('description') or '')
            # Simple deterministic summary placeholder (trim to 512 chars)
            summary = text[:512]
            qa = {
                'id': obj.get('key'),
                'task': 'summarization',
                'input': text,
                'output': summary
            }
            outf.write(json.dumps(qa, ensure_ascii=False) + '\n')
    return jsonl_out

if __name__ == '__main__':
    # default locate the processed file
    from ..utils.config import OUTPUT_DIR
    in_file = Path(OUTPUT_DIR) / 'jira_corpus.jsonl'
    out = generate_tasks(in_file)
    print('Wrote tasks to:', out)
