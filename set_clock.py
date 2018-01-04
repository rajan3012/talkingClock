__author__ = 'Rajan'


import tkinter as tk
from sound import Sound
import datetime
import tkinter.font as tkfont


###############################################################################
# Sound objects for the auditory menus and display.

# Hour sound objects
hour_sound_objects = [
    Sound( "wav_files/hours_f/6AM_f.wav" ),
    Sound( "wav_files/hours_f/7AM_f.wav" ),
    Sound( "wav_files/hours_f/8AM_f.wav" ),
    Sound( "wav_files/hours_f/9AM_f.wav" ),
    Sound( "wav_files/hours_f/10AM_f.wav" ),
    Sound( "wav_files/hours_f/11AM_f.wav" ),
    Sound( "wav_files/hours_f/12PM_f.wav" ),
    Sound( "wav_files/hours_f/1PM_f.wav" ),
    Sound( "wav_files/hours_f/2PM_f.wav" ),
    Sound( "wav_files/hours_f/3PM_f.wav" ),
    Sound( "wav_files/hours_f/4PM_f.wav" ),
    Sound( "wav_files/hours_f/5PM_f.wav" ),
    Sound( "wav_files/hours_f/6PM_f.wav" ),
    Sound( "wav_files/hours_f/7PM_f.wav" ),
    Sound( "wav_files/hours_f/8PM_f.wav" ),
    Sound( "wav_files/hours_f/9PM_f.wav" ),
    Sound( "wav_files/hours_f/10PM_f.wav" ),
    Sound( "wav_files/hours_f/11PM_f.wav" ),
    Sound( "wav_files/hours_f/12AM_f.wav" ),
    Sound( "wav_files/hours_f/1AM_f.wav" ),
    Sound( "wav_files/hours_f/2AM_f.wav" ),
    Sound( "wav_files/hours_f/3AM_f.wav" ),
    Sound( "wav_files/hours_f/4AM_f.wav" ),
    Sound( "wav_files/hours_f/5AM_f.wav" )
]


