#-*- coding:utf-8 -*-
u'''
Comments here
'''

__version__ = '0.6.0'
__author__ = '@ThomasConnors'
__license__ = 'LGPLv3'


def setup(app):

    from . import tweet, user, timeline

    app.add_js_file('https://platform.twitter.com/widgets.js')

    app.add_node(tweet.tweet,
                 html=(tweet.visit, tweet.depart))
    app.add_directive('tweet', tweet.TweetDirective)

    app.add_node(timeline.timeline,
                 html=(timeline.visit, timeline.depart))
    app.add_directive('timeline', timeline.TimelineDirective)

    app.add_node(user.twnode,
                 html=(user.visit, user.depart))
    app.add_role('tw', user.tw_role)