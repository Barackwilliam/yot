from django.test import TestCase

# Create your tests here.



# Kama models zote ziko kwenye file moja, tumia import hii:
from django.db import models
from django.core.validators import MinValueValidator

# ========== KU-CREATE DESTINATIONS ZOTE ==========

# 1. SERENGETI NATIONAL PARK
serengeti, created = Travels_Destination.objects.get_or_create(
    name="Serengeti National Park",
    defaults={
        'Offer_in_percent': 15,
        'image': None,
        'location': "Northern Tanzania",
        'description': """The Serengeti National Park is undoubtedly Tanzania's most famous wildlife sanctuary and one of the world's most spectacular natural wonders. Spanning over 14,750 square kilometers, it's renowned for the annual Great Migration where over 1.5 million wildebeest, 250,000 zebras, and hundreds of thousands of other ungulates undertake a circular 1,000-kilometer journey in search of fresh grazing.

UNESCO World Heritage Site (1981)
Key Features:
- Home to the Great Migration (one of the Seven Natural Wonders of Africa)
- Hosts the largest concentration of large mammals on Earth
- World-class predator viewing (lions, cheetahs, leopards)
- Diverse ecosystems: Seronera Valley, Western Corridor, Northern Lobo, and Southern Plains
- Over 500 bird species recorded
- Ancient rock paintings at Moru Kopjes""",
        'slug': "serengeti-national-park",
        'is_unesco_site': True
    }
)

# 2. KILIMANJARO NATIONAL PARK
kilimanjaro, created = Travels_Destination.objects.get_or_create(
    name="Kilimanjaro National Park",
    defaults={
        'Offer_in_percent': 10,
        'image': None,
        'location': "Northern Tanzania, Kilimanjaro Region",
        'description': """Mount Kilimanjaro National Park protects Africa's highest peak and the world's highest free-standing mountain. Rising 5,895 meters (19,341 feet) above sea level, Kilimanjaro is a dormant volcano with three distinct cones: Kibo (highest), Mawenzi, and Shira.

UNESCO World Heritage Site (1987)
Key Features:
- Africa's highest peak (5,895m/19,341ft)
- World's highest free-standing mountain
- One of the Seven Summits (highest peaks on each continent)
- Five distinct climatic zones: Cultivation, Rainforest, Heath/Moorland, Alpine Desert, Arctic Summit
- Unique flora including giant groundsels and lobelias""",
        'slug': "kilimanjaro-national-park",
        'is_unesco_site': True
    }
)

# 3. ZANZIBAR ARCHIPELAGO
zanzibar, created = Travels_Destination.objects.get_or_create(
    name="Zanzibar Archipelago",
    defaults={
        'Offer_in_percent': 20,
        'image': None,
        'location': "Indian Ocean, off the coast of Tanzania",
        'description': """The Zanzibar Archipelago is a tropical paradise consisting of several islands, with Unguja (commonly called Zanzibar Island) and Pemba being the main ones. Known as the "Spice Islands," Zanzibar offers a unique blend of African, Arab, Indian, and European influences.

UNESCO World Heritage Site: Stone Town (2000)
Key Features:
- Stone Town: Historic center with winding alleys, carved doors, and ancient buildings
- Pristine white-sand beaches with turquoise waters
- Rich cultural heritage and history (slave trade, spice trade)
- Diverse marine life and coral reefs for snorkeling/diving
- Spice plantations (cloves, nutmeg, cinnamon, vanilla)""",
        'slug': "zanzibar-archipelago",
        'is_unesco_site': True
    }
)

# 4. NGORONGORO CONSERVATION AREA
ngorongoro, created = Travels_Destination.objects.get_or_create(
    name="Ngorongoro Conservation Area",
    defaults={
        'Offer_in_percent': 12,
        'image': None,
        'location': "Northern Tanzania, between Serengeti and Lake Manyara",
        'description': """The Ngorongoro Conservation Area is a UNESCO World Heritage Site and one of Africa's most incredible natural wonders. The area is famous for the Ngorongoro Crater, the world's largest intact volcanic caldera, often called "Africa's Garden of Eden."

UNESCO World Heritage Site (1979)
Key Features:
- Ngorongoro Crater: 20km wide, 600m deep caldera
- Olduvai Gorge: "Cradle of Mankind" with important hominid fossils
- Empakaai Crater: Smaller crater with beautiful lake
- Olmoti Crater: Shallow crater with montane forest
- Active human population (Maasai pastoralists) coexisting with wildlife""",
        'slug': "ngorongoro-conservation-area",
        'is_unesco_site': True
    }
)

# 5. TARANGIRE NATIONAL PARK
tarangire, created = Travels_Destination.objects.get_or_create(
    name="Tarangire National Park",
    defaults={
        'Offer_in_percent': 8,
        'image': None,
        'location': "Northern Tanzania, southeast of Lake Manyara",
        'description': """Tarangire National Park is often called the "Elephant Paradise" of Tanzania and is famous for its massive elephant herds, ancient baobab trees, and diverse birdlife. Though less visited than Serengeti or Ngorongoro, it offers exceptional wildlife viewing, especially during the dry season.

Key Features:
- Second largest concentration of wildlife after Serengeti during dry season
- Famous for large elephant herds (up to 300 individuals)
- Ancient baobab trees (some over 1,000 years old)
- Tarangire River - lifeline during dry months
- Over 550 bird species (highest density in Tanzania)""",
        'slug': "tarangire-national-park",
        'is_unesco_site': False
    }
)

