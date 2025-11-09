# Vehicle Traffic Monitor - Technical Reference

## Architecture Overview

### Application Structure

```
VehicleTrafficMonitor (Main Application)
├── UI Layer
│   ├── MenuBar (File, Setup, Tools)
│   ├── StatusBar
│   ├── LogPanel (Left side)
│   └── CANMonitorPanel (Right side)
│       ├── CAN1 Display
│       └── CAN2 Display
├── Dialog Windows
│   ├── PasswordDialog
│   ├── DeviceSelectionDialog
│   ├── MonitorSetupDialog
│   └── ReadWriteWindow
└── Backend
    ├── J2534Interface (j2534.py)
    ├── MessageQueue (threading.queue)
    └── MonitorThread (background CAN monitoring)
```

### Key Components

#### 1. Main Window (VehicleTrafficMonitor)
- **Purpose**: Primary application window
- **Responsibilities**:
  - Menu management
  - Device selection
  - Monitor configuration
  - CAN message display
  - Logging
  - File I/O

#### 2. Password Dialog (PasswordDialog)
- **Purpose**: Secure access to Read/Write tools
- **Authentication**: Simple password check ("cancan")
- **Security**: Can be enhanced with hashing

#### 3. Device Selection Dialog (DeviceSelectionDialog)
- **Purpose**: J2534 device enumeration and selection
- **Data Source**: Windows Registry (HKEY_LOCAL_MACHINE\SOFTWARE\PassThruSupport.04.04)
- **Fallback**: Demo mode if no devices found

#### 4. Monitor Setup Dialog (MonitorSetupDialog)
- **Purpose**: Configure CAN monitoring parameters
- **Settings**:
  - Filter configuration
  - Protocol selection
  - Wakeup monitoring
  - Timing parameters

#### 5. Read/Write Window (ReadWriteWindow)
- **Purpose**: ECU diagnostic communication
- **Features**:
  - Target selection
  - Protocol configuration
  - Message transmission
  - Response display
  - Connection management

## Data Flow

### CAN Message Capture Flow

```
Vehicle CAN Bus
    ↓
J2534 Pass-Thru Device
    ↓
J2534 DLL (PassThruReadMsgs)
    ↓
Python J2534 Wrapper (j2534.py)
    ↓
Monitor Thread (monitor_can_bus)
    ↓
Message Queue (queue.Queue)
    ↓
UI Update (update_messages)
    ↓
CAN Display Widgets
```

### Diagnostic Message Flow

```
User Input (Read/Write Window)
    ↓
Hex String Parsing
    ↓
PassThruMsg Structure
    ↓
J2534 DLL (PassThruWriteMsgs)
    ↓
Vehicle ECU
    ↓
ECU Response
    ↓
J2534 DLL (PassThruReadMsgs)
    ↓
Response Display
```

## J2534 Interface

### Key Functions Used

```python
# Device Management
PassThruOpen(device_name) -> device_id
PassThruClose(device_id)

# Channel Management
PassThruConnect(device_id, protocol, flags, baudrate) -> channel_id
PassThruDisconnect(channel_id)

# Message Operations
PassThruReadMsgs(channel_id, msgs, num_msgs, timeout)
PassThruWriteMsgs(channel_id, msgs, num_msgs, timeout)

# Filter Management
PassThruStartMsgFilter(channel_id, filter_type, mask, pattern, flow_control)
PassThruStopMsgFilter(channel_id, filter_id)
```

### Message Structure (PassThruMsg)

```python
class PassThruMsg:
    ProtocolID: int       # Protocol identifier
    RxStatus: int         # Receive status flags
    TxFlags: int          # Transmit flags
    Timestamp: int        # Message timestamp (microseconds)
    DataSize: int         # Number of data bytes
    ExtraDataIndex: int   # Index to extra data
    Data: bytes          # Message data (up to 4128 bytes)
```

## Threading Model

