import re

def delete_html_tags(html_file, result_file='cleaned.txt', drop_empty_lines=True):

    with open(html_file, encoding='utf-8') as f:
        html = f.read()

    text = re.sub(r'<.*?>', '', html)

    lines = text.splitlines()
    if drop_empty_lines:
        lines = [ln.strip() for ln in lines if ln.strip()]
    else:
        lines = [ln.rstrip() for ln in lines]

    with open(result_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))



