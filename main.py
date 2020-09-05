from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.metrics import sp
from kivy.core.window import Window
from kivy.graphics import Color, BorderImage
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.clock import Clock
from functools import partial
import numpy as np
import random
import Sudoku

'''
Class: WelcomePage
    Starting Screen of the App.
    Function: selected_level 
        Read the difficulty level selection and move to Game Screen.
Class: Matrixpage
    Main Game screen, Here the 9*9 Sudoku window will appear along with buttons.
    Function: sudoku_fun
        calling the Sudoku algorithms model and place the values to the 9*9 game area,
        according to the difficulty level and dynamically choose the entered columns
    Function: check_matrix 
        Check button functionality.
        Compare the entered the values show the WRONG bubble using show bubble function 
    Function: remove_bubble
        To remove the message after couble of seconds.
    Function: show_bubble
        Show the WRONG message to the user.
    Function: home_page
        Home button functionality.
        Back to Home scree WelcomPage.
    Function: new_page
        New button functionality.
        show the new game with the same difficulty level        
    Function: clear_val
        Clear button functionality.
        Clear all the entred values.
'''


class WelcomePage(BoxLayout):

    # - Level selection
    def selected_level(self, value):
        global level_text
        print("selected level: ", value)
        level_text = value
        self.clear_widgets()
        self.add_widget(Matrixpage())