# Minute sound objects
minute_sound_objects = [
    Sound( "wav_files/minutes_f/00_f.wav" ),
    Sound( "wav_files/minutes_f/05_f.wav" ),
    Sound( "wav_files/minutes_f/10_f.wav" ),
    Sound( "wav_files/minutes_f/15_f.wav" ),
    Sound( "wav_files/minutes_f/20_f.wav" ),
    Sound( "wav_files/minutes_f/25_f.wav" ),
    Sound( "wav_files/minutes_f/30_f.wav" ),
    Sound( "wav_files/minutes_f/35_f.wav" ),
    Sound( "wav_files/minutes_f/40_f.wav" ),
    Sound( "wav_files/minutes_f/45_f.wav" ),
    Sound( "wav_files/minutes_f/50_f.wav" ),
    Sound( "wav_files/minutes_f/55_f.wav" )
]
'''
minute_sound_objects = [
    Sound( "wav_files/minutes_f/00_f.wav" ),
    Sound( "wav_files/minutes_f/01_f.wav" ),
    Sound( "wav_files/minutes_f/02_f.wav" ),
    Sound( "wav_files/minutes_f/03_f.wav" ),
    Sound( "wav_files/minutes_f/04_f.wav" ),
    Sound( "wav_files/minutes_f/05_f.wav" ),
    Sound( "wav_files/minutes_f/06_f.wav" ),
    Sound( "wav_files/minutes_f/07_f.wav" ),
    Sound( "wav_files/minutes_f/08_f.wav" ),
    Sound( "wav_files/minutes_f/09_f.wav" ),
    Sound( "wav_files/minutes_f/10_f.wav" ),
    Sound( "wav_files/minutes_f/11_f.wav" ),
    Sound( "wav_files/minutes_f/12_f.wav" ),
    Sound( "wav_files/minutes_f/13_f.wav" ),
    Sound( "wav_files/minutes_f/14_f.wav" ),
    Sound( "wav_files/minutes_f/15_f.wav" ),
    Sound( "wav_files/minutes_f/16_f.wav" ),
    Sound( "wav_files/minutes_f/17_f.wav" ),
    Sound( "wav_files/minutes_f/18_f.wav" ),
    Sound( "wav_files/minutes_f/19_f.wav" ),
    Sound( "wav_files/minutes_f/20_f.wav" ),
    Sound( "wav_files/minutes_f/21_f.wav" ),
    Sound( "wav_files/minutes_f/22_f.wav" ),
    Sound( "wav_files/minutes_f/23_f.wav" ),
    Sound( "wav_files/minutes_f/24_f.wav" ),
    Sound( "wav_files/minutes_f/25_f.wav" ),
    Sound( "wav_files/minutes_f/26_f.wav" ),
    Sound( "wav_files/minutes_f/27_f.wav" ),
    Sound( "wav_files/minutes_f/28_f.wav" ),
    Sound( "wav_files/minutes_f/29_f.wav" ),
    Sound( "wav_files/minutes_f/30_f.wav" ),
    Sound( "wav_files/minutes_f/31_f.wav" ),
    Sound( "wav_files/minutes_f/32_f.wav" ),
    Sound( "wav_files/minutes_f/33_f.wav" ),
    Sound( "wav_files/minutes_f/34_f.wav" ),
    Sound( "wav_files/minutes_f/35_f.wav" ),
    Sound( "wav_files/minutes_f/36_f.wav" ),
    Sound( "wav_files/minutes_f/37_f.wav" ),
    Sound( "wav_files/minutes_f/38_f.wav" ),
    Sound( "wav_files/minutes_f/39_f.wav" ),
    Sound( "wav_files/minutes_f/40_f.wav" ),
    Sound( "wav_files/minutes_f/41_f.wav" ),
    Sound( "wav_files/minutes_f/42_f.wav" ),
    Sound( "wav_files/minutes_f/43_f.wav" ),
    Sound( "wav_files/minutes_f/44_f.wav" ),
    Sound( "wav_files/minutes_f/45_f.wav" ),
    Sound( "wav_files/minutes_f/46_f.wav" ),
    Sound( "wav_files/minutes_f/47_f.wav" ),
    Sound( "wav_files/minutes_f/48_f.wav" ),
    Sound( "wav_files/minutes_f/49_f.wav" ),
    Sound( "wav_files/minutes_f/50_f.wav" ),
    Sound( "wav_files/minutes_f/51_f.wav" ),
    Sound( "wav_files/minutes_f/52_f.wav" ),
    Sound( "wav_files/minutes_f/53_f.wav" ),
    Sound( "wav_files/minutes_f/54_f.wav" ),
    Sound( "wav_files/minutes_f/55_f.wav" ),
    Sound( "wav_files/minutes_f/56_f.wav" ),
    Sound( "wav_files/minutes_f/57_f.wav" ),
    Sound( "wav_files/minutes_f/58_f.wav" ),
    Sound( "wav_files/minutes_f/59_f.wav" )
]
'''

# Days of the week sound objects
days_sound_objects = [
    Sound( "wav_files/days_of_week_f/monday_f.wav" ),
    Sound( "wav_files/days_of_week_f/tuesday_f.wav" ),
    Sound( "wav_files/days_of_week_f/wednesday_f.wav" ),
    Sound( "wav_files/days_of_week_f/thursday_f.wav" ),
    Sound( "wav_files/days_of_week_f/friday_f.wav" ),
    Sound( "wav_files/days_of_week_f/saturday_f.wav" ),
    Sound( "wav_files/days_of_week_f/sunday_f.wav" ),
]

entering_hour_sound = [
    Sound( "wav_files\entering_hour_f/entering_6am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_7am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_8am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_9am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_10am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_11am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_12pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_1pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_2pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_3pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_4pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_5pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_6pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_7pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_8pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_9pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_10pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_11pm.wav" ),
    Sound( "wav_files\entering_hour_f/entering_12am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_1am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_2am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_3am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_4am.wav" ),
    Sound( "wav_files\entering_hour_f/entering_5am.wav" )
]

entering_day_sound = [
    Sound( "wav_files\entering_day_f/entering_monday.wav" ),
    Sound( "wav_files\entering_day_f/entering_tuesday.wav" ),
    Sound( "wav_files\entering_day_f/entering_wednesday.wav" ),
    Sound( "wav_files\entering_day_f/entering_thursday.wav" ),
    Sound( "wav_files\entering_day_f/entering_friday.wav" ),
    Sound( "wav_files\entering_day_f/entering_saturday.wav" ),
    Sound( "wav_files\entering_day_f/entering_sunday.wav" ),
]

