
pals = [
    {
        "id": 1,
        "name": "Shania Twain",
        "email": "ShanTwa@penpals.pen"
    },
    {
        "id": 2,
        "name": "Robert Hannah",
        "email": "YogiB@penpals.pen"
    },
    {
        "id": 3,
        "name": "Charles Schultz",
        "email": "CharlieB@penpals.pen"
    },
    {
        "id": 4,
        "name": "Bobcat Goldthwait",
        "email": "BobbieG@penpals.pen"
    },
    {
        "id": 5,
        "name": "Mary Shelley",
        "email": "FrankiesMom@penpals.pen"
    },
    {
        "id": 6,
        "name": "Robert Frost",
        "email": "ThePoet@penpals.pen"
    }
]

letters = [
    {
        "authorId": 1,
        "recipientId": 1,
        "letterText": "topic test 1",
        "timestamp": "Wed Oct 19 2022 00:56:07 GMT-0600 (Central Standard Time)",
        "id": 1
    },
    {
        "authorId": 2,
        "recipientId": 3,
        "letterText": "Hey bro, I just wanted to write you a long letter to test out this sweet new IPP site. It's pretty sick, I think. You just click on some stuff and type out whatever you want to say then it gets posted up on the page for everyone to see, but also you can say what the topics for your message are and they're kind of like emojis except they're totally words. It's crazy. Anyway, I'm the 2nd person to post anything, so I'll always be better than you, so remember that. Anyway, Yogi>Charlie.",
        "timestamp": "Wed Oct 19 2022 07:56:07 GMT-0600 (Central Standard Time)",
        "id": 2
    },
    {
        "authorId": 2,
        "recipientId": 3,
        "letterText": "gdrgdrhrh",
        "timestamp": "Wed Oct 19 2022 10:56:07 GMT-0600 (Central Standard Time)",
        "id": 3
    },
    {
        "authorId": 3,
        "recipientId": 4,
        "letterText": "I miss you bro",
        "timestamp": "Mon Jan 09 2023 13:56:07 GMT-0600 (Central Standard Time)",
        "id": 8
    }
]

topics = [
    {
        "id": 1,
        "topic": "Business"
    },
    {
        "id": 2,
        "topic": "Just Because"
    },
    {
        "id": 3,
        "topic": "Love"
    },
    {
        "id": 4,
        "topic": "Congrats"
    },
    {
        "id": 5,
        "topic": "RSVP"
    }
]

lettertopics = [
    {
        "timestamp": "Wed Oct 19 2022 00:56:07 GMT-0600 (Central Standard Time)",
        "topics": [
            1
        ],
        "id": 1
    },
    {
        "timestamp": "Wed Oct 19 2022 07:56:07 GMT-0600 (Central Standard Time)",
        "topics": [
            1,
            2
        ],
        "id": 2
    },
    {
        "timestamp": "Wed Oct 19 2022 10:56:07 GMT-0600 (Central Standard Time)",
        "topics": [
            2
        ],
        "id": 3
    },
    {
        "timestamp": "Mon Jan 09 2023 13:56:07 GMT-0600 (Central Standard Time)",
        "topics": [
            1,
            2,
            3,
            4,
            5
        ],
        "id": 8
    }
]

# DATABASE = {pals, letters, lettertopics, topics}

def get_all_pals():
    """For GET requests to collection"""
    return pals

def get_all_letters():
    """For GET requests to collection"""
    return letters

def get_all_topics():
    """For GET requests to collection"""
    return topics

def get_all_lettertopics():
    """For GET requests to collection"""
    return lettertopics

def create_letter(letter):
    """posts a new letter"""
    max_id = letters[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the letter dictionary
    letter["id"] = new_id

    # Add the letter dictionary to the list
    letters.append(letter)

    # Return the dictionary with `id` property added
    return letter

def create_lettertopics(lettertopic):
    """posts a new lettertopic"""
    max_id = lettertopics[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the letter dictionary
    lettertopic["id"] = new_id

    # Add the lettertopic dictionary to the list
    lettertopics.append(lettertopic)

    # Return the dictionary with `id` property added
    return lettertopic
