import requests
import re
import time
import os
from contextlib import closing

count = 0

kv_video = {
    'cookie': 'STUDY_PERSIST="aB3nOkxcPNgwAe5iJFKKSMbImXt1xp+axKXoEPw5DZ3lUpL+NmaTG1meuRlRql2LBBR5z8N4snwDLC1Hk/JCU5wogOkvdb25CLmrCR592cxxt1TYn3vOJnxEQjDwU3QOSBFq7tLt4/0TY4P/yWEtEKTlwrbLnoNaNhoRba10Guvw9tyk7C+ocDLDdFL2CikkBmjrmzvA4pJPOwea1JsWn10I7TB5rN2wUSeHvW1YKYJOSdFA6J5jrZLCRv8JU8qN8WQLi3xTJ45sq/acjsEWiA=="; STUDY_SESS="n1oSkC6ko6uwOFVCPjH6m8uTeduOsKbkwyDflnyQJXOl3vVC3smdubFKwXv7eRBsk0PiktV4/v0kYjeepJ6w/P2HLxIDVPCEj+mrsdXzBxEdKx2NprgKRmA2ASqWiN88+bvOgwkdnyLMPsKBqr6QkQOJKpJ7RGlYQMGBRvKDF9Inppr6KrivyjY6FmKs/Qou"; STUDY_INFO="1967325755@qq.com|11|1030121983|1611107359799"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://www.icourse163.org',
    'referer': 'https://www.icourse163.org/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site'
}
kv_pdf = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}


# request Payload
data_get_ID = {  # https://www.icourse163.org/dwr/call/plaincall/CourseBean.getLastLearnedMocTermDto.dwr
    'callCount': '1',
    'scriptSessionId': '${scriptSessionId}190',
    'httpSessionId': 'e41c678f2cb044c0a12c4778412c7344',
    'c0-scriptName': 'CourseBean',
    'c0-methodName': 'getLastLearnedMocTermDto',
    # 'c0-methodName':'getMocTermDto',      # 注释掉的是MOOC更新之前的写法，现在也还能用，但是不知道MOOC更新前POST的内容，就没多大参考价值
    'c0-id': '0',
    'c0-param0': 'number:1460672441',
    # 'c0-param1': 'number:1',
    # 'c0-param2': 'boolean:true',
    'batchId': '1611048630796'
}

# request Payload
data_get_VideoUrl = {  # https://www.icourse163.org/dwr/call/plaincall/CourseBean.getLessonUnitLearnVo.dwr
    'callCount': '1',
    'scriptSessionId': '${scriptSessionId}190',
    'httpSessionId': 'e41c678f2cb044c0a12c4778412c7344',
    'c0-scriptName': 'CourseBean',
    'c0-methodName': 'getLessonUnitLearnVo',
    'c0-id': '0',
    'c0-param0': 'number:1005926247',
    'c0-param1': 'number:1',  # 1 for pdf or 3 or video
    'c0-param2': 'number:0',
    'c0-param3': 'number:1256673007',
    'batchId': '1611048630815'
}


def batch_id():
    return round(time.time() * 1000)


def postHTMLText(url, headers=None, data=None):
    try:
        r = requests.post(url, headers=headers, data=data)  # 注意，这里是POST
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('Get HTML Error!')
        return ''


