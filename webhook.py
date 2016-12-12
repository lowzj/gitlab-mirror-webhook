#!/usr/bin/env python
# -*- coding:utf-8 -*-
import commands
import hmac
import json
import os
import web

from hashlib import sha1

#==============================================================================
# environment variable
SECRET = os.getenv('GITLAB_MIRROR_WEBHOOK_SECRET')
WORK_DIR = os.etenv('GITLAB_MIRROR_WORK_DIR')


#==============================================================================
urls = (
    '/', 'Index'
)


def getRepoName(data):
  try:
    return json.loads(data).get('repository').get('name')
  except Exception, e:
    print e

def getSignature():
  sig = web.ctx.env.get('HTTP_X_HUB_SIGNATURE')
  if sig:
    shaName, signature = sig.split('=')
    if shaName == 'sha1':
      return signature
  return ''

def verifySignature(secret, signature, data):
  if secret and signature:
    mac = hmac.new(str(secret), msg=data, digestmod=sha1)
    expected = str(mac.hexdigest())
    print ("expected signature: %s, request signature: %s" %(expected, str(signature)))
    return expected == str(signature)
  return not secret and not signature

class Index:
  def GET(self):
    return "Hello World"

  def POST(self):
    signature = getSignature()
    if verifySignature(SECRET, signature, web.data()):
      repository = getRepoName(web.data())
      update_gitlab_mirror = "cd $s && ./update_mirror.sh %s" %(WORK_DIR, repository)
      out = commands.getoutput(update_gitlab_mirror)
      return out
    return web.unauthorized()

app = web.application(urls, globals())
if __name__ == "__main__":
  app.run()
