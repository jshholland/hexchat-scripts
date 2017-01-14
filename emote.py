# -*- coding: utf-8 -*-
import hexchat

__module_name__ = 'emote'
__module_version__ = '0.2'
__module_description__ = 'Print Unicode emoticons to IRC'

EMOTES = {
    'SHRUG': u'¯\\_(ツ)_/¯',
    'FLIP': u'(╯°□°）╯︵ ┻━┻',
    'UNFLIP': u'┬──┬ ノ( ゜-゜ノ)',
    'CSI': u'''\
•_•)
( •_•)>⌐■-■
(⌐■_■)''',
    'DISAPPROVE': u'ಠ_ಠ',
}

def fullwidth(s):
    trans = str.maketrans({a: a + 0xff00 - 0x20 for a in range(0x21, 0x7f)})
    return s.translate(trans)

def emote_cb(word, word_eol, emote):
    hexchat.command(u'SAY {}'.format(emote))
    return hexchat.EAT_ALL

def fullwidth_cb(word, word_eol, userdata):
    hexchat.command(u'SAY {}'.format(fullwidth(word_eol[1])))
    return hexchat.EAT_ALL

for name, emote in EMOTES.items():
    hexchat.hook_command(name, emote_cb, emote)

hexchat.hook_command('FULLWIDTH', fullwidth_cb)
