def music(jaja):
        import requests,time
        file=open("spotifyplaylist.txt",'r') #input file which you copied the song links
        s=file.readlines()
        d=[]
        g=''
        LLL=[]
        PPP=[]
        OOO=[]
        WWW=[]
        VVV=[]
        num=0
        d=s
        print(len(d))
        num+=1
        print(num)
        for b in d:
                b=b.rstrip()
                OOO.append(b)
                r=requests.get(b)
                content=r.content
                data=''
                content=str(content)[105:200]
                for i in range(len(content)):
                    if content[i]=='|':
                          break
                    elif content[i] in '#&':
                            continue
                    else:
                          data+=content[i]
                if 'x27;' or 'xe2' or 'x80' or 'x9' or '/' or '?'in data:
                        dist=''
                        for fd in data:
                                if 'x27;' not in dist and 'xe2' not in dist and 'x80' not in dist and 'x9' not in dist and '/' not in dist and '?' not in dist:
                                        dist+=fd
                                else:
                                        dist=dist[0:-4]
                        data=dist
                if data[0] in '123456789':
                        data='a'+data
                if ':' in data:
                      h=''
                      for v in data:
                              if v!=':':
                                      h+=v
                      data=h
                data=data.rstrip()
                data8=data
                LLL.append(data8)
                data=data.split()
                beta=''
                for g in data:  
                    beta+=g+'+'
                beta2='https://www.youtube.com/results?search_query='+beta[0:-1]
                r=requests.get(beta2)
                content=r.content
                content=str(content)
                data1=''
                for i in range(500000,515000):
                    data1+=content[i]
                    if data1.endswith('"commandMetadata":{"webCommandMetadata":{"url":"/watch'):
                        data1=''
                        data1=content[i-5:i+15]
                        break
                if len(data1)<21:
                    hai=data1[9::]
                    hai2='https://dl.ytmp3.ink/youtube/get?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D'+hai
                    r=requests.get(hai2)
                    hai3=str(r.content)
                    hai3=hai3.split('=')
                    try:
                      gui=hai3[1]
                    except:
                        r=requests.get(hai2)
                        hai3=str(r.content)
                        hai3=hai3.split('=')
                    op=''
                    for m in gui:
                            if m=='"':
                                    break
                            else:
                               op+=m
                    gui=op
                    hai4='https://api.fabdl.com/youtube/mp3-convert-task?token='+gui
                    s=requests.get(hai4)
                    if 'error' not in str(s):
                            print(data8)
                    else:
                        hai4='https://api.fabdl.com/youtube/mp3-convert-task?token='+gui
                        s=requests.get(hai4)
                    hai5=str(s.content)
                    hai5=hai5[20:52]
                    hai6='https://api.fabdl.com/youtube/download-mp3/'+hai5
                    h=requests.get(hai6)
                    hi99=data8+'.mp3'
                    hi99=jaja+hi99
                    try:
                      f=open(hi99,'wb')
                      f.write(h.content)
                    except:
                            substitute=''
                            for iii in hi99:
                                    if iii=='x':
                                            substitute=substitute[0:-1]
                                    else:
                                            substitute+=iii
                            hi99=substitute
                            f=open(hi99,'wb')
                            f.write(h.content)
                    import pathlib
                    if pathlib.Path(hi99).stat().st_size<8:
                            hai2='https://dl.ytmp3.ink/youtube/get?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D'+hai
                            r=requests.get(hai2)
                            hai3=str(r.content)
                            hai3=hai3.split('=')
                            try:
                              gui=hai3[1]
                            except:
                                r=requests.get(hai2)
                                hai3=str(r.content)
                                hai3=hai3.split('=')
                            op=''
                            for m in gui:
                                    if m=='"':
                                            break
                                    else:
                                       op+=m
                            gui=op
                            hai4='https://api.fabdl.com/youtube/mp3-convert-task?token='+gui
                            s=requests.get(hai4)
                            if 'error' not in str(s):
                                        print(data8)
                            else:
                                hai4='https://api.fabdl.com/youtube/mp3-convert-task?token='+gui
                                s=requests.get(hai4)
                            hai5=str(s.content)
                            hai5=hai5[20:52]
                            hai6='https://api.fabdl.com/youtube/download-mp3/'+hai5
                            h=requests.get(hai6)
                            hi99=data8+'.mp3'
                            hi99=jaja+hi99
                            try:
                                  f=open(hi99,'wb')
                                  f.write(h.content)
                            except:
                                    substitute=''
                                    for iii in hi99:
                                            if iii=='x':
                                                    substitute=substitute[0:-1]
                                            else:
                                                    substitute+=iii
                                    hi99=substitute
                                    f=open(hi99,'wb')
                                    f.write(h.content)
                            if pathlib.Path(hi99).stat().st_size>8:
                                    PPP.append(data8)
                    else:
                            PPP.append(data8)
                            WWW.append(b)
                else:
                        beta=''
                        for g in data:
                            beta+=g+'+'
                        beta2='https://www.youtube.com/results?search_query='+beta[0:-1]
                        r=requests.get(beta2)
                        content=r.content
                        content=str(content)
                        data1=''
                        for i in range(500000,515000):
                            data1+=content[i]
                            if data1.endswith('"commandMetadata":{"webCommandMetadata":{"url":"/watch'):
                                data1=''
                                data1=content[i-5:i+15]
                                break
                        if len(data1)<21:
                            hai=data1[9::]
                            hai2='https://dl.ytmp3.ink/youtube/get?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D'+hai
                            r=requests.get(hai2)
                            hai3=str(r.content)
                            hai3=hai3.split('=')
                            try:
                              gui=hai3[1]
                            except:
                                r=requests.get(hai2)
                                hai3=str(r.content)
                                hai3=hai3.split('=')
                            op=''
                            for m in gui:
                                    if m=='"':
                                            break
                                    else:
                                       op+=m
                            gui=op
                            hai4='https://api.fabdl.com/youtube/mp3-convert-task?token='+gui
                            s=requests.get(hai4)
                            if 'error' not in str(s):
                                    print(data8)
                            else:
                                    hai4='https://api.fabdl.com/youtube/mp3-convert-task?token='+gui
                                    s=requests.get(hai4)
                            hai5=str(s.content)
                            hai5=hai5[20:52]
                            hai6='https://api.fabdl.com/youtube/download-mp3/'+hai5
                            h=requests.get(hai6)
                            hi99=data8+'.mp3'
                            hi99=jaja+hi99
                            f=open(hi99,'wb')
                            ggg=open(hi99,'rb')
                            f.write(h.content)
                            import pathlib
                            if pathlib.Path(hi99).stat().st_size<8:
                                    hai2='https://dl.ytmp3.ink/youtube/get?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D'+hai
                                    r=requests.get(hai2)
                                    hai3=str(r.content)
                                    hai3=hai3.split('=')
                                    gui=hai3[1]
                                    op=''
                                    for m in gui:
                                            if m=='"':
                                                    break
                                            else:
                                               op+=m
                                    gui=op
                                    hai4='https://api.fabdl.com/youtube/mp3-convert-task?token='+gui
                                    s=requests.get(hai4)
                                    if 'error' not in str(s):
                                            print(data8)
                                    else:
                                            hai4='https://api.fabdl.com/youtube/mp3-convert-task?token='+gui
                                            s=requests.get(hai4)
                                    hai5=str(s.content)
                                    hai5=hai5[20:52]
                                    hai6='https://api.fabdl.com/youtube/download-mp3/'+hai5
                                    h=requests.get(hai6)
                                    hi99=data8+'.mp3'
                                    hi99=jaja+hi99
                                    try:
                                       f=open(hi99,'wb')
                                       f.write(h.content)
                                    except:
                                            substitute=''
                                            for iii in hi99:
                                                    if iii=='x':
                                                            substitute=substitute[0:-1]
                                                    else:
                                                            substitute+=iii
                                            hi99=substitute
                                            f=open(hi99,'wb')
                                            f.write(h.content)
                                    if pathlib.Path(hi99).stat().st_size<8:
                                            PPP.append(data8)
                                            WWW.append(b)
                            else:
                                     PPP.append(data8)
                                     WWW.append(b)
        fo=open('spotifyplaylist.txt','w') #optional save in same file or make new file and edit the input file in next try
        for www in LLL:
                if www not in PPP:
                        print(www)
        for yyy in OOO:
                if yyy not in WWW:
                        fo.write(yyy)
                        fo.flush()
                        VVV.append(yyy)
        if VVV!=[]:
             music(VVV)
music('your/path/where to download the music')
                

            
