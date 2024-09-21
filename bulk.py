import tkinter as tk
import ttkbootstrap as ttk
import pyautogui 
import time

def start():
    time.sleep(10)
    #getting values from the user
    getmsg = input_String.get()
    getno = input_int .get()
    
    for i in range (getno):
        pyautogui.typewrite(getmsg)
        pyautogui.press('enter')
    dispmsg =  outputmsg.set( f"{getno} Msg Has Been Sent")
        


window = tk.Tk()

#Window Title
window.title('Bulk MSG Tool')
window.iconbitmap('alert.ico')

#Window Size
window.minsize(300,260)
window.maxsize(300,260)

#heading
heading = tk.Label(master = window, font ='Ariel 10 italic', text = 'MSG BOX')
heading.pack(padx=1-0, pady=10)

outputmsg = tk.StringVar()
output = tk.Label(master=window, font = 'Ariel 10 bold', text='0 Msg Has Been Sent', textvariable = outputmsg )
output.pack()

#Container for Button label and Entry
main_frame = ttk.Frame(master=window)

#label for Number
DisplayNumber = tk.Label(master=main_frame, text = 'Enter How Many Msg To Be Sent', font = 'Ariel 10 bold')
DisplayNumber.pack(padx = 5, pady = 5)

#input from user for integer value
input_int = tk.IntVar()
input_entry = ttk.Entry(master = main_frame, textvariable = input_int)
input_entry.pack( fill = 'x', padx = 5, pady= 5)


#label for Msg
DisplayMsg = tk.Label(master=main_frame, text = 'Enter What Msg To Be Sent.', font = 'Ariel 10 bold')
DisplayMsg.pack(padx = 5, pady = 5)

input_String = tk.StringVar()
input_String = ttk.Entry(master = main_frame, textvariable = input_String)
input_String.pack( fill = 'x', padx = 5, pady= 5)


#start Buttoon
start = ttk.Button(master =  main_frame, text='Start', command=start)
start.pack(fill= 'x', padx = 15, pady= 15)

main_frame.pack()


window.mainloop()