# Vehicle Traffic Monitor (VTM) v7.81.6

A Python-based recreation of the Ford Motor Company Vehicle Traffic Monitor tool for CAN bus monitoring, diagnostics, and ECU communication using J2534 Pass-Thru devices.

## Features

### Core Functionality
- **Dual CAN Bus Monitoring**: Simultaneous monitoring of CAN 1 (HS-CAN) and CAN 2 (MS-CAN)
- **J2534 Pass-Thru Support**: Compatible with J2534-compliant diagnostic interfaces
- **Real-time Message Display**: Live CAN message capture and display
- **Message Filtering**: Support for pass filters, block filters, and diagnostic message filtering
- **Data Logging**: Save captured CAN traffic to log files

### Advanced Features
- **Read/Write Tool**: Password-protected ECU diagnostic interface (password: `cancan`)
- **ISO15765 (UDS) Support**: Send and receive diagnostic messages
- **Multiple Protocol Support**: ISO15765, ISO9141, J1850PWM, J1850VPW, CAN
- **Device Selection**: Support for multiple J2534 devices
- **Wakeup Monitoring**: Monitor for network wakeup events

## Installation

### Requirements
- Python 3.7 or higher
- Windows OS (for J2534 device support)
- J2534-compliant Pass-Thru device (e.g., Ford VCM-II, Drew Technologies Mongoose)

### Setup

1. Clone or download the project files:
```bash
git clone <repository-url>
cd vehicle-traffic-monitor
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. Ensure your J2534 device drivers are properly installed

4. Place the `j2534.py` library in the same directory as `vtm_main.py`

## Usage

### Starting the Application

```bash
python vtm_main.py
```

### Basic Workflow

1. **Select J2534 Device**
   - Navigate to `Setup → Device Selection`
   - Choose your J2534 Pass-Thru device from the list
   - Click OK to confirm

2. **Configure Monitor Settings**
   - Navigate to `Setup → Monitor Setup`
   - Configure CAN 1 and CAN 2 filters
   - Set protocol to monitor (CAN 1, CAN 2, or Both)
   - Configure wakeup monitoring if needed
   - Click OK to save settings

3. **Start Monitoring**
   - Click the `Start` button
   - CAN messages will appear in real-time in the CAN 1 and CAN 2 windows
   - Log messages appear in the left panel

4. **Stop Monitoring**
   - Click the `Stop` button to halt monitoring

### Read/Write Tool

1. Navigate to `Tools → Read / Write`
2. Enter password: `cancan`
3. Configure target ECU settings:
   - Target ID (e.g., 7E0 for PCM)
   - Protocol (ISO15765 recommended)
   - Baud rate (500K for HS-CAN)
4. Click `Connect` to establish communication
5. Enter diagnostic commands in hex format (e.g., `22 D1 00`)
6. Click `Send` to transmit the message
7. Responses appear in the message display area

### Saving Data

- **Save Session**: `File → Save As...` - Save current configuration and data
- **Save Data Log**: `File → Save As... (Data Log)` - Export CAN messages to log file
- **Open Session**: `File → Open` - Load previously saved session

## Supported ECU Modules

The Read/Write tool supports communication with various vehicle modules:
- **PCM** - Powertrain Control Module (7E0)
- **TCM** - Transmission Control Module (7E1)
- **ABS** - Anti-lock Braking System (7E2)
- **RCM** - Restraint Control Module (7E5)
- **IPC** - Instrument Panel Cluster (7E6)
- **BCM** - Body Control Module (7E7)
- **PAM** - Parking Aid Module (7E8)

## Message Filtering

### Filter Types
- **No Filters**: Display all CAN messages
- **Diagnostic Messages Only**: Show only UDS diagnostic messages (7xx range)
- **Pass Filters**: Only show messages matching specified IDs
- **Block Filters**: Hide messages matching specified IDs

### Filter Configuration
1. Open `Setup → Monitor Setup`
2. Select filter type for CAN 1 and/or CAN 2
3. Enter up to 3 filter IDs per channel
4. Use hex format (e.g., `07DF`, `726`)
5. Click OK to apply filters

## Protocols

### ISO15765 (ISO-TP over CAN)
- Default protocol for modern Ford vehicles
- Supports extended addressing
- Automatic flow control
- Baud rates: 500K (HS-CAN), 125K (MS-CAN)

### Other Protocols
- **ISO9141**: K-Line protocol for older vehicles
- **J1850PWM**: 41.6 kbps PWM protocol
- **J1850VPW**: 10.4 kbps VPW protocol
- **CAN**: Raw CAN bus access

## Demo Mode

If no J2534 device is available, the application runs in demo mode:
- Simulates CAN message traffic
- Allows UI testing without hardware
- Read/Write tool generates simulated responses

## Project Structure

```
vehicle-traffic-monitor/
├── vtm_main.py           # Main application file
├── j2534.py              # J2534 interface library
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Troubleshooting

### "No J2534 device available"
- Verify J2534 device drivers are installed
- Check device is connected via USB
- Try selecting device manually in Device Selection

### "Connection failed"
- Verify vehicle ignition is ON
- Check OBD-II cable connection
- Ensure correct protocol is selected
- Verify baud rate matches vehicle network

### "Incorrect password"
- Read/Write password is: `cancan` (case-sensitive)

### No messages displayed
- Verify Start button has been clicked
- Check Monitor Setup protocol selection
- Verify filters aren't blocking messages
- Ensure vehicle network is active

## Technical Details

### CAN Message Format
```
ID: DATA_BYTES [COUNT]
Example: 7E0: 02 01 00 00 00 00 00 00 [123]
```

### UDS Diagnostic Format
```
Request:  [SID] [DID_HIGH] [DID_LOW] [DATA...]
Response: [SID+40] [DID_HIGH] [DID_LOW] [DATA...]

Example:
Request:  22 D1 00        (Read DID 0xD100)
Response: 62 D1 00 12 34  (Response with data 0x1234)
```

### Common Service IDs (SID)
- `0x10` - Diagnostic Session Control
- `0x11` - ECU Reset
- `0x22` - Read Data By Identifier
- `0x27` - Security Access
- `0x2E` - Write Data By Identifier
- `0x31` - Routine Control
- `0x34` - Request Download
- `0x36` - Transfer Data
- `0x37` - Request Transfer Exit

## Safety and Legal

⚠️ **WARNING**: This tool provides direct access to vehicle control modules.

- Only use on vehicles you own or have permission to access
- Improper use can damage vehicle systems or void warranties
- Some operations may be restricted by law in your jurisdiction
- Always follow proper diagnostic procedures
- Keep vehicle in a safe state during diagnostics

## Credits

Original software: Ford Motor Company
Python recreation: Community project
J2534 interface: Based on SAE J2534 standard

## License

This is an educational recreation. Refer to your local laws regarding automotive diagnostic tools.

## Support

For issues, questions, or contributions:
- Check the Troubleshooting section
- Review J2534 device documentation
- Consult Ford diagnostic documentation
- Ensure all drivers and software are up to date

---

**Version**: 7.81.6
**Compatible Devices**: J2534-compliant Pass-Thru devices
**Platform**: Windows (Python 3.7+)
