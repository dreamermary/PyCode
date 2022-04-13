# -*- coding: UTF-8 -*-
#
# if __name__ == '__main__':
#     langCode = "zh"
#     sList = [
#         "D:\\temp_file\\月亮与六便士\\output\\月亮与六便士043\\vocals.wav",
#         "D:\\temp_file\\月亮与六便士\\output\\月亮与六便士045（end）\\vocals.wav",
#
#     ]
#     oList = [
#         "D:\\temp_file\\月亮与六便士\\text\\月亮与六便士043.zh-cn.srt",
#         "D:\\temp_file\\月亮与六便士\\text\\月亮与六便士045（end）.zh-cn.srt",
#         ]
#     for sourceFile,outputFileSRT in zip(sList,oList):
#         fOutput = ctr_autosub.Ctr_Autosub.generate_subtitles(source_path = sourceFile,
#                                                  output = outputFileSRT,
#                                                  src_language = langCode,
#                                                  listener_progress = None)
#
#         print(fOutput)
#     print("ok")
#
import _3_gene_subtitle
if __name__ == '__main__':
    _3_gene_subtitle.temp()

