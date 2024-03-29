import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from backend import Flipper_Back as FB
import socket
# from enter_sudo import App_enter_sudo
import os
from getpass import getpass


class App_Submit(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.minsize(840, 50)
        self.maxsize(850, 175)
        self.resizable(0, 0)

        self.frame_Main = ctk.CTkFrame(master=self,
                                       corner_radius=10)
        ######minimal
        self.frame_submit_minimal = ctk.CTkFrame(master=self.frame_Main,
                                                 fg_color="blue",
                                                 border_width=5,
                                                 corner_radius=10)
        self.direction = ctk.StringVar()
        self.ip = ctk.StringVar()
        self.action = ctk.StringVar()
        self.chain = ctk.StringVar()
        self.entry_ip_dns = ctk.CTkEntry(master=self.frame_submit_minimal,
                                         placeholder_text="IP/DNS",
                                         textvariable=self.ip)

        self.option_box_direction = ctk.CTkOptionMenu(master=self.frame_submit_minimal,
                                                      values=[
                                                          "source", "destination"],
                                                      variable=self.direction,)
        self.option_box_action = ctk.CTkOptionMenu(master=self.frame_submit_minimal,
                                                   values=[
                                                          "DROP", "ACCEPT", "RETURN", "REJECT"],
                                                   variable=self.action,)
        self.option_box_chain = ctk.CTkOptionMenu(master=self.frame_submit_minimal,
                                                  values=FB.chain_names(),
                                                  variable=self.chain,)

        self.frame_submit_optional = ctk.CTkFrame(master=self.frame_Main,
                                                  fg_color="red",
                                                  border_width=5,
                                                  corner_radius=10)
        self.button_submit = ctk.CTkButton(master=self.frame_submit_minimal,
                                           text="Submit",
                                           command=self.submit)
        ###### optional
        self.packet_type = ctk.StringVar()
        self.Port_number = ctk.StringVar()
        self.option_box_packet = ctk.CTkOptionMenu(master=self.frame_submit_optional,
                                                   values=[
                                                       "udp", "tcp", "icmp", "all"],
                                                   variable=self.packet_type,)
        self.entry_port = ctk.CTkEntry(master=self.frame_submit_optional,
                                       placeholder_text="Port_number",
                                       textvariable=self.Port_number)

        #placement :
        self.frame_Main.grid(column=0, row=0, padx=10, pady=10)
        ###main :
        self.frame_submit_minimal.grid(column=0, row=0, padx=10, pady=10)
        self.frame_submit_optional.grid(column=0, row=1, padx=10, pady=10)
        ######minimal:
        self.option_box_chain.grid(column=0, row=0, padx=10, pady=10)
        self.entry_ip_dns.grid(column=1, row=0, padx=10, pady=10)
        self.option_box_direction.grid(column=2, row=0, padx=10, pady=10)
        self.option_box_action.grid(column=3, row=0, padx=10, pady=10)
        self.button_submit.grid(column=4, row=0, padx=10, pady=10)
        self.entry_ip_dns.insert(0, "IP lub DNS")
        self.entry_ip_dns.bind(
            "<Button-1>", lambda event: self.clear_entry(event, self.entry_ip_dns, 10))
        ######optional:
        self.entry_port.grid(column=1, row=0, padx=10, pady=10)
        self.entry_port.insert(0, "numer portu")
        self.entry_port.bind(
            "<Button-1>", lambda event: self.clear_entry(event, self.entry_port, 11))
        self.option_box_packet.grid(column=0, row=0, padx=10, pady=10)

    def submit(self):
        if self.option_box_direction.get() == "source":
          SourcDest = "-s"
        else:
            SourcDest = "-d"
        if self.Port_number.get().isnumeric():
            SourcDest = "-p -" + SourcDest + \
                "port " + str(self.Port_number.get())
        flagi = [self.option_box_chain.get(), SourcDest,
                 self.entry_ip_dns.get(), self.option_box_action.get()]
        FB.AddRule(flagi)
        self.destroy()

    def clear_entry(self, event, entry, last):
        entry.delete(0, last)

        #Flipper_Back.AddRule("INPUT", "-s", self.entry.get(), "DROP")
        ### definition
        # app = App_Submit()
        # app.title("nowa reguła")
        # app.mainloop()
        # app.title("nowa reguła")
        # app.mainloop()
        # app.mainloop()
        # app.mainloop()
