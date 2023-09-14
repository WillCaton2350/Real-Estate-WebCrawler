from scrapy import Item, Field

class SubletWebcrawlerItem(Item):
    id = Field()
    Url = Field()
    Description = Field()
    Rental = Field()
    Rent = Field()
    Location = Field()
    Lease = Field()
    Amenities = Field()
    Not_Included = Field()