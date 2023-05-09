from threading import Thread

class download(object):
                
    def __init__(self):
        from pytube import YouTube
        
        x_a = False  
        while x_a == False:
            self.g_artist = str(input('Please enter the name of an artist: '))
            if not not self.g_artist:
                x_a = True
                break
        
        x_a = False
        while x_a == False:
            self.g_titles = str(input('Please enter the songs title: '))
            if not not self.g_titles:
                x_a = True
                break
        
        continue_question = {'end': exit, 'cont': '', 'redo': download}
        
        while True:
            continue_i = str(input("Would You Like To (Cont/Redo/end): "))
            print()
            if continue_i.lower() in continue_question:
                for e in continue_question:
                    if continue_i.lower() == 'cont':
                        pass
                    elif continue_i.lower() == e:
                        Thread(target=continue_question[e]()).start()
                        break
                break    
        
        Thread(target=self.linking()).start()
        Yt = YouTube(self.main_url, use_oauth=True, allow_oauth_cache=True)

        video = Yt.streams.filter(only_audio=True).first()



        names = f"{video.title}.mp4".translate({ord(i): None for i in '/\\:"><|'})
        Thread(target=self.getname(q_title=self.g_titles, q_artist=self.g_artist))
        Thread(target=video.download(filename=names))
        print('Downloaded.')
        print()
        print('converting....')
        from moviepy.editor import AudioFileClip
        clip = AudioFileClip(names) 
        final = f'{self.artist} - {self.tracks}'
        namef = f"{final}".translate({ord(i): None for i in '/\\:"><|'})
        print('Converting:', namef)
        clip.write_audiofile(f'audio/{namef}.mp3')
        clip.close()
        from os import remove
        remove(names)
        probables = {'y': download, 'n': exit}
        while True:
            inputYN = str(input('Again (Y/N): '))
            if inputYN.lower() in probables:
                for e in probables:
                    if inputYN.lower() == e:
                        Thread(target=probables[e](), daemon=True).start()
                        break
                break    
        
        
    def linking(self):
        from urllib.request import Request, urlopen
        from re import findall
        songname = f'{self.g_artist} {self.g_titles}'
        val = "+".join(songname.split()) + '+official+audio'
        base_url = f"https://www.youtube.com/results?search_query={val}+official+audio"
        try:
            html_see = Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
            html_ope = urlopen(html_see)
            regex_is = findall(r'watch\?v=(\S{11})', html_ope.read().decode())
            self.main_url = f"https://www.youtube.com/watch?v={regex_is[0]}"
        except:
            print()
            print('could not fetch video, check Your connection')
            exit()
        
        print()
        print(self.main_url)

    def getname(self, q_title, q_artist):
        from musixmatch import Musixmatch
        token = 'd9ca967208167963939c8a6787339e02'
        mains = Musixmatch(token)
        try:
            songs = mains.matcher_track_get(q_title, q_artist)
            self.tracks = songs['message']['body']['track']['track_name' ]
            self.artist = songs['message']['body']['track']['artist_name']
        except:
            print('The names (artist, title) are wrong')
            exit()

class urlDownload(download):
    def __init__(self, link):
        from pytube import YouTube
        print('process starting...')

        Yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        video = Yt.streams.filter(only_audio=True).first()
        sname = f"{video.title}.mp4".translate({ord(i): None for i in '/\\:"><|'})
        Thread(target = video.download(filename=sname))
        print('Downloaded: {}'.format(sname))
        
        from moviepy.editor import AudioFileClip
        clip = AudioFileClip(sname) 
        print('Converting:', sname)
        clip.write_audiofile(f'audio/{sname}.mp3')
        clip.close()

        from os import remove
        remove(sname)

    

class mainruns(download):

    def __init__(self):    
        outcomes = {'end': exit, 'url': urlDownload, 'download': download}
        while True:
            whatTD = str(input('Choose (end/url/download): '))
            if whatTD.lower() in outcomes:
                for e in outcomes:
                    if whatTD.lower() == e:
                        if e == 'url':
                            link = str(input('please enter link: '))
                            Thread(target=outcomes[e](link), daemon=True).start()
                        else:  
                            Thread(target=outcomes[e](), daemon=True).start()
                            break
                break    


if __name__ == '__main__':  
   Thread(target=mainruns())
#%%

#%%

#%%
