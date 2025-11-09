#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
#################################################################################################################################################################################################
#                                                                  
#                                                                                                                                                                                                 
#                                                   .  ..   ....   ...   ..  ...  ....    ........   .........      .  .    ..      ...........    ....                                               
#                                              ..                                                                                                         .                                              
#                                             :                            ...                                             ....                   ....     ..                                            
#                                            :      ?YY!    :YY7   :Y!  .?J!~!J?.  !YY^   ?J  :JJ.  .JJ. .JJY^    ~YJ?   ~J?~~7J!   ?Y.   .Y?  .7J~^~??.    :                                            
#                                           .      ~5~7Y.   :5JJ?  :5!  ?5:   :5J  7Y?Y^  JY   .YJ .YJ.  .YJ75:  ^57YJ  :5?    75~  ?5:   .YJ  ~5?          :                                            
#                                          ..     .Y? .Y?   :5!.JJ :5!  JY.   .YJ  75:^5^ JY    .J?J7    .YJ 7Y.:5~.YJ  :57    !5!  ?Y:   .YJ   :!??7~.     :                                            
#                                          .      ?57^^J5~  :5! .JJ~Y!  JY.   .YJ  75: ^Y~JJ     :YJ     .YJ  ?YY!  YJ  :57    !5~  ?5:   .YJ       .757    :                                            
#                            ...          .      !5!.:.:J5. :5!   ?557  ^Y?^::?Y^  75^  ^YYY     .5J     .YJ   ~^  .YJ   7Y!::~Y?.  :Y?^::?Y~  ^J7:.:7Y^     .    .   .         ...                      
#                  ..                            ::     .:.  :.    ::.    .:::.    .:.   .:.      :.      :.        :.    .::^:.      .:::.     .::::.                                   ..              
#                 :                                                                                                                                                                       ..             
#                .       !?7    77   !7 .!!77!!^ .!7!7!.  !77    !77. .~7!!7: .!!77!!^ !7  !7   .7~ :7!!!!.        !7!    :?^     :?^     :?^    ~??:    ^?7:   7!   ^7!!77^   77!!!!.     :             
#                :      ~Y!Y~   JJ   ?Y    ?Y.  .Y?   ?Y  JJJ7  ~Y?Y. ?Y.  !5.   ?Y.   7Y. :Y^  !Y. ^Y~           ~J~J^   ^Y~     ^5~     ^5~   :5!7Y.   !5?Y:  YJ  ~5~   ^~.  YY.         :             
#               .      .Y! !Y.  JJ   ?Y    ?Y   .57   !5. J?.Y~:5:!Y. JJ   ^5^   ?Y    7Y.  7J .J~  :J7~~~       .J~ !J.  ^Y~     ^Y~     ^Y~   JJ .Y7   ~5:^5^ J?  75.        JJ!~~:     ..             
#               :      7Y7^!Y?  JJ   ?Y    ?Y   .57   ?5. J? :Y5~ 7Y. JY   ~5:   ?Y    7J.  .Y~~J   :Y^          ?J!^!J7  ^Y~     ^Y~     ^Y~  ~Y?~~JY:  ~5: ^Y!J?  75:   .:   JJ          .             
#              .      ^Y^   ~Y: ^J7~!J^    7J    ~J!~!J^  ??  .:  !Y. :?7~~?!    ?J    7J.   !JJ^   :J7~~~:     ~J: . ^J^ :J7~~~^ :J?~!!^ :Y~ .J7   .JJ  ~Y:  :YY?  .7J!~!J7.  JJ!~~!.     :             
#              :                  ...              ..                   ...                                                                                            ...          .      :             
#               .                                                                                                                                                                         .              
#                :                          .             ..:^^~~!!!!!!!!!!!~~^:..        ..........................................................................................     .               
#                :                                  .:^!!!!~^:...           ..:^~!!!!^:.                                                                                                 :               
#               ..      ..................      .:!7!~:.                            ..^~!!^.      ..................................................................................     :               
#               :                            :!7!^.                 .:^^..                :~7!^.             ...............................................                             :               
#               :                         .!?!:                  .!?YYYYYJ?~.                .:!7^.                                                                                      :               
#               :      .............    ^?7:                   ^?YYYYYYYYYYYY?^                  :!7:   .:....::::::::::::::::::::::::::::..........................................     :               
#               :                     ~J!.     :!!.          :JYYYYYYYYYYYYYYYY?:          ^!:     .~7^                                                                                  :               
#               :      ..........   ~J~.     !YY~           ~YYJYYYYYYYYYYYYYYJYY^          .?Y7.     ^7^  ..::::::::::::....        ...............................................     :               
#               :                 :J7.  .!:.JJ~            ^YYYYJ?!~^::::^~7?YYYYY:           ^?Y~ !.   ~?:    .............:::::.                                                       .               
#                :               !J:   :Y~.7^::           .YYJ!:             .:7YYJ           ..:7^.Y!   .7!                   ....:..                                                 ..                
#                 ..           .J7    :Y? .^77.           7Y7.                  .?5^           ~7:. ^Y~    ^?:                       ....                                             .                  
#                     ..      :Y~  .^ ?J.^JJ~            .Y!  :~!!!^      ^!!!~.  ??            :?J~.?J .~  .?^                         ...                                        ..                    
#                     .      :Y^   J: Y?77:              !?        ::    ^.       .J.             :!??Y. J:  .?^                           .:.                                    ..                     
#                    ..     :Y^   !5..J^.::              J:   .:~~:       .^!~:    !~             ^:.^J: ??   .J:                             ..                                  :                      
#                    :     .Y~    JY: .:J!              :?   ^^^~~^.      .^^^::   .J              7?:. .JJ.   :J.                              .::..!.                ...       ..                      
#                   :      7?    .YY..?Y^               ?:            ^.            J:              ~J?..JJ.    !?   ................................^::...                      :                       
#                   .     :5.  .: 7J~Y!.                J.   :      . ?^ .     ..   ~!               .7J^?7 .   .J:                                       ...::...              ..                       
#                  .      7?   ^? .YJ..7.               J:   :?~.   :!7!^.  .^7!    ?^              .~ :JJ. 7:   !7    ......                                    ...:...          ..                     
#                  :      Y^   ~Y~ ~.:Y7                .J.   :^~!~~!7.~!~~~!^~    ^?                7?..! ^Y^   :J         ......                                     ......        .                   
#                  .     :5.   :YY: :YJ.                 :?.   .  .:^^.:~^.. :.   ^7                 .JJ. .JJ.   .J.              ....                                       ...       .                 
#                 ..     :Y.    !Y? JY:                   .!^   .    .Y!    .    ~^                   :Y? ~Y~     J:  .::::::....      ..        ............                    ..     .                
#                 ..     ^Y    . ~Y7Y^ ~              .:^!7??7       :Y7       .7??7!^:.             ~ ~Y~J~ :    J:   ............:.......   :..... .........................   .::.    :               
#                 ..     :Y.   !! .J? :Y:        :~!?JYYYYYYYYJ.     :5!      .JYYYYYYYYJ?!^.       .Y. J?. ~7   .Y.       .^^............  :.                                ...   :.   .               
#                 ..     .Y:   .5?..: 7Y:       ~YYYYYYYYYYYYYY?      :      .JYJJJJJJJJYYYYJ.      ^Y! ^ .7Y:   :J   :....             .^ .:          ..............           ...  ^    :              
#                  :      J7    ~YY~  JY.      .YYYYYYYYYYYYYYYY^    ~??.    7YJJJJJJJJJJJJJY!      :Y?  ^YY~    77    ....::::::::::....   ^                                    : ..~:   .              
#                  :      ~Y     :J5?.!Y..~    ~YYYYYYYYYYYYYYYYY.   .Y?    ~YYYYYYJJJJJJJJJYJ    ~..Y!.?Y?:    .Y.          ...........    ..                                  :.    :    .             
#                  ..      Y~    . :?J7Y. Y~   JYYYYYYYYYYYYYYYYY7   .Y?   .YYYYYJJYJJJJJJJJJY:  !J :J7J7: .    77                           ^     ...................          :     ^    :             
#                   :      ^Y.   ^7: .^?^ ?Y:  !YYYYYYYYYJYYYYYYYY^  7YY:  JYJYJJYYYJJYJYJJYY7. ^Y7 !?^..^7.   ^J.   .:..........             ^                                ^    ..!.   :             
#                    .      7J    :JJ!:.. :YJ   .!YYYYYYYYYYYYYYYYY..YYY7 7YJJJJJJJYYJYJYYJ!.   JY. ..:7J7    .Y:    :::::::::::::::.....     .:                              :.   :: ^    :             
#                    .       ?7     ~JYJ!: ~Y: !^ .!JYYYYYYYYYYJJYY7!YYYJ!YYYYYYJJJJJJYYJ~  ^! ~Y: :7JY7:    .J^   .~                          :.                            .^       ^   ..             
#                     :       ?7      .^7J?^!J  J?.  ^?YYYYYJJYYJJJYYJYYYYYYYYYJYYYYYY?^  :J? :J^^?J7^.     .J^    ^       ..                   ^                           .^       .:   .              
#                      .       7?     .:...::~~  !Y!.  .~7JYYYYYYYYYYYYYYYYYYYYYYYJ?~.  .7J^ .~^::...:.    :?:    ^                 .            :..........................:        ^.   .              
#                     .         ~J:    .~77!^:::. :!J7:    .:~!7?JJJYYYYYJJJJ?7!^:.  .^77^. .:.:^~77~.    !7.     ..............     .:..............................................::   ..             
#                  ..            .?!      .^!?JJJJ7!7?7!:.    ..:::::::::::::.    .:!??777JJJJJ?7~.     :?^                              ..............................................   .              
#                 .                ~J^       ..       ..:~7?JJ7~:^^~!^:~~~^:~7J?7!^:..  .......       .7!.   .................  ...  ....:::::::::::::::::::::::::::.:.........:....     ..              
#                :      .........    !?^      :~!!77?JYYYJ?~.  :!~:      .^!^..:~?JYYYJ?7!!~~^.     .7!.                                                                      .        ..                
#               ..                    .~?~.      ..:^^:..   .!J~.           :77:   .:^^~^^..      ^7!.         ..                                               ...       ...     .                      
#               .                        :!7^.             .?~                :7~              :!7^        ...                                                                 ..                        
#               .      ..............       ^!7~.                                          .:!!^.     .......      .         .............................                    ..    . .                  
#               .                              :~!!~:.                                 .^~!~:                                                                                             ..             
#                :                                 .:~!!~^:.                    ..:^~!~^.                                                                                                   :            
#                 .        .~7?J?J????????????????7~:.  ..:^~~~~~~~^^^^^^~~~~!~~~^:.   .:~!7!~:     .^   ::.  :.  .^   .:.  .^   ::.  .:   ::   ^   .::   ^   .:.  .^   ::.  .^   :.  .::    :           
#                  :      ~YYYYYYYYYYYYYYYYYYYYYYYYY5YY?7~^:......................:~7?JYYYYYYYY?     ?  ^: !  ^^   ?  :~ !.  ?  ^: 7  .7  ! .7  !.  7 ^^  7. .! !.  ?  .~ !. .7   :~  ! ^^   :           
#                  :      JYJJJYYYJJJJYJ?7!!!!!!!!!!!!!777777?JJ??77777777???JJYYYYYYYJJJJJJJJJY^   .7  .^.^  ^~   7.  ~.~   7. .:.~  .7  ::::  !:  ~.^.  !:  ~.~   7.  ~.~  .7   :~  ~.^.   :           
#                  :      JJJJJJJJYJYY!.                      .!YYYYYYYYYYYYYYYYYJJYYJJJJJJJJJJY^                                                                                            :           
#                  :      JYJJJJYYYYY^  ^JJJJJJJJJJJJJJJJJJJ?:  ~YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY^                                                                                            :           
#                  :      JYJJJYYYYY^  !YYYYYYYYYYYYYYYYYYYYYY^  ^YYYYYYYYJJJJJJJJJJJJJJJJJJYYJY^   .7   ^~   !:  .7   .7  .^.~  :!  :::^ ^.::  7.  ~.~. .7  .~.~  .7  .^.^  ^^  ~.^. ~.~.   :           
#                  :      JYJJJYYYJ:  75YYYYYYYYYYYYYYYYYYYYYYY~  ^YYYYYYYY~               .JYJY^    ?   .!   ~^   ?    7  ^: 7  .7  !. ! ! .~  !:  7 ^:  7  .~ !   7  ~. !  :~  ! ^: ! ~:   :           
#                  :      JYJJY7:.    ..........................   ..:!YYYY^                ?YJY^   .:.  .:   ::  .:.   :.  ...  .:   ..   ..   :.  ...   :.  ...  .:.  ..   .:  ...  ...    :           
#                  :      JJJYJ                                        JYYY^      :!        JYYY^                                                                                            :           
#                  :      JYJYJ   ~??7?7~                    ~7????^   ?YYY^  ^..^..... :^  JYYY^   ^:^  .~   ^:  ::^  .~  .^:. .::.  ^:   ^:  ::^  ^:^  .~  .^:: .::: .::. ::^.  ~.  ::^    ^           
#                  :      JJJYJ   !JJYYJ?     :::::::::^.    ?JJJYY~   ?YYY^  ^.  ^.  . .:  ?YJY^  .~ !. .?   ^~  7 :^  7  ~. 7 7  !  :~   :~  7 ^:.! ~.  7  ~. 7 !. 7 7 .! 7 .~  !.  ! ~.   ^           
#                  :      JJJJJ                                        ?YJY^       ..:7^    ?YJY^   ^.^  .!   ^^  :.:  .!. .::. .::.  ^^   :^  :.^  ^.^  .!  .::: .::: .::. :.^.  ~:  :.^    :           
#                  :      JJJYJ                                        ?YJY^                ?YJY^                                                                                            :           
#                  :      JYJYJ       ^^^^^^^^^^^^^^^^^^^^^^^^^^.      ?YYY!...............:JYJY^   ...  .:   ..  .:.   :   ..   ..   ..   ..  ...  .:   ..   ..   :.  .:.   :   ...  ...    :           
#                  :      JJJYJ      .YYYYYYYYYYYYYYYYYYYYYYYYY5^      JYJJYYYYYYYYYYYYYYYYYJJJY^  .! !. .7  7 .~ 7 ^:  7  ^: !  ^^   ^~  ! :^ ! ^:  ?   :!   ^~   ~^  7 :^  ?  .! ! .! !.   :           
#                  :      JJJJY?~^::^?YJJJJJJJJJYJJYJJJYJJJYJJJY?^^^^^7YJJYYYJYYJYJJYJJJYJJJJJJY^   ~.~  .7  ^.:: ~.^.  7. .^.~  ^~   ^~  ~.^. ~.^.  7.  :!   :!   ~^  ~.^.  7.  ~.~  ~.~    :           
#                  :      JYJJJYYYYYYYJJJJJJJJJJYJJJYYJJJJJJJJJJYYYYYYYJJJJYJYYYYJJJJJJJYJJJJJJY:                                                                                            .           
#                  :      :JYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ^                                                                                             .           
#                  ..       :~!0x416E6F6E796D6F7573204175746F6D6F7469766520416C6C69616E6365!~:      :!  :::^  7.  ~.~  ~.~ .^.^  ^~  ~.^. .7.  ~.~  :!  :^.^ ::.^  ~:  ^.^. .7   .7  .^.^    .           
#                   ..                                                                              .7  !. !  !: .! ~.:~ ! ~. 7  :~  7 :^  7. .~ !.  7  ~. ! ~. 7  ^^  7 .^  ?    7  ~. 7   ..           
#                     .                                                                             .^   ..   :.  ...  ...  :.   ::  .:.   ^.  ...  .^.  :..  .:.  ::  .::  .^.   ^.  :..   :            
#                       ...                                                                                                                                                               ..             
#                                                                                                                             .  ...   .              .................................         #
#
#
#################################################################################################################################################################################################   

