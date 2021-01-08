from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item


player = Actor(
    char="@",
    color=(219, 156, 30),
    name="Omegaman",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=100, base_defense=1, base_power=1),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

orc = Actor(
    char="O",
    color=(80, 41, 137),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=0),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

nh1 = Actor(
    char="O",
    color=(80, 41, 137),
    name="Nameless Horror",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=1, base_defense=0, base_power=20),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=0),
)

nh2 = Actor(
    char="O",
    color=(80, 41, 137),
    name="Nameless Horror",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=8, base_defense=0, base_power=40),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=0),
)

nh3 = Actor(
    char="O",
    color=(80, 41, 137),
    name="Nameless Horror",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=0, base_power=20),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=0),
)

nh4 = Actor(
    char="O",
    color=(80, 41, 137),
    name="Nameless Horror",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=0, base_power=120),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=0),
)

nh5 = Actor(
    char="O",
    color=(80, 41, 137),
    name="Nameless Horror",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=50, base_defense=2, base_power=98),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=0),
)

rat = Actor(
    char="r",
    color=(107, 122, 109),
    name="Rat",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=2, base_defense=0, base_power=7),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=1),
)

walkingcadaver = Actor(
    char='c',
    color=(238, 122, 109),
    name='Walking Cadaver',
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=50, base_defense=0, base_power=55),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=0),
)

cadaver = Item(
    char='c',
    color=(238, 122, 109),
    name='Cadaver',
    consumable=consumable.CadaverConsumable(amount=5),
)

paralyze_fungus = Item(
    char='"',
    color=(130, 107, 65),
    name = "Dark Fungus",
    consumable=consumable.ParalyzeFungusConsumable(number_of_turns = 13),
)

confusion_scroll = Item(
    char='"',
    color=(77, 170, 172),
    name="Iridescent Fungus",
    consumable=consumable.ConfusionConsumable(number_of_turns=20),
)
#fireball_scroll = Item(
#    char="~",
#    color=(255, 0, 0),
#    name="Prayer2optional",
#    consumable=consumable.FireballDamageConsumable(damage=200, maximum_range=5),
#)
health_potion = Item(
    char='"',
    color=(225, 32, 7),
    name="Familiar Fungus",
    consumable=consumable.HealingConsumable(amount=100),
)
lightning_scroll = Item(
    char="~",
    color=(252, 116, 72),
    name="Prayer",
    consumable=consumable.LightningDamageConsumable(damage=200, maximum_range=5),
)
green_fungus = Item(
    char='"',
    color=(65, 91, 54),
    name="Grassy Fungus",
    consumable=consumable.GreenFungusConsumable(number_of_turns=0),
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(252, 116, 72), name="Ancient Sword", equippable=equippable.Sword())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)
