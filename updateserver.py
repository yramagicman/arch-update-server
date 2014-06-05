#!/usr/bin/python2
import pynotify
import feedparser
import commands
pynotify.init("Basic")
community = feedparser.parse('https://www.archlinux.org/feeds/packages/x86_64/feed/')
core = feedparser.parse('https://www.archlinux.org/feeds/packages/x86_64/core/')
extra = feedparser.parse('https://www.archlinux.org/feeds/packages/x86_64/extra/')
multilib = feedparser.parse('https://www.archlinux.org/feeds/packages/x86_64/multilib/')
packages = commands.getstatusoutput('pacman -Q')
localpac = packages[1]
localpac = localpac.splitlines()
packages = []
localpacname = []
update = []
def loopFeed(feed):
    for i in range(0, len(feed['entries'])):
        pkgname=feed['entries'][i]['title']
        packages.append(pkgname)
loopFeed(community)
loopFeed(core)
loopFeed(extra)
loopFeed(multilib)
for i in range(0, len(localpac)):
    localpacname.append(localpac[i][:localpac[i].index(' ')])

for package in packages:
    rpack = package[:package.index(" ")]
    if rpack in localpacname:
        remote, local = package[:package.rindex(" ")], localpac[localpacname.index(rpack)]
        rvnum = remote[remote.rindex(" "):]
        lvnum = local[local.rindex(" "):]
        count = 0
        updates =""
        if lvnum != rvnum:
            count = count + 1
            updates = updates + rpack + " " + lvnum + " => " + rvnum + "\n"
if count == 0:
    n = pynotify.Notification("Move along, nothing to see here",
    'No updates for today, you should still\nsudo pacman -Sy for \
older updates')
    n.show()
else:
    n = pynotify.Notification("Updates availiable", updates)
    n.show()

