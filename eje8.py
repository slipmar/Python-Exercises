import markdown
import codecs

def txttohtml(pathIn, pathOut):
	input_file = codecs.open(pathIn, mode="r", encoding="utf-8")
	text = input_file.read()
	html = markdown.markdown(text)

	output_file = codecs.open(pathOut, "w", 
		encoding="utf-8", 
		errors="xmlcharrefreplace"
	)

	output_file.write(html)