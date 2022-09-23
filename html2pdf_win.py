from cgitb import html
import pdfkit
import sys

def html2pdf(html,pdf):
	path_wkthmltopdf = r'D:\\com\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
	config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
	#加上启动参数
	wkhtmltopdf_options = {
		'enable-local-file-access': None
	}

	pdfkit.from_file(html, pdf, configuration=config, options=wkhtmltopdf_options)

# usage: python html2pdf_win.py test1.html test1.pdf
html2pdf(sys.argv[1],sys.argv[2])