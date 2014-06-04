#!/usr/bin/python2
import feedparser
import commands
community = feedparser.parse('https://www.archlinux.org/feeds/packages/x86_64/feed/')
core = feedparser.parse('https://www.archlinux.org/feeds/packages/x86_64/core/')
extra = feedparser.parse('https://www.archlinux.org/feeds/packages/x86_64/extra/')
multilib = feedparser.parse('https://www.archlinux.org/feeds/packages/x86_64/multilib/')
packages = commands.getstatusoutput('pacman -Q')
localpac = packages[1]
localpac = packages[1].splitlines()
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
for i in packages:
    if i in localpacname:
        print i
print
print update