# 6. NIRUHU GAME RESERVE
niruhu, created = Travels_Destination.objects.get_or_create(
    name="Niruhu Game Reserve (formerly Selous)",
    defaults={
        'Offer_in_percent': 25,
        'image': None,
        'location': "Southern Tanzania",
        'description': """Niruhu Game Reserve, formerly known as Selous Game Reserve, is Africa's largest protected wildlife reserve covering approximately 50,000 square kilometers. This vast wilderness offers a more remote and authentic safari experience compared to the northern parks.

UNESCO World Heritage Site (1982)
Key Features:
- Largest protected wildlife area in Africa
- One of the last remaining strongholds of the African wild dog
- Diverse landscapes: miombo woodlands, open grasslands, swamps, lakes
- Rufiji River system with oxbow lakes and channels
- Boating safaris on the Rufiji River""",
        'slug': "niruhu-game-reserve",
        'is_unesco_site': True
    }
)

print(f"✅ Destinations zimeundwa au zimepatikana: {Travels_Destination.objects.count()}")

# ========== KU-ADD PACKAGE ITEMS KWA SERENGETI ==========
print("\n⏳ Kuanza ku-add package items kwa Serengeti...")

# Kwanza, futa items zilizopo kwa Serengeti (kuepuka duplicates)
serengeti.package_items.all().delete()

# Inclusions za Serengeti
serengeti_inclusions = [
    "Park entry fees and conservation fees",
    "Professional English-speaking safari guide",
    "4x4 safari vehicle with pop-up roof",
    "All game drives as per itinerary",
    "Bottled drinking water in vehicle",
    "Government taxes and VAT",
    "Emergency medical evacuation insurance",
    "All meals during safari (breakfast, lunch, dinner)",
    "Accommodation as specified in itinerary",
    "AMREF Flying Doctors emergency cover"
]

# Exclusions za Serengeti
serengeti_exclusions = [
    "International flights and visa fees",
    "Travel and medical insurance",
    "Tips for guides and camp staff",
    "Alcoholic and soft drinks",
    "Personal shopping and souvenirs",
    "Optional activities (hot air balloon safari, etc.)",
    "Accommodation before/after safari",
    "Items of personal nature",
    "Any changes to itinerary not specified"
]

# Create inclusion items
for item in serengeti_inclusions:
    TravelPackageItem.objects.create(
        content_object=serengeti,
        item_type=TravelPackageItem.INCLUDE,
        description=item
    )
    print(f"  ✓ Added inclusion: {item[:50]}...")

# Create exclusion items
for item in serengeti_exclusions:
    TravelPackageItem.objects.create(
        content_object=serengeti,
        item_type=TravelPackageItem.EXCLUDE,
        description=item
    )
    print(f"  ✓ Added exclusion: {item[:50]}...")

print(f"✅ Package items {len(serengeti_inclusions) + len(serengeti_exclusions)} zimeongezwa kwa Serengeti")

# ========== KU-ADD PACKAGE ITEMS KWA KILIMANJARO ==========
print("\n⏳ Kuanza ku-add package items kwa Kilimanjaro...")

# Futa items zilizopo
kilimanjaro.package_items.all().delete()

# Inclusions za Kilimanjaro
kilimanjaro_inclusions = [
    "All park fees, camping fees, and rescue fees",
    "Professional mountain guides and assistant guides",
    "Porters for personal luggage (max 15kg per person)",
    "Cook and kitchen team",
    "All meals on the mountain (breakfast, lunch, dinner)",
    "Camping equipment (tents, sleeping mats, mess tent)",
    "Clean, purified drinking water throughout climb",
    "Emergency oxygen cylinder and first aid kit",
    "Airport transfers (arrival and departure)",
    "Pre-climb briefing and equipment check"
]

# Exclusions za Kilimanjaro
kilimanjaro_exclusions = [
    "International and domestic flights",
    "Tanzania visa fees",
    "Travel and medical insurance",
    "Tips for guides, porters, and cooks",
    "Personal climbing gear (rental available)",
    "Hotel accommodation before/after climb",
    "Alcoholic and soft drinks",
    "Personal expenses (laundry, phone calls, etc.)",
    "Meals not specified in itinerary"
]

# Create items for Kilimanjaro
for item in kilimanjaro_inclusions:
    TravelPackageItem.objects.create(
        content_object=kilimanjaro,
        item_type=TravelPackageItem.INCLUDE,
        description=item
    )
    print(f"  ✓ Added inclusion: {item[:50]}...")

for item in kilimanjaro_exclusions:
    TravelPackageItem.objects.create(
        content_object=kilimanjaro,
        item_type=TravelPackageItem.EXCLUDE,
        description=item
    )
    print(f"  ✓ Added exclusion: {item[:50]}...")

print(f"✅ Package items {len(kilimanjaro_inclusions) + len(kilimanjaro_exclusions)} zimeongezwa kwa Kilimanjaro")

# ========== HAKIKI YA MWISHO ==========
print("\n" + "="*50)
print("Hakiki ya Mwisho:")
print("="*50)

# Check kila destination
destinations = Travels_Destination.objects.all()
for dest in destinations:
    includes_count = dest.includes.count()
    excludes_count = dest.excludes.count()
    print(f"{dest.name}:")
    print(f"  - Includes: {includes_count} items")
    print(f"  - Excludes: {excludes_count} items")
    print(f"  - Total: {includes_count + excludes_count} package items")

print("\n" + "="*50)
print("✅ Usajili wa Destinations umekamilika kikamilifu!")
print(f"✅ Jumla ya Destinations: {Travels_Destination.objects.count()}")
print(f"✅ Jumla ya Package Items zote: {TravelPackageItem.objects.count()}")
print("="*50)