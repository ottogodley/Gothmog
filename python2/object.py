class Object:
	#Generic object: player, monster, item, stairs etc.
	#always represented by a character on screen
	def __init__(self, x, y, char, colour):
		self.x = x
		self.y = y
		self.char = char
		self.color = color

	def move(self, dx, dy):
		#move by the given amount
		self.x += dx
		self.y += dy

	def draw(self):
		#set the color and then draw the character that represents this object at is pos
		libtcod.console_set_foreground_color(con, self.color)
		libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

	def clear(self):
		#erase the character representation of this object
		libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
