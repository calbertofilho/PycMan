class Colors:
	BLACK       =   (  0,   0,   0)
	BLUE        =   ( 13,  64, 216)
	CYAN        =   ( 21, 204, 209)
	DARK_BLUE   =   ( 44,  44, 127)
	DARK_GRAY   =   ( 26,  31,  40)
	GREEN       =   ( 47, 230,  23)
	LIGHT_BLUE  =   ( 59,  85, 162)
	ORANGE      =   (226, 116,  17)
	PURPLE      =   (166,   0, 247)
	RED         =   (232,  18,  18)
	WHITE       =   (255, 255, 255)
	YELLOW      =   (237, 234,   4)

	@classmethod
	def get_colors(cls):
		return [cls.BLACK, cls.BLUE, cls.CYAN, cls.DARK_BLUE, cls.DARK_GRAY, cls.GREEN, cls.LIGHT_BLUE, cls.ORANGE, cls.PURPLE, cls.RED, cls.WHITE, cls.YELLOW]
