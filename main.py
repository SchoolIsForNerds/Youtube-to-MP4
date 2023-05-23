import tkinter as tk
import ttkbootstrap as ttk
from pytube import YouTube

class downloader:

    def __init__(self) -> None:
        self.root = ttk.Window(title = "YT to MP4",
                               themename = 'vapor',
                               size = (450, 250),
                               resizable = (False, False),
                               iconphoto = 'icon.png')
        
        self.root.place_window_center()

        self.link = tk.StringVar()
        self.outText = tk.StringVar()

    def convert(self):
        try:
            url = YouTube(str(self.link.get()))
        except:
            self.outText.set('Couldn\'t find link')
            raise SystemError("Not a link")
            
        try:
            video = url.streams.filter(mime_type = 'video/mp4')
            d = video.get_highest_resolution()
        except:
            raise SystemError("MP4 not found")
            
        try:
            d.download('downloads')
            self.link.set('')
            self.outText.set('Downloaded')
        except:
            raise SystemError("Couldn't download")      
         

    def main(self):
        title = ttk.Label(master = self.root, 
                          text = "Youtube To MP4", 
                          font = "Consolas 24 bold",
                          bootstyle = 'secondary')
        title.pack(pady = 24)

        frame = ttk.Frame(self.root)

        input = ttk.Entry(frame, 
                          textvariable = self.link)
        input.pack(side = "left", padx = 10)

        button = ttk.Button(frame, text = "Convert", 
                            command = self.convert,
                            bootstyle = 'secondary, outline')
        
        button.pack(side = "left")

        frame.pack(pady = 10)

        output = ttk.Label(self.root, 
                           text = 'Output', 
                           font = "Consolas 12", 
                           textvariable = self.outText,
                           bootstyle = 'success')
        output.pack()

        self.root.mainloop()

if __name__ == "__main__":
    d = downloader()
    d.main()
