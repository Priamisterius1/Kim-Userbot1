from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.kims(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.1)
    await typew.edit("`Hai Perkenalkan Namaku 𝐊𝐈𝐌`")
    sleep(2)
    await typew.edit("`umur setiap Tahun tambah`")
    sleep(2)
    await typew.edit("`Tinggal Di pati Jawa tengah Indonesia, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(2)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(2)
    await typew.edit("`karna itu penting`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.creator(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.3)
    await typew.edit("`𝐊𝐈𝐌`")
    sleep(3)
    await typew.edit("`panggil kim aja`")
    sleep(2)
    await typew.edit("`kalo mau kenalan bilang aja`")
# Create by myself @localheart