'''

    The Anonymous Automotive Alliance Presents 

             A J2534 Implementation.

               In 32 bit Python.

              Deployed 21/10/2025

           Communication is Essential.

          Without it what would we have?

'''

#################################################################################################################################################################################################   
from enum import IntEnum, Flag
from abc import ABC, abstractmethod
from ctypes import *
from typing import List, Optional
import os

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ConfigParameter(IntEnum):
    DATA_RATE = 0x01
    LOOPBACK = 0x03
    NODE_ADDRESS = 0x04
    NETWORK_LINE = 0x05
    P1_MIN = 0x06
    P1_MAX = 0x07
    P2_MIN = 0x08
    P2_MAX = 0x09
    P3_MIN = 0x0A
    P3_MAX = 0x0B
    P4_MIN = 0x0C
    P4_MAX = 0x0D
    W1 = 0x0E
    W2 = 0x0F
    W3 = 0x10
    W4 = 0x11
    W5 = 0x12
    TIDLE = 0x13
    TINIL = 0x14
    TWUP = 0x15
    PARITY = 0x16
    BIT_SAMPLE_POINT = 0x17
    SYNC_JUMP_WIDTH = 0x18
    W0_MIN = 0x19
    T1_MAX = 0x1A
    T2_MAX = 0x1B
    T4_MAX = 0x1C
    T5_MAX = 0x1D
    ISO15765_BS = 0x1E
    ISO15765_STMIN = 0x1F
    DATA_BITS = 0x20
    FIVE_BAUD_MOD = 0x21
    BS_TX = 0x22
    STMIN_TX = 0x23
    T3_MAX = 0x24
    ISO15765_WFT_MAX = 0x25
    W1_MIN = 0X26
    W2_MIN = 0X27
    W3_MIN = 0X28
    W4_MAX = 0X29
    N_BR_MIN = 0X2A
    ISO15765_PAD_VALUE = 0X2B
    N_AS_MAX = 0X2C
    N_AR_MAX = 0X2D
    N_BS_MAX = 0X2E
    N_CR_MAX = 0X2F
    N_CS_MIN = 0X30
    ECHO_PHYSCIAL_CHANNEL_TX = 0X31
    CAN_MIXED_FORMAT = 0x00008000
    J1962_PINS = 0x00008001
    SW_CAN_HS_DATA_RATE = 0x00008010
    SW_CAN_SPEEDCHANGE_ENABLE = 0x00008011
    SW_CAN_RES_SWITCH = 0x00008012
    ACTIVE_CHANNELS = 0x00008020
    SAMPLE_RATE = 0x00008021
    SAMPLES_PER_READING = 0x00008022
    READINGS_PER_MSG = 0x00008023
    AVERAGING_METHOD = 0x00008024
    SAMPLE_RESOLUTION = 0x00008025
    INPUT_RANGE_LOW = 0x00008026
    INPUT_RANGE_HIGH = 0x00008027
    UEB_T0_MIN = 0x00008028
    UEB_T1_MAX = 0x00008029
    UEB_T2_MAX = 0x0000802A
    UEB_T3_MAX = 0x0000802B
    UEB_T4_MIN = 0x0000802C
    UEB_T5_MAX = 0x0000802D
    UEB_T6_MAX = 0x0000802E
    UEB_T7_MIN = 0x0000802F
    UEB_T7_MAX = 0x00008030
    UEB_T9_MIN = 0x00008031
    J1939_PINS = 0x0000803D
    J1708_PINS = 0x0000803E
    J1939_T1 = 0x0000803F
    J1939_T2 = 0x00008040
    J1939_T3 = 0x00008041
    J1939_T4 = 0x00008042
    J1939_BRDCST_MIN_DELAY = 0x00008043
    TP2_0_T_BR_INT = 0x00008044
    TP2_0_T_E = 0x00008045
    TP2_0_MNTC = 0x00008046
    TP2_0_T_CTA = 0x00008047
    TP2_0_MNCT = 0x00008048
    TP2_0_MNTB = 0x00008049
    TP2_0_MNT = 0x0000804A
    TP2_0_T_Wait = 0x0000804B
    TP2_0_T1 = 0x0000804C
    TP2_0_T3 = 0x0000804D
    TP2_0_IDENTIFER = 0x0000804E
    TP2_0_RXIDPASSIVE = 0x0000804F
    

