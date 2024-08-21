
import board

import digitalio
import analogio

from time import sleep

led = digitalio.DigitalInOut( board.LED )
led.direction = digitalio.Direction.OUTPUT
led.value = False

# ---- SETTINGS ----

# define the analog input pins
AIP = [ 
  board.GP26_A0, 
  board.GP27_A1,
  #board.GP28_A2, # if not used in hardware setup, please disable here
]

# tolerance to change (+/-)
# if more then <value> difference between new and current value,
#  current value will be updated
WOBBLE_THRESHOLD = 4
# if you have a bad hardware setup or small potentiometers,
# you can adjust it here
# BE AWARE, THIS MAY IMPACT THE VOLUME STEP SIZE


# min and max, so that it never can go == 0, 
#  because windows will mute the specified audio stream completely
#  you would have to enable it manualy, 
#  ... so this is here to prevent that
_OUT_MIN_VALUE = 8
_OUT_MAX_VALUE = 1000

_MIN_VAL = 0
_MAX_VAL = 1024

# convert from 16-bit to 8-bit
def value_convertion(val:int):
  return int(((val+1)/(65535+1))*1024)
# +1 to avoid/midigate zero-division errors

# interval for the loop
_ACTION_INTERVAL_DELAY = 0.050

_ACTION_BREAKER_pin = digitalio.DigitalInOut( board.GP17 )
_ACTION_BREAKER_pin.direction = digitalio.Direction.INPUT
_ACTION_BREAKER_pin.pull = digitalio.Pull.UP

# ---- -------- ----

# internaly used AnalogIn instances for AIP[x]
APIO: list[analogio.AnalogIn] = []

CVAL: list[int] = [] # current values
PVAL: list[int] = [] # previous values



# ---- -------- ----
# variable auto-setup generator

sleep(0.001)
led.value = True

for a in range( 0, len( AIP ) ):
  APIO.append( 0 )
  CVAL.append( 0 )
  PVAL.append( 0 )
  APIO[a] = analogio.AnalogIn( AIP[a] )
  vl = value_convertion( APIO[a].value )
  if vl < _OUT_MIN_VALUE or vl > _OUT_MAX_VALUE:
    if vl < _OUT_MIN_VALUE:
      CVAL[a] = _OUT_MIN_VALUE
    elif vl > _OUT_MAX_VALUE:
      CVAL[a] = _MAX_VAL
  else:
    CVAL[a] = vl

sleep(0.025)
led.value = False



# ---- -------- ----
# ----   MAIN   ----

while _ACTION_BREAKER_pin.value:
  hc = False
  for a in range( 0, len( APIO ) ):
    vl = value_convertion( APIO[a].value )
    if vl-WOBBLE_THRESHOLD > CVAL[a] or vl+WOBBLE_THRESHOLD < CVAL[a]:
      PVAL[a] = CVAL[a]
      if vl < _OUT_MIN_VALUE or vl > _OUT_MAX_VALUE:
        if vl < _OUT_MIN_VALUE:
          CVAL[a] = _OUT_MIN_VALUE
        elif vl > _OUT_MAX_VALUE:
          CVAL[a] = _MAX_VAL
      else:
        CVAL[a] = vl
      if not CVAL[a] == PVAL[a]:
        hc = True
    del vl
  
  if hc:
    led.value = True
  
  print((''.join([str(cr)+'|' for cr in CVAL]))[:-1])

  sleep( _ACTION_INTERVAL_DELAY )
  if hc:
    led.value = False




# ---- -------- ----
# ----  DEINIT  ----

led.value = True
for a in range( 0, len( APIO ) ):
  APIO[a].deinit()
led.value = False

for a in range(0,4):
  led.value = True
  sleep(0.100)
  led.value = False
  sleep(0.050)
  led.value = True
  sleep(0.250)
  led.value = False
  sleep(0.150)

