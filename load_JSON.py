import json


def load_JSONFile(file):
    # 打开 JSON 文件
    with open(file, 'r') as json_file:
        # 读取文件内容并解析为字典
        data_dict = json.load(json_file)

    # {"searchList":[],"dirList":["css\/\/","img\/\/","js\/\/","movie\/\/","public\/\/"]}
    #['file', 'hima920230524100000fd.png', 145158337, '2023/05/24 10:23:55', '/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/2023/05-24/10']    
    arr=[]
    result=[]
    for data in ((data_dict)):
        dic=((json.loads(data)))
        if not dic['searchList']:
            continue
        d=(dic['searchList'])
        arr.extend(d)


    for i in range(len(arr)):
        a=arr[i]
        hashUrl=a[-1].split('/')[5]
        d_url=a[-1]+'/'+a[1]
        dic={'name':a[1],
            'hashUrl':hashUrl,
            'd_url':d_url
        }
        result.append(dic)
    return(result)



def load_JSON(json_file):
    data_dict = eval(json_file)
    arr=[]
    result=[]
    for data in ((data_dict)):
        dic=((json.loads(data)))
        if not dic['searchList']:
            continue
        d=(dic['searchList'])
        arr.extend(d)


    for i in range(len(arr)):
        a=arr[i]
        hashUrl=a[-1].split('/')[5]
        d_url=a[-1]+'/'+a[1]
        dic={'name':a[1],
            'hashUrl':hashUrl,
            'd_url':d_url
        }
        result.append(dic)
    return(result)
if __name__ == "__main__":
#{'name': 'hima920230524100000fd.png', 'hashUrl': 'bDw2maKV', 'd_url': '/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/2023/05-24/10/hima920230524100000fd.png'}
    print((load_JSON(r'C:\ZY\Projects\himawari\mp4_urls\2024-05-02.json')))
