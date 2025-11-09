#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vehicle Traffic Monitor v7.81.6
Ford Motor Company
CAN Bus Monitoring and Diagnostic Tool
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
from tkinter.simpledialog import Dialog
import threading
import time
from datetime import datetime
from typing import List, Optional
import queue
import os
import sys

# Import the J2534 library
try:
    from j2534 import *
except ImportError:
    print("Warning: j2534.py not found. Running in demo mode.")
    PassThruMsg = None


class PasswordDialog(Dialog):
    """Password dialog for Read/Write access"""
    
    def __init__(self, parent):
        self.password = None
        super().__init__(parent, title="Passcode")
    
    def body(self, master):
        tk.Label(master, text="Passcode:", anchor='w').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.password_entry = tk.Entry(master, show='*', width=30)
        self.password_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_entry.focus()
        return self.password_entry
    
    def buttonbox(self):
        box = tk.Frame(self)
        tk.Button(box, text="Cancel", width=10, command=self.cancel).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(box, text="Submit", width=10, command=self.ok, default=tk.ACTIVE).pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", lambda e: self.ok())
        self.bind("<Escape>", lambda e: self.cancel())
        box.pack()
    
    def apply(self):
        self.password = self.password_entry.get()


class DeviceSelectionDialog(Dialog):
    """J2534 Pass-Thru Device Selection Dialog"""
    
    def __init__(self, parent, devices: List[str]):
        self.devices = devices
        self.selected_device = None
        super().__init__(parent, title="Pass-Thru Device Selection")
    
    def body(self, master):
        tk.Label(master, text="Pass-Thru Device:", anchor='w').pack(anchor='w', padx=10, pady=5)
        
        self.device_combo = ttk.Combobox(master, values=self.devices, state='readonly', width=40)
        if self.devices:
            self.device_combo.current(0)
        self.device_combo.pack(padx=10, pady=5, fill=tk.X)
        
        note_text = ("To ensure full functionality of this application, it is\n"
                    "recommended that a fully compliant J2534-2 Pass-Thru device\n"
                    "is used.")
        tk.Label(master, text=note_text, justify=tk.LEFT, anchor='w').pack(anchor='w', padx=10, pady=10)
        
        return self.device_combo
    
    def buttonbox(self):
        box = tk.Frame(self)
        tk.Button(box, text="Cancel", width=10, command=self.cancel).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(box, text="Ok", width=10, command=self.ok, default=tk.ACTIVE).pack(side=tk.LEFT, padx=5, pady=5)
        box.pack(pady=10)
    
    def apply(self):
        self.selected_device = self.device_combo.get()