class IJ2534(ABC):
    @abstractmethod
    def LoadLibrary(self, device: 'J2534Device') -> bool:
        pass

    @abstractmethod
    def FreeLibrary(self) -> bool:
        pass

    @abstractmethod
    def PassThruOpen(self, name: c_void_p, deviceId: c_uint) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruClose(self, deviceId: c_uint) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruConnect(self, deviceId: c_uint, protocolId: 'ProtocolID', flags: 'ConnectFlag', baudRate: 'BaudRate', channelId: c_uint) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruDisconnect(self, channelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruReadMsgs(self, channelId: c_int, msgs: c_void_p, numMsgs: c_int, timeout: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruStartPeriodicMsg(self, channelId: c_int, msg: c_void_p, msgId: c_int, timeInterval: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruStopPeriodicMsg(self, channelId: c_int, msgId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruStartMsgFilter(self, channelid: c_int, filterType: 'FilterType', maskMsg: c_void_p, patternMsg: c_void_p, flowControlMsg: c_void_p, filterId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruStopMsgFilter(self, channelId: c_int, filterId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruSetProgrammingVoltage(self, deviceId: c_int, pinNumber: 'PinNumber', voltage: c_uint) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruReadVersion(self, deviceId: c_int, firmwareVersion: c_void_p, dllVersion: c_void_p, apiVersion: c_void_p) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruGetLastError(self, errorDescription: c_void_p) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruIoctl(self, channelId: c_int, ioctlID: c_int, input: c_void_p, output: c_void_p) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruQueueMsgs(self, channelId: c_int, msg: c_void_p, numMsgs: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruScanForDevices(self, DeviceCount: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruGetNextDevice(self, Device: 'SDEVICE') -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruLogicalConnect(self, PhyscialChannelId: c_int, protocolId: 'ProtocolID', flags: 'ConnectFlag', ChannelDescriptor: c_void_p, LogicalChannelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruLogicalDisconnect(self, LogicalChannelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruSelect(self, ChannelSetPtr: c_void_p, SelectType: c_uint, Timeout: c_uint) -> 'J2534Err':
        pass

    @abstractmethod
    def PassThruWriteMsgs(self, channelId: c_int, msg: c_void_p, numMsgs: c_int, timeout: c_int) -> 'J2534Err':
        pass


class IJ2534Extended(IJ2534):
    @abstractmethod
    def GetConfig(self, channelId: c_int, config: List['SConfig']) -> 'J2534Err':
        pass

    @abstractmethod
    def SetConfig(self, channelId: c_int, config: List['SConfig']) -> 'J2534Err':
        pass

    @abstractmethod
    def SW_CAN_BusSpeed(self, ChannelID: c_int, Option: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def ReadBatteryVoltage(self, deviceId: c_int, voltage: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def ReadProgrammingVoltage(self, deviceId: c_int, voltage: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def FiveBaudInit(self, channelId: c_int, targetAddress: c_byte, keyword1: c_byte, keyword2: c_byte) -> 'J2534Err':
        pass

    @abstractmethod
    def FastInit(self, channelId: c_int, txMsg: 'PassThruMsg', rxMsg: 'PassThruMsg') -> 'J2534Err':
        pass

    @abstractmethod
    def ClearTxBuffer(self, channelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def ClearRxBuffer(self, channelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def ClearPeriodicMsgs(self, channelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def ClearMsgFilters(self, channelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def ClearFunctMsgLookupTable(self, channelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def AddToFunctMsgLookupTable(self, channelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def DeleteFromFunctMsgLookupTable(self, channelId: c_int) -> 'J2534Err':
        pass

    @abstractmethod
    def ReadAllMessages(self, channelId: c_int, numMsgs: c_int, timeout: c_int, messages: List['PassThruMsg'], readUntilTimeout: bool) -> 'J2534Err':
        pass


class Ioctl(IntEnum):
    GET_CONFIG = 0x01
    SET_CONFIG = 0x02
    READ_VBATT = 0x03
    FIVE_BAUD_INIT = 0x04
    FAST_INIT = 0x05
    CLEAR_TX_BUFFER = 0x07
    CLEAR_RX_BUFFER = 0x08
    CLEAR_PERIODIC_MSGS = 0x09
    CLEAR_MSG_FILTERS = 0x0A
    CLEAR_FUNCT_MSG_LOOKUP_TABLE = 0x0B
    ADD_TO_FUNCT_MSG_LOOKUP_TABLE = 0x0C
    DELETE_FROM_FUNCT_MSG_LOOKUP_TABLE = 0x0D
    READ_PROG_VOLTAGE = 0x0E
    BUS_ON = 0x0F
    SW_CAN_HS = 0x8000  # Request swcan Highspeed
    SW_CAN_NS = 0x8001  # Request swcan low speed
    SET_POLL_RESPONSE = 0x8002  # aldl
    BECOME_MASTER = 0x8003  # aldl
    START_REPEAT_MESSAGE = 0x8004
    QUERY_REPEAT_MESSAGE = 0x8005
    STOP_REPEAT_MESSAGE = 0x8006
    GET_ConnectedDevice_CONFIG = 0x8007
    SET_ConnectedDevice_CONFIG = 0x8008
    PROTECT_J1939_ADDR = 0x8009
    REQUEST_CONNECTION = 0x800A
    TEARDOWN_CONNECTION = 0x800B
    GET_Device_INFO = 0x800C
    GET_PROTOCOL_INFO = 0x800D

class GET_DEVICE_INFO_Defines(IntEnum):
    SERIAL_NUMBER = 0x00000001
    J1850PWM_SUPPORTED = 0x00000002
    J1850VPW_SUPPORTED = 0x00000003
    ISO9141_SUPPORTED = 0x00000004
    ISO14230_SUPPORTED = 0x00000005
    CAN_SUPPORTED = 0x00000006
    ISO15765_SUPPORTED = 0x00000007
    SCI_A_ENGINE_SUPPORTED = 0x00000008
    SCI_A_TRANS_SUPPORTED = 0x00000009
    SCI_B_ENGINE_SUPPORTED = 0x0000000A
    SCI_B_TRANS_SUPPORTED = 0x0000000B
    SW_ISO15765_SUPPORTED = 0x0000000C
    SW_CAN_SUPPORTED = 0x0000000D
    GM_UART_SUPPORTED = 0x0000000E
    UART_ECHO_BYTE_SUPPORTED = 0x0000000F
    HONDA_DIAGH_SUPPORTED = 0x00000010
    J1939_SUPPORTED = 0x00000011
    J1708_SUPPORTED = 0x00000012
    TP2_0_SUPPORTED = 0x00000013
    J2610_SUPPORTED = 0x00000014
    ANALOG_IN_SUPPORTED = 0x00000015
    MAX_NON_VOLATILE_STORAGE = 0x00000016
    SHORT_TO_GND_J1962 = 0x00000017
    PGM_VOLTAGE_J1962 = 0x00000018
    J1850PWM_PS_J1962 = 0x00000019
    J1850VPW_PS_J1962 = 0x0000001A
    ISO9141_PS_K_LINE_J1962 = 0x0000001B
    ISO9141_PS_L_LINE_J1962 = 0x0000001C
    ISO14230_PS_K_LINE_J1962 = 0x0000001D
    ISO14230_PS_L_LINE_J1962 = 0x0000001E
    CAN_PS_J1962 = 0x0000001F
    ISO15765_PS_J1962 = 0x00000020
    SW_CAN_PS_J1962 = 0x00000021
    SW_ISO15765_PS_J1962 = 0x00000022
    GM_UART_PS_J1962 = 0x00000023
    UART_ECHO_BYTE_PS_J1962 = 0x00000024
    HONDA_DIAGH_PS_J1962 = 0x00000025
    J1939_PS_J1962 = 0x00000026
    J1708_PS_J1962 = 0x00000027
    TP2_0_PS_J1962 = 0x00000028
    J2610_PS_J1962 = 0x00000029
    J1939_PS_J1939 = 0x0000002A
    J1708_PS_J1939 = 0x0000002B
    ISO9141_PS_K_LINE_J1939 = 0x0000002C
    ISO9141_PS_L_LINE_J1939 = 0x0000002D
    ISO14230_PS_K_LINE_J1939 = 0x0000002E
    ISO14230_PS_L_LINE_J1939 = 0x0000002F
    J1708_PS_J1708 = 0x00000030
    FT_CAN_SUPPORTED = 0x00000031
    FT_ISO15765_SUPPORTED = 0x00000032
    FT_CAN_PS_J1962 = 0x00000033
    FT_ISO15765_PS_J1962 = 0x00000034
    J1850PWM_SIMULTANEOUS = 0x00000035
    J1850VPW_SIMULTANEOUS = 0x00000036
    ISO9141_SIMULTANEOUS = 0x00000037
    ISO14230_SIMULTANEOUS = 0x00000038
    CAN_SIMULTANEOUS = 0x00000039
    ISO15765_SIMULTANEOUS = 0x0000003A
    SCI_A_ENGINE_SIMULTANEOUS = 0x0000003B
    SCI_A_TRANS_SIMULTANEOUS = 0x0000003C
    SCI_B_ENGINE_SIMULTANEOUS = 0x0000003D
    SCI_B_TRANS_SIMULTANEOUS = 0x0000003E
    SW_ISO15765_SIMULTANEOUS = 0x0000003F
    SW_CAN_SIMULTANEOUS = 0x00000040
    GM_UART_SIMULTANEOUS = 0x00000041
    UART_ECHO_BYTE_SIMULTANEOUS = 0x00000042
    HONDA_DIAGH_SIMULTANEOUS = 0x00000043
    J1939_SIMULTANEOUS = 0x00000044
    J1708_SIMULTANEOUS = 0x00000045
    TP2_0_SIMULTANEOUS = 0x00000046
    J2610_SIMULTANEOUS = 0x00000047
    ANALOG_IN_SIMULTANEOUS = 0x00000048
    PART_NUMBER = 0x00000049
    FT_CAN_SIMULTANEOUS = 0x0000004A
    FT_ISO15765_SIMULTANEOUS = 0x0000004B


class RxStatus(Flag):
    NONE = 0x00000000
    TX_MSG_TYPE = 0x00000001
    START_OF_MESSAGE = 0x00000002
    RX_BREAK = 0x00000004
    TX_INDICATION_SUCCESS = 0x00000008
    ISO15765_PADDING_ERROR = 0x00000010
    ERROR_INDICATION = 0x20
    BUFFER_OVERFLOW = 0x40
    ISO15765_ADDR_TYPE = 0x00000080
    CAN_29BIT_ID = 0x00000100
    TX_FAILED = 0x200
    SW_CAN_HV_TX = 0x00000400
    SW_CAN_NS_RX = 0x00040000
    SW_CAN_HS_RX = 0x00020000
    SW_CAN_HV_RX = 0x00010000


class ConnectFlag(Flag):
    NONE = 0x0000
    ISO9141_K_LINE_ONLY = 0x1000
    CAN_ID_BOTH = 0x0800
    ISO9141_NO_CHECKSUM = 0x0200
    CAN_29BIT_ID = 0x0100
    FULL_DUPLEX = 0x1


class TxFlag(Flag):
    NONE = 0x00000000
    SCI_TX_VOLTAGE = 0x00800000
    SCI_MODE = 0x00400000
    WAIT_P3_MIN_ONLY = 0x00000200
    CAN_29BIT_ID = 0x00000100
    ISO15765_ADDR_TYPE = 0x00000080
    ISO15765_FRAME_PAD = 0x00000040
    SW_CAN_HV_TX = 0x00000400


class ProtocolID(IntEnum):
    J1850VPW = 0x01
    J1850PWM = 0x02
    ISO9141 = 0x03
    ISO14230 = 0x04
    CAN = 0x05
    ISO15765 = 0x06
    SCI_A_ENGINE = 0x07
    SCI_A_TRANS = 0x08
    SCI_B_ENGINE = 0x09
    SCI_B_TRANS = 0x0A
    ISO15765_LOGICAL = 0x200
    # J2534-2 protocols
    J1850VPW_PS = 0x8000
    J1850PWM_PS = 0x8001
    ISO9141_PS = 0x8002
    ISO14230_PS = 0x8003
    CAN_PS = 0x8004
    ISO15765_PS = 0x8005
    J2610_PS = 0x8006
    SW_ISO15765_PS = 0x8007
    SW_CAN_PS = 0x8008
    GM_UART_PS = 0x8009
    UART_ECHO_BYTE_PS = 0x800A
    HONDA_DIAGH_PS = 0x800B
    J1939_PS = 0x800C
    J1708_PS = 0x800D
    TP2_0_PS = 0x800E
    FT_CAN_PS = 0x800F
    FT_ISO15765_PS = 0x8010


class BaudRate(IntEnum):
    ISO9141_10400 = 10400
    ISO9141_10000 = 10000
    ISO14230_10400 = 10400
    ISO14230_10000 = 10000
    J1850PWM_41600 = 41600
    J1850PWM_83300 = 83300
    J1850VPW_10400 = 10400
    J1850VPW_41600 = 41600
    CAN_125000 = 125000
    CAN_250000 = 250000
    CAN_500000 = 500000
    CAN_33333 = 33333
    CAN_83333 = 83333
    ISO15765_125000 = 125000
    ISO15765_250000 = 250000
    ISO15765_500000 = 500000
    GMUART_8192 = 8192
    GMUART_160 = 160


class PinNumber(IntEnum):
    AUX = 0
    PIN_1 = 1
    PIN_3 = 3
    PIN_6 = 6
    PIN_9 = 9
    PIN_11 = 11
    PIN_12 = 12
    PIN_13 = 13
    PIN_14 = 14
    PIN_15 = 15


class PinVoltage(IntEnum):
    FEPS_VOLTAGE = 18000
    SHORT_TO_GROUND = 0xFFFFFFFE
    VOLTAGE_OFF = 0xFFFFFFFF


class FilterType(IntEnum):
    PASS_FILTER = 0x01
    BLOCK_FILTER = 0x02
    FLOW_CONTROL_FILTER = 0x03


class J2534Err(IntEnum):
    STATUS_NOERROR = 0x00
    ERR_NOT_SUPPORTED = 0x01
    ERR_INVALID_CHANNEL_ID = 0x02
    ERR_INVALID_PROTOCOL_ID = 0x03
    ERR_NULL_PARAMETER = 0x04
    ERR_INVALID_FLAGS = 0x06
    ERR_FAILED = 0x07
    ERR_ConnectedDevice_NOT_CONNECTED = 0x08
    ERR_TIMEOUT = 0x09
    ERR_INVALID_MSG = 0x0A
    ERR_INVALID_TIME_INTERVAL = 0x0B
    ERR_EXCEEDED_LIMIT = 0x0C
    ERR_INVALID_MSG_ID = 0x0D
    ERR_ConnectedDevice_IN_USE = 0x0E
    ERR_INVALID_IOCTL_ID = 0x0F
    ERR_BUFFER_EMPTY = 0x10
    ERR_BUFFER_FULL = 0x11
    ERR_BUFFER_OVERFLOW = 0x12
    ERR_PIN_INVALID = 0x13
    ERR_CHANNEL_IN_USE = 0x14
    ERR_MSG_PROTOCOL_ID = 0x15
    ERR_INVALID_FILTER_ID = 0x16
    ERR_NO_FLOW_CONTROL = 0x17
    ERR_NOT_UNIQUE = 0x18
    ERR_INVALID_BAUDRATE = 0x19
    ERR_INVALID_ConnectedDevice_ID = 0x1A
    ERR_ConnectedDevice_NOT_OPEN = 0X1B
    ERR_NULL_REQUIRED = 0X1C
    ERR_FILTER_TYPE_NOT_SUPPORTED = 0X1D
    ERR_IOCTL_PARAM_ID_NOT_SUPPORTED = 0X1E
    ERR_VOLTAGE_IN_USE = 0X1F
    ERR_PIN_IN_USE = 0X20
    ERR_INIT_FAILED = 0X21
    ERR_OPEN_FAILED = 0X22
    ERR_BUFFER_TOO_SMALL = 0X23
    ERR_LOG_CHAN_NOT_ALLOWED = 0X24
    ERR_SELECT_TYPE_NOT_SUPPORTED = 0X25
    ERR_CONCURRENT_API_CALL = 0X26
    ERR_OEM_VOLTAGE_TOO_HIGH = 0x77
    ERR_OEM_VOLTAGE_TOO_LOW = 0x78
    ERR_ACCESS_VIOLATION = 0x1000
    ERR_DLL_NOT_LOADED = 0x1001
    ERR_RESOURCE_IN_USE = 0x1002
    ERR_OUT_OF_MEMORY = 0x1999
    ERR_ALDL_HEARTBEAT_NOT_FOUND = 0x5000
    ERR_NO_RESPONSE_FROM_MODULE = 0x5001


class J2534Device:
    def __init__(self):
        self.Vendor = ""
        self.Name = ""
        self.FunctionLibrary = ""
        self.ConfigApplication = ""
        self.CAN = 0
        self.ISO14230 = 0
        self.ISO15765 = 0
        self.ISO9141 = 0
        self.J1850PWM = 0
        self.J1850VPW = 0
        self.SCI_A_ENGINE = 0
        self.SCI_A_TRANS = 0
        self.SCI_B_ENGINE = 0
        self.SCI_B_TRANS = 0
        self.CAN_PS = 0
        self.FT_CAN_PS = 0
        self.FT_ISO15765_PS = 0
        self.GM_UART_PS = 0
        self.ISO14230_PS = 0
        self.ISO15765_PS = 0
        self.ISO9141_PS = 0
        self.SW_CAN_PS = 0
        self.SW_ISO15765_PS = 0
        self.J1850VPW_PS = 0

    def __str__(self):
        return self.Name


class NativeMethods:
    if os.name == 'nt':
        _kernel32 = windll.kernel32
        
        @staticmethod
        def LoadLibrary(dllToLoad: str) -> c_void_p:
            return NativeMethods._kernel32.LoadLibraryW(dllToLoad)
        
        @staticmethod
        def GetProcAddress(hModule: c_void_p, procedureName: str) -> c_void_p:
            return NativeMethods._kernel32.GetProcAddress(hModule, procedureName.encode('ascii'))
        
        @staticmethod
        def FreeLibrary(hModule: c_void_p) -> bool:
            return bool(NativeMethods._kernel32.FreeLibrary(hModule))
    else:
        # For non-Windows systems, use ctypes.CDLL
        _loaded_libs = {}
        
        @staticmethod
        def LoadLibrary(dllToLoad: str) -> c_void_p:
            try:
                lib = CDLL(dllToLoad)
                handle = c_void_p(id(lib))
                NativeMethods._loaded_libs[handle.value] = lib
                return handle
            except:
                return c_void_p(0)
        
        @staticmethod
        def GetProcAddress(hModule: c_void_p, procedureName: str) -> c_void_p:
            if hModule.value in NativeMethods._loaded_libs:
                lib = NativeMethods._loaded_libs[hModule.value]
                try:
                    func = getattr(lib, procedureName)
                    return cast(func, c_void_p)
                except:
                    return c_void_p(0)
            return c_void_p(0)
        
        @staticmethod
        def FreeLibrary(hModule: c_void_p) -> bool:
            if hModule.value in NativeMethods._loaded_libs:
                del NativeMethods._loaded_libs[hModule.value]
                return True
            return False


class J2534DllWrapper:
    def __init__(self):
        self.m_pDll = c_void_p(0)
        
        # Define delegate types
        self.PassThruOpen = None
        self.PassThruClose = None
        self.PassThruScanForDevices = None
        self.PassThruGetNextDevice = None
        self.PassThruConnect = None
        self.PassThruDisconnect = None
        self.PassThruReadMsgs = None
        self.PassThruWriteMsgs = None
        self.PassThruQueueMsgs = None
        self.PassThruLogicalConnect = None
        self.PassThruLogicalDisconnect = None
        self.PassThruSelect = None
        self.PassThruStartPeriodicMsg = None
        self.PassThruStopPeriodicMsg = None
        self.PassThruStartMsgFilter = None
        self.PassThruStartPassBlockMsgFilter = None
        self.PassThruStopMsgFilter = None
        self.PassThruSetProgrammingVoltage = None
        self.PassThruReadVersion = None
        self.PassThruGetLastError = None
        self.PassThruIoctl = None
        
        # Define function prototypes
        self.Open = None
        self.Close = None
        self.ScanForDevices = None
        self.GetNextDevice = None
        self.Connect = None
        self.Disconnect = None
        self.ReadMsgs = None
        self.WriteMsgs = None
        self.WriteQueueMsgs = None
        self.ConnectLogical = None
        self.DisconnectLogical = None
        self.SelectChannelToCheck = None
        self.StartPeriodicMsg = None
        self.StopPeriodicMsg = None
        self.StartMsgFilter = None
        self.StartPassBlockMsgFilter = None
        self.StopMsgFilter = None
        self.SetProgrammingVoltage = None
        self.ReadVersion = None
        self.GetLastError = None
        self.Ioctl = None

    def LoadJ2534Library(self, path: str) -> bool:
        self.m_pDll = NativeMethods.LoadLibrary(path)
        
        if not self.m_pDll:
            return False
        
        # Load PassThruOpen
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruOpen")
        if pAddressOfFunctionToCall:
            self.Open = CFUNCTYPE(c_int, c_void_p, POINTER(c_uint))(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruClose
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruClose")
        if pAddressOfFunctionToCall:
            self.Close = CFUNCTYPE(c_int, c_uint)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruConnect
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruConnect")
        if pAddressOfFunctionToCall:
            self.Connect = CFUNCTYPE(c_int, c_uint, c_int, c_int, c_int, POINTER(c_uint))(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruDisconnect
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruDisconnect")
        if pAddressOfFunctionToCall:
            self.Disconnect = CFUNCTYPE(c_int, c_int)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruReadMsgs
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruReadMsgs")
        if pAddressOfFunctionToCall:
            self.ReadMsgs = CFUNCTYPE(c_int, c_int, c_void_p, POINTER(c_int), c_int)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruWriteMsgs
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruWriteMsgs")
        if pAddressOfFunctionToCall:
            self.WriteMsgs = CFUNCTYPE(c_int, c_int, c_void_p, POINTER(c_int), c_int)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruStartPeriodicMsg
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruStartPeriodicMsg")
        if pAddressOfFunctionToCall:
            self.StartPeriodicMsg = CFUNCTYPE(c_int, c_int, c_void_p, POINTER(c_int), c_int)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruStopPeriodicMsg
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruStopPeriodicMsg")
        if pAddressOfFunctionToCall:
            self.StopPeriodicMsg = CFUNCTYPE(c_int, c_int, c_int)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruStartMsgFilter
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruStartMsgFilter")
        if pAddressOfFunctionToCall:
            self.StartMsgFilter = CFUNCTYPE(c_int, c_int, c_int, c_void_p, c_void_p, c_void_p, POINTER(c_int))(pAddressOfFunctionToCall.value)
        
        # Load PassThruStartMsgFilter (as StartPassBlockMsgFilter)
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruStartMsgFilter")
        if pAddressOfFunctionToCall:
            self.StartPassBlockMsgFilter = CFUNCTYPE(c_int, c_int, c_int, POINTER(PassThruMsg), POINTER(PassThruMsg), c_int, POINTER(c_int))(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruStopMsgFilter
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruStopMsgFilter")
        if pAddressOfFunctionToCall:
            self.StopMsgFilter = CFUNCTYPE(c_int, c_int, c_int)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruSetProgrammingVoltage
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruSetProgrammingVoltage")
        if pAddressOfFunctionToCall:
            self.SetProgrammingVoltage = CFUNCTYPE(c_int, c_int, c_uint, c_uint)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruReadVersion
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruReadVersion")
        if pAddressOfFunctionToCall:
            self.ReadVersion = CFUNCTYPE(c_int, c_int, c_void_p, c_void_p, c_void_p)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruGetLastError
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruGetLastError")
        if pAddressOfFunctionToCall:
            self.GetLastError = CFUNCTYPE(c_int, c_void_p)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        # Load PassThruIoctl
        pAddressOfFunctionToCall = NativeMethods.GetProcAddress(self.m_pDll, "PassThruIoctl")
        if pAddressOfFunctionToCall:
            self.Ioctl = CFUNCTYPE(c_int, c_int, c_int, c_void_p, c_void_p)(pAddressOfFunctionToCall.value)
        else:
            return False
        
        return True

    def FreeLibrary(self) -> bool:
        if self.m_pDll:
            NativeMethods.FreeLibrary(self.m_pDll)
        return True


class J2534Functions(IJ2534):
    def __init__(self):
        self._ConnectedDevice = None
        self._J2534DllWrapper = None
        self._IsDLLLoaded = False

    def __str__(self):
        return "Deployed publicly for the greater automotive good by the Anonymous Automotive Alliance, Oct 2025."

    @property
    def IsDLLLoaded(self) -> bool:
        return self._IsDLLLoaded

    @property
    def DeviceName(self) -> str:
        return self._ConnectedDevice.Name if self._ConnectedDevice else ""

    def LoadLibrary(self, device: J2534Device) -> bool:
        try:
            self._ConnectedDevice = device
            self._J2534DllWrapper = J2534DllWrapper()
            self._IsDLLLoaded = self._J2534DllWrapper.LoadJ2534Library(self._ConnectedDevice.FunctionLibrary)
            return self._IsDLLLoaded
        except Exception:
            self._IsDLLLoaded = False
            return self._IsDLLLoaded

    def FreeLibrary(self) -> bool:
        self._IsDLLLoaded = False
        if self._J2534DllWrapper:
            return self._J2534DllWrapper.FreeLibrary()
        return True

    def PassThruOpen(self, name: c_void_p, deviceId: c_uint) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            result = J2534Err(self._J2534DllWrapper.Open(name, byref(deviceId)))
            return result
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruClose(self, deviceId: c_uint) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.Close(deviceId))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruScanForDevices(self, DeviceCount: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.ScanForDevices(byref(DeviceCount)))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruGetNextDevice(self, Device: 'SDEVICE') -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.GetNextDevice(byref(Device)))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruQueueMsgs(self, channelId: c_int, msgs: c_void_p, numMsgs: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.WriteQueueMsgs(channelId, msgs, byref(numMsgs)))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruLogicalConnect(self, PhyscialChannelId: c_int, protocolId: ProtocolID, flags: ConnectFlag, ChannelDescriptor: c_void_p, LogicalChannelId: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.ConnectLogical(PhyscialChannelId, protocolId, flags, byref(ChannelDescriptor), byref(LogicalChannelId)))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruLogicalDisconnect(self, LogicalChannelId: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.DisconnectLogical(LogicalChannelId))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruSelect(self, ChannelSetPtr: c_void_p, SelectType: c_uint, Timeout: c_uint) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.SelectChannelToCheck(byref(ChannelSetPtr), SelectType, Timeout))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruConnect(self, deviceId: c_uint, protocolId: ProtocolID, flags: ConnectFlag, baudRate: BaudRate, channelId: c_uint) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.Connect(deviceId, protocolId, flags, baudRate, byref(channelId)))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruDisconnect(self, channelId: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.Disconnect(channelId))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruReadMsgs(self, channelId: c_int, msgs: c_void_p, numMsgs: c_int, timeout: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.ReadMsgs(channelId, msgs, byref(numMsgs), timeout))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruWriteMsgs(self, channelId: c_int, msgs: c_void_p, numMsgs: c_int, timeout: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.WriteMsgs(channelId, msgs, byref(numMsgs), timeout))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruStartPeriodicMsg(self, channelId: c_int, msg: c_void_p, msgId: c_int, timeInterval: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.StartPeriodicMsg(channelId, msg, byref(msgId), timeInterval))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruStopPeriodicMsg(self, channelId: c_int, msgId: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.StopPeriodicMsg(channelId, msgId))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruStartMsgFilter(self, channelid: c_int, filterType: FilterType, maskMsg: c_void_p, patternMsg: c_void_p, flowControlMsg: c_void_p, filterId: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.StartMsgFilter(channelid, int(filterType), maskMsg, patternMsg, flowControlMsg, byref(filterId)))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruStopMsgFilter(self, channelId: c_int, filterId: c_int) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.StopMsgFilter(channelId, filterId))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruSetProgrammingVoltage(self, deviceId: c_int, pinNumber: PinNumber, voltage: c_uint) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.SetProgrammingVoltage(deviceId, int(pinNumber), voltage))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruReadVersion(self, deviceId: c_int, firmwareVersion: c_void_p, dllVersion: c_void_p, apiVersion: c_void_p) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.ReadVersion(deviceId, firmwareVersion, dllVersion, apiVersion))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruGetLastError(self, errorDescription: c_void_p) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.GetLastError(errorDescription))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION

    def PassThruIoctl(self, channelId: c_int, ioctlID: c_int, input: c_void_p, output: c_void_p) -> J2534Err:
        try:
            if not self.IsDLLLoaded:
                return J2534Err.ERR_DLL_NOT_LOADED
            return J2534Err(self._J2534DllWrapper.Ioctl(channelId, ioctlID, input, output))
        except Exception:
            return J2534Err.ERR_ACCESS_VIOLATION


class J2534FunctionsExtended(J2534Functions, IJ2534Extended):
    def GetConfig(self, channelId: c_int, config: List[SConfig]) -> J2534Err:
        try:
            sConfigList = SConfigList()
            sConfigList.ListPtr = cast(create_string_buffer(sizeof(SConfig) * len(config)), c_void_p)
            sConfigList.Count = len(config)
            for i in range(len(config)):
                memmove(sConfigList.ListPtr.value + sizeof(SConfig) * i, addressof(config[i]), sizeof(SConfig))
            
            output = c_void_p(0)
            input_ptr = cast(create_string_buffer(sizeof(SConfigList)), c_void_p)
            memmove(input_ptr.value, addressof(sConfigList), sizeof(SConfigList))
            
            err = J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.GET_CONFIG), input_ptr, output))
            
            configList = Utils.AsStruct(input_ptr, SConfigList).GetList()
            
            config.clear()
            for i in range(len(configList)):
                config.append(configList[i])
            
            return err
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def SetConfig(self, channelId: c_int, config: List[SConfig]) -> J2534Err:
        try:
            sConfigList = SConfigList()
            sConfigList.ListPtr = cast(create_string_buffer(sizeof(SConfig) * len(config)), c_void_p)
            sConfigList.Count = len(config)
            for i in range(len(config)):
                memmove(sConfigList.ListPtr.value + sizeof(SConfig) * i, addressof(config[i]), sizeof(SConfig))
            
            output = c_void_p(0)
            input_ptr = cast(create_string_buffer(sizeof(SConfigList)), c_void_p)
            memmove(input_ptr.value, addressof(sConfigList), sizeof(SConfigList))
            
            Err = J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.SET_CONFIG), input_ptr, output))
            
            return Err
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def SW_CAN_BusSpeed(self, ChannelID: c_int, Option: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            
            if Option == 0:
                return J2534Err(self._J2534DllWrapper.Ioctl(ChannelID, int(Ioctl.SW_CAN_HS), input_val, output))
            else:
                return J2534Err(self._J2534DllWrapper.Ioctl(ChannelID, int(Ioctl.SW_CAN_NS), input_val, output))
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def ReadBatteryVoltage(self, deviceId: c_int, voltage: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = cast(create_string_buffer(8), c_void_p)
            
            returnValue = J2534Err(self._J2534DllWrapper.Ioctl(deviceId, int(Ioctl.READ_VBATT), input_val, output))
            if returnValue == J2534Err.STATUS_NOERROR:
                voltage = cast(output, POINTER(c_int)).contents.value
            
            return returnValue
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def ReadProgrammingVoltage(self, deviceId: c_int, voltage: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = cast(create_string_buffer(8), c_void_p)
            
            voltage = int(self._J2534DllWrapper.Ioctl(deviceId, int(Ioctl.READ_PROG_VOLTAGE), input_val, output))
            
            return J2534Err.STATUS_NOERROR
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def FiveBaudInit(self, channelId: c_int, targetAddress: c_byte, keyword1: c_byte, keyword2: c_byte) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            
            inputArray = SByteArray()
            outputArray = SByteArray()
            inputArray.NumOfBytes = 1
            outputArray.NumOfBytes = 2
            
            memmove(input_val, addressof(inputArray), sizeof(SByteArray))
            memmove(output, addressof(outputArray), sizeof(SByteArray))
            
            returnValue = J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.FIVE_BAUD_INIT), input_val, output))
            
            return returnValue
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def FastInit(self, channelId: c_int, txMsg: PassThruMsg, rxMsg: PassThruMsg) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            uRxMsg = PassThruMsg()
            
            memmove(input_val, addressof(txMsg), sizeof(PassThruMsg))
            memmove(output, addressof(uRxMsg), sizeof(PassThruMsg))
            
            returnValue = J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.FAST_INIT), input_val, output))
            if returnValue == J2534Err.STATUS_NOERROR:
                memmove(addressof(rxMsg), output, sizeof(PassThruMsg))
            
            return returnValue
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def ClearTxBuffer(self, channelId: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            return J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.CLEAR_TX_BUFFER), input_val, output))
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def ClearRxBuffer(self, channelId: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            return J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.CLEAR_RX_BUFFER), input_val, output))
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def ClearPeriodicMsgs(self, channelId: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            return J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.CLEAR_PERIODIC_MSGS), input_val, output))
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def ClearMsgFilters(self, channelId: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            return J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.CLEAR_MSG_FILTERS), input_val, output))
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def ClearFunctMsgLookupTable(self, channelId: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            return J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.CLEAR_FUNCT_MSG_LOOKUP_TABLE), input_val, output))
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def AddToFunctMsgLookupTable(self, channelId: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            # TODO: fix this
            return J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.ADD_TO_FUNCT_MSG_LOOKUP_TABLE), input_val, output))
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def DeleteFromFunctMsgLookupTable(self, channelId: c_int) -> J2534Err:
        try:
            input_val = c_void_p(0)
            output = c_void_p(0)
            # TODO: fix this
            return J2534Err(self._J2534DllWrapper.Ioctl(channelId, int(Ioctl.DELETE_FROM_FUNCT_MSG_LOOKUP_TABLE), input_val, output))
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY

    def ReadAllMessages(self, channelId: c_int, numMsgs: c_int, timeout: c_int, messages: List[PassThruMsg], readUntilTimeout: bool = True) -> J2534Err:
        """
        Poll for messages until we get a timeout
        """
        try:
            rxMsgs = cast(create_string_buffer(sizeof(PassThruMsg) * numMsgs), c_void_p)
            m_status = J2534Err.STATUS_NOERROR
            m_status2 = J2534Err.STATUS_NOERROR
            
            # Read the first block of messages
            m_status = self.PassThruReadMsgs(channelId, rxMsgs, numMsgs, timeout)
            if m_status == J2534Err.STATUS_NOERROR:
                msgs = Utils.AsMsgList(rxMsgs, numMsgs)
                if len(msgs) > 0:
                    messages.extend(msgs)
                
                # If we are only reading this block then return now
                if not readUntilTimeout:
                    return m_status
            else:
                msgs = Utils.AsMsgList(rxMsgs, numMsgs)
                if len(msgs) > 0:
                    messages.extend(msgs)
                # If we failed on the first read give up now
                return m_status
            
            # We successfully read one block, now keep going
            while J2534Err.STATUS_NOERROR == m_status2:
                m_status2 = self.PassThruReadMsgs(channelId, rxMsgs, numMsgs, timeout)
                if m_status2 == J2534Err.STATUS_NOERROR:
                    msgs = Utils.AsMsgList(rxMsgs, numMsgs)
                    for msg in msgs:
                        messages.append(msg)
                else:
                    break
            
            return J2534Err.STATUS_NOERROR
        except MemoryError:
            return J2534Err.ERR_OUT_OF_MEMORY


