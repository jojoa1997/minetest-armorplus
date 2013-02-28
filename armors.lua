
-- Boilerplate to support localized strings if intllib mod is installed.
local S;
if (minetest.get_modpath("intllib")) then
    dofile(minetest.get_modpath("intllib").."/intllib.lua");
    S = intllib.Getter(minetest.get_current_modname());
else
    S = function ( s ) return s; end
end

print("armorplus: Adding extra armors...");

local function regarmor ( name, label, mat, level )
    armor.register_armor("armorplus", name, label, mat, level);
    armorplus.add_material("armorplus", name);
end

-- Intentionally unobtainable by normal means (for admins only).
regarmor("air", S("Air"), "air", 50);

regarmor("fire", S("Fire"), "bucket:bucket_lava", 3);
regarmor("water", S("Water"), "bucket:bucket_water", 3);

if (minetest.get_modpath("moreores")) then
    regarmor("copper", S("Copper"), "moreores:copper_ingot", 1);
    regarmor("bronze", S("Bronze"), "moreores:bronze_ingot", 2);
    regarmor("silver", S("Silver"), "moreores:silver_ingot", 3);
    regarmor("gold", S("Gold"), "moreores:gold_ingot", 4);
    regarmor("mithril", S("Mithril"), "moreores:mithril_ingot", 5);
    print("armorplus: Support for More Ores added!");
end

if (minetest.get_modpath("gloopores")) then
    regarmor("kalite", S("Kalite"), "gloopores:kalite_lump", 1);
    regarmor("akalin", S("Akalin"), "gloopores:akalin_ingot", 1);
    regarmor("alatro", S("Alatro"), "gloopores:alatro_ingot", 2);
    regarmor("arol", S("Arol"), "gloopores:arol_ingot", 2);
    regarmor("talinite", S("Talinite"), "gloopores:talinite_ingot", 2);
    print("armorplus: Support for Gloop Ores added!");
end

if (minetest.get_modpath("snow")) then
    regarmor("snow", S("Snow"), "snow:snow", 1);
    regarmor("ice", S("Ice"), "snow:ice", 2);
    print("armorplus: Support for Snow added!");
end

-- TODO: Support for Obsidian/Obmese
-- TODO: Support for Diamonds

print("armorplus: Extra armors added!");
