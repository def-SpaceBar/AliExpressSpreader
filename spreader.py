import os
import csv
import requests
import time
import random
import pyautogui
import pyperclip
from moviepy.editor import VideoFileClip


vidfile = 'C:\\Users\\User\\Desktop\\Projects\\CSV\\content\\vid.mp4'

# ######     HASHTAGS    #######
hashtags_1 = '#shoppingdiscounts #ilovecoupons #coupon101 #aliexpressturkey #shop #couponfriends #aliexpresswomen #newbiecouponer #aliexpressespaña #couponnewbie #productoftheweek #aliexpressshopping #couponcommunity'
hashtags_2 = '#gadetstore #techpromotions #couponfriends #shopping #aliexpressbrasil #aliexpressbr #gadgetlover #techies #aliexpressespaña #aliexpressturkey #aliexpressblogger #ilovecoupons #coupondeals #newbiecouponer #extremecoupons #aliexpressfrance #couponworld'
hashtags_3 = '#aliexpressblogger #ilovecoupons #coupondeals #newbiecouponer #extremecoupons #aliexpressfrance #couponworld #likeslikes #coupon101 #aliexpressshopping #shop #shoppingdiscounts #aliexpressreview #couponcode #couponnewbie #couponmom #couponingfamily #aliexpresslook #coupondeals'
hashtags_4 = '#gadetstore #techpromotions #couponfriends #shopping #aliexpressbrasil #aliexpressbr #gadgetlover #techies #aliexpressespaña #aliexpressturkey #aliexpressblogger #ilovecoupons #coupondeals #newbiecouponer #extremecoupons #aliexpressfrance #couponworld #likeslikes #coupon101'
hashtags_5 = '#extremecouponing #aliexpressbrasil #couponfriends #couponcommunity #aliexpressturkey #aliexpressblogger #f4follow #aliexpressbr #aliexpressreview #gadgetlover #couponcode #techpromotions #productoftheweek #coupondeals #aliexpressshopping #shoppingdiscounts #aliexpressblogger'
hashtags_6 = '#aliexpressreview #gadgetlover #couponcode #techpromotions #productoftheweek #coupondeals #aliexpressshopping #shoppingdiscounts #aliexpressblogger #coupon101 #coupondeals #howtocoupon #aliexpress #aliexpresslook #extremecoupons'
hashtags_7 = '#aliexpresspoland #aliexpresswomen #likeslikes #shop #gadetstore #ilovecoupons #newbiecouponer #couponingfamily #shopping #couponnewbie #couponmom #techies #aliexpressespaña #extremecouponing'
hashtags_8 = '#aliexpressespaña #extremecouponing #aliexpressbrasil #couponfriends #couponcommunity #aliexpressturkey #aliexpressblogger #f4follow #aliexpressbr #aliexpressreview #gadgetlover #couponcode #techpromotions #productoftheweek #coupondeals #aliexpressshopping #shoppingdiscounts #aliexpressblogger'
hashtags_9 = '#extremecoupons #techpromotions #aliexpressblogger #newbiecouponer #couponmom #f4follow #shopping #shop #aliexpresswomen #techies #gadgetlover #coupondeals #coupon101'
hashtags_10 = '#coupondeals #couponworld #couponer #shop #shopping #extremecouponing #aliexpress #f4follow #couponnewbie #aliexpressblogger #couponingfamily #newbiecouponer #techies #coupon101 #couponcode #couponcommunity #aliexpresswomen #aliexpressturkey #ilovecoupons #howtocoupon #aliexpressreview'
hashtags_11 = '#f4follow #couponnewbie #aliexpressblogger #couponingfamily #newbiecouponer #techies #coupon101 #couponcode #couponcommunity #aliexpresswomen #aliexpressturkey #ilovecoupons #howtocoupon #aliexpressreview #aliexpressblogger #aliexpressespaña #aliexpresspoland'
hashtags_12 = '#aliexpressespaña #aliexpresspoland #aliexpressshopping #aliexpressbrasil #aliexpressbr #couponmom #likeslikes #gadetstore #promogadget #gadgetlover #techpromotions #couponfriends #shoppingdiscounts #aliexpresslook'
hashtags_13 = '#aliexpresspoland #extremecoupons #f4follow #productoftheweek #aliexpressblogger #shop #aliexpressbr #aliexpressshopping #promogadget #couponfriends #aliexpressturkey #gadgetlover #techies #likesforlike #couponcode'
hashtags_14 = '#aliexpressturkey #gadgetlover #techies #likesforlike #couponcode #coupondeals #aliexpressblogger #newbiecouponer #shoppingdiscounts #aliexpressbrasil #likeslikes #techpromotions #couponingfamily #aliexpresswomen #couponworld '
hashtags_15 = '#likeslikes #techpromotions #couponingfamily #aliexpresswomen #couponworld #ilovecoupons #couponer #gadetstore #extremecouponing #howtocoupon #shopping #aliexpressreview #couponcommunity #couponmom #coupon101 #aliexpressespaña '
hashtags_16 = '#aliexpressbr #aliexpressblogger #shop #couponnewbie #aliexpressshopping #couponfriends #productoftheweek #aliexpressfrance #likeslikes #aliexpressreview #ilovecoupons #shoppingdiscounts #likesforlike #couponingfamily #coupon101'
hashtags_17 = '#newbiecouponer #aliexpresspoland #shopping #extremecoupons #coupondeals #aliexpresslook #couponmom #aliexpressbrasil #gadetstore #aliexpressblogger #aliexpressbr #aliexpressblogger #shop #couponnewbie #aliexpressshopping '
hashtags_18 = '#howtocoupon #coupondeals #gadgetlover #couponer #f4follow #promogadget #extremecouponing #techies #aliexpress #couponworld #aliexpressturkey #couponcode #aliexpresswomen #aliexpressespaña #techpromotions #couponcommunity'
hashtags_19 = '#couponnewbie #aliexpresslook #aliexpressbr #couponcode #aliexpressbrasil #coupon101 #coupondeals #ilovecoupons #aliexpressespaña #aliexpress #aliexpressturkey #tech #gadgetlover #gadget'
hashtags_20 = '#aliexpresswomen #couponingfamily #couponmom #extremecouponing #aliexpresspoland #aliexpressblogger #coupondeals #likesforlike #aliexpressblogger #couponcommunity #shoppingdiscounts #couponfriends #couponer #techpromotions'
hashtags_21 = '#aliexpressreview #gadgetlover #couponworld #shopping #productoftheweek #likeslikes #techies #newbiecouponer #gadetstore #f4follow #promogadget #extremecoupons #howtocoupon #aliexpressshopping'
hashtags_22 = '#likeslikes #couponcommunity #aliexpresslook #shop #couponcode #ilovecoupons #couponworld #shopping #promogadget #aliexpressbr #couponingfamily #f4follow #aliexpress #aliexpressturkey'
hashtags_23 = '#howtocoupon #gadgetlover #couponer #extremecouponing #aliexpressblogger #aliexpresspoland #couponnewbie #extremecoupons #aliexpressfrance #coupondeals #couponfriends #couponmom #shoppingdiscounts #aliexpressreview'
hashtags_29 = '#aliexpressshopping #newbiecouponer #coupondeals #aliexpresswomen #techies #likesforlike #aliexpressespaña #aliexpressblogger #techpromotions #coupon101 #gadetstore #productoftheweek #aliexpressbrasil'
hashtags_list = [hashtags_1, hashtags_2, hashtags_3, hashtags_4, hashtags_5, hashtags_6, hashtags_7, hashtags_8, hashtags_9, hashtags_10, hashtags_11, hashtags_12, hashtags_13, hashtags_14, hashtags_15, hashtags_16, hashtags_17, hashtags_18, hashtags_19, hashtags_20, hashtags_21, hashtags_22, hashtags_23, hashtags_29]
# ######     HASHTAGS    #######

