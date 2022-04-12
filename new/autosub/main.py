# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   main.py
# @Time    :   2021/4/7 14:25
from concurrent.futures.thread import ThreadPoolExecutor

import new._0_prepare as _0_prepare
import new._00_crawler_xmly as _00_crawler_xmly
import new._2_split_back as _2_split_back
import new._4_cutting_piece as _4_cutting_piece
import _3_gene_subtitle


if __name__ == '__main__':
    _0_prepare.main()

    _00_crawler_xmly.main()

    _2_split_back.main()

    _3_gene_subtitle.main()

    _4_cutting_piece.main()

