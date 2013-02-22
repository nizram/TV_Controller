import time
import serial

"""
NEC PX-42VM5HA Control Codes

Power
	ON			9FH 80H 60H 4EH 00H CDH
	OFF			9FH 80H 60H 4FH 00H CEH
Input Switch
	VIDEO1(BNC)		DFH 80H 60H 47H 01H 01H 08H
	VIDEO2(RCA)		DFH 80H 60H 47H 01H 02H 09H
	VIDEO2(S-Video)		DFH 80H 60H 47H 01H 03H 0AH
	DVD1/HD1(RCA/Component)	DFH 80H 60H 47H 01H 05H 0CH
	DVD2/HD2(5BNC/Compnent)	DFH 80H 60H 47H 01H 06H 0DH
	RGB1(15pin HD)		DFH 80H 60H 47H 01H 07H 0EH
	RGB2(5BNC/RGB)		DFH 80H 60H 47H 01H 08H 1FH
	RGB3(DVI)		DFH 80H 60H 47H 01H 0CH 13H
Audio Mute
	ON			9FH 80H 60H 3EH 00H BDH
	OFF			9FH 80H 60H 3FH 00H BEH
Picture Mode
	NORMAL			DFH 80H 60H 0AH 01H 01H CBH
	THEAT.1			DFH 80H 60H 0AH 01H 02H CCH
	THEAT.2			DFH 80H 60H 0AH 01H 03H CDH
	DEFAULT			DFH 80H 60H 0AH 01H 04H CEH
	BRIGHT			DFH 80H 60H 0AH 01H 05H CFH
Screen Mode
	STADIUM			DFH 80H 60H 51H 01H 02H 13H
	ZOOM			DFH 80H 60H 51H 01H 03H 14H
	NORMAL			DFH 80H 60H 51H 01H 04H 15H
	FULL			DFH 80H 60H 51H 01H 05H 16H
	2.35:1			DFH 80H 60H 51H 01H 0AH 1BH
Auto Picture
	ON			DFH 80H 60H 7FH 03H 03H 09H 00H 4DH
	OFF			DFH 80H 60H 7FH 03H 03H 09H 01H 4EH
Cinema Mode
	ON			DFH 80H 60H C1H 01H 01H 82H
	OFF			DFH 80H 60H C1H 01H 02H 83H

Communication Protocol:
	Interface: RS-232C
	Communication: Asynchronous
	Baud Rate: 9600
	Data Length: 8bits
	Parity: Odd
	Stop Bit: 1bit
	Communication Code: Hex
"""

ser = serial.Serial(
	port='COM1',
	baudrate=9600,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

ser.close()
ser.open()
ser.isOpen()


#ON="9FH 80H 60H 4EH 00H CDH"
ON=bytearray([0x9F,0x80,0x60,0x4E,0x00,0xCD])
ON2="\x9f\x80\x60\x4e\x00\xcd"
#OFF="9FH 80H 60H 4FH 00H CEH"
OFF=bytearray([0x9F,0x80,0x60,0x4F,0x00,0xCE])
OFF2="\x9f\x80\x60\x4f\x00\xce"

ser.write(OFF)
time.sleep(30)
ser.write(ON)
ser.close()
