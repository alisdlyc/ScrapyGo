# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

'''
    @:param comment 对于该参数，直接存入所有的评论信息，房东与房客通过添加一个字段来区分
'''


class UserItem(Item):
    user_id = Field()
    is_landlord = Field()
    img_url = Field()
    house_list = Field()
    star_comments = Field()
    guest_comments = Field()

class CommentItem(Item):
    custom_id = Field()
    comments = Field()
