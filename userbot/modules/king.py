from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**nginceng**")


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


@register(outgoing=True, pattern='^.mrk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`CUKUP MENARIK SIIIH`")
    sleep(2)
    await typew.edit("`TAPI MAAF GW BELOM TERTARIK`")


# Create by myself @localheart

CMD_HELP.update({
    "Kim":
    "⚡𝘾𝙈𝘿⚡`.king`\
    \nUsage: alive bot.\
    \n\n⚡𝘾𝙈𝘿⚡`.sadboy`\
    \nUsage: hiks\
    \n\n⚡𝘾𝙈𝘿⚡`.punten` ; ⚡𝘾𝙈𝘿⚡`.pantau`\
    \nUsage: cobain aja.\
    \n\n⚡𝘾𝙈𝘿⚡`.mrk`\
    \nUsage: coba aja.\
    \n\n⚡𝘾𝙈𝘿⚡`kosong`\
    \nUsage: tunggu update selanjutnya."
})
