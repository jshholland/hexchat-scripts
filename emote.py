# -*- coding: utf-8 -*-
import hexchat

__module_name__ = 'emote'
__module_version__ = '0.1'
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

def emote_cb(word, word_eol, emote):
    hexchat.command(u'SAY {}'.format(emote))

for name, emote in EMOTES.items():
    hexchat.hook_command(name, emote_cb, emote)