### Main Thread
- **Responsibilities**:
  - UI rendering and updates
  - User input handling
  - File I/O operations
- **Blocking Operations**: None (delegates to worker threads)

### Monitor Thread
- **Responsibilities**:
  - Continuous CAN message reading
  - Message filtering
  - Queue management
- **Communication**: Via `threading.queue.Queue`
- **Lifecycle**: Daemon thread, automatically terminated on app exit

### Thread Safety
- **Queue**: Thread-safe by design
- **UI Updates**: All UI updates in main thread via `after()` method
- **Shared State**: Minimal; configuration is copied

## Message Filtering

### Filter Types

1. **No Filters**
   - All messages pass through
   - Implementation: No J2534 filters installed

2. **Diagnostic Messages Only**
   - Messages in range 0x700-0x7FF
   - Implementation: Pass filter with mask 0x700

3. **Pass Filters**
   - Only specified IDs shown
   - Implementation: Multiple J2534 pass filters

4. **Block Filters**
   - Specified IDs hidden
   - Implementation: J2534 block filters

### Filter Implementation

```python
# Example: Diagnostic messages only
mask = PassThruMsg(ProtocolID=ISO15765, Data=b'\x00\x07\x00\x00')
pattern = PassThruMsg(ProtocolID=ISO15765, Data=b'\x00\x07\x00\x00')
PassThruStartMsgFilter(channel_id, PASS_FILTER, mask, pattern, None)
```

## Protocol Support

### ISO15765 (ISO-TP)
- **Layer**: Transport layer over CAN
- **Features**:
  - Single-frame messages (≤7 bytes)
  - Multi-frame messages (>7 bytes)
  - Flow control
  - Extended addressing
- **Baud Rates**: 500K (HS-CAN), 125K (MS-CAN)

### Message Format
```
Single Frame:  [0x0N] [DATA...]           (N = length)
First Frame:   [0x1N] [0xNN] [DATA...]    (N = length high/low)
Consecutive:   [0x2N] [DATA...]           (N = sequence)
Flow Control:  [0x30] [BS] [ST]           (BS=block size, ST=sep time)
```

## UDS (Unified Diagnostic Services)

### Request Format
```
[Service ID] [Sub-function/DID] [Data...]
```

### Response Format
```
Positive: [Service ID + 0x40] [Data...]
Negative: [0x7F] [Service ID] [NRC]
```

### Negative Response Codes (NRC)
```
0x10 - General Reject
0x11 - Service Not Supported
0x12 - Sub-function Not Supported
0x13 - Incorrect Message Length
0x22 - Conditions Not Correct
0x31 - Request Out Of Range
0x33 - Security Access Denied
0x35 - Invalid Key
0x36 - Exceed Number Of Attempts
0x37 - Required Time Delay Not Expired
0x78 - Response Pending
```

## Security Considerations

### Password Protection
- **Current**: Simple string comparison
- **Recommended**: 
  - Hash passwords (bcrypt/argon2)
  - Rate limiting
  - Session timeouts
  - Audit logging

### ECU Security Access
- **Challenge-Response**: ECU sends seed, tool responds with key
- **Algorithm**: Proprietary per manufacturer
- **Implementation**: External to VTM (user-provided)

### Data Protection
- **Logging**: May contain sensitive vehicle data
- **Storage**: Plain text (consider encryption)
- **Transmission**: No network features (local only)

## Performance Optimization

### Message Display
- **Issue**: High message rates can overwhelm UI
- **Solutions**:
  - Limit display buffer (currently 1000 lines)
  - Batch updates (update every 50ms)
  - Virtual scrolling (future enhancement)

### Memory Management
- **Issue**: Long monitoring sessions accumulate memory
- **Solutions**:
  - Periodic buffer clearing
  - Generator-based message reading
  - Explicit garbage collection

## Extension Points

### Adding New Protocols
1. Add protocol definition to `PROTOCOLS` dict
2. Update protocol combobox values
3. Implement protocol-specific message handling
4. Add filter logic if needed