# ######     TikTok HASHTAGS    #######
tt_hashtags_pool = ['#coupon', '#sale', '#shop', '#followforfollowback', '#lifehack', '#howto', '#tiktok', '#foryoupage', '#fyp', '#fyp', '#foryou', '#viral', '#followme', '#fun', '#follow', '#bestvideo', '#tiktok4fun', '#thisis4u', '#loveyoutiktok', '#youtube', '#youtuber', '#viralvideos', '#viralpost', '#likeforlikes', '#trending', '#explore', '#lfl', '#duet', '#code', '#tiktokers', '#explorepage', '#couponer', '#fypシ']
# ######     TikTok HASHTAGS    #######


# Telegram API Connection
api = 'nope'
channelid = '-1001516954483'
channelid_updates = '-1001547537905'
parsemode = 'HTML'

# #### TELEGRAM URLS ######
baseurl_sendmsg = f'https://api.telegram.org/bot{api}/sendMessage'
baseurl_sendphoto = f'https://api.telegram.org/bot{api}/sendPhoto'
baseurl_sendvideo = f'https://api.telegram.org/bot{api}/sendVideo'

# MEDIA #
media_location = 'C:\\Users\\user\\Desktop\\Projects\\CSV\\content'
video = 'vid.mp4'
picture = 'pic.jpg'
# MEDIA #

# #### Resource download PICTURE #####
def get_pic(row1):
    l = row1.split(',')
    response = requests.get(l[0])
    open("content\\pic.jpg", "wb").write(response.content)
    if 'pic.jpg' in os.listdir('C:\\Users\\user\\Desktop\\Projects\\CSV\\content'):
        print('picture downloaded')
        return True
    else:
        print('did not download picture')
        return False
# #### Resource download PICTURE #####

# #### Resource download VIDEO #####
def get_vid(row2):
    print(row2)
    if ',' in row2:
        l = row2.split(',')
        response = requests.get(l[0])
        open("content\\vid.mp4", "wb").write(response.content)
        if 'vid.mp4' in os.listdir('C:\\Users\\user\\Desktop\\Projects\\CSV\\content'):
            print('video downloaded')
            return True
        else:
            print('did not download video')
            return False
    else:
        response = requests.get(row2)
        open("content\\vid.mp4", "wb").write(response.content)
        if 'vid.mp4' in os.listdir('C:\\Users\\user\\Desktop\\Projects\\CSV\\content'):
            print('video downloaded')
            return True
        else:
            print('did not download video')
            return False
