class Letter():
    """defines LETTER class"""
    def __init__(self, authorId, recipientId, lettertext, timestamp, id):
        self.id = id
        self.authorId = authorId
        self.recipientId = recipientId
        self.lettertext = lettertext
        self.timestamp = timestamp
