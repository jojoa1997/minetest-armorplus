#! /usr/bin/env python

import zlib
import os
import sys
import array
import cStringIO
from PIL import Image, ImageDraw, ImageColor

enable_moreores = True;
enable_gloopores = True;
enable_snow = True;
enable_powerplant = True;

parts = {
    "helmet": ((32, 0, 32, 16),),
    "chest": ((16, 16, 24, 16),
              (40, 20, 16, 4),
              (44, 16, 4, 4),
             ),
    "boots": ((0, 16, 16, 16),),
    "shield": ((40, 24, 16, 8),),
};

items = ( "helmet", "chest", "boots", "shield" );

materials = {
    ### default ###
    "wood":     ((  0,  96,   0, 255),
                 (  0, 128,   0, 255),
                 (  0, 160,   0, 255),
                ),
    "steel":    ((160, 160, 160, 255),
                 (192, 192, 192, 255),
                 (224, 224, 224, 255),
                ),
    "mese":     ((  0,   0,   0, 255),
                 (192, 192,   0, 255),
                 (255, 255,   0, 255),
                ),
    "fire":     ((255, 255,   0, 255),
                 (224,   0,   0, 255),
                 (255, 140,   0, 255),
                ),
    "water":    ((255, 255, 255, 255),
                 (224,   0, 224, 255),
                 (128, 128, 255, 255),
                ),
    # OMG! H4xx!
    "air":      ((192, 192, 192, 160),
                 (224, 224, 224, 160),
                 (255, 255, 255, 160),
                ),
};

def merge ( d ):
    for key in d:
        materials[key] = d[key];
    #end
#end

if (enable_moreores):
    ### moreores ###
    merge({
        "copper":   ((176, 128,   0, 255),
                     (184, 160,   0, 255),
                     (192, 192,   0, 255),
                    ),
        "bronze":   ((208, 128,   0, 255),
                     (216, 160,   0, 255),
                     (224, 192,   0, 255),
                    ),
        "silver":   ((176, 176, 176, 255),
                     (200, 200, 200, 255),
                     (224, 224, 224, 255),
                    ),
        "gold":     ((160, 160,   0, 255),
                     (192, 192,   0, 255),
                     (255, 255,   0, 255),
                    ),
        #"gold":     ((208, 168,   0, 255),
        #             (216, 184,   0, 255),
        #             (224, 200,   0, 255),
        #            ),
        "mithril":  ((  0,   0, 160, 255),
                     (  0,   0, 186, 255),
                     (  0,   0, 192, 255),
                    ),
    });
#end

if (enable_gloopores):
    ### gloopores ###
    merge({
        "kalite":   ((120,   0,   0, 255),
                     (180,   0,   0, 255),
                     (240,   0,   0, 255),
                    ),
        "akalin":   ((120, 120, 255, 255),
                     (180, 180, 255, 255),
                     (240, 240, 255, 255),
                    ),
        "alatro":   ((100,   0, 160, 255),
                     (100,   0, 186, 255),
                     (100,   0, 192, 255),
                    ),
        "arol":     ((120, 120,   0, 255),
                     (180, 180,   0, 255),
                     (240, 240,   0, 255),
                    ),
        "talinite": ((255, 255, 255, 255),
                     (180, 180, 180, 255),
                     (255, 255, 255, 255),
                    ),
    });
#end

if (enable_snow):
    merge({
        "snow":     ((160, 160, 255, 255),
                     (200, 200, 255, 255),
                     (240, 240, 255, 255),
                    ),
        "ice":      ((140, 140, 220, 255),
                     (180, 180, 230, 255),
                     (220, 220, 240, 255),
                    ),
    });
#end

img = Image.open("armor.png");

colors = (
    (160, 160, 160, 255),
    (192, 192, 192, 255),
    (224, 224, 224, 255),
);

unmatched_colors = [ ];

def repl_colors ( pix, size, mat ):
    for i in range(len(colors)):
        src = colors[i];
        dst = materials[mat][i];
        if (src == dst): continue;
        for y in range(size[1]):
            for x in range(size[0]):
                c = pix[(x, y)];
                if (c[3] == 0): continue;
                if ((not (c in colors)) and (not (c in unmatched_colors))):
                    print("Unmatched color: %s" % repr(c));
                    unmatched_colors.append(c);
                #end
                if (c == src): pix[(x, y)] = dst;
            #end
        #end
    #end
#end

pix = img.load();

def blit ( p1, p2, sx, sy, dx, dy, w, h ):
    for y in range(h):
        for x in range(w):
            p2[(dx+x, dy+y)] = p1[(sx+x, sy+y)];
        #end
    #end
#end

for mat in materials:
    i = 0;
    for part in parts:
        tmpimg = Image.new("RGBA", (64, 32), (0, 0, 0, 0));
        tmppix = tmpimg.load();
        for area in parts[part]:
            x, y, w, h = area[0], area[1], area[2], area[3];
            blit(pix, tmppix, x, y, x, y, w, h);
        #end
        repl_colors(tmppix, (64, 32), mat);
        tmpimg.save("../textures/armorplus_%s_%s_skin.png" % (mat, part));
        item = items[i];
        tmpimg = Image.new("RGBA", (16, 16), (0, 0, 0, 0));
        tmppix = tmpimg.load();
        blit(pix, tmppix, i * 16, 32, 0, 0, 16, 16);
        repl_colors(tmppix, (16, 16), mat);
        tmpimg.save("../textures/armorplus_%s_%s.png" % (mat, item));
        i += 1;
    #end
#end
