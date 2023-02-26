import streamlit as st
import home
import whatwedo
import howtouse
import contact

class MainPage:

    def __init__(self):

        self.h = home.Home()
        self.wh = whatwedo.WhatWeDo()
        self.hw = howtouse.HowToUse()
        self.c = contact.Contact()

    def mainpage_display(self):

        self.h.home_display()
        self.wh.whatwedo_display()
        self.hw.howtouse_display()
        self.c.contact_display()





