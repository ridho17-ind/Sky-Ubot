from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
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
    typew.pattern_match.group(1)
    await typew.edit("**Afreal Peler☑️**")
    await typew.edit("**Afreal Peler✅**")
    sleep(1)
    await typew.edit("**Anggra Gilaa☑️**")
    await typew.edit("**Anggra Gilaa✅**")
    sleep(2)
    await typew.edit("**Eggyol Depresi☑️**")
    await typew.edit("**Eggyol Depresi✅**")
    sleep(2)
    await typew.edit("**Enggoy Gajelas☑️**")
    await typew.edit("**Enggoy Gajelas✅**")
    sleep(2)
    await typew.edit("**Ica GJM!☑️**")
    await typew.edit("**Ica GJM!✅**")
    sleep(2)
    await typew.edit("**Aldi GJB!☑️**")
    await typew.edit("**Aldi GJB!✅**")
    sleep(2)
    await typew.edit("**Bintang,MengRibet☑️**")
    await typew.edit("**Bintang,MengRibet✅**")
    sleep(2)
    await typew.edit("**Afreal,Mengintil☑️**")
    await typew.edit("**Afreal,Mengintil✅**")
    sleep(3)
    await typew.edit("**CUMA SKYZO YANG BENER!**")

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
