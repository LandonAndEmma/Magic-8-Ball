from tkinter import *
import random
import winsound

root = Tk()
root.configure(background='black')
root.geometry('150x117')
root.minsize(150, 117)
root.maxsize(150, 117)
root.resizable(150,117)
root.title('Magic 8-Ball')
icon = PhotoImage(file='sprites/icon.png')
root.iconphoto(True, icon)
answer_dict = {1: 'It is certain.', 2: 'It is decidedly so.', 3: 'Without a doubt.', 4: 'Yes definitely.',
               5: 'You may rely on it.', 6: 'As I see it, yes.', 7: 'Most likely.', 8: 'Outlook good.', 9: 'Yes.',
               10: 'Signs point to yes.', 11: 'Reply hazy, try again.', 12: 'Ask again later.',
               13: 'Better not tell you now.', 14: 'Cannot predict now.', 15: 'Concentrate and ask again.',
               16: "Don't count on it.", 17: 'My reply is no.', 18: 'My sources say no.', 19: 'Outlook not so good.',
               20: 'Very doubtful.'}
sound_dict = {1: 'sfx/shaking1.wav', 2: 'sfx/shaking2.wav', 3: 'sfx/shaking3.wav', 4: 'sfx/shaking4.wav',
              5: 'sfx/shaking5.wav', 6: 'sfx/shaking6.wav', 7: 'sfx/shaking7.wav'}


def shake():
    sound = random.randint(1, 7)
    sound_string = sound_dict[sound]
    winsound.PlaySound(sound_string, winsound.SND_FILENAME)
    answer = random.randint(1, 20)
    answer_string = answer_dict[answer]
    outputlabel.config(text=answer_string, relief=FLAT, bg='blue', fg='white')
    outputlabel.pack()


info = Label(root, text='Input a yes or no question\n then push the button\n to shake the Magic 8-Ball.', relief=FLAT,
             bg='black', fg='white')
info.pack()
entry = Entry(root, relief=FLAT, bg="grey", fg="white")
entry.focus_set()
entry.pack()
rolltheball = Button(root, text='Shake the Magic 8-Ball?', relief=FLAT, bg='grey', fg='white', command=shake)
rolltheball.pack()
outputlabel = Label(root, relief=FLAT, bg='black', fg='white')
outputlabel.pack()
root.mainloop()
