
Visual Armor Mod for Minetest
Copyright (C) 2013 Diego Martínez <lkaezadl3@gmail.com>

This is more of a proof of concept than an actual mod. Some more work needs
 to be done.

Someone (I forgot who) made a "3D Armor" mod. I take a different approach here.
Instead of attaching an entity to a player (or something like that), I use the
 texture transformations (actually, overlaying) to blend several player
 textures together: First the "base" player texture, then the boots,
 chestplate, and finally the helmet.

This currently requires 3 different player textures for each "material". Since
 I planned originally to modify cornernote's armor mod, support is provided for
 wood, steel, and MESE gear.

This mod requires the armor mod (which in turn requires inventory_plus).
Change your gear in the Armor UI, and after a moment (approx 1 second) the
 player texture will be updated.

KNOWN BUGS/ISSUES/WHATEVER
--------------------------
- This only supports the default character.png; support for skin switchers
   (like Zeg9's) is planned.
- Armor textures and player textures must be the same dimensions. If this is
   not the case, the texture will not be overlaid correctly.
- Media downloads may get big due to the fact that lots of big textures must
   be transferred to the client (this is only the first time the images are
   transferred, of course).
