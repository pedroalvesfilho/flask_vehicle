"""Populate the item catalog database some initial content.
This script should only be run on an empty database.
"""
from sqlalchemy import func

from catalog.database_setup import User, Category, Item
from catalog.connect_to_database import connect_to_database


def populate():    
    session = connect_to_database()

    # Make sure the database is empty before running this inital data dump.
    category_count = session.query(func.count(Category.id)).scalar()
    if category_count > 0:
        session.close()
        return

    # Create the categories for Vehicles

    categoryBicycles = Category(name="Bicycles")
    session.add(categoryBicycles)
    session.commit()

    categoryMotor = Category(name="Motor Vehicles")
    session.add(categoryMotor)
    session.commit()

    categoryRailed = Category(name="Railed Vehicles")
    session.add(categoryRailed)
    session.commit()

    categoryWatercraft = Category(name="Watercraft")
    session.add(categoryWatercraft)
    session.commit()

    categoryAircraft = Category(name="Aircraft")
    session.add(categoryAircraft)
    session.commit()

    categorySpacecraft = Category(name="Spacecraft")
    session.add(categorySpacecraft)
    session.commit()

    # Create a user
    user1 = User(name="Rui Bot", email="rui@localhost.com")
    session.add(user1)
    session.commit()

    item1 = Item(
        user=user1,
        category=categoryBicycles,
        name="Chinese Flying Pigeon",
        description=(
            "The most popular bicycle model-and most popular vehicle of any kind in"
            "the world-is the Chinese Flying Pigeon, with about 500 million produced"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Left_side_of_Flying_Pigeon.jpg/1280px-Left_side_of_Flying_Pigeon.jpg"
    )
    session.add(item1)
    session.commit()

    item2 = Item(
        user=user1,
        category=categoryBicycles,
        name=" Trek Y-Foil",
        description=(
            "A carbon fiber Trek Y-Foil from the late 1990s"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Trek_Y_Foil.jpg/1280px-Trek_Y_Foil.jpg"

    )
    session.add(item2)
    session.commit()

    item3 = Item(
        user=user1,
        category=categoryMotor,
        name="1927 Ford Model T",
        description=(
            "1927 Ford Model T"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/1/15/Late_model_Ford_Model_T.jpg"
    )
    session.add(item3)
    session.commit()

    item4 = Item(
        user=user1,
        category=categoryMotor,
        name="Nissan Leaf",
        description=(
            "The Nissan Leaf is an all-electric car launched in December 2010"
        ),

        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/2018_Nissan_Leaf_Tekna_Front.jpg/280px-2018_Nissan_Leaf_Tekna_Front.jpg"
    )
    session.add(item4)
    session.commit()

    item5 = Item(
        user=user1,
        category=categoryMotor,
        name="Freightliner M2 dump truck",
        description=(
            "Big truck: Freightliner M2 dump truck"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Freightliner_M2_106_6x4_2014_%2814240376744%29.jpg/1280px-Freightliner_M2_106_6x4_2014_%2814240376744%29.jpg"
    )
    session.add(item5)
    session.commit()

    item6 = Item(
        user=user1,
        category=categoryMotor,
        name="Doble Decker Bus",
        description=(
            "A New Routemaster double-decker bus, operating for Arriva London on"
            "London Buses route 73"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/LT_471_%28LTZ_1471%29_Arriva_London_New_Routemaster_%2819522859218%29.jpg/1280px-LT_471_%28LTZ_1471%29_Arriva_London_New_Routemaster_%2819522859218%29.jpg"
    )
    session.add(item6)
    session.commit()

    item7 = Item(
        user=user1,
        category=categoryMotor,
        name="Old bus",
        description=(
            "A Toronto Transit Commission bus system trolleybus in Toronto"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Toronto_Flyer_E700A_trolleybus_in_1987.jpg/1280px-Toronto_Flyer_E700A_trolleybus_in_1987.jpg"
    )
    session.add(item7)
    session.commit()

    item8 = Item(
        user=user1,
        category=categoryMotor,
        name="Norton motorcycle",
        description=(
            "A classic Norton motorcycle"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Norton_Motorcycle.jpg/800px-Norton_Motorcycle.jpg"
    )
    session.add(item8)
    session.commit()

    item9 = Item(
        user=user1,
        category=categoryMotor,
        name="Suzuki GS500",
        description=(
            "A Suzuki GS500 with a clearly visible frame, painted silver"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/1997SuzukiGS500E-001.jpg/1280px-1997SuzukiGS500E-001.jpg"
    )
    session.add(item9)
    session.commit()

    item10 = Item(
        user=user1,
        category=categoryRailed,
        name="Glass Frog",
        description=(
            "Japanese Shinkansen 500 Series train, Shinkansen 500 series"
            " at Kyoto Station taken by Nick Coutts on 2005-03-19."
        ),

        image_url="https://upload.wikimedia.org/wikipedia/commons/3/31/Shinkansen_500_Kyoto_2005-03-19.jpg"
    )
    session.add(item10)
    session.commit()

    item11 = Item(
        user=user1,
        category=categoryRailed,
        name="ETT 303 and 304 Sunshine.",
        description=(
            "ETT 303 and 304 Sunshine."
        ),

        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/City_of_Rockhampton_train_%28Sunshine_railway_station%2C_Brisbane%29.jpg/800px-City_of_Rockhampton_train_%28Sunshine_railway_station%2C_Brisbane%29.jpg"
    )
    session.add(item11)
    session.commit()

    item12 = Item(
        user=user1,
        category=categoryWatercraft,
        name="RMS Titanic 3",
        description=(
            "Titanic!!!"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/800px-RMS_Titanic_3.jpg"
    )
    session.add(item12)
    session.commit()

    item13 = Item(
        user=user1,
        category=categoryWatercraft,
        name="Colombo Express",
        description=(
            "The Colombo Express, one of the largest container ships in the world,"
            "owned and operated by Hapag-Lloyd of Germany on its maiden voyage into Hamburg,"
            "with the Kohlbrand bridge in the background"
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Colombo.Express.wmt.jpg/800px-Colombo.Express.wmt.jpg"
    )
    session.add(item13)
    session.commit()

    item14 = Item(
        user=user1,
        category=categoryAircraft,
        name="Cessna 172",
        description=(
            "The Cessna 172 Skyhawk is the most produced aircraft in history."            
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Cessna172-CatalinaTakeOff.JPG/800px-Cessna172-CatalinaTakeOff.JPG"
    )
    session.add(item14)
    session.commit()

    item15 = Item(
        user=user1,
        category=categoryAircraft,
        name="Mil Mi-8",
        description=(
             "The Mil Mi-8 is the most-produced helicopter in history."
        ),
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Mi-8_%28RA-24477%29_Helicopter_in_SPB.jpg/800px-Mi-8_%28RA-24477%29_Helicopter_in_SPB.jpg"
    )
    session.add(item15)
    session.commit()

    session.close()

    print "Populated database with some rows..."


if __name__ == '__main__':
    populate()
