""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.khelp$")
async def usit(e):
    await e.edit(
        f"      ╔════════════╗\n     ✍️𝘽𝘼𝙉𝙏𝙐𝘼𝙉✍️     \n╚════════════╝ \n"
        f"**Hai Tuan muda {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "═⎆ Pemilik : [🍁𝐊𝐈𝐌🍁](t.me/warga_pati) \n"
        "═⎆ Repo    : [Repo](https://github.com/abdurrohimbontro/Kim-Userbot) \n"
        "═⎆ Instragam : [Instagram ✍️𝐊𝐈𝐌✍️](Instagram.com/Kim_) \n"
        "═⎆ Grup Random : [Grup random](https://t.me/crazy_people345)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"      ╔════════════╗\n  ✍️𝘿𝘼𝙁𝙏𝘼𝙍 𝙑𝘼𝙍𝙎✍️     \n╚════════════╝ \n"
        f"**Disini Daftar Vars Dari Tuan {DEFAULTUSER}:**\n"
        "═⎆ Daftar Vars : [DAFTAR VARS](https://raw.githubusercontent.com/abdurrohimbontro/Kim-Userbot/Kim-Userbot/varshelper.txt)")


CMD_HELP.update(
    {
        "helper": "**✘ Plugin : **`helper`\
        \n\n  •  **Perintah :** `.khelp`\
        \n  •  **Function : **Bantuan Untuk ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️.\
        \n\n  •  **Perintah :** `.vars`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Perintah :** `.repo`\
        \n  •  **Function : **Melihat Repo ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️.\
        \n\n  •  **Perintah :** `.string`\
        \n  •  **Function : **Link untuk mengambil String ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️.\
    "
    }
)
