import pygame, sys, os
from pygame.locals import * 
#import thread 
import threading
from System import *

# References
_Sys = None
_CRT = None

# ------------------------------------------------------------
#   Main Routine
# ------------------------------------------------------------

# Constructor
pygame.init() 
 
window = pygame.display.set_mode((300, 200)) 
pygame.display.set_caption( 'PyChip8 v0.2J' ) 

print ("PyChip8 v0.2J: A CHIP8 emulator in Python ")
print ("Copyright (c) 2007 Jay's Factory.")
print ("All Rights Reserved.")

# Create Chip8's System
_Sys = System()

# Initialize Chip8's System
if ( len( sys.argv ) < 2 or
     _Sys.Init( pygame, sys.argv[ 1 ] ) < 0 ) :
    # Failed
    print ("Usage: python " + sys.argv[ 0 ] + " <ROM file name>")
    sys.exit()

# Start Chip8's System
#thread.start_new_thread( _Sys.Run, () )
threading.Thread(target=_Sys.Run, args=()).start()

# ------------------------------------------------------------
#   Window System
# ------------------------------------------------------------

# Key Event 
def input( events ): 
    for event in events: 
        if ( event.type == QUIT ) : 
            sys.exit(0) 
        # KEYDOWN
        elif ( event.type == KEYDOWN ) : 
            if ( event.key == pygame.K_b ) :
                _Sys._IO.Key |= ( 1 << 0 )
            if ( event.key == pygame.K_4 ) :
                _Sys._IO.Key |= ( 1 << 1 )
            if ( event.key == pygame.K_5 ) :
                _Sys._IO.Key |= ( 1 << 2 )
            if ( event.key == pygame.K_6 ) :
                _Sys._IO.Key |= ( 1 << 3 )
            if ( event.key == pygame.K_r ) :
                _Sys._IO.Key |= ( 1 << 4 )
            if ( event.key == pygame.K_t ) :
                _Sys._IO.Key |= ( 1 << 5 )
            if ( event.key == pygame.K_y ) :
                _Sys._IO.Key |= ( 1 << 6 )
            if ( event.key == pygame.K_f ) :
                _Sys._IO.Key |= ( 1 << 7 )
            if ( event.key == pygame.K_g ) :
                _Sys._IO.Key |= ( 1 << 8 )
            if ( event.key == pygame.K_h ) :
                _Sys._IO.Key |= ( 1 << 9 )
            if ( event.key == pygame.K_v ) :
                _Sys._IO.Key |= ( 1 << 10 )
            if ( event.key == pygame.K_n ) :
                _Sys._IO.Key |= ( 1 << 11 )
            if ( event.key == pygame.K_7 ) :
                _Sys._IO.Key |= ( 1 << 12 )
            if ( event.key == pygame.K_u ) :
                _Sys._IO.Key |= ( 1 << 13 )
            if ( event.key == pygame.K_j ) :
                _Sys._IO.Key |= ( 1 << 14 )
            if ( event.key == pygame.K_m ) :
                _Sys._IO.Key |= ( 1 << 15 )
        # KEYUP
        elif ( event.type == KEYUP ) :
            if ( event.key == pygame.K_b ) :
                _Sys._IO.Key &= ~( 1 << 0 )
            if ( event.key == pygame.K_4 ) :
                _Sys._IO.Key &= ~( 1 << 1 )
            if ( event.key == pygame.K_5 ) :
                _Sys._IO.Key &= ~( 1 << 2 )
            if ( event.key == pygame.K_6 ) :
                _Sys._IO.Key &= ~( 1 << 3 )
            if ( event.key == pygame.K_r ) :
                _Sys._IO.Key &= ~( 1 << 4 )
            if ( event.key == pygame.K_t ) :
                _Sys._IO.Key &= ~( 1 << 5 )
            if ( event.key == pygame.K_y ) :
                _Sys._IO.Key &= ~( 1 << 6 )
            if ( event.key == pygame.K_f ) :
                _Sys._IO.Key &= ~( 1 << 7 )
            if ( event.key == pygame.K_g ) :
                _Sys._IO.Key &= ~( 1 << 8 )
            if ( event.key == pygame.K_h ) :
                _Sys._IO.Key &= ~( 1 << 9 )
            if ( event.key == pygame.K_v ) :
                _Sys._IO.Key &= ~( 1 << 10 )
            if ( event.key == pygame.K_n ) :
                _Sys._IO.Key &= ~( 1 << 11 )
            if ( event.key == pygame.K_7 ) :
                _Sys._IO.Key &= ~( 1 << 12 )
            if ( event.key == pygame.K_u ) :
                _Sys._IO.Key &= ~( 1 << 13 )
            if ( event.key == pygame.K_j ) :
                _Sys._IO.Key &= ~( 1 << 14 )
            if ( event.key == pygame.K_m ) :
                _Sys._IO.Key &= ~( 1 << 15 )

while True: 
    input( pygame.event.get() ) 
