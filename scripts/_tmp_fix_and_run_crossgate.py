from pathlib import Path
import runpy

path = Path('scripts/_tmp_align_crossgate_novelty.py')
text = path.read_text()
old = '    review += """\n'
new = '    review += r"""\n'
if text.count(old) != 1:
    raise SystemExit(f'raw-string target count={text.count(old)}')
path.write_text(text.replace(old, new))
runpy.run_path(str(path), run_name='__main__')