class MonitorSetupDialog(Dialog):
    """Monitor Setup Configuration Dialog"""
    
    def __init__(self, parent, config: dict):
        self.config = config.copy()
        super().__init__(parent, title="Monitor Setup")
    
    def body(self, master):
        # Create three columns
        frame_can1 = tk.LabelFrame(master, text="CAN 1 Setup", padx=10, pady=10)
        frame_can1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        
        frame_can2 = tk.LabelFrame(master, text="CAN 2 Setup", padx=10, pady=10)
        frame_can2.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        
        frame_protocol = tk.LabelFrame(master, text="Protocol to Monitor", padx=10, pady=10)
        frame_protocol.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
        
        # CAN 1 Setup
        self.can1_filter = tk.StringVar(value=self.config.get('can1_filter', 'No Filters'))
        tk.Radiobutton(frame_can1, text="No Filters", variable=self.can1_filter, value="No Filters").pack(anchor='w')
        tk.Radiobutton(frame_can1, text="Diagnostic Messages Only", variable=self.can1_filter, value="Diagnostic").pack(anchor='w')
        tk.Radiobutton(frame_can1, text="Pass Filters", variable=self.can1_filter, value="Pass").pack(anchor='w')
        tk.Radiobutton(frame_can1, text="Block Filters", variable=self.can1_filter, value="Block").pack(anchor='w')
        
        tk.Label(frame_can1, text="07xx", anchor='w').pack(anchor='w', pady=2)
        
        tk.Label(frame_can1, text="Filter 1").pack(anchor='w')
        self.can1_filter1 = tk.Entry(frame_can1, width=20)
        self.can1_filter1.pack(fill=tk.X, pady=2)
        
        tk.Label(frame_can1, text="Filter 2").pack(anchor='w')
        self.can1_filter2 = tk.Entry(frame_can1, width=20)
        self.can1_filter2.pack(fill=tk.X, pady=2)
        
        tk.Label(frame_can1, text="Filter 3").pack(anchor='w')
        self.can1_filter3 = tk.Entry(frame_can1, width=20)
        self.can1_filter3.pack(fill=tk.X, pady=2)
        
        tk.Button(frame_can1, text="Clear").pack(pady=5)
        
        self.can1_trigger = tk.BooleanVar(value=self.config.get('can1_trigger', False))
        tk.Checkbutton(frame_can1, text="Set CAN 1 Trigger", variable=self.can1_trigger).pack(anchor='w')
        
        # CAN 2 Setup
        self.can2_filter = tk.StringVar(value=self.config.get('can2_filter', 'No Filters'))
        tk.Radiobutton(frame_can2, text="No Filters", variable=self.can2_filter, value="No Filters").pack(anchor='w')
        tk.Radiobutton(frame_can2, text="Diagnostic Messages Only", variable=self.can2_filter, value="Diagnostic").pack(anchor='w')
        tk.Radiobutton(frame_can2, text="Pass Filters", variable=self.can2_filter, value="Pass").pack(anchor='w')
        tk.Radiobutton(frame_can2, text="Block Filters", variable=self.can2_filter, value="Block").pack(anchor='w')
        
        tk.Label(frame_can2, text="07xx", anchor='w').pack(anchor='w', pady=2)
        
        tk.Label(frame_can2, text="Filter 1").pack(anchor='w')
        self.can2_filter1 = tk.Entry(frame_can2, width=20)
        self.can2_filter1.pack(fill=tk.X, pady=2)
        
        tk.Label(frame_can2, text="Filter 2").pack(anchor='w')
        self.can2_filter2 = tk.Entry(frame_can2, width=20)
        self.can2_filter2.pack(fill=tk.X, pady=2)
        
        tk.Label(frame_can2, text="Filter 3").pack(anchor='w')
        self.can2_filter3 = tk.Entry(frame_can2, width=20)
        self.can2_filter3.pack(fill=tk.X, pady=2)
        
        tk.Button(frame_can2, text="Clear").pack(pady=5)
        
        self.can2_trigger = tk.BooleanVar(value=self.config.get('can2_trigger', False))
        tk.Checkbutton(frame_can2, text="Set CAN 2 Trigger", variable=self.can2_trigger).pack(anchor='w')
        
        tk.Label(frame_can2, text="Baud Rate:").pack(anchor='w', pady=(10, 0))
        self.can2_baudrate = ttk.Combobox(frame_can2, values=["125k (MS CAN)", "500k (HS CAN)"], state='readonly', width=18)
        self.can2_baudrate.set("125k (MS CAN)")
        self.can2_baudrate.pack(fill=tk.X, pady=2)
        
        # Protocol to Monitor
        self.protocol = tk.StringVar(value=self.config.get('protocol', 'Both'))
        tk.Radiobutton(frame_protocol, text="CAN 1 Only", variable=self.protocol, value="CAN1").pack(anchor='w')
        tk.Radiobutton(frame_protocol, text="CAN 2 Only", variable=self.protocol, value="CAN2").pack(anchor='w')
        tk.Radiobutton(frame_protocol, text="Both", variable=self.protocol, value="Both").pack(anchor='w')
        
        tk.Label(frame_protocol, text="Wakeup Monitor", font=('TkDefaultFont', 9, 'bold')).pack(anchor='w', pady=(20, 5))
        self.wakeup_monitor = tk.BooleanVar(value=self.config.get('wakeup_monitor', False))
        tk.Checkbutton(frame_protocol, text="Monitor for Wakeup", variable=self.wakeup_monitor).pack(anchor='w')
        
        tk.Label(frame_protocol, text="Reset Delay: (milliseconds)").pack(anchor='w', pady=(5, 0))
        self.reset_delay = tk.Entry(frame_protocol, width=20)
        self.reset_delay.insert(0, str(self.config.get('reset_delay', 5000)))
        self.reset_delay.pack(fill=tk.X, pady=2)
        
        tk.Label(frame_protocol, text="Capture Time: (milliseconds)").pack(anchor='w', pady=(5, 0))
        self.capture_time = tk.Entry(frame_protocol, width=20)
        self.capture_time.insert(0, str(self.config.get('capture_time', 5000)))
        self.capture_time.pack(fill=tk.X, pady=2)
    
    def buttonbox(self):
        box = tk.Frame(self)
        tk.Button(box, text="Cancel", width=10, command=self.cancel).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(box, text="Ok", width=10, command=self.ok, default=tk.ACTIVE).pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()
    
    def apply(self):
        self.config['can1_filter'] = self.can1_filter.get()
        self.config['can2_filter'] = self.can2_filter.get()
        self.config['can1_trigger'] = self.can1_trigger.get()
        self.config['can2_trigger'] = self.can2_trigger.get()
        self.config['protocol'] = self.protocol.get()
        self.config['wakeup_monitor'] = self.wakeup_monitor.get()
        try:
            self.config['reset_delay'] = int(self.reset_delay.get())
            self.config['capture_time'] = int(self.capture_time.get())
        except ValueError:
            pass


