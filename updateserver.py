#!/usr/bin/python2
import feedparser
import commands
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

#print
#print localpacname
for package in packages:
    rpack = package[:package.index(" ")]
    #print blah,
    if rpack in localpacname:
        remote, local = package[:package.rindex(" ")], localpac[localpacname.index(rpack)]
        #print remote, local
        rvnum = remote[remote.rindex(" "):]
        lvnum = local[local.rindex(" "):]
        if lvnum != rvnum:
            print rpack + " " + lvnum + " => " + rvnum
