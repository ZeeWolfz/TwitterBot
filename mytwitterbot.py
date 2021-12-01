# mytwitterbot.py
# IAE 101, Fall 2019
# Project 02 - Building a Twitterbot
# Name: Chengzhi Dong
# netid: CHENGDONG   
# Student ID:  112890166

import sys
import simple_twit

def main():
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    api = simple_twit.create_api()
    # YOUR CODE BEGINS HERE


    #First
    last_tweet = simple_twit.get_home_timeline(api, 1)
    for e in last_tweet:
        if e.favorite_count > 5 :
            new_tweet = "I'm very happy that my last tweet has been liked " + str(e.favorite_count)+ " times!"
            new_pic = "thank_you.jpg"
        else:
            new_tweet = "My last tweet did not receive many likes. I will do better next time."
            new_pic = "never_give_up.jpg"

    simple_twit.send_media_tweet(api, new_tweet, new_pic)

    #Second
    friend = simple_twit.get_my_friends(api, 1)
    for t in friend:
        retweet_name = t.screen_name
        print(retweet_name)
        
    friend_post = simple_twit.get_user_timeline(api, retweet_name, 1)
    for i in friend_post:
        retweet_id = i.id
    simple_twit.retweet(api, retweet_id)

    #Third
    import random
    lucky_color = ["blue", "green", "yellow", "purple", "red", "orange"]
    c = random.randint(0, 5)
    lucky_num = random.randint(1, 9)
    today_tweet = "Today, my lucky color is " + lucky_color[c] +" and my lucky number is " + str(lucky_num) + "."
    today_pic = lucky_color[c]+"_landscape.jpg"
    simple_twit.send_media_tweet(api, today_tweet, today_pic)


if __name__ == "__main__":
       main()
