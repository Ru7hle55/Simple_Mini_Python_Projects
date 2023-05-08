from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, askyesno
from tkinter import filedialog as fd
import qrcode
import cv2


# APPLICATION'S FUNCTIONALITIES

# Close Application Functionality
def close_window():

    if askyesno(title='Close QR generator and reader', message='Are you sure you want to exit the program ?'):
        window.destroy()


# Generate the QR Code
def generate_qr_code():

    qr_code_data = str(data_entry.get())
    qr_code_name = str(filename_entry.get())

    if qr_code_name.strip() == '':
        showerror(title='ERROR', message='Empty filename entry field\nMake sure the filename entry '
                                         'field is filled when generating the QRCode')

    else:
        if askyesno(title='Confirmation', message='Do you want to create a QRCode with the provided information?'):

            try:
                qr = qrcode.QRCode(version=1, box_size=6, border=4)
                qr.add_data(qr_code_data)
                qr.make(fit=True)
                name = qr_code_name + '.png'
                qr_code_image = qr.make_image(fill_color="black", back_color="white")
                qr_code_image.save(name)

                global Image

                Image = PhotoImage(file=f'{name}')
                image_label1.config(image=Image)

                reset_button.config(state=NORMAL, command=reset)

            except:
                showerror(title='ERROR', message='Please, provide a valid file name !')


# Clear the QR Code Image Label
def reset():

    if askyesno(title='Reset', message='Are you sure you want to reset ?'):
        image_label1.config(image='')
        reset_button.config(state=DISABLED)


# QR Code File Path
def open_dialog():

    name = fd.askopenfilename()
    file_entry.delete(0, END)
    file_entry.insert(0, name)


# Reading the QR Code
def reading_qr_code():

    image_file = file_entry.get()

    if image_file.strip() == '':
        showerror(title='ERROR', message='Please provide a QR code image file to detect !')

    else:
        try:
            qr_image = cv2.imread(f'{image_file}')
            qr_reader = cv2.QRCodeDetector()

            global qr_code_image

            qr_code_image = PhotoImage(file=f'{image_file}')
            image_label2.config(image=qr_code_image)
            data, pts, st_code = qr_reader.detectAndDecode(qr_image)
            data_label.config(text=data)

        except:
            showerror(title='ERROR', message='An error occurred while detecting data from the provided file.'
                                             '\nMake sure the image file is a valid QRCode')


# CREATING THE WINDOW
window = Tk()
window.title("QR code generator and reader")
window.iconbitmap(window, "qr_icon.ico")
window.geometry("500x480+340+80")
window.resizable(False, False)

window.protocol('WM_DELETE_WINDOW', close_window)


# WIDGETS STYLES
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 11))

entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Datum', 15))

button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font=('DatumChe', 10))


# SETTING THE NOTEBOOK AND THE TWO TABS
tab_control = ttk.Notebook(window)

first_tab = ttk.Frame(tab_control)
second_tab = ttk.Frame(tab_control)

tab_control.add(first_tab, text='QR code generator')
tab_control.add(second_tab, text='QR code reader')

tab_control.pack(expand=1, fill="both")


# MAKING A CANVAS TO EACH TAB
first_canvas = Canvas(first_tab, width=500, height=480)
first_canvas.pack()

second_canvas = Canvas(second_tab, width=500, height=480)
second_canvas.pack()


# ADDING WIDGETS TO THE QR GENERATOR TAB
image_label1 = Label(window)
first_canvas.create_window(250, 150, window=image_label1)


qr_data_label = ttk.Label(window, text='QR code data', style='TLabel')
data_entry = ttk.Entry(window, width=55, style='TEntry')

first_canvas.create_window(70, 330, window=qr_data_label)
first_canvas.create_window(300, 330, window=data_entry)

filename_label = ttk.Label(window, text='Filename', style='TLabel')
filename_entry = ttk.Entry(width=55, style='TEntry')

first_canvas.create_window(84, 360, window=filename_label)
first_canvas.create_window(300, 360, window=filename_entry)


reset_button = ttk.Button(window, text='RESET', style='TButton', state=DISABLED)
generate_button = ttk.Button(window, text='GENERATE', style='TButton', command=generate_qr_code)

first_canvas.create_window(300, 390, window=reset_button)
first_canvas.create_window(410, 390, window=generate_button)


# ADDING WIDGETS TO THE QR DETECTOR TAB
image_label2 = Label(window)
data_label = ttk.Label(window)

second_canvas.create_window(250, 150, window=image_label2)
second_canvas.create_window(250, 300, window=data_label)

file_entry = ttk.Entry(window, width=60, style='TEntry')
browse_button = ttk.Button(window, text='BROWSE', style='TButton', command=open_dialog)

second_canvas.create_window(200, 350, window=file_entry)
second_canvas.create_window(430, 350, window=browse_button)

detect_button = ttk.Button(window, text='QR code detect', style='TButton', command=reading_qr_code)
second_canvas.create_window(65, 385, window=detect_button)


window.mainloop()
