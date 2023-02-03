# noinspection PyUnresolvedReferences
from app import db
from models import User, UserImage, Pool, PoolImage, Reservation, Message

db.drop_all()
db.create_all()

# region create dummy users#########################

user1 = User(
    email="test1@email.com",
    username="test1",
    password="pasword",
    location="Los Angeles",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/brooke-cagle-R0Ea06wC2IM-unsplash.jpg"
)

user2 = User(
    email="test2@email.com",
    username="test2",
    password="password2",
    location="San Francisco",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/jake-nackos-IF9TK5Uy-KI-unsplash.jpg"
)

user3 = User(
    email="test3@email.com",
    username="test3",
    password="password3",
    location="New York",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/joseph-gonzalez-iFgRcqHznqg-unsplash.jpg"
)


db.session.add_all([user1, user2, user3])
db.session.commit()
# endregion


# region pools#########################
pool1 = Pool(
    id=1,
    owner_username="test1",
    rate=10.00,
    size="20x20",
    description="The best pool ever!",
    city="Los Angeles",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/big-tiny-belly-XtnNrQYC7ts-unsplash.jpg"
)

pool2 = Pool(
    id=2,
    owner_username="test2",
    rate=20.00,
    size="20x50",
    description="The pool with the best view!",
    city="San Francisco",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/joe-ciciarelli-08AJKJf75kw-unsplash.jpg"
)

pool3 = Pool(
    id=3,
    owner_username="test3",
    rate=25.00,
    size="20x50",
    description="Its heated!!",
    city="New York",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/john-fornander-y3_AHHrxUBY-unsplash.jpg"
)

pool4 = Pool(
    id=4,
    owner_username="test1",
    rate=10.00,
    size="12x20",
    description="Small but quaint",
    city="San Francisco",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/florian-schmidinger-b_79nOqf95I-unsplash.jpg"
)

pool5 = Pool(
    id=5,
    owner_username="test3",
    rate=15.00,
    size="24x40",
    description="High rise and private!",
    city="New York",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/jerome-pcuVPWxddLI-unsplash.jpg"
)

pool6 = Pool(
    id=5,
    owner_username="test1",
    rate=10.00,
    size="24x40",
    description="Small but quaint",
    city="New York",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/ferdinand-asakome-oUdt2BJrLJE-unsplash.jpg"
)

pool7 = Pool(
    id=5,
    owner_username="test1",
    rate=12.00,
    size="=15x30",
    description="A Backyard Paradise!",
    city="Los Angeles",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/xavi-serra-NF93JnqD1Fo-unsplash.jpg"
)

pool8 = Pool(
    id=5,
    owner_username="test2",
    rate=20.00,
    size="=15x30",
    description="Pool on the golf course!",
    city="Los Angeles",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/nick-nolan-8w1JRVzx0sw-unsplash.jpg"
)

pool9 = Pool(
    id=5,
    owner_username="test2",
    rate=20.00,
    size="=15x30",
    description="A pool fit for royalty!",
    city="Los Angeles",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/avi-werde-hHz4yrvxwlA-unsplash.jpg"
)

pool10 = Pool(
    id=5,
    owner_username="test2",
    rate=20.00,
    size="=15x30",
    description="Treat yoself!",
    city="Los Angeles",
    image_url="https://sharebnb-gmm.s3.us-west-1.amazonaws.com/thor-schroeder-T91WhuBxDec-unsplash.jpg"
)

db.session.add_all([pool1, pool2, pool3, pool4, pool5, pool6, pool7])
db.session.commit()
# endregion

# region poolImages
# pool1Image = PoolImage(
#     id=1,
#     pool_owner="test1",
#     image_url="",
# )

# pool2Image = PoolImage(
#     id=2,
#     pool_owner="test2",
#     image_url="",
# )

# db.session.add_all([pool1Image, pool2Image])
# db.session.commit()
# endregion

# region reservations#########################
reservation1 = Reservation(
    id=1,
    booked_username="test1",
    pool_id=1,
    reservation_date_created="Wed, 01 Feb 2023 12:01:00 GMT",
    start_date="Fri, 03 Feb 2023 12:01:00 GMT",
    end_date="Sun, 05 Feb 2023 12:01:00 GMT",
)

reservation2 = Reservation(
    id=2,
    booked_username="test2",
    pool_id=2,
    reservation_date_created="Wed, 08 Feb 2023 12:01:00 GMT",
    start_date="Fri, 10 Feb 2023 12:01:00 GMT",
    end_date="Sun, 12 Feb 2023 12:01:00 GMT",
)

db.session.add_all([reservation1, reservation2])
db.session.commit()
# endregion

# region messages#########################

message1 = Message(
    id=1,
    sender_username="test1",
    recipient_username="test2",
    title="is your pool available?",
    body="Hi there, i'd like to see if your pool is available for this weekend?",
    listing=1,
    timestamp="Wed, 01 Feb 2023 12:01:00 GMT"
)

message2 = Message(
    id=2,
    sender_username="test2",
    recipient_username="test1",
    title="I love your pool!",
    body="Hi there, my friends and I were wondeirng if your pool is free this weekend?",
    listing=1,
    timestamp="Thu, 02 Feb 2023 12:01:00 GMT"
)

message3 = Message(
    id=3,
    sender_username="test1",
    recipient_username="test2",
    title="Great! Come through!",
    body="yes its available! book it and you can come through!",
    listing=1,
    timestamp="Thu, 02 Feb 2023 12:11:00 GMT"
)

db.session.add_all([message1, message2])
db.session.commit()
# endregion
