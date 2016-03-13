#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, math
import tweepy, config, random
from random import randint

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

scenes = ["tropical","american","desert","city","ocean","space"]
# scenes = ["space"]
trees = { "tropical":["🌴 ","🌱 ","🐢","🦀 ","🌴 ","🌴 ","🌴 ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          "american":["🌲 ","🌳 ","   ","   ","🐎 ","🌲 ","🌳 ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
          "desert":["🐍 ","🐢 ","🌵 ","🐫 ","🌱 ","🌵 ","🌵 ","   ","   ","   ","   ","   ","   ","   ","   "],
          "city":["🏠 ","🏡 ","🏚 ","🏢 ","🏬 ","🏣 ","🏤 ","🏥 ","🏦 ","🏨 ","🏪 ","🏫 ","🏩 ","💒 ","🏛 ","⛪ ","🕌 ","🕍 ","🌲 ","🌳 ","   ","   ","   ","   ","   "],
          "ocean":["🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","🌊 ","⛵ ","🛥 ","🚤 ","⛴ ","🛳"],
          "space":["✨ ","✨ ","✨ ","✨ ","✨ ","✨ ","✨ ","✨ ","✨ ","✨ ","🌑 ","🌏 ","🌕 ",
                  "   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",
                  "   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",]}
cars = ["🚎💨","🚌 ","🚗 ","🚕💨 ","🚙 ","🚌 ","🚎 ","🏎 ","🚓 ","🚑 ","🚒 ","🚐 ","🚚 ","🚛 ","🚜 ","🏍 ","🚲 ","🚕",
        "   ","   ","   ","   ","   ","   ","   ","   "]
spaceships = ["🚀  ","🛰  ", "   ", "   ", "   ", "   ", "   ", "   "]        
sky = ["🌞 ","🌤 ","⛅ ","☁"]

def setScene():
  global scene
  randInt = randint(0,int(len(scenes)-1))
  scene = scenes[randInt]
  print("Scene: " + scene)

def getTrees():
  randInt = randint(0,int(len(trees[scene])-1))
  # return trees[scene][randInt]
  # one = trees[scene][randInt]
  # print("Trees: " + trees[scene][randInt])
  return trees[scene][randInt]

def getSky():
  if scene == "space":
    return random.choice(trees['space'])
  else:
    return random.choice(sky)

def getCars():
  randInt = randint(0,int(len(cars)-1))
  if scene == "space":
    return random.choice(spaceships)
  else:
    return random.choice(cars)


setScene()

if scene == "ocean":
  tweet = "🌊 🌊 🌊 🌊 🌊 🌊 🌊 🌊 " + "\n" +\
        "🌊 " + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + "🌊" + "\n" +\
        "🌊 " + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + "🌊" + "\n" +\
        "🌊 " + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + "🌊" + "\n" +\
        "🌊 🌊 🌊 🌊 🌊 🌊 🌊 🌊 " + "\n"
else:
  tweet = getTrees() + getTrees() + getSky() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + "\n" +\
        getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + "\n" +\
        getCars() +  getCars() + getCars() + getCars() + getCars() + getCars() + getCars() + getCars() + "\n" +\
        getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + "\n" +\
        getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees() + getTrees()

print("MyTweet: " + str(len(tweet)) + "\n" + tweet)

def main():
  # Fill in the values noted in previous step here
  api = get_api(config.cfg)
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
   main()
