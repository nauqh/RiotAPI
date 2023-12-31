"""Embed factory

This module creates hikari embed for displaying on Discord.

"""

import hikari


def patch_emb(version: str, url: str) -> hikari.Embed:
    embed = (
        hikari.Embed(
            title=f"📝 Patch {version.replace('-', '.')} notes",
            description="**Author**: `Riot Riru`",
            colour="#9bf6ff",
            url=url
        )
        .add_field(
            "View patch details",
            url
        )
        .set_image("./assets/patch.jpg")
        .set_thumbnail("https://i.imgur.com/shAjLsZ.png")
    )
    return embed


def rotation_emb(names: list) -> hikari.Embed:
    embed = (
        hikari.Embed(
            title=f"📝 Free Rotation",
            description="This week's free rotation is:",
            colour="#9bf6ff"
        )
        .add_field(
            "`Champions`",
            '\n'.join(['**' + name + '**' for name in names[:10]]),
            inline=True
        )
        .add_field(
            "`Champions`",
            '\n'.join(['**' + name + '**' for name in names[10:20]]),
            inline=True
        )
        .set_thumbnail("https://i.imgur.com/shAjLsZ.png")
    )
    return embed


def display_champs(champs: list) -> str:
    display = ""
    for champ in champs:
        display += f"**{champ['name']}**: {champ['kda']} - {champ['winrate']} WR\n"

    return display


def profile_emb(profile: dict, champs: dict, rank: dict) -> hikari.Embed:
    if not rank:
        text = "**Unranked**"
    else:
        text = f"""**{rank['tier']}**
            {rank['lp']} / {rank['win_lose'][:-3]}  
            Winrate {rank['win_lose'][-3:]}
            """
    embed = (
        hikari.Embed(
            title=f"✨ {profile['name']}",
            description="You asked for it, you got it",
            colour="#9bf6ff",
            url=profile['url']
        )
        .set_thumbnail(profile['avatar'])
        .add_field(
            "📑 Level/Region",
            f"{profile['level']} / {profile['region'].upper()}",
            inline=False
        )
        .add_field(
            "🗂️ Rank",
            text,
            inline=True
        )
        .add_field(
            "🏆 Champions",
            display_champs(champs),
            inline=True
        )
        .add_field(
            "🕹️ Live game",
            "Not curently playing",
            inline=False
        )

    )
    return embed