entering_minutes_sound = [
    Sound( "wav_files\entering_minute_f/entering_0.wav" ),
    Sound( "wav_files\entering_minute_f/entering_5.wav" ),
    Sound( "wav_files\entering_minute_f/entering_10.wav" ),
    Sound( "wav_files\entering_minute_f/entering_15.wav" ),
    Sound( "wav_files\entering_minute_f/entering_20.wav" ),
    Sound( "wav_files\entering_minute_f/entering_25.wav" ),
    Sound( "wav_files\entering_minute_f/entering_30.wav" ),
    Sound( "wav_files\entering_minute_f/entering_35.wav" ),
    Sound( "wav_files\entering_minute_f/entering_40.wav" ),
    Sound( "wav_files\entering_minute_f/entering_45.wav" ),
    Sound( "wav_files\entering_minute_f/entering_50.wav" ),
    Sound( "wav_files\entering_minute_f/entering_55.wav" ),

]
###############################################################################
# Create some sounds to assist with navigation.
PRESS_AGAIN_TO_QUIT = Sound \
    ( "wav_files/menus_modes_navigation_f/Press_again_to_quit_f.wav")

EXIT = Sound \
    ( "wav_files/menus_modes_navigation_f/exit_f.wav")

EXITING_PROGRAM = Sound \
    ( "wav_files/menus_modes_navigation_f/Exiting_program_f.wav")

SET_HOUR = Sound \
    ( "wav_files/menus_modes_navigation_f/Set_hour_f.wav")

SET_MINUTE = Sound \
    ( "wav_files/menus_modes_navigation_f/Set_minutes_f.wav")

SET_DAY = Sound \
    ( "wav_files/menus_modes_navigation_f/Set_day_of_week_f.wav" )

ENTER_MAIN_AND_DAY = Sound \
    ( "wav_files\entering_main_f/Entering_main_and_day.wav" )

ENTER_MAIN_AND_HOUR = Sound \
    ( "wav_files\entering_main_f/Entering_main_and_hour.wav" )

ENTER_MAIN_AND_MINUTE = Sound \
    ( "wav_files\entering_main_f/Entering_main_and_minute.wav" )

YOU_SELECTED = Sound \
    ( "wav_files/menus_modes_navigation_f/you_selected_f.wav" )

ENTER_MAIN_MENU = Sound \
    ( "wav_files/menus_modes_navigation_f/Entering_main_menu.wav" )

ENTER_HOUR_MENU = Sound \
    ( "wav_files/menus_modes_navigation_f/Entering_set_hour_menu.wav" )

ENTER_DAY_MENU = Sound \
    ( "wav_files/menus_modes_navigation_f/Entering_set_day_menu.wav" )

ENTER_MINUTES_MENU = Sound \
    ( "wav_files/menus_modes_navigation_f/Entering_set_minutes_menu.wav" )

WELCOME = Sound \
    ( "wav_files/menus_modes_navigation_f/complete_welcome.wav" )
################################################################################



