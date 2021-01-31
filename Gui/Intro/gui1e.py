from tkinter import *

# expand=YES : asks the packer to expand the allocated space
# for the widget in general into any unclaimed space in the
# widget's parent

# fill: can be used to stretch the widget to occupy all of its allocated
# space

Label(text='Hello GUI World!').pack(expand=YES,fill=BOTH)
mainloop()
