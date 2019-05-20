'''
University of Latvia Faculty of Computing Qualification paper:
Implementation of the board game "Scrabble"

tile.py:
Contains the class modelling game tiles.

Author:         Matīss Apinis (ma17058)
Date created:   2019/04/28
Date edited:    2019/04/29
'''

'''
To-do for tile.py:
1) Make draw_tile(...) primary in rack.py rectangle drawing.
'''

# Libraries:
import pygame as pg

# Local files:
import board
import rack

class Tile:
    COLOR_TILE_BORDER = (100, 100, 100)
    COLOR_TILE_AREA = (230, 230, 230)

    COLOR_TILE_BORDER_UNCLICKED = (100, 100, 100)
    COLOR_TILE_BORDER_CLICKED = (70, 70, 70)

    COLOR_TILE_AREA_UNCLICKED = (230, 230, 230)
    COLOR_TILE_AREA_CLICKED = (200, 200, 200)

    pg.font.init()

    NAME_FONT_LETTER = 'liberationsans'
    NAME_FONT_VALUE = 'liberationsans'

    SIZE_FONT_LETTER = 72
    SIZE_FONT_VALUE = 6

    FONT_LETTER = pg.font.SysFont(NAME_FONT_LETTER, SIZE_FONT_VALUE)
    FONT_VALUE = pg.font.SysFont(NAME_FONT_VALUE, SIZE_FONT_VALUE)

    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
        self.color_area = Tile.COLOR_TILE_AREA_UNCLICKED

    def is_tile_clicked(self, tile_clicked=False):
        if tile_clicked:
            self.color_area = Tile.COLOR_TILE_AREA_CLICKED
        else:
            self.color_area = Tile.COLOR_TILE_AREA_UNCLICKED

    def is_tile_blank(self):
        return self.letter == '' and self.value == 0

    ## TBC:
    def draw_tile(self, DISPLAY_SCRABBLE, x_position, y_position):
        pg.draw.rect(DISPLAY_SCRABBLE, Tile.COLOR_TILE_BORDER,
                     (x_position + 2, rack.Rack.DISTANCE_LEFT + 2, board.Board.SIZE_SQUARE_AREA - 3,
                      board.Board.SIZE_SQUARE_AREA - 3))

        pg.draw.rect(DISPLAY_SCRABBLE, Tile.COLOR_TILE_AREA,
                     (x_position + 3, rack.Rack.DISTANCE_LEFT + 3, board.Board.SIZE_SQUARE_AREA - 5,
                      board.Board.SIZE_SQUARE_AREA - 5))

        # Class.FONT_VARIABLE.render(text, antialias, color, background)
        text_letter = Tile.FONT_LETTER.render(self.letter, True, Tile.COLOR_TILE_BORDER, Tile.COLOR_TILE_AREA)
        area_letter = text_letter.get_rect()
        area_letter.center = (x_position + board.Board.SIZE_SQUARE_AREA / 2, y_position + board.Board.SIZE_SQUARE_AREA / 2)
        DISPLAY_SCRABBLE.blit(text_letter, area_letter)

        text_value = Tile.FONT_VALUE.render(str(self.value), True, Tile.COLOR_TILE_BORDER, Tile.COLOR_TILE_AREA)
        area_value = text_letter.get_rect()
        area_value.center = (x_position + board.Board.SIZE_SQUARE_AREA - 3, y_position + board.Board.SIZE_SQUARE_AREA/3 - 3)
        DISPLAY_SCRABBLE.blit(text_value, area_value)

        print(self.letter, self.value)

        ''' From rack.py:
        for i in range(Rack.DIMENSION_RACK):
            x_position = Rack.DISTANCE_TOP + i * (board.Board.SIZE_SQUARE_AREA + board.Board.SIZE_SQUARE_BORDER + board.Board.SIZE_SQUARE_GAP)

            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_BORDER,
                         (x_position + 2, Rack.DISTANCE_LEFT + 2, board.Board.SIZE_SQUARE_AREA - 3, board.Board.SIZE_SQUARE_AREA - 3))

            pg.draw.rect(DISPLAY_SCRABBLE, tile.Tile.COLOR_TILE_AREA,
                         (x_position + 3, Rack.DISTANCE_LEFT + 3, board.Board.SIZE_SQUARE_AREA - 5, board.Board.SIZE_SQUARE_AREA - 5))
        '''

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