class visual_clock():
    daybutton_dict= {}
    hourbutton_dict = {}
    minutebutton_dict = {}
    def __init__(self, parent):
        self.myParent = parent
        #self.myParent.config(bg = "white")
        #self.myMainFrame = tk.Frame.__init__(self, parent)S
        self.initUI()

    def initUI(self):
        self.myParent.title("Visual-Auditory clock")

        self.labelFrame = tk.Frame(self.myParent, bd = 2 , bg = "white")
        self.mainFrame = tk.Frame(self.myParent, bd = 2 , bg = "white")
        self.dayFrame = tk.Frame(self.myParent, bd = 2 , bg = "white")
        self.hourFrame = tk.Frame(self.myParent, bd = 2, bg = "white")
        self.minuteFrame = tk.Frame(self.myParent, bd =2, bg = "white")
        self.clockDetailsFrame = tk.Frame(self.myParent, bd =2 , bg = "white", relief = tk.RIDGE)

        self.separatorFrame1 = tk.Frame(self.myParent,bd = 2, height = 10, bg = 'white')
        self.separatorFrame2 = tk.Frame(self.myParent,bd = 2, height = 10, bg = 'white')
        self.separatorFrame3 = tk.Frame(self.myParent,bd = 2, height = 10, bg = 'white')
        self.separatorFrame4 = tk.Frame(self.myParent,bd = 2, height = 10, bg = 'white')
        self.separatorFrame5 = tk.Frame(self.myParent,bd = 2, height = 10, bg = 'white')
        #self.columnseparator = tk.Frame(self.myParent,bd = 2, , bg = 'white')
        #bindings
        self.myParent.bind("<j>", self.keyPress)
        self.myParent.bind("<J>", self.keyPress)
        self.myParent.bind("<k>", self.keyPress)
        self.myParent.bind("<K>", self.keyPress)
        self.myParent.bind("<space>", self.keyPress)
        self.myParent.bind("<Tab>", self.no_op)
        #self.myParent.bind("<Tab>",FocusIn)
        self.myParent.bind_class("Button","<FocusIn>",focusInHandler)
        self.myParent.bind_class("Button","<FocusOut>",focusOutHandler)
        self.myParent.bind("<Button-1>",self.mouseClick) #left
        #self.myParent.bind("<Button-2>",self.mouseClick) #mid
        #self.myParent.bind("<Button-3>",self.mouseClick)  #right
        #self.myParent.bind("<Button-4>",self.mouseClick) #scroll up
        #self.myParent.bind("<Button-5>",self.mouseClick) # scroll down

        #disable click on other areas of frame.
        self.labelFrame.bind("<Button-1>", self.no_op)
        self.mainFrame.bind("<Button-1>", self.no_op)
        self.dayFrame.bind("<Button-1>", self.no_op)
        self.hourFrame.bind("<Button-1>", self.no_op)
        self.minuteFrame.bind("<Button-1>", self.no_op)
        self.clockDetailsFrame.bind("<Button-1>", self.no_op)
        self.separatorFrame1.bind("<Button-1>", self.no_op)
        self.separatorFrame2.bind("<Button-1>", self.no_op)
        self.separatorFrame3.bind("<Button-1>", self.no_op)
        self.separatorFrame4.bind("<Button-1>", self.no_op)
        self.separatorFrame5.bind("<Button-1>", self.no_op)
        '''#disable hover
        self.myParent.bind('<Enter>', self.no_op)
        self.myParent.bind('<Leave>', self.no_op)'''
        #create frame grid


        #frames gridding
        self.labelFrame.pack(fill = tk.X)
        self.separatorFrame1.pack(fill = tk.X)
        self.mainFrame.pack(fill = tk.X)
        self.separatorFrame2.pack(fill = tk.X)
        self.dayFrame.pack(fill = tk.X)
        self.separatorFrame3.pack(fill = tk.X)
        self.hourFrame.pack(fill = tk.X)
        self.separatorFrame4.pack(fill = tk.X)
        self.minuteFrame.pack(fill = tk.X)
        self.separatorFrame5.pack(fill = tk.X)
        self.clockDetailsFrame.pack(fill = tk.X)
        #self.separatorFrame.pack(fill = tk.X)

        #create the grid inside the labels
        #Label frame grid
        self.labelFrame.columnconfigure(0, pad=25)
        self.labelFrame.columnconfigure(1, pad=70)
        self.labelFrame.rowconfigure(0, pad=20)

        #MAIN FRAME GRID
        self.mainFrame.columnconfigure(0, pad=25)
        self.mainFrame.columnconfigure(1, pad=5) #setday
        self.mainFrame.columnconfigure(2, pad=5) #set hour
        self.mainFrame.columnconfigure(3, pad=5) # set minute
        self.mainFrame.columnconfigure(4, pad=5) # exit

        self.mainFrame.rowconfigure(0, pad=5)

        #DAY frame Grid creation
        self.dayFrame.rowconfigure(0, pad=2)

        self.dayFrame.columnconfigure(0,pad=25)
        self.dayFrame.columnconfigure(1, pad=5) #monday
        self.dayFrame.columnconfigure(2, pad=5) #tuesday
        self.dayFrame.columnconfigure(3, pad=5) #wednesday
        self.dayFrame.columnconfigure(4, pad=5) #thursday
        self.dayFrame.columnconfigure(5, pad=5) #friday
        self.dayFrame.columnconfigure(6, pad=5) #saturday
        self.dayFrame.columnconfigure(7, pad=5) #sunday

        #HOUR frame GRID creation
        self.hourFrame.columnconfigure(0, pad = 25)
        for i in range(1,13):
            self.hourFrame.columnconfigure(i, pad = 5)

        for i in range(0,2):
            self.hourFrame.rowconfigure(i, pad = 5)

        #MINUTE frame GRID creation
        self.minuteFrame.columnconfigure(0, pad = 25)
        for i in range(1,13):
            self.minuteFrame.columnconfigure(i, pad = 5)

        for i in range(0,5):
            self.minuteFrame.rowconfigure(i, pad = 5)

        #CLOCK DETAILS grid
        self.clockDetailsFrame.columnconfigure(0, pad = 25)
        self.clockDetailsFrame.columnconfigure(1, pad = 5)
        self.clockDetailsFrame.columnconfigure(2, pad = 5)
        self.clockDetailsFrame.columnconfigure(3, pad = 5)
        self.clockDetailsFrame.columnconfigure(4, pad = 5)

        self.clockDetailsFrame.rowconfigure(0, pad = 5)

        #create widgets
        self.createWidgets()
        self.disableWidgets(self.dayFrame.winfo_children())
        self.disableWidgets(self.hourFrame.winfo_children())
        self.disableWidgets(self.minuteFrame.winfo_children())
        WELCOME.play()

    def no_op(self, event):
        return "break"

    def disableWidgets(self, childList):

        for child in childList:
            child["state"] = tk.DISABLED

    def enableWidgets(self, childList):
        for child in childList:
            child["state"] = tk.NORMAL

    def createWidgets(self):
        defaultFont  = tkfont.nametofont("TkDefaultFont")
        print('Default font family', defaultFont["family"])
        buttonFont = tkfont.Font(family = 'Segoe UI', size=9, weight = 'bold')

        #Main frame gridding
        '''self.menuLabel = tk.Label(self.labelFrame, text = "Menu", fg = "black", bg = "white")
        self.menuLabel.grid(row = 0, column = 0)
        self.menuLabel.bind("<Button-1>",self.no_op)

        self.menuItemsLabel = tk.Label(self.labelFrame, text = "Menu Items", fg = "black", bg = "white")
        self.menuItemsLabel.grid(row = 0, column = 1)
        self.menuItemsLabel.bind("<Button-1>",self.no_op)'''

        ############Level1 - Main Menu
        '''self.mainmenuButton = tk.Button(self.mainFrame, text = "Main Menu", takefocus = 0, width = 12, font = buttonFont)
        self.mainmenuButton.grid(row = 0, column = 0)
        print("Main Menu id - ",self.mainmenuButton)
        self.mainmenuButton.bind("<Button-1>",self.no_op)'''

        self.setDayButton = tk.Button(self.mainFrame, text = "Set Day", width = 12, font = buttonFont)
        self.setDayButton.grid(row = 0, column = 1)
        print("Set day id -",self.setDayButton)

        self.setHourButton = tk.Button(self.mainFrame, text = "Set Hour", width = 12, font = buttonFont)
        self.setHourButton.grid(row = 0, column = 2)
        print("Set hour id -",self.setHourButton)

        self.setMinutesButton = tk.Button(self.mainFrame, text = "Set Minutes", width = 12,font = buttonFont)
        self.setMinutesButton.grid(row = 0, column = 3)
        print("Set minutes id -",self.setMinutesButton)

        self.exitButton = tk.Button(self.mainFrame, text = "Exit Program", width = 12, font = buttonFont)
        self.exitButton.grid(row = 0, column = 4)
        print("Exit id -",self.exitButton)
        #self.exitButton.bind("<Button-1>", self.exitProgram)
        #self.exitButton.bind("<space>", self.exitProgram)

        ##############Level2 - Set day

        '''self.setDay2 = tk.Button(self.dayFrame, text = "Set Day",overrelief = tk.RIDGE, width = 12, takefocus =0)
        self.setDay2.grid(row = 0, column = 0)
        self.setDay2.bind("<Button-1>",self.no_op)'''

        daylist = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        dcol = 1
        for daytext in daylist:
            self.daybutton_dict[daytext] = tk.Button(self.dayFrame, text = daytext,width = 12, font = buttonFont)
            self.daybutton_dict[daytext].grid(row = 0, column = dcol)
            dcol+=1

        #print(self.daybutton_dict)

        #######LEVEL 3 - Set hour

        '''self.setHour2 = tk.Button(self.hourFrame, text = "Set Hour",overrelief = tk.RIDGE, width = 12, takefocus =0)
        self.setHour2.grid(row = 0, column = 0)
        self.setHour2.bind("<Button-1>",self.no_op)'''

        amPMtext = "AM"
        hourtext = 6
        hourlist = []
        for i in range(1,25):
            if i>=7 and i<=18:
                ampmtext = "PM"
            else:
                ampmtext = "AM"
            hourlist.append(str(hourtext)+ampmtext)
            hourtext = (hourtext + 1)%13
            if hourtext == 0:
                hourtext+=1

        hcol = 1
        hrow = 0
        #print(hourlist)
        count = 0
        for hrow in range(0,2):
            #print("Hrow",hrow)
            for hcol in range(1,13):
                hourtext = hourlist[count]
                #print("Hcol",hcol)
                #print("HOUrtext - ", hourtext)
                self.hourbutton_dict[hourtext] = tk.Button(self.hourFrame, text=hourtext, width =8 ,font = buttonFont)
                #print("button id of ",hourtext," is", self.hourbutton_dict[hourtext])
                self.hourbutton_dict[hourtext].grid(row=hrow, column=hcol, pady=2)
                count+=1




        #######LEVEL 4 - Set minutes
        '''self.setMinute2 = tk.Button(self.minuteFrame, text = "Set Minutes",overrelief = tk.RIDGE, width = 12, takefocus =0)
        self.setMinute2.grid(row = 0, column = 0)
        self.setMinute2.bind("<Button-1>",self.no_op)'''

        minutelist = []
        for i in range(0,60,5):
            minutetext = str(str(i).zfill(2))
            minutelist.append(minutetext)

        count = 0
        #print(minutelist)
        for mrow in range(0,1):
            for mcol in range(1,13):
                minutetext = minutelist[count]
                #print("MinuteText - ", minutetext)
                self.minutebutton_dict[minutetext] = tk.Button(self.minuteFrame, text = minutetext, width =8, font = buttonFont)
                #print("button id of ",minutetext," is", self.minutebutton_dict[minutetext])
                self.minutebutton_dict[minutetext].grid(row=mrow, column=mcol, pady=2)
                count+=1

        #print(self.minutebutton_dict)
        #####CLOCK DETAILS
        self.clockDetailsLabel = tk.Label(self.clockDetailsFrame, text = "Clock Details ->", fg = "black", bg = "white")
        self.clockDetailsLabel.grid(row = 0, column = 1)
        self.clockDetailsLabel.bind("<Button-1>",self.no_op)

        self.selectedDayLabel = tk.Label(self.clockDetailsFrame, fg = "black", bg = "white")
        self.selectedDayLabel["text"] = "Not selected"
        self.selectedDayLabel.grid(row = 0, column = 2)
        self.selectedDayLabel.bind("<Button-1>",self.no_op)

        self.selectedHourLabel = tk.Label(self.clockDetailsFrame, fg = "black", bg = "white")
        self.selectedHourLabel["text"] = "Not selected"
        self.selectedHourLabel.grid(row = 0, column = 3)
        self.selectedHourLabel.bind("<Button-1>",self.no_op)

        self.selectedMinutesLabel = tk.Label(self.clockDetailsFrame, fg = "black", bg = "white")
        self.selectedMinutesLabel["text"] = "Not selected"
        self.selectedMinutesLabel.grid(row = 0, column = 4)
        self.selectedMinutesLabel.bind("<Button-1>",self.no_op)

    def exitProgram(self, event):
        print("Exiting Program")
        EXITING_PROGRAM.play_to_end()
        #time.sleep(10)
        self.myParent.destroy()


    def mouseClick(self, event):
        #if event.widget in self.mainFrame.winfo_children() or event.widget in self.hourFrame.winfo_children() or event.widget in self.dayFrame.winfo_children() or event.widget in self.minuteFrame:
        report_event(event)

    def keyPress(self, event):
        try:
            report_event(event)
        except Exception:
            print("Error:")

