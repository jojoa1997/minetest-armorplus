
local textures = {
    helmet = { none=""; };
    boots = { none=""; };
    shield = { none=""; };
    chest = { none=""; };
};

local materials = { "wood", "steel", "mese" };
local parts = { "chest", "helmet", "boots", "shield" };

for _, mat in ipairs(materials) do
    for _, part in ipairs(parts) do
        textures[part]["armor:"..mat.."_"..part] = "^armorplus_"..mat.."_"..part.."_skin.png";
    end
end

armorplus = { };

armorplus.add_material = function ( modname, matname )
    for _, t in ipairs(parts) do
        local itemname = modname..":"..matname.."_"..t;
        local texname = modname.."_"..matname.."_"..t.."_skin.png";
        textures[t][itemname] = "^"..texname;
    end
end

dofile(minetest.get_modpath("armorplus").."/armors.lua");

local function get_item ( inv, list )
    local stack = inv:get_stack("armor_"..list, 1);
    return ((not stack:is_empty()) and stack:get_name()) or "none";
end

local player_armor = { };

local function update_player_texture ( player )
    local name = player:get_player_name();
    local inv = minetest.get_inventory({type="detached"; name=name.."_armor"});
    if (not inv) then return; end
    local armor = player_armor[name];
    local hname = get_item(inv, "helmet");
    local helmet = textures.helmet[hname] or "";
    local cname = get_item(inv, "chest");
    local chest = textures.chest[cname] or "";
    local bname = get_item(inv, "boots");
    local boots = textures.boots[bname] or "";
    local sname = get_item(inv, "shield");
    local shield = textures.shield[sname] or "";
    if ((hname ~= armor.helmet) or (cname ~= armor.chest)
     or (bname ~= armor.boots) or (sname ~= armor.shield)) then
        player:set_properties({
            visual = "mesh",
            textures = { "armorplus_character.png"..boots..chest..helmet..shield },
            visual_size = {x=1, y=1},
        });
        player_armor[name] = {
            helmet = hname;
            chest = cname;
            boots = bname;
            shield = sname;
        };
    end
end

minetest.register_on_joinplayer(function(player)
    player_armor[player:get_player_name()] = {
        helmet = "none";
        chest = "none";
        boots = "none";
        shield = "none";
    };
    update_player_texture(player);
end)

local function updater ( )
    for _, player in ipairs(minetest.get_connected_players()) do
        update_player_texture(player);
    end
    minetest.after(1, updater);
end
minetest.after(1, updater);