class J2534Exception(Exception):
    def __init__(self, error: J2534Err):
        super().__init__(str(error))
        self._error = error

    @property
    def Error(self) -> J2534Err:
        return self._error

class PassThruMsg(Structure):
    _fields_ = [
        ("ProtocolID", c_int),
        ("RxStatus", c_uint),
        ("TxFlags", c_uint),
        ("Timestamp", c_uint),
        ("DataSize", c_uint),
        ("ExtraDataIndex", c_uint),
        ("Data", c_byte * 4128)
    ]

    def __init__(self, myProtocolId: ProtocolID = None, myTxFlag: TxFlag = None, myByteArray: bytes = None):
        super().__init__()
        if myProtocolId is not None:
            self.ProtocolID = myProtocolId
        if myTxFlag is not None:
            self.TxFlags = myTxFlag
        if myByteArray is not None:
            self.SetBytes(myByteArray)

    def SetBytes(self, myByteArray: bytes):
        self.DataSize = len(myByteArray)
        for i in range(len(myByteArray)):
            self.Data[i] = myByteArray[i]

    def GetBytes(self) -> bytes:
        return bytes(self.Data[:self.DataSize])

    def ToString(self, tab: str) -> str:
        return (
            f"{os.linesep}{tab}Protocol: {self.ProtocolID}{os.linesep}"
            f"{tab}RxStatus: {self.RxStatus}{os.linesep}"
            f"{tab}Timestamp: {self.Timestamp}{os.linesep}"
            f"{tab}ExtraDataIndex: {self.ExtraDataIndex}{os.linesep}"
            f"{tab}Data: {'-'.join(f'{b:02X}' for b in self.GetBytes())}"
        )


