from CPU import *
from PPU import *
from IO import *

class System :

    # Resources
    parent = None
    _RAM = [] 
    _CPU = None
    _PPU = None
    _IO = None
    _CRT = None

    # ------------------------------------------------------------
    #   Initialize Resources
    # ------------------------------------------------------------
    def Init( self, p, FileName ) :

	self.parent = p
	self._CRT = self.parent.display.get_surface()
	
	# Initialize CPU
	self._CPU = CPU()
	self._CPU.CPU_Init( self )

	# Initialize PPU
	self._PPU = PPU()
	self._PPU.PPU_Init( self )

	# Initialize I/O
	self._IO = IO()
	self._IO.IO_Init( self )

	# Initialize RAM
	for _n in range ( 0x800 ) :
	    self._RAM.append( 0x00 )

	# Load ROM image
	if ( self.LoadRom( FileName ) < 0 ) :
	    # Failed
	    return -1

	# Successful
	#print self._RAM
	return 0

    def Run( self ) :

        # Main loop
	while ( 1 ) :
            self._CPU.CPU_Step( 10 )

            # VSYNC occurs per 1/60 second
            if ( self._IO.Delay ) :
                self._IO.Delay -= 1
            if ( self._IO.Sound ) :
                self._IO.Sound -= 1

    # ------------------------------------------------------------
    #   Finalize Resources
    # ------------------------------------------------------------
    def Fin( self ) :
	print self._IO.IO_Fin()
	print self._PPU.PPU_Fin()	
	print self._CPU.CPU_Fin()

    # ------------------------------------------------------------
    #   Load ROM image
    # ------------------------------------------------------------
    def LoadRom( self, FileName ) :
	try:
	    # Open ROM file
	    _fp = open( FileName, 'rb' )

	    # Allocate Memory for ROM Image
	    _n = 0
	    while ( 1 ) :
		_b = _fp.read( 1 )
		if ( _b == "" ) :
		    break
		self._RAM[ _n ] = ord( _b )
		_n += 1

	    # File close
	    _fp.close()

	    # Successful
	    return 0

	except:
	    # Failed
	    return -1

    # ------------------------------------------------------------
    #   Blit
    # ------------------------------------------------------------
    def Blit( self ):
	self.parent.display.flip()

    # ------------------------------------------------------------
    #   Point Set
    # ------------------------------------------------------------
    def pset( self, x, y, c ):
	x += 10
	y += 10
	white = (255, 255, 255)
	black = (0, 0, 0)
	rect = self.parent.Rect(x*3, y*3, 3, 3 )

	# Draw rectangle
	if ( c == 1 ):
	    self.parent.draw.rect( self._CRT, white, rect )
	elif ( c == 0 ):
	    self.parent.draw.rect( self._CRT, black, rect )

# End of System.py

