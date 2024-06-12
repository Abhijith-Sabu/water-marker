from tkinter import *
from tkinter import filedialog,Label
from PIL import Image,ImageTk
import tkinter.messagebox
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


file1= file2= None

# image uploader function
def water_marker():
    if file1 and file2:
        load_logo= Image.open(file2).convert('RGBA')
        background_img= Image.open(file1).convert('RGBA')
        load_logo=load_logo.resize((24,24),Image.Resampling.LANCZOS)
        logo_x = 0
        logo_y = 0
        background_img.paste(load_logo,(logo_x,logo_y),mask=load_logo)
        background_img.show()
    else:
              
        tkinter.messagebox.showinfo("No file is Choosen !!",  "Please choose an Image file.")





# 	fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
# 	path = filedialog.askopenfilename(filetypes=fileTypes)

# 	# if file is selected
# 	if len(path):
# 		img = Image.open(path)
# 		# img = img.resize((200, 200))
# 		img_width,img_height=img.size
# 		img = img.resize((250, 250), Image.Resampling.LANCZOS)

# 		pic = ImageTk.PhotoImage(img)

# 		# re-sizing the app window in order to fit picture
# 		# and buttom
# 		app.geometry("800x700")
# 		imgLabel.config(image=pic)
# 		imgLabel.image = pic
		

# 	# if no file is selected, then we are displaying below message
# 	else:
# 		tkinter.messagebox.showinfo("No file is Choosen !!",  "Please choose a file.")


def image_file():
	global file1
	FileType=[("Image files", "*.png;*.jpg;*.jpeg")]
	file1 = filedialog.askopenfilename(filetypes=FileType)
	
def logo():
    """
    Opens a file dialog to select an image file and stores the file path in
    the global variable `file2`.
    """
    global file2
    
    # Define the file types to be displayed in the file dialog
    FileType=[("Image files", "*.png;*.jpg;*.jpeg")]
    
    # Open the file dialog and store the selected file path in `file2`
    file2 = filedialog.askopenfilename(filetypes=FileType)

	
# Main method
if __name__ == "__main__":

        # defining tkinter object
        app = Tk()

        # setting title and basic size to our App
        app.title(" Add your water mark")
        app.configure(bg='white')
        app.geometry("500x450")

        # adding background image
        img=Image.open(r'D:\project\python\85-WATER-MARKgui\logo.jpeg')
        img=img.resize((200,200))
        phto_img = ImageTk.PhotoImage(img)
        imgLabel = Label(app, image=phto_img)
        imgLabel.pack()

        # adding background color to our upload button
        app.option_add("*Label*Background", "red")
 
            
        water_markbtn = Button(app,text='locate WTR M',command=logo,width=24,bg='gray')
        water_markbtn.pack(side=BOTTOM,pady=40,padx=60)



        # defining our upload buttom
        uploadButton = Button(app, text="Locate Image", command=image_file,width=24,bg='lightgreen')
        uploadButton.pack(side=BOTTOM, pady=20)

        show_final_image = Button(app,text='show',command=water_marker,width=24,bg=RED)
        show_final_image.pack(side=BOTTOM)
		



    

        app.mainloop()


 





