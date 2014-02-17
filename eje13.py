import textwrap

def wraptext(text, width):
	dedented_text = textwrap.dedent(text).strip()
	print textwrap.fill(dedented_text, width=width)
