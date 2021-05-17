main_widget_sheet =        '''QPushButton{\n
                               background-color:rgba(85,98,112,255);\n
                               color:rgba(255,255,255,200);\n
                               border-radius:5px;\n
                               font-size:11px;\n
                           }\n
                           QPushButton:pressed{\n
                               padding-left:5px;\n
                               padding-top:5px;\n
                               background-color:rgba(225,200,5,1);\n
                               background-position:calc(100% - 10px)center;\n
                           }\n
                           QPushButton:hover{\n
                               background-color:rgba(255,200,0,1);\n
                           }\n
                           QPushButton#pushbutton_exit{\n
                               background-color:rgba(255,255,255,255);\n
                               color:rgba(0,0,0,200);\n
                               border-radius:8px;\n
                           }\n
                           QPushButton#pushbutton_exit:pressed{\n
                               padding-left:4px;\n
                               padding-top:4px;\n
                               background-position:calc(100% - 10px)center;\n
                           }\n
                           QPushButton#pushbutton_exit:hover{\n
                               color:rgba(10,10,10,200);\n
                               padding-left:3px;\n
                               padding-top:3px;\n
                               background-position:calc(100% - 10px)center;\n
                           }'''
main_lbl_window_sheet = '''background-color:rgba(255,255,255,255);\n
                                      border-radius:10px;\n'''
login_widget_sheet ='''QPushButton#pushButton{\n
                               background-color:rgba(85,98,112,255);\n
                               color:rgba(255,255,255,200);\n
                               border-radius:5px;\n
                           }\n
                           QPushButton#pushButton:pressed{\n
                               padding-left:5px;\n
                               padding-top:5px;\n
                               background-color:rgba(225,200,5,1);\n
                               background-position:calc(100% - 10px)center;\n
                           }\n
                           QPushButton#pushButton:hover{\n
                               background-color:rgba(255,200,0,1);\n
                           }'''
login_left_window_sheet = '''background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 220, 5, 255), stop:1 rgba(255, 107, 107, 255));\n
            border-radius:10px;'''
login_input_sheet = '''background-color:rgba(0,0,0,0);\n
                                    border:2px solid rgba(0,0,0,0);\n
                                    border-bottom-color:rgba(46,82,101,200);\n
                                    color:rgb(0,0,0);\n
                                    padding-bottim:7px;'''
select_widget_sheet = '''QPushButton#pushButton{\n
                                 background-color:rgba(85,98,112,255);\n
                                 color:rgba(255,255,255,200);\n
                                 border-radius:5px;\n
                             }\n
                             QPushButton#pushButton:pressed{\n
                                 padding-left:5px;\n
                                 padding-top:5px;\n
                                 background-color:rgba(225,200,5,1);\n
                                 background-position:calc(100% - 10px)center;\n
                             }\n
                             QPushButton#pushButton:hover{\n
                                 background-color:rgba(255,200,0,1);\n
                             }\n
                           QComboBox::drop-down{\n
                               border : 0px;\n
                           }\n'''
select_combobox_sheet = '''font-size: 1rem;\n
                                      font-weight: 400;\n
                                      line-height: 1.5;\n
                                    \n
                                      color: #444;\n
                                      background-color: #fff;\n
                                    \n
                                      padding: 0.6em 1.4em 0.5em 0.8em;\n
                                      margin: 0;\n
                                    \n
                                      border: 1px solid #aaa;\n
                                      border-radius: 0.5em;\n
                                      box-shadow: 0 1px 0 1px rgba(0, 0, 0, 0.04);\n
                                    appearance:none;\n
                                    -webkit-appearance:none;'''