def report_event(event):     ### (5)
    global firstEntry
    event_name = {"2": "KeyPress", "4": "ButtonPress"} #dictionary
    print ("Time:", str(event.time))
    print ("EventType=" + str(event.type))
    #print("EventName = " + event_name[str(event.type)])
    print ("EventWidgetId=" + str(event.widget), \
           "EventKeySymbol=" + str(event.keysym), \
           "Widget Name=" + str(event.widget.focus_displayof),\
           "Event Number="+ str(event.num))

    if firstEntry == True :
        print('First ENtry in report event', str(firstEntry))
        if event.num == 1 or event.keysym == 'space': #first selection buttons disabled
            myapp.no_op(event)
        else:
            print('First ENtry in report event else', str(firstEntry))
            ENTER_MAIN_MENU.play_to_end()
            myapp.setDayButton.focus_set()
            firstEntry = False
    else:
        key_action(event)
    #print("widget details",event.widget.get())

def checkSelectedWidget(event,selectedWidget):
    if selectedWidget is None:
         selectedWidget = event.widget
    else:
        selectedWidget["bg"] = defaultbg
        selectedWidget = event.widget

    selectedWidget["background"] = "#cce5ff"
    return selectedWidget

def spacePressAction(event):
    global selected_menuWidget
    global selected_dayWidget
    global selected_minuteWidget
    global selected_hourWidget

    global firstDay
    global firstMinute
    global firstHour

    global blueWidget
    global transition_sound
    current_datetime = datetime.datetime.now()
    now_day = current_datetime.strftime("%A")
    now_hour = current_datetime.strftime("%I%p")
    now_hour = now_hour.lstrip('0')
    now_minutes = current_datetime.strftime("%M")
    now_minutes = str(int(round(int(now_minutes)/5)*5)).zfill(2) #rounding to nearest integer
    print("NOW Day - ",now_day)
    print("NOW Hour - ",now_hour)
    print("NOW Minutes - ", now_minutes)

    if event.widget["state"] != tk.DISABLED:
        # enable next level
        #day
        print("Button pressed not disabled")
        #print("Event Widget ->", event.widget)
        #print("Exit Button id ->", myapp.exitButton)
        #exit
        if event.widget == myapp.exitButton:
            print("Exit button pressed")
            #report_event(event)   ### (4)
            myapp.exitProgram(event) #kills gui
            exit() #end program

        #set day
        if event.widget == myapp.setDayButton:
            # myapp.dayFrame["state"] = tk.ACTIVE
            selected_menuWidget = checkSelectedWidget(event, selected_menuWidget)
            myapp.disableWidgets(myapp.mainFrame.winfo_children())
            myapp.enableWidgets(myapp.dayFrame.winfo_children())
            transition_sound = True
            if firstDay == True:
                myapp.daybutton_dict[now_day].focus_set()
                firstDay = False
            else:
                selected_dayWidget.focus_set()

        #day slected
        if event.widget in myapp.dayFrame.winfo_children():
            #for single selcteion on levels 2 and below
            selected_dayWidget = checkSelectedWidget(event, selected_dayWidget)
            print("Day selected = ", selected_dayWidget["text"])
            myapp.selectedDayLabel.config(text = str(selected_dayWidget["text"]))
            myapp.enableWidgets(myapp.mainFrame.winfo_children())
            myapp.disableWidgets(myapp.dayFrame.winfo_children())
            transition_sound = True
            myapp.setDayButton.focus_set()
            myapp.setDayButton.config(bg = defaultbg)

        #set hour
        if event.widget == myapp.setHourButton:
            selected_menuWidget = checkSelectedWidget(event, selected_menuWidget)
            myapp.disableWidgets(myapp.mainFrame.winfo_children())
            myapp.enableWidgets(myapp.hourFrame.winfo_children())
            transition_sound = True
            if firstHour == True:
                myapp.hourbutton_dict[now_hour].focus_set()
                firstHour = False
            else:
                selected_hourWidget.focus_set()

        #hour selected
        if event.widget in myapp.hourFrame.winfo_children():
            #for single selcteion on levels 2 and below
            selected_hourWidget = checkSelectedWidget(event, selected_hourWidget)
            print("Hour selected = ", selected_hourWidget["text"])
            myapp.selectedHourLabel.config(text = str(selected_hourWidget["text"]))
            myapp.enableWidgets(myapp.mainFrame.winfo_children())
            myapp.disableWidgets(myapp.hourFrame.winfo_children())
            transition_sound = True
            myapp.setHourButton.focus_set()
            myapp.setHourButton.config(bg = defaultbg)

        #set minute
        if event.widget == myapp.setMinutesButton:
            selected_menuWidget = checkSelectedWidget(event, selected_menuWidget)
            myapp.disableWidgets(myapp.mainFrame.winfo_children())
            myapp.enableWidgets(myapp.minuteFrame.winfo_children())
            transition_sound = True
            #myapp.minutebutton_dict["00"].focus_set()
            if firstMinute == True:
                myapp.minutebutton_dict[now_minutes].focus_set()
                firstMinute = False
            else:
                selected_minuteWidget.focus_set()


        #minute selected
        if event.widget in myapp.minuteFrame.winfo_children():
            #for single selcteion on levels 2 and below
            selected_minuteWidget = checkSelectedWidget(event, selected_minuteWidget)
            print("Minute selected = ", selected_minuteWidget["text"])
            myapp.selectedMinutesLabel.config(text = str(selected_minuteWidget["text"])) #entering the selection in the label;
            myapp.enableWidgets(myapp.mainFrame.winfo_children())
            myapp.disableWidgets(myapp.minuteFrame.winfo_children())
            transition_sound = True
            myapp.setMinutesButton.focus_set()
            myapp.setMinutesButton.config(bg = defaultbg)

    blueWidget = event.widget

