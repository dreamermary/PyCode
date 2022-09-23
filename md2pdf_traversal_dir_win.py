from cgitb import html
import os
import markdown
import pdfkit
from tqdm import tqdm




def search_md(root):
    results = []

    names = os.listdir(root)

    for name in names:
        cur_path = os.path.join(root,name)
        if name.endswith('.md'):
            results.append(cur_path)
        elif os.path.isdir(cur_path):
            results += search_md(cur_path)
    return results

def convert(inmd_path,outpdf_path):
    html_str = md2html(inmd_path)

    html_path = r'E:\softdata\vscode\java\git\test\temp.html'
    outfile = open(html_path,'w',encoding='utf-8')
    outfile.write(html_str)
    outfile.close()


    html2pdf(html_path,outpdf_path)


def md2html(inmd): 
    '''
    return: hmtl str
    '''
    with open(inmd,'r',encoding='utf-8') as fmd:
        md = fmd.read()

        exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

        html = '''
        <html lang="zh-cn">
        <head>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <link href="github.css" rel="stylesheet">
        <link href="default.css" rel="stylesheet">
        </head>
        <body>
        %s
        </body>
        </html>
        '''

        ret = markdown.markdown(md,extensions=exts)
        return html % (ret)

def html2pdf(html_path:str,pdf_path:str):
    
    path_wkthmltopdf = r'D:\\com\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    #加上启动参数
    wkhtmltopdf_options = {
        'enable-local-file-access': None
    }
    # pdfkit.from_string(html_str, pdf_path, configuration=config, options=wkhtmltopdf_options)
    pdfkit.from_file(html_path, pdf_path, configuration=config, options=wkhtmltopdf_options)


# repo_root = r'E:\softdata\vscode\java\git\android_interview'
# out_root = r'E:\softdata\vscode\java\git\android_interview_pdf'
# # repo_root = r'E:\softdata\vscode\java\git\AndroidNote'
# # out_root = r'E:\softdata\vscode\java\git\AndroidNote_pdf'
repo_root = r'E:\softdata\vscode\java\git\test\testmd'
out_root = r'E:\softdata\vscode\java\git\test\testpdf'

md_list = search_md(repo_root)
for li in tqdm(md_list):
    out_pdf_path = li.replace(repo_root,out_root).replace(".md",".pdf")
    os.makedirs(os.path.dirname(out_pdf_path),exist_ok=True)
    try:
        if os.path.exists(out_pdf_path):
            pass
        else:
            convert(li,out_pdf_path)
    except:
        print(li)
