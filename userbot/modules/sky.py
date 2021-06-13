from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Pertama-tama kamu cantik**")
    sleep(2)
    await typew.edit("**Kedua kamu manis**")
    sleep(2)
    await typew.edit("**Dan yang terakhir adalah kamu bukan jodohku**")
    sleep(2)
    await typew.edit("**Mengsedih😭**")
    sleep(2)
    await typew.edit("**Btw Admin Nya Ganteng Ga?**")
    sleep(2)
    await typew.edit("**Hehehehe Nanya Doang**") 
    sleep(2)
    await typew.edit("**Awikwokwokwowok**")
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
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.geez(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(2)
    await typew.edit("**Afreal Stres☑️**")
    await typew.edit("**Afreal Stres✅**")
    sleep(3)
    await typew.edit("**Anggra Gilaa☑️**")
    await typew.edit("**Anggra Gilaa✅**")
    sleep(2)
    await typew.edit("**Abdul Depresi☑️**")
    await typew.edit("**Abdul Depresi✅**")
    sleep(2)
    await typew.edit("**Yunus Gajelas☑️**")
    await typew.edit("**Yunus Gajelas✅**")
    sleep(2)
    await typew.edit("**Eggyol Babi!☑️**")
    await typew.edit("**Eggyol Babi!✅**")
    sleep(2)
    await typew.edit("**Fauza Wibu Gagak!☑️**")
    await typew.edit("**Fauza Wibu Gagak!✅**")
    sleep(2)
    await typew.edit("**Lynxking Tolol!☑️**")
    await typew.edit("**Lynzking Tolol!✅**")
    sleep(2)
    await typew.edit("**Feri,Mengintil!☑️**")
    await typew.edit("**Feri,Mengintil!✅**")
    sleep(2)
    await typew.edit("**CUMA SKYZO YANG BENER😎**")

# Create by myself @localheart

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: misi."
})