### Custom Message Handlers
```python
def custom_handler(msg: PassThruMsg) -> str:
    """Process and format CAN message"""
    can_id = int.from_bytes(msg.Data[0:4], 'big')
    data = msg.Data[4:msg.DataSize]
    return f"{can_id:03X}: {data.hex(' ').upper()}"
```

### Plugin Architecture (Future)
```python
class VTMPlugin:
    def on_message(self, channel: int, msg: PassThruMsg):
        """Called for each CAN message"""
        pass
    
    def on_connect(self, channel_id: int):
        """Called when channel opens"""
        pass
    
    def on_disconnect(self, channel_id: int):
        """Called when channel closes"""
        pass
```

## Testing

### Unit Testing
```python
import unittest

class TestJ2534Interface(unittest.TestCase):
    def test_device_enumeration(self):
        devices = enumerate_j2534_devices()
        self.assertIsInstance(devices, list)
    
    def test_message_parsing(self):
        msg = parse_hex_string("22 D1 00")
        self.assertEqual(len(msg), 3)
        self.assertEqual(msg[0], 0x22)
```

### Integration Testing
- Test with actual J2534 device
- Verify protocol compliance
- Validate message timing
- Check filter operation

### Demo Mode Testing
- No hardware required
- Simulated message generation
- UI functionality verification

## Debugging

### Enable Verbose Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### J2534 Error Codes
```python
STATUS_NOERROR = 0x00
ERR_INVALID_CHANNEL_ID = 0x07
ERR_INVALID_PROTOCOL_ID = 0x08
ERR_TIMEOUT = 0x09
ERR_BUFFER_EMPTY = 0x0A
ERR_BUFFER_FULL = 0x0B
```

### Common Issues
1. **Device Not Found**: Check drivers, registry entries
2. **Connection Timeout**: Verify vehicle network is active
3. **No Messages**: Check filters, protocol selection
4. **Garbled Messages**: Verify baud rate, protocol match

## Code Style

### Naming Conventions
- **Classes**: PascalCase (`VehicleTrafficMonitor`)
- **Functions**: snake_case (`start_monitoring`)
- **Constants**: UPPER_SNAKE_CASE (`READ_WRITE_PASSWORD`)
- **Private**: Leading underscore (`_internal_method`)

### Documentation
- Docstrings for all public classes and methods
- Inline comments for complex logic
- Type hints where applicable

### Error Handling
```python
try:
    result = risky_operation()
except SpecificException as e:
    self.log(f"Error: {str(e)}")
    # Handle or re-raise
```

## Future Enhancements

### Short Term
- [ ] Save/load session data
- [ ] Export to CSV/Excel
- [ ] Message statistics
- [ ] Search and filter in display

### Medium Term
- [ ] Protocol analyzer
- [ ] DTC (trouble code) reader
- [ ] Graphical message visualization
- [ ] Replay captured data

### Long Term
- [ ] Plugin system
- [ ] Remote monitoring
- [ ] Database integration
- [ ] Automated test sequences

## References

### Standards
- SAE J2534: PassThru Vehicle Programming
- ISO 14229: Unified Diagnostic Services (UDS)
- ISO 15765: Diagnostics on CAN
- ISO 11898: CAN Specification

### Documentation
- Ford Service Procedures
- J2534 API Documentation
- Python ctypes Documentation
- Tkinter Reference

## Contributing

### Code Review Checklist
- [ ] Follows style guide
- [ ] Includes documentation
- [ ] Handles errors gracefully
- [ ] Thread-safe if applicable
- [ ] Tested in demo mode
- [ ] Tested with real hardware

### Pull Request Template
```markdown
## Description
Brief description of changes

## Testing
- [ ] Tested in demo mode
- [ ] Tested with J2534 device
- [ ] No regressions

## Checklist
- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] Tests pass
```

---

**Version**: 7.81.6
**Last Updated**: 2025
**Maintainer**: Community
