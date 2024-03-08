import tkinter
from tkinter import filedialog

root=tkinter.Tk()
root.title("PDF Text Extractor")

def openfile():
    filename=filedialog.askopenfilename(title="Opend PDF file", initialdir="C:\\Users\\user\\Desktop\\ziya tkinter\\PDF_converter", filetypes=[("PDF files", "*.pdf")])
    print(filename)
filename_label=tkinter.Label(root, text="No File Selected")
outputfile_text=tkinter.Text(root)
openfile_button=tkinter.Button(root, text="Open PDF File", command=openfile)

filename_label.pack()
outputfile_text.pack()
openfile_button.pack()
root.mainloop()