"""
Project.1
"""
from tkinter import *
import datetime
from typing import Any

app = Tk()
app.title("Health App - 0")
app.geometry('600x500')

duration = [datetime.datetime(1995, 1, 1), datetime.datetime(1995, 2, 1),
            datetime.datetime(1995, 3, 1), datetime.datetime(1995, 4, 1),
            datetime.datetime(1995, 5, 1), datetime.datetime(1995, 6, 1),
            datetime.datetime(1995, 7, 1), datetime.datetime(1995, 8, 1),
            datetime.datetime(1995, 9, 1), datetime.datetime(1995, 10, 1),
            datetime.datetime(1995, 11, 1), datetime.datetime(1995, 12, 1),
            datetime.datetime(1996, 1, 1), datetime.datetime(1996, 2, 1),
            datetime.datetime(1996, 3, 1), datetime.datetime(1996, 4, 1),
            datetime.datetime(1996, 5, 1), datetime.datetime(1996, 6, 1),
            datetime.datetime(1996, 7, 1), datetime.datetime(1996, 8, 1),
            datetime.datetime(1996, 9, 1), datetime.datetime(1996, 10, 1),
            datetime.datetime(1996, 11, 1), datetime.datetime(1996, 12, 1)
            ]
first_date = 1
last_date = 100,000


day_scale = Scale(app, orient=HORIZONTAL, length=500, width=20, sliderlength=10,
                   from_=first_date.day, to=last_date.day, tickinterval=1)
day_scale.pack()


def get_value():
    # my_year = Label(app, text=year_slider.get()).pack()
    # my_month = Label(app, text=month_slider.get()).pack()
    # final = (my_year, my_month)
    year_value = (Label(app, text=year_scale.get()).pack())
    month_value = (Label(app, text=month_scale.get()).pack())
    date_value = (Label(app, text=date_scale.get()).pack())
    output = 'the selected date is: ' + str(year_value) + str(month_value) + \
             str(date_value)
    return output


# Label(app, text=month_scale.get()).pack(),
# Label(app, text=date_scale.get()).pack())

year_button = Button(app, text='select the date', command=get_value).pack()

app.mainloop()
