class Auction:
    def __init__(self, number, title, time, cp):
        self.auctionNum=number
        self.auctionTitle=title
        self.auctionTime=time
        self.auctionCurrentPrice=float(cp)
    def display(self):
        return ("Auction Number: {} \nTitle: {} \nTime Remaining: {} \nCurrent Price: ${} \n".format(self.auctionNum, self.auctionTitle, self.auctionTime.display(), self.auctionCurrentPrice))