class Matrixpage(AnchorLayout):
    scount = 0
    mcount = 0
    check_text = StringProperty()
    dl_text = StringProperty()
    dynamic_button = StringProperty()
    r0c0 = StringProperty()
    r0c1 = StringProperty()
    r0c2 = StringProperty()
    r0c3 = StringProperty()
    r0c4 = StringProperty()
    r0c5 = StringProperty()
    r0c6 = StringProperty()
    r0c7 = StringProperty()
    r0c8 = StringProperty()
    r1c1 = StringProperty()
    r1c0 = StringProperty()
    r1c2 = StringProperty()
    r1c3 = StringProperty()
    r1c4 = StringProperty()
    r1c5 = StringProperty()
    r1c6 = StringProperty()
    r1c7 = StringProperty()
    r1c8 = StringProperty()
    r2c0 = StringProperty()
    r2c1 = StringProperty()
    r2c2 = StringProperty()
    r2c3 = StringProperty()
    r2c4 = StringProperty()
    r2c5 = StringProperty()
    r2c6 = StringProperty()
    r2c7 = StringProperty()
    r2c8 = StringProperty()
    r3c0 = StringProperty()
    r3c1 = StringProperty()
    r3c2 = StringProperty()
    r3c3 = StringProperty()
    r3c4 = StringProperty()
    r3c5 = StringProperty()
    r3c6 = StringProperty()
    r3c7 = StringProperty()
    r3c8 = StringProperty()
    r4c0 = StringProperty()
    r4c1 = StringProperty()
    r4c2 = StringProperty()
    r4c3 = StringProperty()
    r4c4 = StringProperty()
    r4c5 = StringProperty()
    r4c6 = StringProperty()
    r4c7 = StringProperty()
    r4c8 = StringProperty()
    r5c0 = StringProperty()
    r5c1 = StringProperty()
    r5c2 = StringProperty()
    r5c3 = StringProperty()
    r5c4 = StringProperty()
    r5c5 = StringProperty()
    r5c6 = StringProperty()
    r5c7 = StringProperty()
    r5c8 = StringProperty()
    r6c0 = StringProperty()
    r6c1 = StringProperty()
    r6c2 = StringProperty()
    r6c3 = StringProperty()
    r6c4 = StringProperty()
    r6c5 = StringProperty()
    r6c6 = StringProperty()
    r6c7 = StringProperty()
    r6c8 = StringProperty()
    r7c0 = StringProperty()
    r7c1 = StringProperty()
    r7c2 = StringProperty()
    r7c3 = StringProperty()
    r7c4 = StringProperty()
    r7c5 = StringProperty()
    r7c6 = StringProperty()
    r7c7 = StringProperty()
    r7c8 = StringProperty()
    r8c0 = StringProperty()
    r8c1 = StringProperty()
    r8c2 = StringProperty()
    r8c3 = StringProperty()
    r8c4 = StringProperty()
    r8c5 = StringProperty()
    r8c6 = StringProperty()
    r8c7 = StringProperty()
    r8c8 = StringProperty()

    def __init__(self, **kwargs):
        super(Matrixpage, self).__init__(**kwargs)
        self.sudoku_fun()
        Matrixpage.show_timer(self)
        print("12ds")

    def sudoku_fun(self):
        global level_text
        if level_text == 1:
            self.dl_text = 'Easy'
        elif level_text == 2:
            self.dl_text = 'Medium'
        elif level_text == 3:
            self.dl_text = 'Tricky'
        else:
            self.dl_text = 'oops'

        global row1, row2, row3, row4, row5, row6, row7, row8, row9
        s_matrix = np.zeros((9, 9), dtype=np.uint8)
        rv = Sudoku.smain()
        print(Sudoku.a)
        s_matrix = Sudoku.a

        # Select the value to display in a sudoku row and column
        item = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if level_text == 1:
            choice_item = [3, 4, 5, 6, 7]
            #Row1:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r1d_value = item[0:no_column]
            #Row2:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r2d_value = item[0:no_column]
            #Row3:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r3d_value = item[0:no_column]
            #Row4:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r4d_value = item[0:no_column]
            #Row5:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r5d_value = item[0:no_column]
            #Row6:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r6d_value = item[0:no_column]
            #Row7:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r7d_value = item[0:no_column]
            #Row8:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r8d_value = item[0:no_column]
            #Row9:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r9d_value = item[0:no_column]
        elif level_text == 2:
            choice_item = [2, 3, 4, 5, 6]
            #Row1:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r1d_value = item[0:no_column]
            #Row2:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r2d_value = item[0:no_column]
            #Row3:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r3d_value = item[0:no_column]
            #Row4:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r4d_value = item[0:no_column]
            #Row5:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r5d_value = item[0:no_column]
            #Row6:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r6d_value = item[0:no_column]
            #Row7:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r7d_value = item[0:no_column]
            #Row8:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r8d_value = item[0:no_column]
            #Row9:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r9d_value = item[0:no_column]
        elif level_text == 3:
            choice_item = [0, 1, 2, 3, 4]
            #Row1:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r1d_value = item[0:no_column]
            #Row2:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r2d_value = item[0:no_column]
            #Row3:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r3d_value = item[0:no_column]
            #Row4:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r4d_value = item[0:no_column]
            #Row5:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r5d_value = item[0:no_column]
            #Row6:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r6d_value = item[0:no_column]
            #Row7:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r7d_value = item[0:no_column]
            #Row8:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r8d_value = item[0:no_column]
            #Row9:
            random.shuffle(item)
            no_column = random.choice(choice_item)
            r9d_value = item[0:no_column]

        display_value = r1d_value
        row1 = display_value
        if 1 in display_value:
            self.r0c0 = str(s_matrix[0, 0])
        else:
            self.r0c0 = ""
        if 2 in display_value:
            self.r0c1 = str(s_matrix[0, 1])
        else:
            self.r0c1 = ""
        if 3 in display_value:
            self.r0c2 = str(s_matrix[0, 2])
        else:
            self.r0c2 = ""
        if 4 in display_value:
            self.r0c3 = str(s_matrix[0, 3])
        else:
            self.r0c3 = ""
        if 5 in display_value:
            self.r0c4 = str(s_matrix[0, 4])
        else:
            self.r0c4 = ""
        if 6 in display_value:
            self.r0c5 = str(s_matrix[0, 5])
        else:
            self.r0c5 = ""
        if 7 in display_value:
            self.r0c6 = str(s_matrix[0, 6])
        else:
            self.r0c6 = ""
        if 8 in display_value:
            self.r0c7 = str(s_matrix[0, 7])
        else:
            self.r0c7 = ""
        if 9 in display_value:
            self.r0c8 = str(s_matrix[0, 8])
        else:
            self.r0c8 = ""

        display_value = r2d_value
        row2 = display_value
        if 1 in display_value:
            self.r1c0 = str(s_matrix[1, 0])
        else:
            self.r1c0 = ""
        if 2 in display_value:
            self.r1c1 = str(s_matrix[1, 1])
        else:
            self.r1c1 = ""
        if 3 in display_value:
            self.r1c2 = str(s_matrix[1, 2])
        else:
            self.r1c2 = ""
        if 4 in display_value:
            self.r1c3 = str(s_matrix[1, 3])
        else:
            self.r1c3 = ""
        if 5 in display_value:
            self.r1c4 = str(s_matrix[1, 4])
        else:
            self.r1c4 = ""
        if 6 in display_value:
            self.r1c5 = str(s_matrix[1, 5])
        else:
            self.r1c5 = ""
        if 7 in display_value:
            self.r1c6 = str(s_matrix[1, 6])
        else:
            self.r1c6 = ""
        if 8 in display_value:
            self.r1c7 = str(s_matrix[1, 7])
        else:
            self.r1c7 = ""
        if 9 in display_value:
            self.r1c8 = str(s_matrix[1, 8])
        else:
            self.r1c8 = ""

        display_value = r3d_value
        row3 = display_value
        if 1 in display_value:
            self.r2c0 = str(s_matrix[2, 0])
        else:
            self.r2c0 = ""
        if 2 in display_value:
            self.r2c1 = str(s_matrix[2, 1])
        else:
            self.r2c1 = ""
        if 3 in display_value:
            self.r2c2 = str(s_matrix[2, 2])
        else:
            self.r2c2 = ""
        if 4 in display_value:
            self.r2c3 = str(s_matrix[2, 3])
        else:
            self.r2c3 = ""
        if 5 in display_value:
            self.r2c4 = str(s_matrix[2, 4])
        else:
            self.r2c4 = ""
        if 6 in display_value:
            self.r2c5 = str(s_matrix[2, 5])
        else:
            self.r2c5 = ""
        if 7 in display_value:
            self.r2c6 = str(s_matrix[2, 6])
        else:
            self.r2c6 = ""
        if 8 in display_value:
            self.r2c7 = str(s_matrix[2, 7])
        else:
            self.r2c7 = ""
        if 9 in display_value:
            self.r2c8 = str(s_matrix[2, 8])
        else:
            self.r2c8 = ""

        display_value = r4d_value
        row4 = display_value
        if 1 in display_value:
            self.r3c0 = str(s_matrix[3, 0])
        else:
            self.r3c0 = ""
        if 2 in display_value:
            self.r3c1 = str(s_matrix[3, 1])
        else:
            self.r3c1 = ""
        if 3 in display_value:
            self.r3c2 = str(s_matrix[3, 2])
        else:
            self.r3c2 = ""
        if 4 in display_value:
            self.r3c3 = str(s_matrix[3, 3])
        else:
            self.r3c3 = ""
        if 5 in display_value:
            self.r3c4 = str(s_matrix[3, 4])
        else:
            self.r3c4 = ""
        if 6 in display_value:
            self.r3c5 = str(s_matrix[3, 5])
        else:
            self.r3c5 = ""
        if 7 in display_value:
            self.r3c6 = str(s_matrix[3, 6])
        else:
            self.r3c6 = ""
        if 8 in display_value:
            self.r3c7 = str(s_matrix[3, 7])
        else:
            self.r3c7 = ""
        if 9 in display_value:
            self.r3c8 = str(s_matrix[3, 8])
        else:
            self.r3c8 = ""

        display_value = r5d_value
        row5 = display_value
        if 1 in display_value:
            self.r4c0 = str(s_matrix[4, 0])
        else:
            self.r4c0 = ""
        if 2 in display_value:
            self.r4c1 = str(s_matrix[4, 1])
        else:
            self.r4c1 = ""
        if 3 in display_value:
            self.r4c2 = str(s_matrix[4, 2])
        else:
            self.r4c2 = ""
        if 4 in display_value:
            self.r4c3 = str(s_matrix[4, 3])
        else:
            self.r4c3 = ""
        if 5 in display_value:
            self.r4c4 = str(s_matrix[4, 4])
        else:
            self.r4c4 = ""
        if 6 in display_value:
            self.r4c5 = str(s_matrix[4, 5])
        else:
            self.r4c5 = ""
        if 7 in display_value:
            self.r4c6 = str(s_matrix[4, 6])
        else:
            self.r4c6 = ""
        if 8 in display_value:
            self.r4c7 = str(s_matrix[4, 7])
        else:
            self.r4c7 = ""
        if 9 in display_value:
            self.r4c8 = str(s_matrix[4, 8])
        else:
            self.r4c8 = ""

        display_value = r6d_value
        row6 = display_value
        if 1 in display_value:
            self.r5c0 = str(s_matrix[5, 0])
        else:
            self.r5c0 = ""
        if 2 in display_value:
            self.r5c1 = str(s_matrix[5, 1])
        else:
            self.r5c1 = ""
        if 3 in display_value:
            self.r5c2 = str(s_matrix[5, 2])
        else:
            self.r5c2 = ""
        if 4 in display_value:
            self.r5c3 = str(s_matrix[5, 3])
        else:
            self.r5c3 = ""
        if 5 in display_value:
            self.r5c4 = str(s_matrix[5, 4])
        else:
            self.r5c4 = ""
        if 6 in display_value:
            self.r5c5 = str(s_matrix[5, 5])
        else:
            self.r5c5 = ""
        if 7 in display_value:
            self.r5c6 = str(s_matrix[5, 6])
        else:
            self.r5c6 = ""
        if 8 in display_value:
            self.r5c7 = str(s_matrix[5, 7])
        else:
            self.r5c7 = ""
        if 9 in display_value:
            self.r5c8 = str(s_matrix[5, 8])
        else:
            self.r5c8 = ""

        display_value = r7d_value
        row7 = display_value
        if 1 in display_value:
            self.r6c0 = str(s_matrix[6, 0])
        else:
            self.r6c0 = ""
        if 2 in display_value:
            self.r6c1 = str(s_matrix[6, 1])
        else:
            self.r6c1 = ""
        if 3 in display_value:
            self.r6c2 = str(s_matrix[6, 2])
        else:
            self.r6c2 = ""
        if 4 in display_value:
            self.r6c3 = str(s_matrix[6, 3])
        else:
            self.r6c3 = ""
        if 5 in display_value:
            self.r6c4 = str(s_matrix[6, 4])
        else:
            self.r6c4 = ""
        if 6 in display_value:
            self.r6c5 = str(s_matrix[6, 5])
        else:
            self.r6c5 = ""
        if 7 in display_value:
            self.r6c6 = str(s_matrix[6, 6])
        else:
            self.r6c6 = ""
        if 8 in display_value:
            self.r6c7 = str(s_matrix[6, 7])
        else:
            self.r6c7 = ""
        if 9 in display_value:
            self.r6c8 = str(s_matrix[6, 8])
        else:
            self.r6c8 = ""

        display_value = r8d_value
        row8 = display_value
        if 1 in display_value:
            self.r7c0 = str(s_matrix[7, 0])
        else:
            self.r7c0 = ""
        if 2 in display_value:
            self.r7c1 = str(s_matrix[7, 1])
        else:
            self.r7c1 = ""
        if 3 in display_value:
            self.r7c2 = str(s_matrix[7, 2])
        else:
            self.r7c2 = ""
        if 4 in display_value:
            self.r7c3 = str(s_matrix[7, 3])
        else:
            self.r7c3 = ""
        if 5 in display_value:
            self.r7c4 = str(s_matrix[7, 4])
        else:
            self.r7c4 = ""
        if 6 in display_value:
            self.r7c5 = str(s_matrix[7, 5])
        else:
            self.r7c5 = ""
        if 7 in display_value:
            self.r7c6 = str(s_matrix[7, 6])
        else:
            self.r7c6 = ""
        if 8 in display_value:
            self.r7c7 = str(s_matrix[7, 7])
        else:
            self.r7c7 = ""
        if 9 in display_value:
            self.r7c8 = str(s_matrix[7, 8])
        else:
            self.r7c8 = ""

        display_value = r9d_value
        row9 = display_value
        if 1 in display_value:
            self.r8c0 = str(s_matrix[8, 0])
        else:
            self.r8c0 = ""
        if 2 in display_value:
            self.r8c1 = str(s_matrix[8, 1])
        else:
            self.r8c1 = ""
        if 3 in display_value:
            self.r8c2 = str(s_matrix[8, 2])
        else:
            self.r8c2 = ""
        if 4 in display_value:
            self.r8c3 = str(s_matrix[8, 3])
        else:
            self.r8c3 = ""
        if 5 in display_value:
            self.r8c4 = str(s_matrix[8, 4])
        else:
            self.r8c4 = ""
        if 6 in display_value:
            self.r8c5 = str(s_matrix[8, 5])
        else:
            self.r8c5 = ""
        if 7 in display_value:
            self.r8c6 = str(s_matrix[8, 6])
        else:
            self.r8c6 = ""
        if 8 in display_value:
            self.r8c7 = str(s_matrix[8, 7])
        else:
            self.r8c7 = ""
        if 9 in display_value:
            self.r8c8 = str(s_matrix[8, 8])
        else:
            self.r8c8 = ""

    def remove_bubble(self, bubble, *largs):
        self.ids.bbox.remove_widget(bubble)

    def show_bubble(self, bx, by):
        bubble = Bubble(size_hint=[None, None], size=[20, 20], pos=[bx, by])
        bubble.add_widget(BubbleButton(text='WRONG', font_size= '10sp',color= [0,0,0,1], size=[6, 3]))
        bubble.background_color = (255, 0, 0, 1)
        bubble.arrow_pos = 'bottom_right'
        self.ids.bbox.add_widget(bubble)
        Clock.schedule_once(partial(self.remove_bubble, bubble), 1.5)

    def timer_bubble(self, tx1, tx2, clr, fn):
        bubble = Bubble(size_hint=[None, None], size=[50, 35], pos=[375, 490])
        bubble.add_widget(BubbleButton(text="{:02d}:{:02d}".format(tx1, tx2),
                                       font_size='15sp', color=[0, 0, 0, clr], size=[10, 10]))
        bubble.background_color = (0, 0, 0, 0)
        self.ids.bbox.add_widget(bubble)
        if fn == "stop":
            Clock.schedule_once(partial(self.remove_bubble, bubble), 60)
        if fn == "run":
            Clock.schedule_once(partial(self.remove_bubble, bubble), 1)

    def stop(self):
        self.dynamic_button = "Start"
        Clock.unschedule(self.Running_Clock)
        self.timer_bubble(self.mcount, self.scount, 0.25, "stop")

    def start(self):
        self.dynamic_button = "Pause"
        Clock.unschedule(self.Running_Clock)
        Clock.schedule_interval(self.Running_Clock, 1)

    def Running_Clock(self, dt):
        self.scount = self.scount + 1
        self.mcount += 0
        if self.scount == 60:
            self.scount = 0
            self.mcount += 1
        self.timer_bubble(self.mcount, self.scount, 1, "run")

    def show_timer(self):
        self.dynamic_button = "Pause"
        bubble = Bubble(size_hint=[None, None], size=[50, 35], pos=[375, 490])
        bubble.add_widget(BubbleButton(text='START', font_size='15sp', color=[0, 0, 0, 1], size=[10, 10]))
        bubble.background_color = (0, 0, 0, 0)
        self.ids.bbox.add_widget(bubble)
        Clock.schedule_interval(self.Running_Clock, 1)
        Clock.schedule_once(partial(self.remove_bubble, bubble), 1)

    # -Clear the User entered name

    def check_matrix(self, instance, arg):
        finish_flag = True
        self.check_text = 'Not Completed'
        #Row 1 check
        if self.row00.text != str(Sudoku.a[0, 0]):
            Matrixpage.show_bubble(self, 174, 454)
            finish_flag = False
        if self.row01.text != str(Sudoku.a[0, 1]):
            Matrixpage.show_bubble(self, 228, 454)
            finish_flag = False
        if self.row02.text != str(Sudoku.a[0, 2]):
            Matrixpage.show_bubble(self, 280, 454)
            finish_flag = False
        if self.row03.text != str(Sudoku.a[0, 3]):
            Matrixpage.show_bubble(self, 332, 454)
            finish_flag = False
        if self.row04.text != str(Sudoku.a[0, 4]):
            Matrixpage.show_bubble(self, 386, 454)
            finish_flag = False
        if self.row05.text != str(Sudoku.a[0, 5]):
            Matrixpage.show_bubble(self, 440, 454)
            finish_flag = False
        if self.row06.text != str(Sudoku.a[0, 6]):
            Matrixpage.show_bubble(self, 492, 454)
            finish_flag = False
        if self.row07.text != str(Sudoku.a[0, 7]):
            Matrixpage.show_bubble(self, 544, 454)
            finish_flag = False
        if self.row08.text != str(Sudoku.a[0, 8]):
            Matrixpage.show_bubble(self, 598, 454)
            finish_flag = False
        #Row 2 check
        if self.row10.text != str(Sudoku.a[1, 0]):
            Matrixpage.show_bubble(self, 174, 415)
            finish_flag = False
        if self.row11.text != str(Sudoku.a[1, 1]):
            Matrixpage.show_bubble(self, 228, 415)
            finish_flag = False
        if self.row12.text != str(Sudoku.a[1, 2]):
            Matrixpage.show_bubble(self, 280, 415)
            finish_flag = False
        if self.row13.text != str(Sudoku.a[1, 3]):
            Matrixpage.show_bubble(self, 332, 415)
            finish_flag = False
        if self.row14.text != str(Sudoku.a[1, 4]):
            Matrixpage.show_bubble(self, 386, 415)
            finish_flag = False
        if self.row15.text != str(Sudoku.a[1, 5]):
            Matrixpage.show_bubble(self, 440, 415)
            finish_flag = False
        if self.row16.text != str(Sudoku.a[1, 6]):
            Matrixpage.show_bubble(self, 492, 415)
            finish_flag = False
        if self.row17.text != str(Sudoku.a[1, 7]):
            Matrixpage.show_bubble(self, 544, 415)
            finish_flag = False
        if self.row18.text != str(Sudoku.a[1, 8]):
            Matrixpage.show_bubble(self, 598, 415)
            finish_flag = False
        #Row 3 check
        if self.row20.text != str(Sudoku.a[2, 0]):
            Matrixpage.show_bubble(self, 174, 376)
            finish_flag = False
        if self.row21.text != str(Sudoku.a[2, 1]):
            Matrixpage.show_bubble(self, 228, 376)
            finish_flag = False
        if self.row22.text != str(Sudoku.a[2, 2]):
            Matrixpage.show_bubble(self, 280, 376)
            finish_flag = False
        if self.row23.text != str(Sudoku.a[2, 3]):
            Matrixpage.show_bubble(self, 332, 376)
            finish_flag = False
        if self.row24.text != str(Sudoku.a[2, 4]):
            Matrixpage.show_bubble(self, 386, 376)
            finish_flag = False
        if self.row25.text != str(Sudoku.a[2, 5]):
            Matrixpage.show_bubble(self, 440, 376)
            finish_flag = False
        if self.row26.text != str(Sudoku.a[2, 6]):
            Matrixpage.show_bubble(self, 492, 376)
            finish_flag = False
        if self.row27.text != str(Sudoku.a[2, 7]):
            Matrixpage.show_bubble(self, 544, 376)
            finish_flag = False
        if self.row28.text != str(Sudoku.a[2, 8]):
            Matrixpage.show_bubble(self, 598, 376)
        #Row 4 check
        if self.row30.text != str(Sudoku.a[3, 0]):
            Matrixpage.show_bubble(self, 174, 336)
            finish_flag = False
        if self.row31.text != str(Sudoku.a[3, 1]):
            Matrixpage.show_bubble(self, 228, 336)
            finish_flag = False
        if self.row32.text != str(Sudoku.a[3, 2]):
            Matrixpage.show_bubble(self, 280, 336)
            finish_flag = False
        if self.row33.text != str(Sudoku.a[3, 3]):
            Matrixpage.show_bubble(self, 332, 336)
            finish_flag = False
        if self.row34.text != str(Sudoku.a[3, 4]):
            Matrixpage.show_bubble(self, 386, 336)
            finish_flag = False
        if self.row35.text != str(Sudoku.a[3, 5]):
            Matrixpage.show_bubble(self, 440, 336)
            finish_flag = False
        if self.row36.text != str(Sudoku.a[3, 6]):
            Matrixpage.show_bubble(self, 492, 336)
            finish_flag = False
        if self.row37.text != str(Sudoku.a[3, 7]):
            Matrixpage.show_bubble(self, 544, 336)
            finish_flag = False
        if self.row38.text != str(Sudoku.a[3, 8]):
            Matrixpage.show_bubble(self, 598, 336)
            finish_flag = False
        #Row 5 check
        if self.row40.text != str(Sudoku.a[4, 0]):
            Matrixpage.show_bubble(self, 174, 296)
            finish_flag = False
        if self.row41.text != str(Sudoku.a[4, 1]):
            Matrixpage.show_bubble(self, 228, 296)
            finish_flag = False
        if self.row42.text != str(Sudoku.a[4, 2]):
            Matrixpage.show_bubble(self, 280, 296)
            finish_flag = False
        if self.row43.text != str(Sudoku.a[4, 3]):
            Matrixpage.show_bubble(self, 332, 296)
            finish_flag = False
        if self.row44.text != str(Sudoku.a[4, 4]):
            Matrixpage.show_bubble(self, 386, 296)
            finish_flag = False
        if self.row45.text != str(Sudoku.a[4, 5]):
            Matrixpage.show_bubble(self, 440, 296)
            finish_flag = False
        if self.row46.text != str(Sudoku.a[4, 6]):
            Matrixpage.show_bubble(self, 492, 296)
            finish_flag = False
        if self.row47.text != str(Sudoku.a[4, 7]):
            Matrixpage.show_bubble(self, 544, 296)
            finish_flag = False
        if self.row48.text != str(Sudoku.a[4, 8]):
            Matrixpage.show_bubble(self, 598, 296)
            finish_flag = False
        #Row 6 check
        if self.row50.text != str(Sudoku.a[5, 0]):
            Matrixpage.show_bubble(self, 174, 257)
            finish_flag = False
        if self.row51.text != str(Sudoku.a[5, 1]):
            Matrixpage.show_bubble(self, 228, 257)
            finish_flag = False
        if self.row52.text != str(Sudoku.a[5, 2]):
            Matrixpage.show_bubble(self, 280, 257)
            finish_flag = False
        if self.row53.text != str(Sudoku.a[5, 3]):
            Matrixpage.show_bubble(self, 332, 257)
            finish_flag = False
        if self.row54.text != str(Sudoku.a[5, 4]):
            Matrixpage.show_bubble(self, 386, 257)
            finish_flag = False
        if self.row55.text != str(Sudoku.a[5, 5]):
            Matrixpage.show_bubble(self, 440, 257)
            finish_flag = False
        if self.row56.text != str(Sudoku.a[5, 6]):
            Matrixpage.show_bubble(self, 492, 257)
            finish_flag = False
        if self.row57.text != str(Sudoku.a[5, 7]):
            Matrixpage.show_bubble(self, 544, 257)
            finish_flag = False
        if self.row58.text != str(Sudoku.a[5, 8]):
            Matrixpage.show_bubble(self, 598, 257)
            finish_flag = False
        #Row 7 check
        if self.row60.text != str(Sudoku.a[6, 0]):
            Matrixpage.show_bubble(self, 174, 218)
            finish_flag = False
        if self.row61.text != str(Sudoku.a[6, 1]):
            Matrixpage.show_bubble(self, 228, 218)
            finish_flag = False
        if self.row62.text != str(Sudoku.a[6, 2]):
            Matrixpage.show_bubble(self, 280, 218)
            finish_flag = False
        if self.row63.text != str(Sudoku.a[6, 3]):
            Matrixpage.show_bubble(self, 332, 218)
            finish_flag = False
        if self.row64.text != str(Sudoku.a[6, 4]):
            Matrixpage.show_bubble(self, 386, 218)
            finish_flag = False
        if self.row65.text != str(Sudoku.a[6, 5]):
            Matrixpage.show_bubble(self, 440, 218)
            finish_flag = False
        if self.row66.text != str(Sudoku.a[6, 6]):
            Matrixpage.show_bubble(self, 492, 218)
            finish_flag = False
        if self.row67.text != str(Sudoku.a[6, 7]):
            Matrixpage.show_bubble(self, 544, 218)
            finish_flag = False
        if self.row68.text != str(Sudoku.a[6, 8]):
            Matrixpage.show_bubble(self, 598, 218)
            finish_flag = False
        #Row 8 check
        if self.row70.text != str(Sudoku.a[7, 0]):
            Matrixpage.show_bubble(self, 174, 178)
            finish_flag = False
        if self.row71.text != str(Sudoku.a[7, 1]):
            Matrixpage.show_bubble(self, 228, 178)
            finish_flag = False
        if self.row72.text != str(Sudoku.a[7, 2]):
            Matrixpage.show_bubble(self, 280, 178)
            finish_flag = False
        if self.row73.text != str(Sudoku.a[7, 3]):
            Matrixpage.show_bubble(self, 332, 178)
            finish_flag = False
        if self.row74.text != str(Sudoku.a[7, 4]):
            Matrixpage.show_bubble(self, 386, 178)
            finish_flag = False
        if self.row75.text != str(Sudoku.a[7, 5]):
            Matrixpage.show_bubble(self, 440, 178)
            finish_flag = False
        if self.row76.text != str(Sudoku.a[7, 6]):
            Matrixpage.show_bubble(self, 492, 178)
            finish_flag = False
        if self.row77.text != str(Sudoku.a[7, 7]):
            Matrixpage.show_bubble(self, 544, 178)
            finish_flag = False
        if self.row78.text != str(Sudoku.a[7, 8]):
            Matrixpage.show_bubble(self, 598, 178)
            finish_flag = False
        #Row 9 check
        if self.row80.text != str(Sudoku.a[8, 0]):
            Matrixpage.show_bubble(self, 174, 139)
            finish_flag = False
        if self.row81.text != str(Sudoku.a[8, 1]):
            Matrixpage.show_bubble(self, 228, 139)
            finish_flag = False
        if self.row82.text != str(Sudoku.a[8, 2]):
            Matrixpage.show_bubble(self, 280, 139)
            finish_flag = False
        if self.row83.text != str(Sudoku.a[8, 3]):
            Matrixpage.show_bubble(self, 332, 139)
            finish_flag = False
        if self.row84.text != str(Sudoku.a[8, 4]):
            Matrixpage.show_bubble(self, 386, 139)
            finish_flag = False
        if self.row85.text != str(Sudoku.a[8, 5]):
            Matrixpage.show_bubble(self, 440, 139)
            finish_flag = False
        if self.row86.text != str(Sudoku.a[8, 6]):
            Matrixpage.show_bubble(self, 492, 139)
            finish_flag = False
        if self.row87.text != str(Sudoku.a[8, 7]):
            Matrixpage.show_bubble(self, 544, 139)
            finish_flag = False
        if self.row88.text != str(Sudoku.a[8, 8]):
            Matrixpage.show_bubble(self, 598, 139)
            finish_flag = False

        if finish_flag:
            self.check_text = "Well done!, You've completed the Game."
        else:
            self.check_text = 'Not Completed'

    # - Home Page
    def home_page(self):
        Sudoku.a = np.zeros((9, 9), dtype=np.uint8)
        Sudoku.done = True
        Sudoku.queue1 = True
        Sudoku.queue2 = True
        Sudoku.queue3 = True
        Sudoku.queue4 = True
        Sudoku.queue5 = True
        Sudoku.queue6 = True
        Sudoku.queue7 = True
        Sudoku.queue8 = True
        Sudoku.queue9 = True
        Sudoku.icount = 0
        Sudoku.q3count = 0
        Sudoku.q5count = 0
        Sudoku.q6count = 0
        Sudoku.q7count = 0
        Sudoku.q8count = 0
        Sudoku.q9count = 0
        self.clear_widgets()
        self.add_widget(WelcomePage())

    # - New screen
    def new_page(self):
        Sudoku.a = np.zeros((9, 9), dtype=np.uint8)
        Sudoku.done = True
        Sudoku.queue1 = True
        Sudoku.queue2 = True
        Sudoku.queue3 = True
        Sudoku.queue4 = True
        Sudoku.queue5 = True
        Sudoku.queue6 = True
        Sudoku.queue7 = True
        Sudoku.queue8 = True
        Sudoku.queue9 = True
        Sudoku.icount = 0
        Sudoku.q3count = 0
        Sudoku.q5count = 0
        Sudoku.q6count = 0
        Sudoku.q7count = 0
        Sudoku.q8count = 0
        Sudoku.q9count = 0
        self.clear_widgets()
        self.add_widget(Matrixpage())

    # -Clear the User entered values
    def clear_val(self):
        if 1 not in row1:
            self.row00.text = ''
        if 2 not in row1:
            self.row01.text = ''
        if 3 not in row1:
            self.row02.text = ''
        if 4 not in row1:
            self.row03.text = ''
        if 5 not in row1:
            self.row04.text = ''
        if 6 not in row1:
            self.row05.text = ''
        if 7 not in row1:
            self.row06.text = ''
        if 8 not in row1:
            self.row07.text = ''
        if 9 not in row1:
            self.row08.text = ''
        if 1 not in row2:
            self.row10.text = ''
        if 2 not in row2:
            self.row11.text = ''
        if 3 not in row2:
            self.row12.text = ''
        if 4 not in row2:
            self.row13.text = ''
        if 5 not in row2:
            self.row14.text = ''
        if 6 not in row2:
            self.row15.text = ''
        if 7 not in row2:
            self.row16.text = ''
        if 8 not in row2:
            self.row17.text = ''
        if 9 not in row2:
            self.row18.text = ''
        if 1 not in row3:
            self.row20.text = ''
        if 2 not in row3:
            self.row21.text = ''
        if 3 not in row3:
            self.row22.text = ''
        if 4 not in row3:
            self.row23.text = ''
        if 5 not in row3:
            self.row24.text = ''
        if 6 not in row3:
            self.row25.text = ''
        if 7 not in row3:
            self.row26.text = ''
        if 8 not in row3:
            self.row27.text = ''
        if 9 not in row3:
            self.row28.text = ''
        if 1 not in row4:
            self.row30.text = ''
        if 2 not in row4:
            self.row31.text = ''
        if 3 not in row4:
            self.row32.text = ''
        if 4 not in row4:
            self.row33.text = ''
        if 5 not in row4:
            self.row34.text = ''
        if 6 not in row4:
            self.row35.text = ''
        if 7 not in row4:
            self.row36.text = ''
        if 8 not in row4:
            self.row37.text = ''
        if 9 not in row4:
            self.row38.text = ''
        if 1 not in row5:
            self.row40.text = ''
        if 2 not in row5:
            self.row41.text = ''
        if 3 not in row5:
            self.row42.text = ''
        if 4 not in row5:
            self.row43.text = ''
        if 5 not in row5:
            self.row44.text = ''
        if 6 not in row5:
            self.row45.text = ''
        if 7 not in row5:
            self.row46.text = ''
        if 8 not in row5:
            self.row47.text = ''
        if 9 not in row5:
            self.row48.text = ''
        if 1 not in row6:
            self.row50.text = ''
        if 2 not in row6:
            self.row51.text = ''
        if 3 not in row6:
            self.row52.text = ''
        if 4 not in row6:
            self.row53.text = ''
        if 5 not in row6:
            self.row54.text = ''
        if 6 not in row6:
            self.row55.text = ''
        if 7 not in row6:
            self.row56.text = ''
        if 8 not in row6:
            self.row57.text = ''
        if 9 not in row6:
            self.row58.text = ''
        if 1 not in row7:
            self.row60.text = ''
        if 2 not in row7:
            self.row61.text = ''
        if 3 not in row7:
            self.row62.text = ''
        if 4 not in row7:
            self.row63.text = ''
        if 5 not in row7:
            self.row64.text = ''
        if 6 not in row7:
            self.row65.text = ''
        if 7 not in row7:
            self.row66.text = ''
        if 8 not in row7:
            self.row67.text = ''
        if 9 not in row7:
            self.row68.text = ''
        if 1 not in row8:
            self.row70.text = ''
        if 2 not in row8:
            self.row71.text = ''
        if 3 not in row8:
            self.row72.text = ''
        if 4 not in row8:
            self.row73.text = ''
        if 5 not in row8:
            self.row74.text = ''
        if 6 not in row8:
            self.row75.text = ''
        if 7 not in row8:
            self.row76.text = ''
        if 8 not in row8:
            self.row77.text = ''
        if 9 not in row8:
            self.row78.text = ''
        if 1 not in row9:
            self.row80.text = ''
        if 2 not in row9:
            self.row81.text = ''
        if 3 not in row9:
            self.row82.text = ''
        if 4 not in row9:
            self.row83.text = ''
        if 5 not in row9:
            self.row84.text = ''
        if 6 not in row9:
            self.row85.text = ''
        if 7 not in row9:
            self.row86.text = ''
        if 8 not in row9:
            self.row87.text = ''
        if 9 not in row9:
            self.row88.text = ''
    roval = False


class SudokuApp(App):
    def build(self):
        self.icon = 'myicon.png'
        return WelcomePage()


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    SudokuApp().run()