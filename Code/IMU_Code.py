PYTHON CODE FOR EXTTACTING GPS RAW DATA IN STATIC AND DYNAMIC MODE

import smbus     #Import SMBus Module of I2C
from time import sleep     #Import

#Some MPU6050 Registers and their Address
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

def MPU_Init():
     #Write to Sample Rate Register
     bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
     #Write to Power Management Register
     bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
     #Write to Configuration Register
     bus.write_byte_data(Device_Address, CONFIG, 0)
     #Write to Gyro Configuration Register
     bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
     #Write to Interrupt Enable Register
     bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
     #Accelero and Gyro Value are 16-bit
     high = bus.read_byte_data(Device_Address, addr)
     low = bus.read_byte_data(Device_Address, addr+1)
     #Concatenate Higher and Lower Value
     value = ((high &lt;&lt; 8) | low)
     #To get Signed Value from MPU6050
     if(value &gt; 32768):
          value = value - 65536
     return value
     
bus = smbus.SMBus(1)     #Or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68      #MPU6050 Device Address

MPU_Init()

print ("Reading Data of Gyroscope and Accelerometer")

while True:
     #Read Accelerometer Raw Value
     acc_x = read_raw_data(ACCEL_XOUT_H)
     acc_y = read_raw_data(ACCEL_YOUT_H)
     acc_z = read_raw_data(ACCEL_ZOUT_H)
     #Read Gyroscope Raw Value
     gyro_x = read_raw_data(GYRO_XOUT_H)
     gyro_y = read_raw_data(GYRO_YOUT_H)
     gyro_z = read_raw_data(GYRO_ZOUT_H)
     #Full Scale Range +/- 250 Degree/C as Per Sensitivity Scale Factor
     Ax = acc_x/16384.0
     Ay = acc_y/16384.0
     Az = acc_z/16384.0
     Gx = gyro_x/131.0
     Gy = gyro_y/131.0
     Gz = gyro_z/131.0

print ("Gx=%.2f"%Gx, u'\u00b0'+"/s", "\tGy=%.2f"%Gy, '\u00b'+"/s", "\tGz=%.2f"%Gz, '\u00b0'+"/s", "\tAx=%.2fg"%Ax, "\tAy=%.2fg"%Ay, "\tAz=%.2f g"%Az)
sleep(1)
