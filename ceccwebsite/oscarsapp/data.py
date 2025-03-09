oscurls = ['chart', 'front', 'loadballot']
umslurls = ['uchart', 'ufront', 'uloadballot']

n = 'name'; u = 'url'; s = 'sub'

amf = 'American Fiction'  ; anf = 'Anatomy of a Fall' ; brb = 'Barbie'
clp = 'The Color Purple'  ; cre = 'The Creator'       ; hld = 'The Holdovers'
kfm = 'Killers of the Flower Moon'                    ; mst = 'Maestro'
mid = 'Mission: Impossible - Dead Reckoning Part One' ; nap = 'Napoleon'
nyd = 'Nyad'              ; opp = 'Oppenheimer'       ; psl = 'Past Lives'
prt = 'Poor Things'       ; rst = 'Rustin'
sos = 'Society of the Snow'
zni = 'The Zone of Interest'

ano = 'Anora'

noms = [
    {'header': 'BEST PICTURE (3pts)',
    'shortname': 'best_pic',
    'nominees': [
        {n: ano, u: 'ano'},
        {n: anf, u: 'anf'},
        {n: brb, u: 'brb'},
        {n: hld, u: 'hld'},
        {n: kfm, u: 'kfm'},
        {n: mst, u: 'mst'},
        {n: opp, u: 'opp'},
        {n: psl, u: 'psl'},
        {n: prt, u: 'prt'},
        {n: zni, u: 'zni'}
        ]
    },
    {'header': 'BEST ACTOR (3pts)',
    'shortname': 'actor',
    'nominees': [
        {n: 'Bradley Cooper', u: 'cooper',   s: mst},
        {n: 'Colman Domingo', u: 'domingo',  s: rst},
        {n: 'Paul Giamatti',  u: 'giamatti', s: hld},
        {n: 'Cillian Murphy', u: 'murphy',   s: opp},
        {n: 'Jeffrey Wright', u: 'wright',   s: amf}
        ]
    },
    {'header': 'BEST ACTRESS (3pts)',
    'shortname': 'actress',
    'nominees': [
        {n: 'Annette Bening', u: 'bening',    s: nyd},
        {n: 'Lily Gladstone', u: 'gladstone', s: kfm},
        {n: 'Sandra Huller',  u: 'huller',    s: anf},
        {n: 'Carey Mulligan', u: 'mulligan',  s: mst},
        {n: 'Emma Stone',     u: 'stone',     s: prt}
        ]
    },
    {'header': 'BEST SUPPORTING ACTOR (2pts)',
    'shortname': 'sup_actor',
    'nominees': [
        {n: 'Sterling K. Brown', u: 'brown',   s: amf},
        {n: 'Robert De Niro',    u: 'de_niro', s: kfm},
        {n: 'Robert Downey Jr.', u: 'downey',  s: opp},
        {n: 'Ryan Gosling',      u: 'gosling', s: brb},
        {n: 'Mark Ruffalo',      u: 'ruffalo', s: prt}
        ]
    },
    {'header': 'BEST SUPPORTING ACTRESS (2pts)',
    'shortname': 'sup_actress',
    'nominees': [
        {n: 'Emily Blunt',          u: 'blunt',    s: opp},
        {n: 'Danielle Brooks',      u: 'brooks',   s: clp},
        {n: 'America Ferrera',      u: 'ferrera',  s: brb},
        {n: 'Jody Foster',          u: 'foster',   s: nyd},
        {n: "Da'Vine Joy Randolph", u: 'randolph', s: hld}
        ]
    },
    {'header': 'BEST ANIMATED FEATURE (1pt)',
    'shortname': 'animated',
    'nominees': [
        {n: 'The Boy and the Heron',               u: 'boh', s: 'Hayao Miyazaki and Toshio Suzuki'},
        {n: 'Elemental',                           u: 'ele', s: 'Peter Sohn and Denise Ream'},
        {n: 'Nimona',                              u: 'nmn', s: 'Nick Bruno, Troy Quane, Karen Ryan and Julie Zackary'},
        {n: 'Spider-Man: Across the Spider-Verse', u: 'sas', s: 'Kemp Powers, Justin K. Thompson, Phil Lord, Christopher Miller and Amy Pascal'},
        {n: 'Robot Dreams',                        u: 'rod', s: 'Pablo Berger, Ibon Cormenzana, Ignasi Estapé and Sandra Tapia Díaz'}
        ]
    },
    {'header': 'BEST CINEMATOGRAPHY (1pt)',
    'shortname': 'cinematography',
    'nominees': [
        {n: 'El Conde', u: 'elc', s: 'Edward Lachman'},
        {n: kfm,        u: 'kfm', s: 'Rodrigo Prieto'},
        {n: mst,        u: 'mst', s: 'Matthew Libatique'},
        {n: opp,        u: 'opp', s: 'Hoyte van Hoytema'},
        {n: prt,        u: 'prt', s: 'Robbie Ryan'}
        ]
    },
    {'header': 'BEST COSTUME DESIGN (1pt)',
    'shortname': 'costume',
    'nominees': [
        {n: brb, u: 'brb', s: 'Jacqueline Durran'},
        {n: kfm, u: 'kfm', s: 'Jacqueline West'},
        {n: nap, u: 'nap', s: 'Janty Yates and Dave Crossman'},
        {n: opp, u: 'opp', s: 'Ellen Mirojnick'},
        {n: prt, u: 'prt', s: 'Holly Waddington'}
        ]
    },
    {'header': 'BEST DIRECTING (2pts)',
    'shortname': 'directing',
    'nominees': [
        {n: zni, u: 'zni', s: 'Jonathan Glazer'},
        {n: prt, u: 'prt', s: 'Yorgos Lanthimos'},
        {n: opp, u: 'opp', s: 'Christopher Nolan'},
        {n: kfm, u: 'kfm', s: 'Martin Scorsese'},
        {n: anf, u: 'anf', s: 'Justine Triet'}
        ]
    },
    {'header': 'BEST DOCUMENTARY - FEATURE (1pt)',
    'shortname': 'documentary',
    'nominees': [
        {n: "Bobi Wine: The People's President", u: 'bwp', s: 'Moses Bwayo, Christopher Sharp and John Battsek'},
        {n: 'The Eternal Memory',                u: 'etm', s: 'Maite Alberdi'},
        {n: 'Four Daughters',                    u: 'frd', s: 'Kaouther Ben Hania and Nadim Cheikhrouha'},
        {n: 'To Kill a Tiger',                   u: 'klt', s: 'Nisha Pahuja, Cornelia Principe and David Oppenheim'},
        {n: '20 Days in Mariupol',               u: 'dym', s: 'Mstyslav Chernov, Michelle Mizner and Raney Aronson-Rath'}
        ]
    },
    {'header': 'BEST DOCUMENTARY - SHORT (1pt)',
    'shortname': 'doc_short',
    'nominees': [
        {n: 'The ABCs of Book Banning',  u: 'abb', s: 'Sheila Nevins and Trish Adlesic'},
        {n: 'The Barber of Little Rock', u: 'blr', s: 'John Hoffman and Christine Turner'},
        {n: 'Island in Between',         u: 'isb', s: 'S. Leo Chiang and Jean Tsien'},
        {n: 'The Last Repair Shop',      u: 'lrs', s: 'Ben Proudfoot and Kris Bowers'},
        {n: 'Nai Nai & Wai Po',          u: 'nnn', s: 'Sean Wang and Sam Davis'}
        ]
    },
    {'header': 'BEST FILM EDITING (1pt)',
    'shortname': 'editing',
    'nominees': [
        {n: anf, u: 'anf', s: 'Laurent Sénéchal'},
        {n: hld, u: 'hld', s: 'Kevin Tent'},
        {n: kfm, u: 'kfm', s: 'Thelma Schoonmaker'},
        {n: opp, u: 'opp', s: 'Jennifer Lame'},
        {n: prt, u: 'prt', s: 'Yorgos Mavropsaridis'}
        ]
    },
    {'header': 'BEST INTERNATIONAL FEATURE FILM (1pt)',
    'shortname': 'foreign',
    'nominees': [
        {n: 'Io Capitano',          u: 'ioc', s: 'Italy'},
        {n: 'Perfect Days',         u: 'prd', s: 'Japan'},
        {n: 'Society of the Snow',  u: 'sos', s: 'Spain'},
        {n: "The Teachers' Lounge", u: 'tel', s: 'Germany'},
        {n: zni,                    u: 'zni', s: 'United Kingdom'}
        ]
    },
    {'header': 'BEST MAKEUP AND HAIRSTYLING (1pt)',
    'shortname': 'makeup',
    'nominees': [
        {n: 'Golda', u: 'gld', s: 'Karen Hartley Thomas, Suzi Battersby and Ashra Kelly-Blue'},
        {n: mst,     u: 'mst', s: 'Kazu Hiro, Kay Georgiou and Lori McCoy-Bell'},
        {n: opp,     u: 'opp', s: 'Luisa Abel'},
        {n: prt,     u: 'prt', s: 'Nadia Stacey, Mark Coulier and Josh Weston'},
        {n: sos,     u: 'sos', s: 'Ana López-Puigcerver, David Martí and Montse Ribé'}
        ]
    },
    {'header': 'BEST ORIGINAL SCORE (1pt)',
    'shortname': 'score',
    'nominees': [
        {n: amf,                                     u: 'amfs', s: 'Laura Karpman'},
        {n: 'Indiana Jones and the Dial of Destiny', u: 'ijds', s: 'John Williams'},
        {n: kfm,                                     u: 'kfms', s: 'Robbie Robertson'},
        {n: opp,                                     u: 'opps', s: 'Ludwig Göransson'},
        {n: prt,                                     u: 'prts', s: 'Jerskin Fendrix'}
        ]
    },
    {'header': 'BEST ORIGINAL SONG (1pt)',
    'shortname': 'song',
    'nominees': [
        {n: 'The Fire Inside',                  u: 'fiis', s: "Flamin' Hot; Music and Lyric by Diane Warren<br><a href='https://www.youtube.com/watch?v=Jv6J_yAp_fw' target='_blank'>Listen Here</a>"},
        {n: "I'm Just Ken" ,                    u: 'ijks', s: "Barbie; Music and Lyric by Mark Ronson and Andrew Wyatt<br><a href='https://www.youtube.com/watch?v=wwux9KiBMjE' target='_blank'>Listen Here</a>"},
        {n: "It Never Went Away",               u: 'nwas', s: "American Symphony; Music and Lyric by Jon Batiste and Dan Wilson<br><a href='https://www.youtube.com/watch?v=27jnCQYRXLc' target='_blank'>Listen Here</a>"},
        {n: 'Wahzhazhe (A Song For My People)', u: 'kfms', s: "Killers of the Flower Moon; Music and Lyric by Scott George<br><a href='https://www.youtube.com/watch?v=nyWCr1ly4oc' target='_blank'>Listen Here</a>"},
        {n: 'What Was I Made For?',             u: 'thls', s: "Barbie; Music and Lyric by Billie Eilish and Finneas O'Connell<br><a href='https://www.youtube.com/watch?v=cW8VLC9nnTo' target='_blank'>Listen Here</a>"}
        ]
    },
    {'header': 'BEST PRODUCTION DESIGN (1pt)',
    'shortname': 'production',
    'nominees': [
        {n: brb, u: 'brb', s: 'Production Design: Sarah Greenwood; Set Decoration: Katie Spencer'},
        {n: kfm, u: 'kfm', s: 'Production Design: Jack Fisk; Set Decoration: Adam Willis'},
        {n: nap, u: 'nap', s: 'Production Design: Arthur Max; Set Decoration: Elli Griff'},
        {n: opp, u: 'opp', s: 'Production Design: Ruth De Jong; Set Decoration: Claire Kaufman'},
        {n: prt, u: 'prt', s: 'Production Design: James Price and Shona Heath; Set Decoration: Zsuzsa Mihalek'}
        ]
    },
    {'header': 'BEST SHORT FILM - ANIMATED (1pt)',
    'shortname': 'anim_short',
    'nominees': [
        {n: 'Letter to a Pig',                                   u: 'lep', s: 'Tal Kantor and Amit R. Gicelter'},
        {n: 'Ninety-Five Senses',                                u: 'nfs', s: 'Jerusha Hess and Jared Hess'},
        {n: 'Our Uniform',                                       u: 'ouu', s: 'Yegane Moghaddam'},
        {n: 'Pachyderme',                                        u: 'pac', s: 'Stéphanie Clément and Marc Rius'},
        {n: 'War Is Over! Inspired by the Music of John & Yoko', u: 'wio', s: 'Dave Mullins and Brad Booker'}
        ]
    },
    {'header': 'BEST SHORT FILM - LIVE ACTION (1pt)',
    'shortname': 'live_short',
    'nominees': [
        {n: 'The After',                          u: 'aft', s: 'Misan Harriman and Nicky Bentham'},
        {n: 'Invincible',                         u: 'inv', s: 'Vincent René-Lortie and Samuel Caron'},
        {n: 'Knight of Fortune',                  u: 'knf', s: 'Lasse Lyskjær Noer and Christian Norlyk'},
        {n: 'Red, White, and Blue',               u: 'rwb', s: 'Nazrin Choudhury and Sara McFarlane'},
        {n: 'The Wonderful Story of Henry Sugar', u: 'wsh', s: 'Wes Anderson and Steven Rales'}
        ]
    },
    {'header': 'BEST SOUND (1pt)',
    'shortname': 'sound',
    'nominees': [
        {n: cre, u: 'cre', s: 'Ian Voigt, Erik Aadahl, Ethan Van der Ryn, Tom Ozanich and Dean Zupancic'},
        {n: mst, u: 'mst', s: 'Steven A. Morrow, Richard King, Jason Ruder, Tom Ozanich and Dean Zupancic'},
        {n: mid, u: 'mid', s: 'Chris Munro, James H. Mather, Chris Burdon and Mark Taylor'},
        {n: opp, u: 'opp', s: "Willie Burton, Richard King, Gary A. Rizzo and Kevin O'Connell"},
        {n: zni, u: 'zni', s: 'Tarn Willers and Johnnie Burn'}
        ]
    },
    {'header': 'BEST VISUAL EFFECTS (1pt)',
    'shortname': 'fx',
    'nominees': [
        {n: cre,                              u: 'cre', s: 'Jay Cooper, Ian Comley, Andrew Roberts and Neil Corbould'},
        {n: 'Godzilla Minus One',             u: 'gmo', s: 'Takashi Yamazaki, Kiyoko Shibuya, Masaki Takahashi and Tatsuji Nojima'},
        {n: 'Guardians of the Galaxy Vol. 3', u: 'ggv', s: 'Stephane Ceretti, Alexis Wajsbrot, Guy Williams and Theo Bialek'},
        {n: mid,                              u: 'mid', s: 'Alex Wuttke, Simone Coco, Jeff Sutherland and Neil Corbould'},
        {n: nap,                              u: 'nap', s: 'Charley Henley, Luc-Ewen Martin-Fenouillet, Simone Coco and Neil Corbould'}
        ]
    },
    {'header': 'BEST ADAPTED SCREENPLAY (1pt)',
    'shortname': 'adapted_screenplay',
    'nominees': [
        {n: amf, u: 'amf', s: 'Written for the screen by Cord Jefferson'},
        {n: brb, u: 'brb', s: 'Written by Greta Gerwig & Noah Baumbach'},
        {n: opp, u: 'opp', s: 'Written for the screen by Christopher Nolan'},
        {n: prt, u: 'prt', s: 'Screenplay by Tony McNamara'},
        {n: zni, u: 'zni', s: 'Written by Jonathan Glazer'}
        ]
    },
    {'header': 'BEST ORIGINAL SCREENPLAY (1pt)',
    'shortname': 'original_screenplay',
    'nominees': [
        {n: anf,            u: 'anf', s: 'Screenplay - Justine Triet and Arthur Harari'},
        {n: hld,            u: 'hld', s: 'Written by David Hemingson'},
        {n: mst,            u: 'mst', s: 'Written by Bradley Cooper & Josh Singer'},
        {n: 'May December', u: 'myd', s: 'Screenplay by Samy Burch; Story by Samy Burch & Alex Mechanik'},
        {n: psl,            u: 'psl', s: 'Written by Celine Song'}
        ]
    }
]