def get_ID_func(url, tid):
    data_get_ID['c0-param0'] = 'number:{}'.format(tid)
    data_get_ID['batchId'] = batch_id()  # 虽然参考这里还加了一个随机函数产生批处理时间作为'batchId'的参数，个人觉得没有必要
    kv = {
        'cookie': 'EDUWEBDEVICE=0ab7115b3d854dae8ce1b0d71a1c966a; WM_TID=g5T0XKWOfThBQUFFAQI%2BPb3bZ726b4qo; __yadk_uid=MbnLeOb6ON3kezNoejvPZ46bbsVQNVq7; bpmns=1; MOOC_PRIVACY_INFO_APPROVED=true; hasVolume=true; videoVolume=0.8; WM_NI=4nhovjBd8NMvGeMBnAwhablVmi43V9kTLY8augfa4lpHGMj21Vz3g2oz3nACXnlCJIfo0ptu6Taonh3idP9qGnB%2FbqbpowUvtYBUz6dHRcdX%2BGfV9JAxBoSHLEMy4tt%2BbW4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed0f63489b5a1adee6288928fb6c45f939f8fbbf56ebcba969bef52a3898a85d02af0fea7c3b92af8b2a890f56282bcf8afd07e85bb83a3ed4bb5b8af83ef5eafb7fcd4d533a98c84babb6bb7b9aa82b768b49889aee93af38ab6d4e63aada6fd8fc4499cb2a4a4c943a6b10091f77ff68caf90ed64f1b7acb1bc7b85b28ed0e17ba2b0a198d87eb8878eb6f93ea8989e84e754e999aab7bc4283a88e90d244909b839ab780b8f5aeb8b737e2a3; CLIENT_IP=124.64.19.205; hb_MA-A976-948FFA05E931_source=cn.bing.com; NTESSTUDYSI=78e13ab1a4f442abb8b46c840eec8586; STUDY_INFO="1967325755@qq.com|11|1030121983|1611067128305"; STUDY_SESS="n1oSkC6ko6uwOFVCPjH6m8uTeduOsKbkwyDflnyQJXOl3vVC3smdubFKwXv7eRBs1zJXtNgUxjw/2K+9/6Riu/2HLxIDVPCEj+mrsdXzBxFHs70kcq5hQnJD9qU5wP0+F6d4HXTPLYMQLs0DjTlrR00af401D3EvKQd5Q0jzPgknppr6KrivyjY6FmKs/Qou"; STUDY_PERSIST="aB3nOkxcPNgwAe5iJFKKSMbImXt1xp+axKXoEPw5DZ3lUpL+NmaTG1meuRlRql2LBBR5z8N4snwDLC1Hk/JCU63udBm/atzzoMz64SOql9klhAV7c93tBmAyJI0XyhAuO+LDeVP0/uSOQ09BRmYkwxE9FxMvdcDjX+4jCmicQa9q7M6nWWwj41VWB7QksJLLV5YWrvhR05r0yr9iVIzOallWsU/2+Zmtx30Ukv4njbZOSdFA6J5jrZLCRv8JU8qN8WQLi3xTJ45sq/acjsEWiA=="; NETEASE_WDA_UID=1030121983#|#1505730973277; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9jbi5iaW5nLmNvbS8="; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1611060574,1611060970,1611066948,1611068902; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1611069210',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    try:
        HTML = postHTMLText(url, headers=kv, data=data_get_ID)
        return HTML
    except requests.HTTPError:
        print('Get ID Error!')
        raise


def get_Video_func(url, ID_list):
    kv = {
        'cookie': 'EDUWEBDEVICE=0ab7115b3d854dae8ce1b0d71a1c966a; WM_TID=g5T0XKWOfThBQUFFAQI%2BPb3bZ726b4qo; __yadk_uid=MbnLeOb6ON3kezNoejvPZ46bbsVQNVq7; bpmns=1; MOOC_PRIVACY_INFO_APPROVED=true; hasVolume=true; videoVolume=0.8; WM_NI=4nhovjBd8NMvGeMBnAwhablVmi43V9kTLY8augfa4lpHGMj21Vz3g2oz3nACXnlCJIfo0ptu6Taonh3idP9qGnB%2FbqbpowUvtYBUz6dHRcdX%2BGfV9JAxBoSHLEMy4tt%2BbW4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed0f63489b5a1adee6288928fb6c45f939f8fbbf56ebcba969bef52a3898a85d02af0fea7c3b92af8b2a890f56282bcf8afd07e85bb83a3ed4bb5b8af83ef5eafb7fcd4d533a98c84babb6bb7b9aa82b768b49889aee93af38ab6d4e63aada6fd8fc4499cb2a4a4c943a6b10091f77ff68caf90ed64f1b7acb1bc7b85b28ed0e17ba2b0a198d87eb8878eb6f93ea8989e84e754e999aab7bc4283a88e90d244909b839ab780b8f5aeb8b737e2a3; hb_MA-A976-948FFA05E931_source=cn.bing.com; NTESSTUDYSI=12f6d9e2101a4fcf8f9cce372aa5a138; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9jbi5iaW5nLmNvbS8="; STUDY_INFO="1967325755@qq.com|11|1030121983|1611107359528"; STUDY_SESS="n1oSkC6ko6uwOFVCPjH6m8uTeduOsKbkwyDflnyQJXOl3vVC3smdubFKwXv7eRBshzRpplicxt/Lt+S95t5iVP2HLxIDVPCEj+mrsdXzBxFBRrud3Ty9KuRSRuYgfdtF8eBNDDHujPECpAnL16GoLfPvtLQ9YjxiCYO+hzQ+WHknppr6KrivyjY6FmKs/Qou"; STUDY_PERSIST="aB3nOkxcPNgwAe5iJFKKSMbImXt1xp+axKXoEPw5DZ3lUpL+NmaTG1meuRlRql2LBBR5z8N4snwDLC1Hk/JCU4tzj384k/jS5ImlAFuGLeFPfk4QSkfUmixD8VSvXvR1MOptyNyayqNARnneZ4gm5kgJbHWNPJAhxlLhIBcVZRL8/IlsIGclqeQxlFgxlY5u5P1u5JBpOK2FN6WFsEHtKMGIeqgGaqrbui2Xkv/Gn+9OSdFA6J5jrZLCRv8JU8qN8WQLi3xTJ45sq/acjsEWiA=="; NETEASE_WDA_UID=1030121983#|#1505730973277; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1611060970,1611066948,1611068902,1611107360; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1611107366',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    for i in range(len(ID_list)):
        data_get_VideoUrl['c0-param0'] = 'number:{}'.format(ID_list[i][1])
        data_get_VideoUrl['c0-param3'] = 'number:{}'.format(ID_list[i][2])
        data_get_VideoUrl['c0-param1'] = 'number:{}'.format(ID_list[i][3])
        try:
            HTML = postHTMLText(url, headers=kv, data=data_get_VideoUrl)
            Video_list = parse_Video(HTML, ID_list[i][0], i)
            # print(Video_list)
            download_Video(Video_list)
        except:
            print('Get Video Error!')


def getHTMLText(url, headers=None, stream=False):
    try:
        r = requests.get(url, headers=headers, stream=False)
        # r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        # r.encoding = r.apparent_encoding      # ? 存疑
        return r
    except:
        print('爬取失败')


def download_Video(list):
    root = 'E://My_Downloads/MOOC/'
    if not os.path.exists(root):
        os.mkdir(root)
    if len(list) == 3:  # PDF下载
        try:
            url = list[2]
            # print(url)
            path = root + list[0].replace('序号：', '') + list[1] + '.pdf'
            if not os.path.exists(path):
                r = getHTMLText(url, headers=kv_pdf, stream=True)
                with open(path, 'wb') as f:
                    f.write(r.content)
                    print('文件保存成功')
            else:
                print('文件已存在')
        except:
            print('Download PDF Error!')
    elif len(list) == 5:  # 视频下载
        try:
            url = list[4]
            path = root + list[0].replace('序号：', '') + list[1] + '.mp4'
            if not os.path.exists(path):
                # r = getHTMLText(url, headers=kv_video, stream=True)  # stream=True控制分块下载
                with closing(requests.get(url,headers=kv_video,stream=True)) as r:
                    content_size = int(r.headers['content-length'])
                    chunk_size = 1024 * 128
                    print("下载开始")
                    with open(path, 'wb') as f:
                        count = 1
                        for chunk in r.iter_content(chunk_size=chunk_size):
                            download_progress = count*1024.0*128*100/content_size
                            f.write(chunk)
                            print('\r视频下载进度：{}%'.format(download_progress), end='')
                            count += 1
                print('文件保存成功')
            else:
                print('文件已存在')
        except:
            print('Download Video Error!')
    return ''


def progress_callfunc(blocknum, blocksize, totalsize):
    '''回调函数
        @blocknum : 已经下载的数据块
        @blocksize : 数据块的大小
        @totalsize: 远程文件的大小
        '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print('进度条 %.2f%%' % percent, end='\r')


def parse_Video(html, name, count):
    video_url_list = []
    video_url_list.append('序号：' + str(count))
    video_url_list.append(name)
    re_video = r's\d*\.mp4[S|H]?h?dUrl=\".*?\"'  # 最小匹配
    video_url = re.findall(re_video, html)
    if video_url == []:  # 说明这是个PDF文件，所以没有找到对应的视频
        re_pdf = r'textOrigUrl:".*?"'
        pdf_url = re.search(re_pdf, html)
        pdf_url = pdf_url.group(0).replace('textOrigUrl:"', '')
        pdf_url = pdf_url.replace('\"', '')
        video_url_list.append(pdf_url)
    else:
        for item in video_url:
            item = re.sub(r's0.mp4[S|H]?h?dUrl="', '', item)
            item = item.replace('\"', '')
            video_url_list.append(item)
    return video_url_list


def parse_ID(html):
    ID_list = []
    tmp = []
    re_name = r'liveInfoDto=null;s\d*\.name=\".*\"'
    name_list = re.findall(re_name, html)
    for item in name_list:
        item = re.sub(r'liveInfoDto=null;s\d*\.name=\"', '', item)
        item = item.replace('\"', '')
        item = item.encode('utf-8').decode("unicode-escape")
        tmp.append(item)
    ID_list.append(tmp)
    tmp = []
    re_contentId = r'attachments=.*;s\d*.chapterId=\d*;s\d*.contentId=\d*'
    contentId = re.findall(re_contentId, html)
    for item in contentId:
        item = re.sub(r'attachments=.*;s\d*.chapterId=\d*;s\d*.contentId=', '', item)
        tmp.append(item)
    ID_list.append(tmp)
    tmp = []
    re_ID = r's\d*\.id=\d*;s\d*.jsonContent=.*;s\d*\.learnCount'
    ID = re.findall(re_ID, html)
    for item in ID:
        item = re.sub(r's\d*\.id=', '', item)
        item = re.sub(r';s\d*.jsonContent=.*;s\d*\.learnCount', '', item)
        tmp.append(item)
    ID_list.append(tmp)
    tmp = []  # 判断下载类型是pdf还是视频
    re_type = r's\d*\.contentId=\d*;s\d*\.contentType=\d;s\d*\.durationInSeconds'
    type = re.findall(re_type, html)
    for item in type:
        item = re.sub(r's\d*\.contentId=\d*;s\d*\.contentType=', '', item)
        item = re.sub(r';s\d*\.durationInSeconds', '', item)
        tmp.append(item)
    ID_list.append(tmp)
    transpose_ID_list = []
    if len(ID_list[0]) != len(ID_list[1]) or len(ID_list[0]) != len(ID_list[2]) or len(ID_list[0]) != len(ID_list[3]):
        print('Length Error!')
        return ''
    for i in range(len(ID_list[0])):
        transpose_ID_list.append([ID_list[0][i], ID_list[1][i], ID_list[2][i], ID_list[3][i]])
    return transpose_ID_list


def show_list(ID_list):
    tmpl = '{:6}\t{:6}'
    for i in range(len(ID_list)):
        print(tmpl.format(i, ID_list[i][0]))

def main():
    tid =input('请输入你想下载的课程的tid（例1460672441）：')
    method = input('是否需要全部下载，请输入:yes/no\n')
    get_ID_url = 'https://www.icourse163.org/dwr/call/plaincall/CourseBean.getLastLearnedMocTermDto.dwr'
    ID_HTML = get_ID_func(get_ID_url, int(tid))
    ID_list = parse_ID(ID_HTML)
    get_VideoUrl_url = 'https://www.icourse163.org/dwr/call/plaincall/CourseBean.getLessonUnitLearnVo.dwr'
    if method == 'yes':
        get_Video_func(get_VideoUrl_url, ID_list)
    elif method == 'no':
        show_list(ID_list)
        key = input("请输入想下载的序号（0-{}）：".format(len(ID_list)-1))
        get_Video_func(get_VideoUrl_url, [ID_list[int(key)]])


if __name__ == '__main__':
    main()