# #### Resource download VIDEO #####


# #### Check Vid Duration
def with_moviepy(filename):
    try:
        clip = VideoFileClip(filename)
        duration = clip.duration
        clip.close()
        return duration
    except:
        print('clip is not useable')
        return 61
# #### Check Vid Duration

# #### Resource cleanup() #####
def cleanup(media_location):
    try:
        os.remove(f'{media_location}\\pic.jpg')
        os.remove(f'{media_location}\\vid.mp4')
        print('clean')
    except FileNotFoundError:
        print('files:')
        for i in os.listdir(media_location):
            print(i)
        print('No files to delete, continue.')
# #### Resource cleanup() #####


# ########################### FUNCTIONS ###############################


# # ######     FB & IG - Post + Story    #######

def metavers_uploadPic(msgContent_facebook, msgContent_instagram):

    url = 'https://business.facebook.com/latest/home'

    # Positions & Delays variables - CREATE POST #
    button_click_delays0 = 0.25
    button_click_delays = 2
    key_press_delays = 0.20
    select_tab = (1539, 15)
    create_post = (716, 524)
    customize = (119, 457)

    # PHOTO
    add_photo = (163, 346)
    upload_from_pc = (176, 399)
    # PHOTO

    # VIDEO
    # add_photo = (317, 348)
    # upload_from_pc = (325, 400)
    select_img = (300, 245)
    # VIDEO

    select_img_ok = (1363, 992)
    location = (166, 678)
    fb_text = (353, 681)
    ig_text_switch = (270, 559)
    ig_text = (247, 662)
    publish_post = (623, 910)
    url_field = (1503, 54)

    # Positions & Delays variables - CREATE STORY #
    create_story = (971, 524)
    add_photo_story = (517, 531)
    # select_img = (912, 666)
    # select_img_ok = (1363, 992)
    publish_story = (1436, 844)


    # CREATE POST #
    pyautogui.click(select_tab, duration=button_click_delays)
    # clicks on url_field to go back to 'url' #
    pyautogui.click(url_field, duration=button_click_delays)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(url, interval=key_press_delays)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.click(1764, 275)
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    time.sleep(2)
    pyautogui.click(1764, 275)
    pyautogui.press('pageup')
    pyautogui.click(create_post, duration=button_click_delays)
    time.sleep(10)
    # add ig to share #
    pyautogui.click(customize, duration=button_click_delays)
    time.sleep(button_click_delays)
    # click add_photo #
    pyautogui.click(add_photo, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on upload_from_pc #
    pyautogui.click(upload_from_pc, duration=button_click_delays)
    time.sleep(button_click_delays)
    # doubleClicks on select_img #
    pyautogui.doubleClick(select_img, duration=button_click_delays)
    time.sleep(10)
    # clicks location + types 'AliExpress' + keyboardFunc 'Enter' #
    # pyautogui.click(location, duration=button_click_delays)
    # pyautogui.typewrite('aliexpress', interval=key_press_delays)
    # time.sleep(1)
    # pyautogui.press('enter')
    # time.sleep(button_click_delays)
    # clicks on fb_text #
    pyautogui.click(fb_text, duration=button_click_delays)
    pyperclip.copy(msgContent_facebook)
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.typewrite(msgContent_facebook, interval=key_press_delays)
    time.sleep(button_click_delays)
    # clicks on ig_text_switch #
    pyautogui.click(ig_text_switch, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on ig_text #
    pyautogui.click(ig_text, duration=button_click_delays)
    time.sleep(1)
    pyautogui.click(ig_text, duration=button_click_delays)
    # pyautogui.typewrite(msgContent_instagram, interval=key_press_delays)
    pyperclip.copy(msgContent_instagram)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(button_click_delays)
    # clicks on publish_post #
    time.sleep(1)
    pyautogui.click(publish_post, duration=button_click_delays)
    time.sleep(1)
    pyautogui.click(publish_post, duration=button_click_delays)
    time.sleep(15)
    # clicks on url_field to go back to 'url' #
    time.sleep(10)
    pyautogui.click(url_field, duration=button_click_delays)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(url, interval=key_press_delays)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)


    # CREATE STORY #
    # clicks on create_story #
    pyautogui.click(1764, 275)
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    time.sleep(2)
    pyautogui.click(1764, 275)
    pyautogui.press('pageup')
    pyautogui.click(create_story, duration=button_click_delays)
    time.sleep(10)
    # clicks on add_photo_story #
    pyautogui.click(add_photo_story, duration=button_click_delays)
    time.sleep(button_click_delays)
    # doubleClicks on select_img #
    pyautogui.doubleClick(select_img, duration=button_click_delays)
    time.sleep(button_click_delays)
    time.sleep(10)
    # clicks on publish_story #
    pyautogui.click(publish_story, duration=button_click_delays)
    time.sleep(button_click_delays)


# # ######     FB & IG - Post + Story    #######




# # ######     FB & IG - Post + Story    #######

def metavers_uploadVid(msgContent_facebook, msgContent_instagram):

    url = 'https://business.facebook.com/latest/home'

    # Positions & Delays variables - CREATE POST #
    button_click_delays0 = 0.25
    button_click_delays = 2
    key_press_delays = 0.20
    select_tab = (1539, 15)
    create_post = (716, 524)
    customize = (119, 457)

    # PHOTO
    # add_photo = (163, 346)
    # upload_from_pc = (176, 399)
    # PHOTO

    # VIDEO
    add_photo = (317, 348)
    upload_from_pc = (325, 400)
    select_img = (300, 245)
    # VIDEO

    select_img_ok = (1363, 992)
    location = (166, 678)
    fb_text = (353, 681)
    ig_text_switch = (270, 559)
    ig_text = (247, 662)
    publish_post = (623, 910)
    url_field = (1503, 54)

    # Positions & Delays variables - CREATE STORY #
    create_story = (971, 524)
    add_photo_story = (517, 531)
    # select_img = (912, 666)
    # select_img_ok = (1363, 992)
    publish_story = (1436, 844)


    # CREATE POST #
    pyautogui.click(select_tab, duration=button_click_delays)
    # clicks on url_field to go back to 'url' #
    pyautogui.click(url_field, duration=button_click_delays)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(url, interval=key_press_delays)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.click(1764, 275)
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    time.sleep(2)
    pyautogui.click(1764, 275)
    pyautogui.press('pageup')
    pyautogui.click(create_post, duration=button_click_delays)
    time.sleep(10)
    # add ig to share #
    pyautogui.click(customize, duration=button_click_delays)
    time.sleep(button_click_delays)
    # click add_photo #
    pyautogui.click(add_photo, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on upload_from_pc #
    pyautogui.click(upload_from_pc, duration=button_click_delays)
    time.sleep(button_click_delays)
    # doubleClicks on select_img #
    pyautogui.doubleClick(select_img, duration=button_click_delays)
    time.sleep(10)
    # clicks location + types 'AliExpress' + keyboardFunc 'Enter' #
    # pyautogui.click(location, duration=button_click_delays)
    # pyautogui.typewrite('aliexpress', interval=key_press_delays)
    # time.sleep(1)
    # pyautogui.press('enter')
    # time.sleep(button_click_delays)
    # clicks on fb_text #
    pyautogui.click(fb_text, duration=button_click_delays)
    pyperclip.copy(msgContent_facebook)
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.typewrite(msgContent_facebook, interval=key_press_delays)
    time.sleep(button_click_delays)
    # clicks on ig_text_switch #
    pyautogui.click(ig_text_switch, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on ig_text #
    pyautogui.click(ig_text, duration=button_click_delays)
    time.sleep(1)
    pyautogui.click(ig_text, duration=button_click_delays)
    # pyautogui.typewrite(msgContent_instagram, interval=key_press_delays)
    pyperclip.copy(msgContent_instagram)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(button_click_delays)
    # clicks on publish_post #
    time.sleep(1)
    pyautogui.click(publish_post, duration=button_click_delays)
    time.sleep(1)
    pyautogui.click(publish_post, duration=button_click_delays)
    time.sleep(0.5)
    pyautogui.click(publish_post, duration=button_click_delays)
    time.sleep(0.5)
    pyautogui.click(publish_post, duration=button_click_delays)
    pyautogui.click(publish_post, duration=button_click_delays)
    time.sleep(15)
    # clicks on url_field to go back to 'url' #
    time.sleep(10)
    pyautogui.click(url_field, duration=button_click_delays)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(url, interval=key_press_delays)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(10)


    # # CREATE STORY #
    # # clicks on create_story #
    # pyautogui.click(1764, 275)
    # pyautogui.press('pageup')
    # pyautogui.press('pageup')
    # pyautogui.press('pageup')
    # time.sleep(2)
    # pyautogui.click(1764, 275)
    # pyautogui.press('pageup')
    # pyautogui.click(create_story, duration=button_click_delays)
    # time.sleep(10)
    # # clicks on add_photo_story #
    # pyautogui.click(add_photo_story, duration=button_click_delays)
    # time.sleep(button_click_delays)
    # # doubleClicks on select_img #
    # pyautogui.doubleClick(select_img, duration=button_click_delays)
    # time.sleep(button_click_delays)
    # time.sleep(10)
    # # clicks on publish_story #
    # pyautogui.click(publish_story, duration=button_click_delays)
    # time.sleep(button_click_delays)


# # ######     FB & IG - Post + Story    #######


# ######     Youtube Upload    #######

def youtube_upload(msgContent_youtube, msgContent_title_youtube):

    url = 'https://studio.youtube.com/channel/UCqLh4jzbJ5-6mVQeh3a6vuQ'

    # Positions & Delays variables - CREATE POST #
    button_click_delays0 = 0.25
    button_click_delays = 1
    key_press_delays = 0.05
    select_tab = (1309, 13)
    create = (1800, 97) # delay 10 seconds
    upload_videos = (1766, 137)
    select_files = (956, 631)
    select_vid = (646, 259)  # double click - wait 10 seconds
    upload_thumbnail = (592, 723)
    select_thumbnail = (295, 247)
    video_title = (721, 356) # do ctrl+a - enter upto 130 characters from product title
    video_description = (753, 523)
    goto_visibility = (1301, 220)
    select_public = (585, 884)
    publish_video = (1387, 881) # delay 10 seconds
    url_field = (1503, 54)
    closeit = (821, 9)


    # Upload Video #
    # select yt tab #
    pyautogui.click(closeit, duration=button_click_delays)
    time.sleep(3)
    pyautogui.click(closeit, duration=button_click_delays)
    time.sleep(1.5)
    pyautogui.click(closeit, duration=button_click_delays)
    pyautogui.click(select_tab, duration=button_click_delays)
    # clicks on url_field to go back to 'url' #
    pyautogui.click(url_field, duration=button_click_delays)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(url, interval=key_press_delays)
    pyautogui.press('enter')
    time.sleep(10)
    # clicks on create #
    pyautogui.click(create, duration=button_click_delays)
    time.sleep(3)
    # clicks on upload_videos #
    pyautogui.click(upload_videos, duration=button_click_delays)
    time.sleep(button_click_delays)
    # click select_files #
    pyautogui.click(select_files, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on select_vid #
    pyautogui.doubleClick(select_vid, duration=button_click_delays)
    time.sleep(10)
    # clicks on upload_thumbnail #
    pyautogui.click(upload_thumbnail, duration=button_click_delays)
    time.sleep(3)
    # doubleClick on select_thumbnail #
    pyautogui.doubleClick(select_thumbnail, duration=button_click_delays)
    time.sleep(3)
    # clicks on video_title #
    pyautogui.click(video_title, duration=button_click_delays)
    pyautogui.hotkey('ctrl', 'a')
    pyperclip.copy(msgContent_title_youtube)
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.typewrite(msgContent_title_youtube, interval=key_press_delays)
    time.sleep(button_click_delays)
    # clicks on video_description #
    pyautogui.doubleClick(video_description, duration=button_click_delays)
    time.sleep(0.75)
    pyautogui.press('delete')
    pyautogui.press('enter')
    pyperclip.copy(msgContent_youtube)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    # pyautogui.typewrite(msgContent_youtube, interval=key_press_delays)
    time.sleep(button_click_delays)
    # clicks on goto_visibility #
    pyautogui.click(goto_visibility, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on publish_video #
    pyautogui.click(publish_video, duration=button_click_delays)
    time.sleep(10)
    # clicks on url_field to go back to 'url' #
    pyautogui.click(url_field, duration=button_click_delays)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(url, interval=key_press_delays)
    pyautogui.press('enter')
    time.sleep(10)

# ######     Youtube Upload    #######



# ######     TikTok Upload    #######

def tiktok_upload(tiktok_title_data):
    upload_url = 'https://www.tiktok.com/he-IL?lang=he-IL'

    button_click_delays0 = 0.25
    button_click_delays = 1.25
    key_press_delays = 0.05
    tiktok_tab = (1096, 13)
    url_bar = (1185, 52)
    up = (614, 92)
    tiktok_upload_btn = (1312, 657)
    tiktok_select_file = (299, 273)
    thumbnail_selector = (853, 473)
    tiktok_title = (747, 311)
    tiktok_publish_btn = (904, 863)



    # reset upload_tiktok #
    pyautogui.click(tiktok_tab, duration=button_click_delays)
    time.sleep(1.25)
    pyautogui.click(url_bar, duration=button_click_delays)
    time.sleep(1.25)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1.25)
    pyautogui.typewrite(upload_url)
    time.sleep(1.25)
    pyautogui.press('enter')
    time.sleep(15)
    pyautogui.click(up, duration=button_click_delays)
    time.sleep(8)
    # clicks on tiktok_upload_btn #
    pyautogui.click(tiktok_upload_btn, duration=button_click_delays)
    time.sleep(1.5)
    # click on tiktok_select_file #
    pyautogui.doubleClick(tiktok_select_file, duration=button_click_delays)
    time.sleep(90)
    # clicks on tiktok_title #
    # pyautogui.click(tiktok_title, duration=button_click_delays)
    # time.sleep(2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(2)
    pyautogui.press('delete')
    time.sleep(1)
    pyautogui.typewrite(tiktok_title_data)
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(1)
    # click on thumbnail_selector #
    pyautogui.click(thumbnail_selector, duration=button_click_delays)
    time.sleep(1.5)
    # clicks on tiktok_publish_btn #
    pyautogui.click(tiktok_publish_btn, duration=button_click_delays)
    time.sleep(1)
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('enter')


# ######     TikTok Upload    #######



# ######     LINKTREE    #######

def linktree_upload(title,link,img_upload_src):
    button_click_delays0 = 0.25
    button_click_delays = 1.25
    key_press_delays = 0.05
    add_newlink_button = (530, 263)
    add_title_button = (458, 366)
    add_link_button = (450, 396)
    add_photo_button = (488, 429)
    upload = (890, 490)
    set_thumbnail_button = (697, 565)
    upload_url = (616, 337)
    upload_url_field = (996, 545)
    link_submit = (1161, 542)
    save_button = upload_button_final = (1275, 740)
    refresh = (1834, 48)
    linktree_tab = (1817, 15)

    # refresh the page #
    pyautogui.click(linktree_tab, duration=button_click_delays)
    time.sleep(1.25)
    pyautogui.click(refresh, duration=button_click_delays)
    time.sleep(10)
    # clicks on add new link #
    pyautogui.click(add_newlink_button, duration=button_click_delays)
    time.sleep(5)
    # click on title & entering text #
    pyautogui.click(add_title_button, duration=button_click_delays)
    time.sleep(button_click_delays0)
    pyautogui.typewrite(title, interval=key_press_delays)
    time.sleep(button_click_delays)
    # click on link & entering link #
    pyautogui.click(add_link_button, duration=button_click_delays)
    time.sleep(button_click_delays0)
    pyautogui.typewrite(link, interval=key_press_delays)
    time.sleep(button_click_delays)
    # clicks on add_photo #
    pyautogui.click(add_photo_button, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on upload #
    pyautogui.click(set_thumbnail_button, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on set_thumbnail_button #
    pyautogui.click(upload, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on upload_url #
    pyautogui.click(upload_url, duration=button_click_delays)
    time.sleep(button_click_delays)
    # clicks on url field & entering url #
    pyautogui.click(upload_url_field, duration=button_click_delays)
    time.sleep(button_click_delays)
    pyautogui.typewrite(img_upload_src, interval=key_press_delays)
    time.sleep(button_click_delays0)
    pyautogui.click(link_submit, duration=button_click_delays)
    time.sleep(7)
    pyautogui.click(save_button, duration=button_click_delays)
    time.sleep(5)
    pyautogui.click(upload_button_final, duration=button_click_delays)
    time.sleep(10)
    pyautogui.click(refresh, duration=button_click_delays)
    time.sleep(1)

# ######     LINKTREE    #######

# ########################### FUNCTIONS ###############################


# CSV Files pool #

pool = 'C:\\Users\\user\\Desktop\\aliexpress csv\\'
parsed = 'C:\\Users\\user\\Desktop\\aliexpress csv\\parsed\\'
csv_list = os.listdir(pool)
print(csv_list)

# Choose what CSV file we want to parse #

choice = input('CSV to parse: ')

# List of wanted columns #
rounds = 0

with open(f'{pool}{choice}', encoding='utf-8') as products:
    heading = next(products)
    product = csv.reader(products)
    for row in product:
        description_of_product = row[3]
        description_of = description_of_product.split(' ')
        description = description_of[0] + ' ' + description_of[1] + ' ' + description_of[2] + ' ' + description_of[3] + ' ' + description_of[4] + ' ' + description_of[5] + ' ' + description_of[6] + ' ' + description_of[7] + ' ' + description_of[8] + ' ' + description_of[9] + ' ' + description_of[10] + ' ' + description_of[11]
        # description = row[3]

        # tiktok title creator
        for_tiktok = description_of[0] + ' ' + description_of[1] + ' ' + description_of[2] + ' ' + description_of[3] + ' '
        t = random.sample(tt_hashtags_pool, 7)
        ta = t[0] + ' ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]

        # Price pre-discount calculator
        discount_precent = row[5]
        discount = discount_precent.split('%')
        discounted_price = row[4]
        discounted_price_number = discounted_price.split(' ')
        try:
            original_price = float(discounted_price_number[1]) / (1 - float(discount[0]) / 100) + 0.005
        except ZeroDivisionError:
            original_price = 0.01
        original_price_format = '{0:.3g}'.format(original_price)
        price_int = float(discounted_price_number[1])
        isaveyou = original_price - price_int
        isaveyou_format = '{0:.3g}'.format(isaveyou)

        # msgContent_allPlatforms

        G = str('"')
        coupon_count = random.randint(1, 3)


        msgContent_tiktok = f'{for_tiktok}ON SALE! {discount_precent} OFF! - LINK IN BIO! | #AliExpress {ta}'

        msgContent_instagram = \
                     f'Product Description 👇🏼\n\n{row[3]}\n\n' \
                     f'✅ FREE SHIPPING 🔥\n' \
                     f'✂ COUPON AVAILABLE: {coupon_count} 🔥\n\n' \
                     f'✂ ✂ ✂   Use the link in our bio!   🔥 🔥 🔥\n\n' \
                     f'Original Price » {original_price_format}$ 👎🏼👎🏼\n' \
                     f'Our Price » {discounted_price_number[1]}$ 🔥\n' \
                     f'Our Discount » {discount_precent}  ✂🔥\n\n' \
                     f'Product Rating » {row[11]}/5 ✅\n' \
                     f'Sold {row[9]} times in last 90days ✅\n\n' \
                     f'\nNote: Those are special & rare discounts we find on the internet, they usually dissapear after a few days so make sure to be quick.\n' \
                     f'\n{random.choice(hashtags_list)}'

        msgContent_facebook = f'Product Description 👇🏼\n\n{row[3]}\n\n' \
                     f'FREE SHIPPING ✅\n' \
                     f'COUPON AVAILABLE » {coupon_count} ✂\n\n' \
                     f'WE SAVE YOU - {isaveyou_format}$\n' \
                     f'🔥 {row[12]} 🔥\n\n' \
                     f'Original Price » {original_price_format}$\n' \
                     f'Our Price » {discounted_price_number[1]}$ 🔥\n' \
                     f'Our Discount » {discount_precent}  ✂🔥\n\n' \
                     f'Product Rating » {row[11]}/5 ✅\n' \
                     f'Sold {row[9]} times in last 90days ✅\n\n' \
                     f'\nNote: Those are special & rare discounts we find on the internet, they usually dissapear after a few days so make sure to be quick.\n' \
                     f'\n{random.choice(hashtags_list)}'

        msgContent_youtube = f'{row[3]}\n\n' \
                     f'FREE SHIPPING ✅\n' \
                     f'COUPON AVAILABLE » {coupon_count} ✂\n\n' \
                     f'WE SAVE YOU - {isaveyou_format}$\n' \
                     f'🔥 {row[12]} 🔥\n\n' \
                     f'Original Price » {original_price_format}$\n' \
                     f'Our Price » {discounted_price_number[1]}$ 🔥\n' \
                     f'Our Discount » {discount_precent}  ✂🔥\n\n' \
                     f'Product Rating » {row[11]}/5 ✅\n' \
                     f'Sold {row[9]} times in last 90days ✅\n' \
                     f'\nNote: Those are special & rare discounts we find on the internet, they usually dissapear after a few days so make sure to be quick.\n\n' \
                     f'Our Website - http://aliexpressbot.com\n' \
                     f'Instagram - https://www.instagram.com/aliexpresscouponbot\n' \
                     f'Facebook - https://www.facebook.com/aliexpresscouponbot\n' \
                     f'Telegram - https://t.me/AliExpressTech2022\n' \
                     f'Linktree - https://linktr.ee/aliexpressdiscounts\n' \
                     f'\nOur channel is mainly about hot #AliExpress products and hot #discounts, we bring you the best #sales from AliExpress with a lot of hot #coupons that will save you a lot of money!'

        msgContent_telegram = f'<b>Product Description 👇🏼\n\n<strong>{row[3]}\n\n</strong></b>' \
                     f'\t<b>✅ FREE SHIPPING 🔥</b>\n' \
                     f'\t<b>✂ COUPON CODES</b> » <b><a href={G}{row[12]}{G}>{coupon_count} Coupons</a></b>\n\n' \
                     f'<b><a href={G}{row[12]}{G}>USING OUR LINK YOU WILL SAVE {isaveyou_format}$</a></b>\n\n' \
                     f'\tOriginal Price » <b>{original_price_format}$</b> 👎🏼👎🏼\n' \
                     f'\tOur Price » <b>{discounted_price_number[1]}$</b> 🔥\n' \
                     f'\tOur Discount » <b>{discount_precent}</b>  ✂🔥\n\n' \
                     f'Product Rating » <b>{row[11]}/5 </b>               ✅\n' \
                     f'Sold <b>{row[9]}</b> times in last 90days   ✅\n\n' \
                     f'                  ➡<b><a href={G}{row[12]}{G}>BUY NOW</a></b>⬅\n' \
                     f'         ➡<b><a href={G}{row[12]}{G}>LIMITED TIME PRICE</a></b>⬅\n\n' \
                     f'\nNote: Those are special & rare discounts we find on the internet, they usually disspear after a few days so make sure to be quick.'

        # Payloads
        payload_photo = {
                        'chat_id': channelid,
                        'photo': row[1],
                        'caption': msgContent_telegram,
                        'parse_mode': 'HTML'
            }
        payload_video = {
                        'chat_id': channelid,
                        'video': row[2],
                        'caption': msgContent_telegram,
                        'parse_mode': 'HTML'
            }
        
        # ############# UPDATES
        payload_updates = {
                        'chat_id': channelid_updates,
                        'text': f'---------\nRunning.\n---------\nstarting round number {rounds}',
            }
        # ####### TikTok
        payload_updates_tiktok = {
                        'chat_id': channelid_updates,
                        'text': '----tiktok----',
            }
        payload_updates_tiktok_uploading = {
                        'chat_id': channelid_updates,
                        'text': 'uploading tiktok',
            }
        payload_updates_tiktok_notuploading = {
                        'chat_id': channelid_updates,
                        'text': 'skipping tiktok upload - no video file',
            }
        # ####### METAVERSE
        payload_updates_metaverse = {
                        'chat_id': channelid_updates,
                        'text': f'----metaverse----',
            }
        payload_updates_metaverse_no = {
                        'chat_id': channelid_updates,
                        'text': 'skipping metaverse upload',
            }
        payload_updates_metaverse_yesPic = {
                        'chat_id': channelid_updates,
                        'text': 'uploading metaverse - picture',
            }
        payload_updates_metaverse_yesVid = {
                        'chat_id': channelid_updates,
                        'text': 'uploading metaverse - video',
            }
        # ####### Linktree
        payload_updates_linktree = {
                        'chat_id': channelid_updates,
                        'text': '----linktree----',
            }
        payload_updates_linktree_uploading = {
                        'chat_id': channelid_updates,
                        'text': 'uploading linktree',
            }
        # ####### Youtube
        payload_updates_youtube = {
                        'chat_id': channelid_updates,
                        'text': '----youtube----',
            }
        payload_updates_youtube_uploading = {
                        'chat_id': channelid_updates,
                        'text': 'uploading youtube - video file exists',
            }
        payload_updates_youtube_noVid = {
                        'chat_id': channelid_updates,
                        'text': 'skipping youtube - no video file found',
            }
        # ####### Telegram
        payload_updates_telegram = {
                        'chat_id': channelid_updates,
                        'text': '----telegram----',
            }
        payload_updates_telegram_post = {
                        'chat_id': channelid_updates,
                        'text': 'uploaded picture / video to telegram channel',
            }


        
        msgContent_title_youtube = description
        print('----------------UPDATES-------------------')
        update = requests.post(baseurl_sendmsg, data=payload_updates)
        print(update.content)

        print('----------------CleanUP()-------------------')
        cleanup(media_location)
        time.sleep(5)

        print('----------------DOWNLOADING-----------------')
        if 'http' in row[1]:
            print('picture link exists - downloading')
            if get_pic(row[1]):
                havePic = True
            else:
                havePic = False
        else:
            print('picture link does not exist')
            havePic = False

        if 'http' in row[2]:
            if get_vid(row[2]):
                haveVid = True
                haveVid_tiktok = True
            else:
                haveVid = False
                haveVid_tiktok = False
        else:
            print('video link does not exist')
            haveVid = False
            haveVid_tiktok = False

        print('-------------------TikTok----------------------')
        if haveVid_tiktok:
            if rounds < 100:
                requests.post(baseurl_sendmsg, data=payload_updates_tiktok)
                update = requests.post(baseurl_sendmsg, data=payload_updates_tiktok_uploading)
                print(update.content)
                tiktok_upload(msgContent_tiktok)
                print('TikTok | Uploaded.')
        else:
            print('haveVid = False | Skipping TikTok')
            requests.post(baseurl_sendmsg, data=payload_updates_tiktok)
            update = requests.post(baseurl_sendmsg, data=payload_updates_tiktok_notuploading)
            print(update.content)

        print('----------------METAVERSE------------------')
        if with_moviepy(vidfile) < 59.9:
            print('METAVERSE | Video is longer than 60, trying picture')
            requests.post(baseurl_sendmsg, data=payload_updates_metaverse)
            update = requests.post(baseurl_sendmsg, data=payload_updates_metaverse_yesVid)
            print(update.content)
            metavers_uploadVid(msgContent_facebook, msgContent_instagram)
        else:
            if havePic == True:
                print('METAVERSE | Trying Picture')
                requests.post(baseurl_sendmsg, data=payload_updates_metaverse)
                update = requests.post(baseurl_sendmsg, data=payload_updates_metaverse_yesPic)
                print(update.content)
                metavers_uploadPic(msgContent_facebook, msgContent_instagram)
            else:
                print('havePic = False | Skipping METAVERSE')
                requests.post(baseurl_sendmsg, data=payload_updates_metaverse)
                update = requests.post(baseurl_sendmsg, data=payload_updates_metaverse_no)
                print(update.content)

        print('----------------LINKTREE-------------------')
        time.sleep(3)
        requests.post(baseurl_sendmsg, data=payload_updates_linktree)
        update = requests.post(baseurl_sendmsg, data=payload_updates_linktree_uploading)
        print(update.content)
        linktree_upload(row[3], row[12], row[1])
        print('LINKTREE | Uploaded.')

        print('-------------------YT----------------------')
        if haveVid:
            if rounds < 100:
                requests.post(baseurl_sendmsg, data=payload_updates_youtube)
                update = requests.post(baseurl_sendmsg, data=payload_updates_youtube_uploading)
                print(update.content)
                youtube_upload(msgContent_youtube, msgContent_title_youtube)
                print('Youtube | Uploaded.')
        else:
            print('haveVid = False | Skipping YT')

        print('-----------------TELEGRAM--------------------')
        if 'https' in row[2]:
            requests.post(baseurl_sendmsg, data=payload_updates_telegram)
            update = requests.post(baseurl_sendmsg, data=payload_updates_telegram_post)
            print(update.content)
            msg = requests.post(baseurl_sendvideo, data=payload_video)
            print(msg.content)
            if msg.status_code == 200:
                print('telegram video uploaded')
                time.sleep(10)
            if msg.status_code == 400:
                msg = requests.post(baseurl_sendphoto, data=payload_photo)
                print(msg.content)
                if msg.status_code == 200:
                    print('telegram photo uploaded')
                time.sleep(10)
        else:
            print('no video')
            requests.post(baseurl_sendmsg, data=payload_updates_telegram)
            update = requests.post(baseurl_sendmsg, data=payload_updates_telegram_post)
            print(update.content)
            msg = requests.post(baseurl_sendphoto, data=payload_photo)
            print(msg.content)
            if msg.status_code == 200:
                print('telegram photo uploaded')
            time.sleep(10)

        print('----------------SLEEPING-------------------')
        rounds += 1
        print(f'rounds - {rounds}')
        time.sleep(2800)