def key_action(event):

    nextWidget = event.widget.tk_focusNext()
    print("Next widget -",nextWidget)
    prevWidget = event.widget.tk_focusPrev()
    print("Previous widget -",prevWidget)
    if (event.keysym).lower() == 'k':
        nextWidget.focus_set()
    if (event.keysym).lower() == 'j':
        prevWidget.focus_set()
    if event.keysym == 'space':# or event.type == '4':
        print("SPACE press on BUTTONS")
        spacePressAction(event)
    if event.type == '4':
        print("MOUSE CLICK on BUTTONS")
        print("Event num is - ", event.num)
        if event.num == 1: #left mouse click
            #focusInHandler(event)   #to speak out
            spacePressAction(event)

def focusInHandler(event):
    global blueWidget
    global transition_sound
    global firstEntry
    print("FocusIn -",event.widget)
    if event.widget["background"] == "#cce5ff":
        blueWidget = event.widget
        print('*******Blue-widget***** =',blueWidget["text"])
    event.widget.configure(bg = "#ffff66")
    if event.widget == myapp.setHourButton:
        print("set hour")
        if transition_sound == False:
            SET_HOUR.play()
        else:
            ENTER_MAIN_AND_HOUR.play()
            transition_sound = False
    if event.widget == myapp.setMinutesButton:
        print("set minutes")
        if transition_sound == False:
            SET_MINUTE.play()
        else:
            ENTER_MAIN_AND_MINUTE.play()
            transition_sound = False
    if event.widget == myapp.setDayButton:
        print("set day")
        print("first entry value",str(firstEntry))
        if transition_sound == False:
            SET_DAY.play()
        else:
            ENTER_MAIN_AND_DAY.play()
            transition_sound = False
    if event.widget == myapp.exitButton:
        print("exit program")
        EXIT.play()

    if event.widget in myapp.dayFrame.winfo_children(): #for days
        position = myapp.dayFrame.winfo_children().index(event.widget)
        print("Postiton of widget ->", position)
        if transition_sound == False:
            days_sound_objects[position].play()
        else:
            entering_day_sound[position].play()
            transition_sound = False
    if event.widget in myapp.hourFrame.winfo_children(): #for hours
        position = myapp.hourFrame.winfo_children().index(event.widget)
        print("Postiton of widget ->", position)
        if transition_sound == False:
            hour_sound_objects[position].play()
        else:
            entering_hour_sound[position].play()
            transition_sound = False
    if event.widget in myapp.minuteFrame.winfo_children(): #for hours
        position = myapp.minuteFrame.winfo_children().index(event.widget)
        print("Postiton of widget ->", position)
        if transition_sound == False:
            minute_sound_objects[position].play()
        else:
            entering_minutes_sound[position].play()
            transition_sound = False

def focusOutHandler(event):
    #if event.widget["background"] != "#cce5ff":
    if event.widget!= blueWidget:
        event.widget.configure(bg = defaultbg)
    elif event.widget == blueWidget:
        event.widget.configure(bg = "#cce5ff")
    print("FocusOut - ",event.widget)


#for first enterance in menu
firstHour = True
firstDay = True
firstMinute = True
blueWidget = None

#
transition_sound = False
#for enterance in program
firstEntry = True
#for recording selected clock details
selected_menuWidget = None
selected_dayWidget= None
selected_hourWidget = None
selected_minuteWidget = None
root = tk.Tk()
defaultbg = root.cget('bg')
myapp = visual_clock(root)
root.mainloop()


