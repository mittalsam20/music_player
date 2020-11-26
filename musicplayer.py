#----------------------------------------------VOLUME FUNCTIONS------------------------------------------
def vup():
    vol= mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    voltext.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    volbar['value']=mixer.music.get_volume()*100

def vdown():
    vol= mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    voltext.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    volbar['value']=mixer.music.get_volume()*100

def mute():
    global cur_vol
    cur_vol=mixer.music.get_volume()
    mixer.music.set_volume(0)
    root.mute_button.grid_remove()
    root.unmute_button.grid()
    root.status_song.configure(text='MUTED')
    voltext.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    volbar['value']=mixer.music.get_volume()*100

def unmute():
    root.mute_button.grid()
    root.unmute_button.grid_remove()
    root.status_song.configure(text='Playing..')
    mixer.music.set_volume(cur_vol)
    voltext.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    volbar['value']=mixer.music.get_volume()*100

#------------------------------------------------PLAY/PAUSE----------------------------------------
def songpath():
    open_song=filedialog.askopenfilename(title='Select Audio File')
    songname.set(open_song)

def playsong():
    root.status_song.configure(text='PLAYING..')
    seekbody.grid()
    mixer.music.load(songname.get())
    mixer.music.play()
    # song_len=int(MP3(songname.get()).info.length)
    # print(song_len)
    # seekbar['maximum']=song_len
    # endtime.configure(text='{}:{}'.format())

def resumesong():
    mixer.music.unpause()
    root.status_song.configure(text='RESUMED')
    root.resume_button.grid_remove()
    root.pause_button.grid()

def pausesong():
    mixer.music.pause()
    root.status_song.configure(text='PAUSED')
    root.pause_button.grid_remove()
    root.resume_button.grid()

def stopsong():
    root.status_song.configure(text='STOPPED')
    mixer.music.stop()

# def realtime():
#     seek_pos=mixer.music.get_pos()/1000
#     seekbar['value']=seek_pos
#     seekbar.after(2,realtime)
#---------------------------------------------GUI FUNCTION-------------------------------------------------

def gui():
    global voltext,volbar,status_song,seekbody,song_len,seekbar,endtime
    #-------------------------------------------------LABELS----------------------------------------------
    browse_song=Label(root,text="Select Audio Track",bg="lawn green",font=('Comic Sans MS',20,'bold'))
    browse_song.grid(row=0,column=0,padx=10,pady=0)

    root.status_song=Label(root,text="No Track Selected",bg="lawn green",font=('Comic Sans MS',20,'bold'))
    root.status_song.grid(row=1,column=2,ipadx=5,ipady=5)

    credit=Label(root,text="MADE BY SAMARTH GARG(18BEC094) \n AND \n SAMAKSH MITTAL(18BEC093)",bg="lawn green",font=('arial',14,'bold'))
    credit.grid(row=3,column=1,padx=0,pady=0,columnspan=3)

    #-------------------------------------------------ENTRIES----------------------------------------------
    song_entry=Entry(root,font=('arial',20,'bold'),width=40,textvariable=songname)
    song_entry.grid(row=0,column=1,columnspan=3,padx=20,pady=0)

    #-------------------------------------------------BUTTONS------------------------------------------
    browse_button=Button(root,text='Browse',font=('Comic Sans MS',25,'bold'),width=8,activebackground='grey30',command=songpath,bd=5)
    browse_button.grid(row=0,column=4,padx=10,pady=20)

    play_button=Button(root,text='PLAY',bg="lawn green",font=('Comic Sans MS',25,'bold'),width=8,bd=5,activebackground='green4',command=playsong)
    play_button.grid(row=1,column=0,pady=10)

    root.resume_button=Button(root,text='RESUME',font=('Comic Sans MS',25,'bold'),width=8,activebackground='grey30',command=resumesong,bd=5)
    root.resume_button.grid(row=2,column=0,pady=10)

    root.pause_button=Button(root,text='PAUSE',font=('Comic Sans MS',25,'bold'),width=8,bd=5,activebackground='grey30',command=pausesong)
    root.pause_button.grid(row=2,column=0,pady=10)

    stop_button=Button(root,text='STOP',bg="firebrick1",font=('Comic Sans MS',25,'bold'),width=8,bd=5,activebackground='red4',command=stopsong)
    stop_button.grid(row=3,column=0)

    vup_button=Button(root,text='Vol +',font=('Comic Sans MS',25,'bold'),width=8,bd=5,activebackground='grey30',command=vup)
    vup_button.grid(row=1,column=4,padx=20,pady=0)

    vdown_button=Button(root,text='Vol -',font=('Comic Sans MS',25,'bold'),width=8,bd=5,activebackground='grey30',command=vdown)
    vdown_button.grid(row=2,column=4,padx=0,pady=0)

    root.unmute_button=Button(root,text='UNMUTE',font=('Comic Sans MS',25,'bold'),width=8,bd=5,activebackground='grey30',command=unmute)
    root.unmute_button.grid(row=3,column=4,padx=0,pady=0)

    root.mute_button=Button(root,text='MUTE',font=('Comic Sans MS',25,'bold'),width=8,bd=5,activebackground='grey30',command=mute)
    root.mute_button.grid(row=3,column=4,padx=0,pady=0)

#----------------------------------------------------------VOLUME  BAR-------------------------------------------------
    vollabel=Label(root,text='',bg='red',bd=1)
    vollabel.grid(row=1,column=5,rowspan=3,padx=10,ipadx=0,pady=20)

    volbar=Progressbar(vollabel,orient=VERTICAL,mode='determinate',value=100,length=220)
    volbar.grid(row=0,column=0,ipadx=8)

    voltext=Label(vollabel,text='100%',bg='lightgray',width=4,font=('arial',10,'bold'))
    voltext.grid(row=0,column=0)

#----------------------------------------------------------SEEK BAR-------------------------------------------------
    seekbody=Label(root,text='',bg='red',bd=1)
    seekbody.grid(row=2,column=1,columnspan=3,padx=0,pady=0)
    seekbody.grid_remove()

    starttime=Label(seekbody,text='0:00',bg='red',bd=1)
    starttime.grid(row=0,column=0,padx=0,pady=0)

    endtime=Label(seekbody,text='3:00',bg='red',bd=1)
    endtime.grid(row=0,column=3,padx=0,pady=0)

    seekbar=Progressbar(seekbody,orient=HORIZONTAL,mode='determinate',value=40,length=530)
    seekbar.grid(row=0,column=2,ipady=2)
#-----------------------------------------------------------------MAIN--------------------------------------------------
from tkinter import *                            # tkinter is imported for GUI
from tkinter import filedialog                   # for browsing through the files
from tkinter.ttk import Progressbar              # for volume and seek bar
from pygame import mixer                         # for different functions like mixer.music.play()
# from mutagen.mp3 import MP3
# import datetime

mixer.init()                                     # intializing mixer into the program(a function from pygame)
root=Tk()
root.geometry('1150x370+120+150')                # 1200X370 is the dimensions of appication dialog box
root.title('MUSIC PLAYER')                       # 100 is the margin from left side and 150 is the margin from top
root.resizable(0,0)
root.configure(bg='gray25')

songname=StringVar()
gui()                                            # calling user defined function gui(all the frontend is in this function)
root.mainloop()                                  # infinte loop

#--------------------------------------MADE BY SAMAKSH MITTAL AND SAMARTH GARG--------------------------------------------------
#-----------------------------------------------END OF PROGRAM-------------------------------------------------------------------