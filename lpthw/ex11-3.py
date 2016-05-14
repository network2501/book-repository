#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

print "What's the IP address you're connecting from?",
src_addr = raw_input()
print "What's the IP address you're connecting to?",
dst_addr = raw_input()
print "what's the latency to your destination?",
dst_latency = raw_input()

print "So you're connecting from %r and trying to access %r but it's taking %r long?" % (src_addr, dst_addr, dst_latency)