class SByteArray(Structure):
    _fields_ = [
        ("NumOfBytes", c_int),
        ("BytePtr", c_void_p)
    ]

    def __str__(self) -> str:
        byteList = Utils.AsList(c_void_p(self.BytePtr), self.NumOfBytes, c_byte)
        return ' '.join(f'{b:02X}' for b in byteList).replace('-', ' ')


class SConfig(Structure):
    _fields_ = [
        ("Parameter", c_int),
        ("Value", c_uint16)
    ]


class SConfigList(Structure):
    _fields_ = [
        ("Count", c_int),
        ("ListPtr", c_void_p)
    ]

    def GetList(self) -> List[SConfig]:
        if self.ListPtr == c_void_p(0).value:
            return []
        return Utils.AsList(c_void_p(self.ListPtr), self.Count, SConfig)


class SParam(Structure):
    _fields_ = [
        ("Parameter", c_uint),  # Name of patameter
        ("Value", c_uint),  # value of parameter
        ("Supported", c_uint)  # support for parameter
    ]


class SParamList(Structure):
    _fields_ = [
        ("Count", c_int),
        ("ListPtr", c_void_p)
    ]

    def GetList(self) -> List[SParam]:
        if self.ListPtr == c_void_p(0).value:
            return []
        return Utils.AsList(c_void_p(self.ListPtr), self.Count, SParam)


