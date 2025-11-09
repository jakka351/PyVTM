# Vehicle Traffic Monitor Configuration
# This file shows available configuration options

## Application Settings
APP_TITLE = "VTM v7.81.6"
APP_GEOMETRY = "1400x800"

## Read/Write Tool Password
# Default password for accessing diagnostic tools
READ_WRITE_PASSWORD = "cancan"

## Default Device
# Set your preferred J2534 device
# Leave empty for manual selection each time
DEFAULT_DEVICE = ""
# Example: DEFAULT_DEVICE = "Bosch - Ford-VCM-II"

## Logging Settings
LOG_TIMESTAMP_FORMAT = "%H:%M:%S.%f"
LOG_MAX_LINES = 1000

## CAN Display Settings
CAN_DISPLAY_MAX_LINES = 1000
CAN_MESSAGE_FORMAT = "{id}: {data}  [{count}]"

## Default Monitor Configuration
DEFAULT_MONITOR_CONFIG = {
    'can1_filter': 'No Filters',
    'can2_filter': 'No Filters',
    'can1_trigger': False,
    'can2_trigger': False,
    'protocol': 'Both',
    'wakeup_monitor': False,
    'reset_delay': 5000,
    'capture_time': 5000
}

## Protocol Settings
PROTOCOLS = {
    'ISO15765': {
        'id': 0x06,  # ISO15765 protocol ID
        'baudrates': ['500K (HS CAN)', '250K', '125K (MS CAN)']
    },
    'ISO9141': {
        'id': 0x03,
        'baudrates': ['10400', '9600']
    },
    'J1850PWM': {
        'id': 0x01,
        'baudrates': ['41600']
    },
    'J1850VPW': {
        'id': 0x02,
        'baudrates': ['10400']
    },
    'CAN': {
        'id': 0x05,
        'baudrates': ['500000', '250000', '125000']
    }
}

## ECU Target IDs
ECU_TARGETS = {
    'PCM - Powertrain Control Module': '7E0',
    'TCM - Transmission Control Module': '7E1',
    'ABS - Anti-lock Braking System': '7E2',
    'RCM - Restraint Control Module': '7E5',
    'IPC - Instrument Panel Cluster': '7E6',
    'BCM - Body Control Module': '7E7',
    'PAM - Parking Aid Module': '7E8'
}

## Message Filtering
# Diagnostic message range for Ford vehicles
DIAGNOSTIC_MSG_RANGE = (0x700, 0x7FF)

# Common Ford CAN IDs to monitor
FORD_COMMON_IDS = [
    0x7E0,  # PCM Request
    0x7E8,  # PCM Response
    0x7E1,  # TCM Request
    0x7E9,  # TCM Response
    0x7DF,  # Functional Request
]

## Color Scheme (for future UI enhancements)
COLORS = {
    'bg_main': '#F0F0F0',
    'bg_panel': '#FFFFFF',
    'fg_text': '#000000',
    'border': '#C0C0C0',
    'highlight': '#0078D7'
}

## File Extensions
FILE_EXTENSIONS = {
    'session': '.vtm',
    'log': '.log',
    'config': '.cfg'
}

## Demo Mode Settings
DEMO_MODE = {
    'enabled': True,  # Allow demo mode if no J2534 device
    'message_rate': 0.1,  # Seconds between simulated messages
    'simulate_responses': True
}

## Advanced Settings
ADVANCED = {
    'enable_raw_can': False,  # Show raw CAN frames
    'auto_reconnect': True,  # Auto reconnect on disconnect
    'keep_alive_interval': 2000,  # Tester present interval (ms)
    'response_timeout': 1000,  # Response timeout (ms)
}

## Security Settings
SECURITY = {
    'require_password': True,  # Require password for Read/Write
    'max_attempts': 3,  # Max password attempts before lockout
    'lockout_time': 300  # Lockout time in seconds
}

## Notes
"""
Configuration Priority:
1. Command-line arguments (highest)
2. Environment variables
3. This configuration file
4. Built-in defaults (lowest)

To use this configuration:
1. Rename to vtm_config.py
2. Place in same directory as vtm_main.py
3. Import in vtm_main.py: from vtm_config import *

Example custom configuration:
- Set DEFAULT_DEVICE to your J2534 device name
- Adjust LOG_MAX_LINES for more/less log retention
- Change READ_WRITE_PASSWORD for additional security
- Modify DEMO_MODE settings for testing
"""
