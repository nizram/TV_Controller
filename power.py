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
ON=bytearray([0x9FH,0x80H,0x60H,0x4EH,0x00H,0xCDH])
#OFF="9FH 80H 60H 4FH 00H CEH"
OFF=bytearray([0x9FH,0x80H,0x60H,0x4FH,0x00H,0xCEH])
#FLAG1=0x9FH
#FLAG2=0x80H
#FLAG3=0x60H
#FLAG4=0x4FH
#FLAG5=0x00H
#FLAG6=0xCEH

ser.write(OFF)
#ser.write(chr(FLAG1))
#ser.write(chr(FLAG2))
#ser.write(chr(FLAG3))
#ser.write(chr(FLAG4))
#ser.write(chr(FLAG5))
#ser.write(chr(FLAG6))

ser.close()
