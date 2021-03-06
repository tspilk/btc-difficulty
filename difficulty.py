"""
Copyright (C) 2013 Tyler Spilker

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the 
"Software"), to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to 
the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
#_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,#
#                                                                      #
#   Project             :   Bitcoin Difficulty Parser                  #
#                                                                      #
#   Program Name        :   difficulty.py                              #
#                                                                      #
#   Author              :   Tyler Spilker                              #
#                                                                      #
#   Date Created        :   2013-05-06                                 #
#                                                                      #
#   Purpose             :   To iterate through bitcoind calls to       #
#                           gather difficulty of every block           #
#                                                                      #
#_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,_,.~'`'~.,#

# If this helped, please feel free to donate me some coins :)
# BTC : 1Lu5kcCh1vU68XmAT9E9KZZAR4deEhTDr4
# LTC : LcvAhhVPgQxRmoGDnNrCBkWdgz3n2dnEYg

import os, ast, time
path = './blockdiff'
#os.system('echo "" >'+path)
last_line = os.popen("tail -n 1 %s" % path).read().split()

f = open(path,'a')
try:
  last_block = int(last_line[0])
except:
  last_block = 0
 
block_count = int(os.popen("bitcoind getblockcount").read().split()[0])


for i in range(block_count)[last_block:]:
  hash = os.popen("bitcoind getblockhash "+str(i)).read().strip("\n")

  block = ast.literal_eval(os.popen("bitcoind getblock " + hash).read())

  f.write(str(block["height"]+1)+"\t")
  f.write(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(block["time"]))))+"\t")
  f.write(str(block["difficulty"])+"\n")
  if i%100 == 0:
    print i
f.close()

