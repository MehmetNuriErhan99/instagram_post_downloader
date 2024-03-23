import instaloader
import tkinter as tk
from tkinter import messagebox

#Mehmet Nuri Erhan


def download_post():
    #login name 
    username = entry_username.get()

    try:
        ##home
        bot = instaloader.Instaloader()
        # profil nesnesi oluşturma
        profile = instaloader.Profile.from_username(bot.context,username)
        #create profile object
        posts = profile.get_posts()
        #download posts

        for index,post in enumerate(posts,1):
            bot.download_post(post, target=f"{profile.username}_{index}")
        #success message
        messagebox.showinfo("Successful","Posts Downloaded")
    except Exception as e:
        messagebox.showerror("Eror",str(e))


#create tkinter interface

root = tk.Tk()
root.title("Instagram Post Downloader")
root.geometry("300x200")

#request username
label = tk.Label(root, text="Login Name:")
label.pack(pady=10)
#username login
entry_username = tk.Entry(root)
entry_username.pack()
#download button
download_button  = tk.Button(root, text="Download Information", command=download_post )
download_button.pack()
root.mainloop()