"""Листы Prepare в формате sp8: S = [(тема, примечание, [(term, подпись, описание)…])]."""
from words import S as _S, NOTE
S = [('Prepare', ' '.join(dict.fromkeys(NOTE[t] for t, *_ in ws if t in NOTE)), [(t, c, d) for t, c, d, _ in ws]) for ws in _S]
DIGITS, REPL = [], {}