class ReadWriteWindow(tk.Toplevel):
    """Read/Write Tool Window"""
    
    def __init__(self, parent, j2534_device=None):
        super().__init__(parent)
        self.title("VTM v7.81.6")
        self.geometry("1200x700")
        self.j2534_device = j2534_device
        
        # Configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        
        # Create main frames
        self.create_log_frame()
        self.create_setup_frame()
        
        self.is_connected = False
        self.channel_id = None
        
    def create_log_frame(self):
        """Create log area on the left"""
        log_frame = tk.Frame(self, relief=tk.SUNKEN, borderwidth=1)
        log_frame.grid(row=0, column=0, sticky='nsew', padx=(5, 0), pady=5)
        
        # Return button
        return_btn = tk.Button(log_frame, text="< Return", command=self.destroy)
        return_btn.pack(anchor='nw', padx=5, pady=5)
        
        tk.Label(log_frame, text="Log:", anchor='w').pack(anchor='w', padx=5, pady=(10, 0))
        
        self.log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, height=30, width=50)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def create_setup_frame(self):
        """Create setup panel on the right"""
        setup_frame = tk.LabelFrame(self, text="Setup", padx=10, pady=10)
        setup_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        # Target ID
        tk.Label(setup_frame, text="Target ID:", anchor='w').grid(row=0, column=0, sticky='w', pady=5)
        self.target_combo = ttk.Combobox(setup_frame, width=40, state='readonly')
        self.target_combo['values'] = [
            'PCM - Powertrain Control Module',
            'TCM - Transmission Control Module',
            'ABS - Anti-lock Braking System',
            'RCM - Restraint Control Module',
            'IPC - Instrument Panel Cluster',
            'BCM - Body Control Module',
            'PAM - Parking Aid Module'
        ]
        self.target_combo.current(0)
        self.target_combo.grid(row=0, column=1, sticky='ew', pady=5, padx=5)
        
        self.target_id_entry = tk.Entry(setup_frame, width=10)
        self.target_id_entry.insert(0, "7E0")
        self.target_id_entry.grid(row=0, column=2, pady=5)
        
        # Protocol
        tk.Label(setup_frame, text="Protocol:", anchor='w').grid(row=1, column=0, sticky='w', pady=5)
        self.protocol_combo = ttk.Combobox(setup_frame, width=40, state='readonly')
        self.protocol_combo['values'] = ['ISO15765', 'ISO9141', 'J1850PWM', 'J1850VPW', 'CAN']
        self.protocol_combo.current(0)
        self.protocol_combo.grid(row=1, column=1, sticky='ew', pady=5, padx=5)
        
        # Baud Rate
        tk.Label(setup_frame, text="Baud Rate:", anchor='w').grid(row=1, column=2, sticky='w', pady=5, padx=(10, 0))
        self.baudrate_combo = ttk.Combobox(setup_frame, width=15, state='readonly')
        self.baudrate_combo['values'] = ['500K (HS CAN)', '250K', '125K (MS CAN)', '100K', '50K']
        self.baudrate_combo.current(0)
        self.baudrate_combo.grid(row=1, column=3, sticky='ew', pady=5)
        
        # Add Message
        tk.Button(setup_frame, text="Add Message", command=self.add_message).grid(row=2, column=0, columnspan=2, sticky='ew', pady=10, padx=(0, 5))
        
        # Connect button
        self.connect_btn = tk.Button(setup_frame, text="Connect", command=self.toggle_connection)
        self.connect_btn.grid(row=2, column=2, columnspan=2, sticky='ew', pady=10, padx=(5, 0))
        
        # Message entry and send
        self.message_entry = tk.Entry(setup_frame, width=60)
        self.message_entry.insert(0, "22 D1 00")
        self.message_entry.grid(row=3, column=0, columnspan=3, sticky='ew', pady=5, padx=(0, 5))
        
        self.send_btn = tk.Button(setup_frame, text="Send", command=self.send_message, state=tk.DISABLED)
        self.send_btn.grid(row=3, column=3, sticky='ew', pady=5)
        
        # Message display area
        self.message_display = scrolledtext.ScrolledText(setup_frame, wrap=tk.WORD, height=30, width=70)
        self.message_display.grid(row=4, column=0, columnspan=4, sticky='nsew', pady=5)
        
        setup_frame.grid_columnconfigure(1, weight=1)
        setup_frame.grid_rowconfigure(4, weight=1)
    
    def log(self, message: str):
        """Add message to log"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
    
    def toggle_connection(self):
        """Toggle connection to ECU"""
        if not self.is_connected:
            self.connect()
        else:
            self.disconnect()
    
    def connect(self):
        """Connect to ECU"""
        self.log("Attempting to connect...")
        
        if self.j2534_device is None:
            self.log("No J2534 device available - running in demo mode")
            self.is_connected = True
            self.connect_btn.config(text="Disconnect")
            self.send_btn.config(state=tk.NORMAL)
            self.message_display.insert(tk.END, "Demo Mode - Connected\n")
            return
        
        try:
            # Connect logic here using j2534_device
            self.log(f"Connected to {self.target_combo.get()}")
            self.is_connected = True
            self.connect_btn.config(text="Disconnect")
            self.send_btn.config(state=tk.NORMAL)
            self.message_display.insert(tk.END, f"Connected to {self.target_combo.get()}\n")
        except Exception as e:
            self.log(f"Connection failed: {str(e)}")
            messagebox.showerror("Connection Error", f"Failed to connect: {str(e)}")
    
    def disconnect(self):
        """Disconnect from ECU"""
        self.log("Disconnecting...")
        
        try:
            # Disconnect logic here
            self.is_connected = False
            self.connect_btn.config(text="Connect")
            self.send_btn.config(state=tk.DISABLED)
            self.message_display.insert(tk.END, "Disconnected\n")
            self.log("Disconnected successfully")
        except Exception as e:
            self.log(f"Disconnect error: {str(e)}")
    
    def send_message(self):
        """Send message to ECU"""
        message = self.message_entry.get().strip()
        if not message:
            return
        
        self.log(f"Sending: {message}")
        
        try:
            # Parse hex message
            data_bytes = bytes.fromhex(message.replace(" ", ""))
            
            # Display sent message
            self.message_display.insert(tk.END, f"\nTX: {message}\n")
            self.message_display.see(tk.END)
            
            # In demo mode, simulate response
            if self.j2534_device is None:
                # Simulate a response
                self.after(100, lambda: self.simulate_response(message))
        except Exception as e:
            self.log(f"Send error: {str(e)}")
            messagebox.showerror("Send Error", f"Failed to send message: {str(e)}")
    
    def simulate_response(self, request: str):
        """Simulate ECU response in demo mode"""
        # Simple simulation
        response = "62 D1 00 12 34 56 78"
        self.message_display.insert(tk.END, f"RX: {response}\n")
        self.message_display.see(tk.END)
        self.log(f"Received: {response}")
    
    def add_message(self):
        """Add message to list"""
        messagebox.showinfo("Add Message", "Message template functionality coming soon")


class VehicleTrafficMonitor(tk.Tk):
    """Main Vehicle Traffic Monitor Application"""
    
    def __init__(self):
        super().__init__()
        
        self.title("VTM v7.81.6")
        self.geometry("1400x800")
        
        # Configuration
        self.monitor_config = {
            'can1_filter': 'No Filters',
            'can2_filter': 'No Filters',
            'can1_trigger': False,
            'can2_trigger': False,
            'protocol': 'Both',
            'wakeup_monitor': False,
            'reset_delay': 5000,
            'capture_time': 5000
        }
        
        self.selected_device = None
        self.j2534_device = None
        self.is_monitoring = False
        self.message_queue = queue.Queue()
        
        # Create UI
        self.create_menu()
        self.create_status_bar()
        self.create_main_layout()
        
        # Initialize J2534 devices
        self.init_j2534()
        
        # Update message display
        self.update_messages()
    
    def create_menu(self):
        """Create menu bar"""
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.file_open)
        file_menu.add_command(label="Save As...", command=self.file_save)
        file_menu.add_command(label="Save As... (Data Log)", command=self.file_save_log)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        
        # Setup menu
        setup_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Setup", menu=setup_menu)
        setup_menu.add_command(label="Device Selection", command=self.show_device_selection)
        setup_menu.add_command(label="Monitor Setup", command=self.show_monitor_setup)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Read / Write", command=self.show_read_write)
    
    def create_status_bar(self):
        """Create status bar"""
        self.status_frame = tk.Frame(self, relief=tk.SUNKEN, borderwidth=1)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.status_label = tk.Label(self.status_frame, text="Status:", anchor='w')
        self.status_label.pack(side=tk.LEFT, padx=5)
    
    def create_main_layout(self):
        """Create main window layout"""
        # Main container
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=2)
        
        # Left side - Log area
        self.create_log_panel(main_frame)
        
        # Right side - CAN monitors
        self.create_can_monitors(main_frame)
    
    def create_log_panel(self, parent):
        """Create log panel on left side"""
        log_frame = tk.Frame(parent, relief=tk.SUNKEN, borderwidth=1)
        log_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        tk.Label(log_frame, text="Log:", anchor='w').pack(anchor='w', padx=5, pady=5)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, width=40)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def create_can_monitors(self, parent):
        """Create CAN monitor panels"""
        right_frame = tk.Frame(parent)
        right_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
        # Configure grid
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_columnconfigure(1, weight=1)
        
        # CAN 1 Monitor
        can1_frame = tk.LabelFrame(right_frame, text="CAN 1", relief=tk.RAISED, borderwidth=2)
        can1_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 2))
        
        self.can1_text = scrolledtext.ScrolledText(can1_frame, wrap=tk.WORD, bg='white')
        self.can1_text.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # CAN 2 Monitor
        can2_frame = tk.LabelFrame(right_frame, text="CAN 2", relief=tk.RAISED, borderwidth=2)
        can2_frame.grid(row=0, column=1, sticky='nsew', padx=(2, 0))
        
        self.can2_text = scrolledtext.ScrolledText(can2_frame, wrap=tk.WORD, bg='white')
        self.can2_text.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Start button
        button_frame = tk.Frame(right_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.start_btn = tk.Button(button_frame, text="Start", command=self.toggle_monitoring, 
                                   width=15, height=2)
        self.start_btn.pack()
    
    def init_j2534(self):
        """Initialize J2534 devices"""
        try:
            # Try to get available J2534 devices
            # This is a placeholder - actual implementation would enumerate registry
            self.available_devices = ["Bosch - Ford-VCM-II", "Drew Technologies - Mongoose"]
            self.log("J2534 subsystem initialized")
        except Exception as e:
            self.available_devices = ["Demo Device"]
            self.log(f"J2534 initialization warning: {str(e)}")
            self.log("Running in demo mode")
    
    def log(self, message: str):
        """Add message to log"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
    
    def toggle_monitoring(self):
        """Toggle CAN monitoring"""
        if not self.is_monitoring:
            self.start_monitoring()
        else:
            self.stop_monitoring()
    
    def start_monitoring(self):
        """Start CAN bus monitoring"""
        if not self.selected_device:
            messagebox.showwarning("No Device", "Please select a Pass-Thru device first.\n(Setup -> Device Selection)")
            return
        
        self.log("Starting CAN monitoring...")
        self.is_monitoring = True
        self.start_btn.config(text="Stop")
        self.status_label.config(text="Status: Monitoring...")
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(target=self.monitor_can_bus, daemon=True)
        self.monitor_thread.start()
    
    def stop_monitoring(self):
        """Stop CAN bus monitoring"""
        self.log("Stopping CAN monitoring...")
        self.is_monitoring = False
        self.start_btn.config(text="Start")
        self.status_label.config(text="Status: Stopped")
    
    def monitor_can_bus(self):
        """Monitor CAN bus in background thread"""
        message_count = 0
        
        while self.is_monitoring:
            # Simulate CAN messages in demo mode
            if message_count % 2 == 0:
                msg = f"7E0: 02 01 00 00 00 00 00 00  [{message_count}]"
                self.message_queue.put(('CAN1', msg))
            else:
                msg = f"726: 05 62 D1 00 12 34 56 78  [{message_count}]"
                self.message_queue.put(('CAN2', msg))
            
            message_count += 1
            time.sleep(0.1)  # Simulate message rate
    
    def update_messages(self):
        """Update message displays from queue"""
        try:
            while True:
                can_channel, message = self.message_queue.get_nowait()
                
                if can_channel == 'CAN1' and self.monitor_config['protocol'] in ['CAN1', 'Both']:
                    self.can1_text.insert(tk.END, message + "\n")
                    self.can1_text.see(tk.END)
                    # Limit display size
                    if int(self.can1_text.index('end-1c').split('.')[0]) > 1000:
                        self.can1_text.delete('1.0', '100.0')
                
                elif can_channel == 'CAN2' and self.monitor_config['protocol'] in ['CAN2', 'Both']:
                    self.can2_text.insert(tk.END, message + "\n")
                    self.can2_text.see(tk.END)
                    # Limit display size
                    if int(self.can2_text.index('end-1c').split('.')[0]) > 1000:
                        self.can2_text.delete('1.0', '100.0')
        
        except queue.Empty:
            pass
        
        # Schedule next update
        self.after(50, self.update_messages)
    
    def show_device_selection(self):
        """Show device selection dialog"""
        dialog = DeviceSelectionDialog(self, self.available_devices)
        if dialog.selected_device:
            self.selected_device = dialog.selected_device
            self.log(f"Selected device: {self.selected_device}")
            self.status_label.config(text=f"Status: Device - {self.selected_device}")
    
    def show_monitor_setup(self):
        """Show monitor setup dialog"""
        dialog = MonitorSetupDialog(self, self.monitor_config)
        self.monitor_config = dialog.config
        self.log("Monitor configuration updated")
    
    def show_read_write(self):
        """Show read/write window with password protection"""
        # Show password dialog
        password_dialog = PasswordDialog(self)
        
        if password_dialog.password == "cancan":
            ReadWriteWindow(self, self.j2534_device)
        elif password_dialog.password is not None:
            messagebox.showerror("Access Denied", "Incorrect password")
    
    def file_open(self):
        """Open saved data file"""
        filename = filedialog.askopenfilename(
            title="Open File",
            filetypes=[("VTM Files", "*.vtm"), ("All Files", "*.*")]
        )
        if filename:
            self.log(f"Opening file: {filename}")
            # Implement file loading
    
    def file_save(self):
        """Save current data"""
        filename = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".vtm",
            filetypes=[("VTM Files", "*.vtm"), ("All Files", "*.*")]
        )
        if filename:
            self.log(f"Saving to: {filename}")
            # Implement file saving
    
    def file_save_log(self):
        """Save data log"""
        filename = filedialog.asksaveasfilename(
            title="Save As (Data Log)",
            defaultextension=".log",
            filetypes=[("Log Files", "*.log"), ("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            self.log(f"Saving log to: {filename}")
            # Implement log saving


def main():
    """Main entry point"""
    app = VehicleTrafficMonitor()
    app.mainloop()


if __name__ == "__main__":
    main()
