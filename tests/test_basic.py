from src.transform.cleaner import strip_html

def test_strip_html_basic():
    assert strip_html('<b>hello</b>') == 'hello'
    assert strip_html('<p>line1</p><br><p>line2</p>') == 'line1 line2'
    assert strip_html(None) == ''
