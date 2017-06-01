#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  temp.py
#
#  Copyright 2017 mdkh <m2khosravizadeh@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  https://ir.linkedin.com/in/mohammad-khosravizadeh-aa326444
#
#
import copy
import aiohttp
import asyncio, bs4
import sys
import telepot
import telepot.aio
import lxml

from .constant import *

from telepot.aio.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent


global list_titles
global all_list

async def request_func(address):
    async with aiohttp.ClientSession() as session:
        async with session.get(address) as resp:
            return await resp.text()


async def main(address):
    find_all4test2 = {}
    list_result = {}
    find_all4test = {}
    find_all4test_temp = await iterate_main(address)
    find_all4test[address] = copy.copy(find_all4test_temp)
    while True:

        find_all4test_temp = await iterate_main(address)
        find_all4test2[address] = copy.copy(find_all4test_temp)
        list_main = copy.copy(find_all4test[address])
        list_result = list(set(find_all4test_temp) - set(list_main))
        count_list_result = len(list_result)

        if  count_list_result != 0:
            find_all4test[address] = copy.copy(find_all4test2[address])
            for count in range(count_list_result):
                list4show_in_bot = [text for text in list_result[count].stripped_strings]
                await send2bot(*list4show_in_bot)

async def send2bot(*args):
    __mychannel = "-100"
    my_bot = telepot.aio.Bot(TOKEN)
    await my_bot.sendMessage(__mychannel, "[*{text4bot}*]({Link4bot})".format(text4bot = args[1], Link4bot = args[0]) + " : \n" + args[2], parse_mode = "Markdown")


async def soup_html(text_request):
    responsesoup = bs4.BeautifulSoup(text_request, "html.parser")
    find_all4test = responsesoup.find_all("item")
    item_html = responsesoup.item.get_text()
    item_link = responsesoup.find_all('link')
    return responsesoup
    linksoups = []
    linktexts = []
    linkimageurls = []


async def iterate_main(address):
    text_request = await request_func(address)
    temp_titles = await soup_html(text_request)
    list_titles = temp_titles.find_all('title')
    find_all4test = temp_titles.find_all("item")
    return find_all4test

async def on_chat_message(msg):
    print("in chat_message: ", msg)

async def on_callback_query(msg):
    pass

async def on_inline_query(msg):
    pass

async def on_chosen_inline_result(msg):
    pass

async def on_channel_post(msg):
    print("msg in ***on_channel_post*** :", msg)

async def on_edited_channel_post(msg):
    pass


async def print_test():
    print("in test_counter")


async def test_counter():
    while True:
        print_test()


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance2(msg)



addresses = ['http://donya-e-eqtesad.com/mining-industry/rss/',
'http://donya-e-eqtesad.com/digital/rss/',
'http://khabaronline.ir/rss/service/economy',
'http://khabaronline.ir/rss/service/ict',
'http://sanjesh.org/rss/rss.aspx'
]

loop = asyncio.get_event_loop()

TOKEN = sys.argv[1]
tasks = []
bot = telepot.aio.Bot(TOKEN)
answerer = telepot.aio.helper.Answerer(bot)
task = asyncio.ensure_future(MessageLoop(bot, {'chat': on_chat_message,
                                   'callback_query': on_callback_query,
                                   'inline_query': on_inline_query,
                                   'chosen_inline_result': on_chosen_inline_result,
                                   'channel_post' : on_channel_post,
                                   'edited_channel_post' : on_edited_channel_post
                                   }).run_forever())

print('Listening ...')


tasks.append(task)
for address in addresses:
    task = asyncio.ensure_future(main(address))
    tasks.append(task)

task = asyncio.ensure_future(print_test())
tasks.append(task)
asyncio.gather(*tasks)
loop.run_forever()
