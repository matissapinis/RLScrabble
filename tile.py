'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

tile.py:
Contains the class modelling game tiles.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/05/28
'''

# Libraries:
import pygame as pg

class Tile:
	COLOR_TILE_BORDER = (100, 100, 100)
	COLOR_TILE_AREA = (230, 230, 230)

	TILE_OUTLINE = (55, 46, 40)
	TILE_BLANK = (110, 92, 80)
	TILE_HIGHLIGHT = (100, 100, 255)
	TILE_COLOR = (220, 185, 167)
	TILE_FLASH = (200, 200, 255)
	PULSE_DURATION = 1.5
	
	SQUARE_SIZE = 48 # 32
	SQUARE_BORDER = 4

	'''
	Initializes members of the class which depend on pg.init() having already been called.
	'''
	@staticmethod
	def initialize():
		Tile.LETTER_FONT = pg.font.SysFont('bahnschrift', 28)
		Tile.VALUE_FONT = pg.font.SysFont('bahnschrift', 12)

	'''
	Initializes a new tile with a letter and its value.
	'''
	def __init__(self, letter, value):
		self.letter = letter
		self.value = value

		self.locked = False

	def is_tile_blank(self):
		return self.letter == ' ' and self.value == 0

	'''
	Redraws only if the tile is animating.
	'''	
	def draw_animated(self, left, y_position, DISPLAY_SCRABBLE, highlight=False):
		self.draw_tile(left, y_position, DISPLAY_SCRABBLE, highlight)
		
	'''
	Draws the tile on the screen.
	'''
	def draw_tile(self, x_position, y_position, DISPLAY_SCRABBLE, highlight=False):
		if highlight:
			pg.draw.rect(DISPLAY_SCRABBLE, Tile.TILE_HIGHLIGHT, (x_position, y_position, Tile.SQUARE_SIZE, Tile.SQUARE_SIZE))
		else:
			pg.draw.rect(DISPLAY_SCRABBLE, Tile.COLOR_TILE_BORDER, (x_position + 1, y_position + 1, Tile.SQUARE_SIZE - 2, Tile.SQUARE_SIZE - 2))
			
		back_color = Tile.COLOR_TILE_AREA
		pg.draw.rect(DISPLAY_SCRABBLE, back_color, (x_position + 2, y_position + 2, Tile.SQUARE_SIZE - 4, Tile.SQUARE_SIZE - 4))
		
		if not self.is_tile_blank():
			# Display the letter of the tile:
			letter_text = Tile.LETTER_FONT.render(self.letter, True, (50, 50, 50))
			letter_area = letter_text.get_rect()
			letter_area.center = (x_position + Tile.SQUARE_SIZE/2, y_position + Tile.SQUARE_SIZE/2)
			DISPLAY_SCRABBLE.blit(letter_text, letter_area)
		
			# Display the value of the tile:
			value_text = Tile.VALUE_FONT.render(str(self.value), True, (50, 50, 50))
			value_area = value_text.get_rect()
			value_area.center = (x_position + Tile.SQUARE_SIZE/2 + Tile.SQUARE_SIZE/3, y_position + Tile.SQUARE_SIZE/2 + Tile.SQUARE_SIZE/3)
			DISPLAY_SCRABBLE.blit(value_text, value_area)
		else:
			# Display the letter of the tile for blanks:
			letter_text = Tile.LETTER_FONT.render(self.letter, True, (50, 50, 50))
			letter_area = letter_text.get_rect()
			letter_area.center = (x_position + Tile.SQUARE_SIZE/2 - 3, y_position + Tile.SQUARE_SIZE/2)
			DISPLAY_SCRABBLE.blit(letter_text, letter_area)

'''
Fonts available on my system via pg.font.get_fonts():
['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms',
'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia',
'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans',
'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhengheimicrosoftjhengheiui',
'microsoftjhengheimicrosoftjhengheiuibold', 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue',
'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui',
'microsoftyaheimicrosoftyaheiuibold', 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti',
'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli',
'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint',
'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight',
'segoeuisymbol', 'simsunnsimsun', 'simsunextb',
'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner',
'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold',
'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic',
'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen',
'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings',
'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular',
'yugothicregularyugothicuisemilight', 'holomdl2assets', 'arialms', 'century', 'wingdings2', 'wingdings3',
'tempussansitc', 'pristina', 'papyrus', 'mistral', 'lucidahandwriting', 'kristenitc', 'juiceitc', 'frenchscript',
'freestylescript', 'bradleyhanditc', 'msoutlook', 'bookantiqua', 'garamond', 'monotypecorsiva', 'centurygothic',
'algerian', 'baskervilleoldface', 'bauhaus93', 'bell', 'berlinsansfb', 'bernardcondensed',
'bodonipostercompressed', 'britannic', 'broadway', 'brushscript', 'californianfb', 'centaur', 'chiller',
'colonna', 'cooperblack', 'footlight', 'harlowsolid', 'harrington', 'hightowertext', 'jokerman', 'kunstlerscript',
'lucidabright', 'lucidacalligraphy', 'lucidafaxregular', 'magneto', 'maturascriptcapitals', 'modernno20',
'niagaraengraved', 'niagarasolid', 'oldenglishtext', 'onyx', 'parchment', 'playbill', 'poorrichard', 'ravie',
'informalroman', 'showcardgothic', 'snapitc', 'stencil', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'widelatin',
'twcen', 'twcencondensed', 'script', 'rockwellextra', 'rockwellcondensed', 'rockwell', 'rage', 'perpetuatitling',
'perpetua', 'palacescript', 'ocraextended', 'maiandragd', 'lucidasanstypewriterregular', 'lucidasansregular',
'imprintshadow', 'haettenschweiler', 'goudystout', 'goudyoldstyle', 'gloucesterextracondensed',
'gillsansultracondensed', 'gillsansultra', 'gillsanscondensed', 'gillsans', 'gillsansextcondensed', 'gigi',
'franklingothicmediumcond', 'franklingothicheavy', 'franklingothicdemicond', 'franklingothicdemi',
'franklingothicbook', 'forte', 'felixtitling', 'erasmediumitc', 'erasitc', 'erasdemiitc', 'engravers', 'elephant',
'edwardianscriptitc', 'curlz', 'copperplategothic', 'centuryschoolbook', 'castellar', 'calisto',
'bookmanoldstyle', 'bodonicondensed', 'bodoniblack', 'bodoni', 'blackadderitc', 'arialrounded', 'agencyfb',
'bookshelfsymbol7', 'msreferencesansserif', 'msreferencespecialty', 'berlinsansfbdemi', 'lucidafax',
'twcencondensedextra', 'lucidasanstypewriter', 'lucidasanstypewriteroblique', 'lucidasansroman', 'balloontlextra',
'balloontl', 'belwetl', 'belwetlmedium', 'belwetlcondensed', 'caxtontl', 'caxtontlbook', 'centuryoldstyletl',
'centuryschoolbooktl', 'courier10pitchtl', 'dutchtl', 'empiretl', 'exotic350tl', 'frakturtl', 'futurablacktl',
'futuratl', 'futuratlextrablack', 'futuratlmedium', 'geometric706tlblack', 'geometric706tlmedium',
'gothic821tlcondensed', 'handelgothictl', 'humanist777tl', 'impresstl', 'incised901tlcondensed',
'incised901tlnord', 'latvjurakstiatl', 'latvjurakstibtl', 'libertytl', 'newsgothictl', 'newsgothictlcondensed',
'originalgaramondtl', 'posterbodonitl', 'revuetl', 'ribbon131tl', 'staccato555tl', 'swisstl', 'umbratl',
'universityromantl', 'vagroundedtl', 'zapfcalligraphic801tl', 'acaslonproboldopentype',
'acaslonprobolditalicopentype', 'acaslonproitalicopentype', 'acaslonproregularopentype',
'acaslonprosemiboldopentype', 'acaslonprosemibolditalicopentype', 'adobefangsongstdregularopentype',
'adobefanheitistdboldopentype', 'adobegothicstdboldopentype', 'adobeheitistdregularopentype',
'adobekaitistdregularopentype', 'adobenaskhmediumopentype', 'agaramondproboldopentype',
'agaramondprobolditalicopentype', 'agaramondproitalicopentype', 'agaramondproregularopentype',
'birchstdopentype', 'blackoakstdopentype', 'brushscriptstdopentype', 'chaparralproboldopentype',
'chaparralprobolditopentype', 'chaparralproitalicopentype', 'chaparralprolightitopentype',
'chaparralproregularopentype', 'charlemagnestdboldopentype', 'cooperblackstditalicopentype',
'cooperblackstdopentype', 'giddyupstdopentype', 'hobostdopentype', 'kozgoproboldopentype',
'kozgoproextralightopentype', 'kozgoproheavyopentype', 'kozgoprolightopentype', 'kozgopromediumopentype',
'kozgoproregularopentype', 'kozminproboldopentype', 'kozminproextralightopentype', 'kozminproheavyopentype',
'kozminprolightopentype', 'kozminpromediumopentype', 'kozminproregularopentype', 'lithosproblackopentype',
'lithosproregularopentype', 'mesquitestdopentype', 'minionproboldcnopentype', 'minionproboldcnitopentype',
'minionpromediumopentype', 'minionpromediumitopentype', 'minionprosemiboldopentype',
'minionprosemibolditopentype', 'myriadarabicopentype', 'nuevastdboldopentype', 'nuevastdboldcondopentype',
'nuevastdboldconditalicopentype', 'nuevastdcondopentype', 'nuevastdconditalicopentype', 'nuevastditalicopentype',
'ocrastdopentype', 'oratorstdslantedopentype', 'oratorstdopentype', 'poplarstdopentype',
'prestigeelitestdbdopentype', 'rosewoodstdregularopentype', 'stencilstdopentype', 'tektonproboldopentype',
'tektonproboldcondopentype', 'tektonproboldextopentype', 'tektonproboldoblopentype', 'trajanproboldopentype',
'trajanproregularopentype', 'adobearabicboldopentype', 'adobearabicbolditalicopentype',
'adobearabicitalicopentype', 'adobearabicregularopentype', 'adobedevanagariboldopentype',
'adobedevanagaribolditalicopentype', 'adobedevanagariitalicopentype', 'adobedevanagariregularopentype',
'adobehebrewboldopentype', 'adobehebrewbolditalicopentype', 'adobehebrewitalicopentype',
'adobehebrewregularopentype', 'adobemingstdlightopentype', 'adobemyungjostdmediumopentype',
'adobesongstdlightopentype', 'kozgopr6nboldopentype', 'kozgopr6nextralightopentype', 'kozgopr6nheavyopentype',
'kozgopr6nlightopentype', 'kozgopr6nmediumopentype', 'kozgopr6nregularopentype', 'kozminpr6nboldopentype',
'kozminpr6nextralightopentype', 'kozminpr6nheavyopentype', 'kozminpr6nlightopentype', 'kozminpr6nmediumopentype',
'kozminpr6nregularopentype', 'lettergothicstdboldopentype', 'lettergothicstdboldslantedopentype',
'lettergothicstdslantedopentype', 'lettergothicstdopentype', 'minionproboldopentype', 'minionprobolditopentype',
'minionproitopentype', 'minionproregularopentype', 'myriadhebrewopentype', 'myriadproboldopentype',
'myriadproboldcondopentype', 'myriadproboldconditopentype', 'myriadprobolditopentype', 'myriadprocondopentype',
'myriadproconditopentype', 'myriadproitopentype', 'myriadproregularopentype', 'myriadprosemiboldopentype',
'myriadprosemibolditopentype', 'sfnsdisplay', 'sfuidisplayregular', 'helveticanormal', 'helveticalightnormal',
'sfnsdisplaythin', 'sfnsdisplayultralight', 'sourcesansproblack', 'sourcesanspro', 'sourcesansproextralight',
'sourcesansprosemibold', 'raleway', 'ralewaymedium', 'ralewaysemibold', 'ralewaythin', 'ralewayblack',
'ralewayextrabold', 'ralewayextralight', 'robotoslab', 'robotoslabregular', 'robotoslabthin', 'cmuconcrete',
'cmuconcreteroman', 'cmuserifroman', 'cmusansserifoblique', 'cmuserifextraromanslanted',
'cmusansserifboldoblique', 'cmusansserifmedium', 'cmusansserifdemicondenseddemicondensed', 'cmusansserif',
cmutypewritertext', 'cmuserif', 'cmutypewritertextregular', 'cmutypewritertextbolditalic',
'cmuserifuprightuprightitalic', 'cmutypewritertextvariablewidth', 'cmutypewritertextvariablewidthmedium',
'cmuserifbolditalic', 'cmuserifextraboldslanted', 'cmubrightoblique', 'cmubrightroman',
'cmubrightsemiboldoblique', 'cmubrightsemibold', 'cmutypewritertextlightoblique', 'cmuclassicalserif',
cmuconcretebolditalic', 'extra', 'dandeleonvintagedemo', 'childrenofthestarlight', 'raphlanokfuture',
'liberationsans']
'''