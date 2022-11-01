import os,sys,json

song1_path="E:\\SteamLibrary\\steamapps\\workshop\\content\\431960\\new\\"
path="E:\\SteamLibrary\\steamapps\\workshop\\content\\431960"

for root,dirs,files in os.walk(path):
    for dir in dirs:
        # 使用join函数将当前目录和文件所在根目录连接起来
        tmp=os.path.join(root, dir)
        if tmp.endswith("songs"):
            if tmp.endswith("images\\songs"):
                break
            path=tmp[0:61]  #E:\SteamLibrary\steamapps\workshop\content\431960\2848357096\

            song=tmp+"\\song.mp3"
            with open(path+"project.json", 'r', encoding='utf8') as fp:
                json_data = json.load(fp)  # 读取json文件
            song1=song1_path="E:\\SteamLibrary\\steamapps\\workshop\\content\\431960\\new\\"+json_data["title"]+".mp3"
            try:
                os.rename(song,song1)
            except:
                #print(song1)
                break
            #print(name)
            #print(os.path.join(root, dir))
            print(len(tmp))
