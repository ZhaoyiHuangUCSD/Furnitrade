from flaskr.model.category_model import (
    get_category_by_catname, get_category_collection
)

mylist = [
	{"category_name": "Cooktops"},
	{"category_name": "Smart lighting"},
	{"category_name": "Cords & chargers"},
	{"category_name": "Extractor hoods & filters"},
	{"category_name": "Dishwashers"},
	{"category_name": "Mobile & tablet accessories"},
	{"category_name": "Refrigerators & freezers"},
	{"category_name": "Tools & hardware"},
	{"category_name": "Microwave ovens"},
	{"category_name": "Speakers"},
	{"category_name": "Ranges"},
	{"category_name": "Ovens"},
	{"category_name": "Cooktops"},
	{"category_name": "Countertops"},
	{"category_name": "Dishwashers"},
	{"category_name": "Extractor hoods & filters"},
	{"category_name": "Kitchen faucets & sinks"},
	{"category_name": "Kitchen integrated lighting"},
	{"category_name": "Kitchen islands & carts"},
	{"category_name": "Knobs & handles"},
	{"category_name": "Microwave ovens"},
	{"category_name": "Modular kitchens"},
	{"category_name": "Ovens"},
	{"category_name": "Pantry"},
	{"category_name": "Ranges"},
	{"category_name": "Refrigerators & freezers"},
	{"category_name": "SEKTION interior organizers"},
	{"category_name": "SEKTION Kitchen cabinets & fronts"},
	{"category_name": "Step stools & step ladders"},
	{"category_name": "Tools & hardware"},
	{"category_name": "Wall storage"},
	{"category_name": "Dining tables"},
	{"category_name": "Dining chairs"},
	{"category_name": "Dining sets"},
	{"category_name": "Dining storage"},
	{"category_name": "Bar tables & chairs"},
	{"category_name": "Stools & benches"},
	{"category_name": "Café furniture"},
	{"category_name": "High chairs"},
	{"category_name": "Junior chairs"},
	{"category_name": "All sofas"},
	{"category_name": "Ceiling lights"},
	{"category_name": "Fabric sofas"},
	{"category_name": "Living room storage system"},
	{"category_name": "Rugs"},
	{"category_name": "Bookcases"},
	{"category_name": "Cushions & cushions covers"},
	{"category_name": "Leather & coated fabric sofas"},
	{"category_name": "TV & Media Storage"},
	{"category_name": "Wall lamps"},
	{"category_name": "Curtain rods & rails"},
	{"category_name": "Floor lamps"},
	{"category_name": "Shelf units"},
	{"category_name": "Sleeper sofas"},
	{"category_name": "Cabinets & display cabinets"},
	{"category_name": "Coffee & side tables"},
	{"category_name": "Curtains & blinds"},
	{"category_name": "Sectionals"},
	{"category_name": "Table lamps"},
	{"category_name": "Armchairs & chaises"},
	{"category_name": "Blankets & throws"},
	{"category_name": "Integrated lighting"},
	{"category_name": "Sideboards, buffets & sofa tables"},
	{"category_name": "Fabrics & sewing"},
	{"category_name": "Ottomans"},
	{"category_name": "Shades, bases & cords"},
	{"category_name": "Wall shelves"},
	{"category_name": "Sofa accessories"},
	{"category_name": "Spotlights"},
	{"category_name": "Storage boxes & baskets"},
	{"category_name": "Extra covers"},
	{"category_name": "LED Light bulbs"},
	{"category_name": "Extra legs"},
	{"category_name": "LED lights"},
	{"category_name": "Smart lighting"},
	{"category_name": "Bedlinen"},
	{"category_name": "Ceiling lights"},
	{"category_name": "Full, Queen and King beds"},
	{"category_name": "Spring mattresses"},
	{"category_name": "Wardrobes"},
	{"category_name": "Comforters"},
	{"category_name": "Foam & latex mattresses"},
	{"category_name": "PAX wardrobe system"},
	{"category_name": "Single beds"},
	{"category_name": "Wall lamps"},
	{"category_name": "Divan beds"},
	{"category_name": "Pillow tops"},
	{"category_name": "Pillows"},
	{"category_name": "Table lamps"},
	{"category_name": "Bedspreads"},
	{"category_name": "Daybeds"},
	{"category_name": "Floor lamps"},
	{"category_name": "Mattress & pillow protectors"},
	{"category_name": "Open clothes & shoe storage system"},
	{"category_name": "Beds with storage"},
	{"category_name": "Chests of drawers"},
	{"category_name": "Cushions & cushions covers"},
	{"category_name": "Shades, bases & cords"},
	{"category_name": "Slatted bed bases"},
	{"category_name": "Dressing tables"},
	{"category_name": "Loft beds & bunk beds"},
	{"category_name": "Mattress bases"},
	{"category_name": "Mirrors"},
	{"category_name": "Rugs"},
	{"category_name": "Spotlights"},
	{"category_name": "Bed legs"},
	{"category_name": "Bed storage"},
	{"category_name": "Blankets & throws"},
	{"category_name": "Integrated lighting"},
	{"category_name": "Nightstands"},
	{"category_name": "Curtains & blinds"},
	{"category_name": "LED Light bulbs"},
	{"category_name": "Clothes organizers"},
	{"category_name": "Curtain rods & rails"},
	{"category_name": "LED lights"},
	{"category_name": "Fabrics & sewing"},
	{"category_name": "Hooks & hangers"},
	{"category_name": "Smart lighting"},
	{"category_name": "Headboards"},
	{"category_name": "Wall shelves"},
	{"category_name": "Racks & stands"},
	{"category_name": "Desks & computer desks"},
	{"category_name": "Wall shelves"},
	{"category_name": "Work lamps"},
	{"category_name": "LED lights"},
	{"category_name": "Office chairs"},
	{"category_name": "Storage cabinets"},
	{"category_name": "Table tops & legs"},
	{"category_name": "Cable management & accessories"},
	{"category_name": "Drawer units"},
	{"category_name": "Shades, bases & cords"},
	{"category_name": "Wall lamps"},
	{"category_name": "Bins & bags"},
	{"category_name": "Bookcases"},
	{"category_name": "Floor lamps"},
	{"category_name": "Smart lighting"},
	{"category_name": "Integrated lighting"},
	{"category_name": "Paper & media organizers"},
	{"category_name": "Shelf units"},
	{"category_name": "Cabinets & display cabinets"},
	{"category_name": "Ceiling lights"},
	{"category_name": "Sideboards, buffets & sofa tables"},
	{"category_name": "Table lamps"},
	{"category_name": "Spotlights"},
	{"category_name": "LED Light bulbs"},
	{"category_name": "Laundry & cleaning"},
	{"category_name": "Open clothes & shoe storage system"},
	{"category_name": "Clothes organizers"},
	{"category_name": "Hooks & hangers"},
	{"category_name": "Sink cabinets"},
	{"category_name": "Towels"},
	{"category_name": "Bath mats"},
	{"category_name": "Bathroom storage"},
	{"category_name": "Shower curtains"},
	{"category_name": "Sinks"},
	{"category_name": "Faucets"},
	{"category_name": "Showers"},
	{"category_name": "Bathroom mirrors"},
	{"category_name": "Bathroom accessories"},
	{"category_name": "Bathroom lighting"},
	{"category_name": "Bathrobes & slippers"},
	{"category_name": "Storage boxes & baskets"},
	{"category_name": "Paper & media organizers"},
	{"category_name": "Hooks & hangers"},
	{"category_name": "Bins & bags"},
	{"category_name": "Waste sorting"},
	{"category_name": "Clothes organizers"},
	{"category_name": "Bathroom accessories"},
	{"category_name": "Food storage & organizing"},
	{"category_name": "Wall Storage"},
	{"category_name": "Bedlinen"},
	{"category_name": "Rugs"},
	{"category_name": "Towels"},
	{"category_name": "Bath mats"},
	{"category_name": "Comforters"},
	{"category_name": "Curtains & blinds"},
	{"category_name": "Pillows"},
	{"category_name": "Shower curtains"},
	{"category_name": "Bathrobes & slippers"},
	{"category_name": "Bedspreads"},
	{"category_name": "Curtain rods & rails"},
	{"category_name": "Fabrics & sewing"},
	{"category_name": "Cushions & cushions covers"},
	{"category_name": "Blankets & throws"},
	{"category_name": "Kitchen textiles"},
	{"category_name": "Table linen"},
	{"category_name": "Children's textiles"},
	{"category_name": "Baby textiles"},
	{"category_name": "Children's textile 8-12"},
	{"category_name": "Mattress & pillow protectors"},
	{"category_name": "Smart lighting"},
	{"category_name": "Ceiling lights"},
	{"category_name": "Table lamps"},
	{"category_name": "Floor lamps"},
	{"category_name": "Work lamps"},
	{"category_name": "Shades, bases & cords"},
	{"category_name": "Integrated lighting"},
	{"category_name": "Spotlights"},
	{"category_name": "Wall lamps"},
	{"category_name": "Children's lighting"},
	{"category_name": "LED Light bulbs"},
	{"category_name": "Cords & chargers"},
	{"category_name": "LED lights"},
	{"category_name": "Decorative lighting"},
	{"category_name": "Outdoor lighting"},
	{"category_name": "Bathroom lighting"},
	{"category_name": "Children's lighting 8-12"},
	{"category_name": "Outdoor flooring"},
	{"category_name": "Tools & hardware"},
	{"category_name": "Oils, stains & product care"},
	{"category_name": "Knobs & handles"},
	{"category_name": "Safety"}
]

def init_category():
	categories = get_category_collection()

	# ADDED Furniture_id as list in each category.
	# By Mao
	for category in mylist:
		category['furniture_id'] = []

	categories.insert_many(mylist)

def delete_categories():
	categories = get_category_collection()
	categories.delete_many({})
	print("Original errorneous categories deleted")

# Check if category name is valid
def validate_category_name(category_name):
	for cat in mylist:
		if category_name in cat['category_name']:
			return True
	return False 