class Utils:
    @staticmethod
    def AsString(ptr: c_void_p) -> str:
        return cast(ptr, c_char_p).value.decode('ascii', errors='ignore')

    @staticmethod
    def ToIntPtr(msg: PassThruMsg) -> c_void_p:
        msgPtr = cast(create_string_buffer(sizeof(PassThruMsg)), c_void_p)
        memmove(msgPtr.value, addressof(msg), sizeof(PassThruMsg))
        return msgPtr

    @staticmethod
    def AsMsgList(ptr: c_void_p, count: int) -> List[PassThruMsg]:
        list_items = []
        for index in range(count):
            list_items.append(Utils.AsStruct(ptr, PassThruMsg))
        return list_items

    @staticmethod
    def AsList(ptr: c_void_p, count: int, struct_type: type) -> List:
        list_items = []
        for index in range(count):
            ptr1 = c_void_p(ptr.value + index * sizeof(struct_type))
            list_items.append(Utils.AsStruct(ptr1, struct_type))
        return list_items

    @staticmethod
    def AsStruct(ptr: c_void_p, struct_type: type):
        return cast(ptr, POINTER(struct_type)).contents

    @staticmethod
    def AsNullableStruct(ptr: c_void_p, struct_type: type) -> Optional:
        if ptr == c_void_p(0).value or ptr is None:
            return None
        return cast(ptr, POINTER(struct_type)).contents

    @staticmethod
    def AsString(list_items: List[PassThruMsg]) -> str:
        str_result = ""
        for index in range(len(list_items)):
            str_result += (
                f"{str_result}{index} -------------------------------{os.linesep}"
                f"{list_items[index].ToString('')}{index} -------------------------------"
            )
        return str_result


class SDEVICE(Structure):
    _fields_ = [
        ("DeviceName", c_char * 80),
        ("DeviceAvailable", c_uint),
        ("DeviceDLLFWStatus", c_uint),
        ("DeviceConnectMedia", c_uint),
        ("DeviceConnectSpeed", c_uint),
        ("DeviceSignalQuality", c_uint),
        ("DeviceSignalStrength", c_uint)
    ]
