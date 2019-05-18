
"""
Simple demo of reading Temperature using a Pt100 sensor with the help of a 
Raspbbery Pi and the ADS1115 AD controller. 
Author: Christos Karapanagiotis
"""

# Import the ADS1x15 module.
import Adafruit_ADS1x15

import time
import csv
from tools import find_nearest

#Import the conversion table
with open("pt100.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    conv_list = list(csv_reader)
    conv_list = list(list(map(float,i)) for i in conv_list)
     
# define the current across the PT100 in mA:
current = 1

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1
#The gain defines the voltage range:
#  Gain = 2/3   --> +/-6.144V
#  Gain = 1     --> +/-4.096V
#  Gain = 2     --> +/-2.048V
#  Gain = 4     --> +/-1.024V
#  Gain = 8     --> +/-0.512V
#  Gain = 16    --> +/-0.256V


# Print nice channel column headers.
print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} |'.format(*range(4)))
print('-' * 37)


# Measurements
while (True):
    # Read all the ADC channel values in a list.
    values = [0]*4
   
    # Read the specified ADC channel using the previously set gain value.
    
    #Display Voltage in mV:
    values[0] = ((adc.read_adc(0, gain=GAIN))*4096/32767)
    #Display Resistance:
    values[1] = values[0] / current
    #Display Temperature:
    values[2] = find_nearest(conv_list,values[1])
        
    # Print the ADC values.
    print('| {0:>6} | {1:>6} | {2:>6} |'.format(*values))
    
    # Pause for two seconds.    
    time.sleep(2)


        
