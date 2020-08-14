import tkinter as tk
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from os import getlogin, remove, sep
from os.path import abspath
# pytube3 is usually getting download issues, so we can go for pytubeX instead.
# 'pip uninstall pytube3' --> 'pip install pytubeX'


class ytToPC(tk.Frame):
    #Master init & general properties:
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.envProp()


    def envProp(self):
        #program status properties:
        self.status = tk.Label(self, textvariable=currStatus, font=('helvetica', 10))
        self.status.pack(pady=3)
        #input box properties:
        self.setLink = tk.Entry(self, textvariable=ytLink, width=35)
        self.setLink.pack(pady=3)
        #"DownMP4" button properties:
        self.downVid = tk.Button(self, text='Download .MP4 format', fg='blue', font=('helvetica', 11, 'bold'), command=self.downToMp4)
        self.downVid.pack(pady=3)
        #"DownMP3" button properties:
        self.downAud = tk.Button(self, text='Download .MP3 format', fg='blue', font=('helvetica', 11, 'bold'), command=self.downToMp3)
        self.downAud.pack(pady=3)
        #"Exit" button properties:
        self.exit = tk.Button(self, text='     Exit     ', fg='red', font=('helvetica', 10, 'bold'), command=self.master.destroy)
        self.exit.pack(pady=5)
        #program info properties:
        self.info = tk.Label(self, text='made by felpshn', fg='grey', font=('helvetica', 9, 'italic'))
        self.info.pack(pady=3)


    def downToMp4(self):
        try:
            currStatus.set('[1/2] Downloading...') #sets a new status for the app.
            root.update() #updates the app.
            downPath = f'{abspath(sep)}Users\\{getlogin()}\\Downloads' #sets the download dir path.
            ytVid = YouTube(ytLink.get()) #gets from the user the yt video link.
            ytVid.streams.filter(adaptive=True, type='video').first().download(downPath, filename='tempVidFile') #"adaptative" gets the best video or audio quality possible.
            ytVid.streams.filter(adaptive=True, type='audio').first().download(downPath, filename='tempAudFile') #"first" gets the first video listed inside the array defined by adaptative param.
            tempVidFile = VideoFileClip(f'{downPath}\\tempVidFile.mp4') #assigns the file as a video file.       #"filename" defines a new name to the downloaded file.
            tempAudFile = AudioFileClip(f'{downPath}\\tempAudFile.mp4') #assigns the file as a audio file.
            currStatus.set('[2/2] Converting & mounting...')
            ytLink.set('This step may take some minutes.')
            root.update()
            clipMount = tempVidFile.set_audio(tempAudFile) #assign an audio clip as the soundtrack of a video clip.
            clipMount.write_videofile(f'{downPath}\\{ytVid.title}.mp4', fps=30) #builds the clip.
            tempVidFile.close() #closes the internal reader.
            tempAudFile.close()
            clipMount.close()
            remove(f'{downPath}\\tempVidFile.mp4') #deletes the temp vid and aud file.
            remove(f'{downPath}\\tempAudFile.mp4')
            currStatus.set('Done!')
            ytLink.set('Check your "Downloads" folder.')
            root.update()
        except:
            currStatus.set('Error! something went wrong.')
            ytLink.set('Invalid Link!')
            root.update()


    def downToMp3(self):
        try:
            currStatus.set('[1/2] Downloading...')
            root.update()
            downPath = f'{abspath(sep)}Users\\{getlogin()}\\Downloads'
            ytVid = YouTube(ytLink.get())
            ytVid.streams.first().download(downPath, filename='tempAudFile')
            tempAudFile = VideoFileClip(f'{downPath}\\tempAudFile.mp4')
            currStatus.set('[2/2] Converting & mounting...')
            ytLink.set('It will be ready in a sec.')
            root.update()
            audMount = tempAudFile.audio
            audMount.write_audiofile(f'{downPath}\\{ytVid.title}.mp3')
            tempAudFile.close()
            audMount.close()
            remove(f'{downPath}\\tempAudFile.mp4')
            currStatus.set('Done!')
            ytLink.set('Check your "Downloads" folder.')
            root.update()
        except:
            currStatus.set('Error! something went wrong.')
            ytLink.set('Invalid link!')
            root.update()


#Tk call & general GUI properties:
root = tk.Tk()
root.title('YouTube 2 PC')
root.geometry('280x190')
root.resizable(0, 0)
#String vars:
currStatus = tk.StringVar()
currStatus.set('Enter the YouTube link below.')
ytLink = tk.StringVar()

app = ytToPC(master=root)
app.mainloop()
