# Vehicle Traffic Monitor - Quick Start Guide

## Installation

1. **Ensure Python is Installed**
   ```bash
   python --version
   # Should show Python 3.7 or higher
   ```

2. **Download Project Files**
   - `vtm_main.py` - Main application
   - `j2534.py` - J2534 interface library
   - `requirements.txt` - Dependencies (optional)

3. **Install Dependencies** (optional)
   ```bash
   pip install -r requirements.txt
   ```

## First Time Setup

### Step 1: Connect Hardware
1. Connect your J2534 Pass-Thru device to your computer via USB
2. Install the device drivers if not already installed
3. Connect the device to the vehicle's OBD-II port
4. Turn vehicle ignition to ON (engine can be off)

### Step 2: Launch Application
```bash
cd path/to/project
python vtm_main.py
```

### Step 3: Select Device
1. Click `Setup` menu
2. Select `Device Selection`
3. Choose your J2534 device (e.g., "Bosch - Ford-VCM-II")
4. Click `Ok`

### Step 4: Configure Monitoring
1. Click `Setup` menu
2. Select `Monitor Setup`
3. Configure settings:
   - **CAN 1 Setup**: Select "No Filters" for full capture
   - **CAN 2 Setup**: Select "No Filters" for full capture
   - **Protocol to Monitor**: Select "Both"
4. Click `Ok`

### Step 5: Start Monitoring
1. Click the `Start` button in the main window
2. CAN messages will start appearing in the CAN 1 and CAN 2 panels
3. Activity is logged in the left panel

### Step 6: Stop Monitoring
1. Click the `Stop` button
2. Save data if needed via `File → Save As... (Data Log)`

## Common Tasks

### Reading ECU Data

1. **Access Read/Write Tool**
   - Click `Tools → Read / Write`
   - Enter password: `cancan`
   - Click `Submit`

2. **Connect to ECU**
   - Select Target ID (e.g., "PCM - Powertrain Control Module")
   - Verify Target ID hex value (e.g., `7E0`)
   - Select Protocol: `ISO15765`
   - Select Baud Rate: `500K (HS CAN)`
   - Click `Connect`

3. **Send Diagnostic Command**
   - Enter command in hex (e.g., `22 D1 00` to read DID D100)
   - Click `Send`
   - Response appears in message display area

### Common Diagnostic Commands

```
# Read VIN
22 F1 90

# Read Calibration ID
22 F1 00

# Read Programming Date
22 F1 99

# Read ECU Software Version
22 F1 A0

# Start Diagnostic Session
10 03

# ECU Reset
11 01

# Security Access Request Seed
27 01

# Tester Present (keep session alive)
3E 00
```

### Saving Data

**Save CAN Traffic Log:**
1. Stop monitoring if active
2. Click `File → Save As... (Data Log)`
3. Choose location and filename
4. Click `Save`

**Save Session:**
1. Click `File → Save As...`
2. Choose location and filename (`.vtm` extension)
3. Click `Save`

## Filtering Messages

### Show Only Diagnostic Messages
1. Open `Setup → Monitor Setup`
2. Select "Diagnostic Messages Only" for CAN 1 or CAN 2
3. Click `Ok`
4. Only messages in the 7xx range will be displayed

### Block Specific IDs
1. Open `Setup → Monitor Setup`
2. Select "Block Filters"
3. Enter IDs to block (e.g., `726`, `620`)
4. Click `Ok`

### Show Only Specific IDs
1. Open `Setup → Monitor Setup`
2. Select "Pass Filters"
3. Enter IDs to show (e.g., `7E0`, `7E8`)
4. Click `Ok`

## Troubleshooting

### No J2534 Device Found
- **Solution 1**: Install device drivers from manufacturer
- **Solution 2**: Check USB connection
- **Solution 3**: Run application in demo mode (will work without device)

### No CAN Messages Appearing
- **Check 1**: Verify vehicle ignition is ON
- **Check 2**: Ensure OBD-II connector is properly seated
- **Check 3**: Check Monitor Setup protocol selection
- **Check 4**: Disable message filters temporarily
- **Check 5**: Verify device is connected in Device Selection

### Read/Write Connection Failed
- **Check 1**: Verify correct Target ID for your vehicle
- **Check 2**: Try starting a diagnostic session first: `10 03`
- **Check 3**: Ensure correct protocol (usually ISO15765 for Ford)
- **Check 4**: Check baud rate (500K for HS-CAN)

### "Incorrect Password" Error
- The password for Read/Write is: `cancan` (lowercase, no spaces)

### Messages Appearing Too Fast
1. Open `Setup → Monitor Setup`
2. Enable filters to reduce message count
3. Use "Diagnostic Messages Only" for cleaner display

## Tips and Best Practices

### General
- Always save data before closing the application
- Use diagnostic message filter to reduce clutter
- Log file timestamps help with debugging

### Diagnostics
- Send `3E 00` (Tester Present) every 2 seconds to maintain session
- Always start with `10 03` (Start Diagnostic Session) before other commands
- Wait for positive response (first byte 0x50 or higher) before sending next command

### Safety
- Never perform diagnostics while vehicle is moving
- Keep vehicle in PARK with parking brake engaged
- Ensure adequate ventilation if engine is running
- Have a second person monitor vehicle status

## Ford-Specific Notes

### Common Target IDs
```
7E0 (PCM)  → 7E8 (Response)
7E1 (TCM)  → 7E9 (Response)
7E2 (ABS)  → 7EA (Response)
```

### Network Configuration
- **HS-CAN**: 500 kbps (Powertrain network)
- **MS-CAN**: 125 kbps (Body/Chassis network)

### Security Access
Most write operations require security access (Service 0x27):
1. Send `27 01` to request seed
2. Calculate key from seed using algorithm
3. Send `27 02 [key_bytes]` to unlock

## Additional Resources

### Documentation
- SAE J2534 Standard
- ISO 14229 (UDS) Specification
- Ford Service Manual for your vehicle

### Commands
- [Read service codes]: `19 02 xx`
- [Clear DTCs]: `14 FF FF FF`
- [Read freeze frame]: `19 04`

## Support

For detailed information, refer to:
- README.md - Full documentation
- j2534.py - J2534 API documentation
- Ford diagnostic documentation

---

**Remember**: Always follow manufacturer diagnostic procedures and safety guidelines.
