import json
from deepdiff import DeepDiff
data1 = [
    {'Product Dimensions': '0.75 x 3.75 x 1.75 inches', 'Item Weight': '0.16 ounces', 'Manufacturer': 'Motorcraft',
     'ASIN': 'B000C5C4QG', 'Country of Origin': 'China', 'Item model number': 'YG346',
     'Customer Reviews': '4.7  4.7 out of 5 stars        814 ratings    4.7 out of 5 stars',
     'Best Sellers Rank': '#41,801 in Automotive (See Top 100 in Automotive)  #4 in Automotive Replacement Air '
                          'Conditioning Orifice Tubes',
     'Is Discontinued By Manufacturer': 'No', 'Assembly required': 'No', 'Batteries required': 'No',
     'Included Components': 'Tube', 'product_title': 'Motorcraft YG346 Fixed Orifice Tube'},
    {'Manufacturer': 'MOOG Chassis Products', 'Brand': 'MOOG', 'Item Weight': '5.2 pounds', 'Product Dimensions': '9.13 x 3.38 x 2.25 inches', 'Country of Origin': 'Mexico', 'Item model number': '8589B', 'Is Discontinued By Manufacturer': 'No', 'Manufacturer Part Number': '8589B', 'ASIN': 'B000C59UIQ', 'Customer Reviews': '4.9  4.9 out of 5 stars        13 ratings    4.9 out of 5 stars', 'Best Sellers Rank': '#956,308 in Automotive (See Top 100 in Automotive)  #56 in Automotive Replacement King Pin Sets', 'Date First Available': 'December 2, 2005', 'product_title': 'MOOG 8589B Steering King Pin Set for Ford F-350'}
]

data2 = [
    {'Product Dimensions': '9 x 6.25 x 2.25 inches', 'Item Weight': '4.23 pounds', 'ASIN': 'B00006JPF2', 'Item model number': '25 LTD', 'Customer Reviews': '4.6  4.6 out of 5 stars        3,550 ratings    4.6 out of 5 stars', 'Best Sellers Rank': '#1,412 in Portable FRS Two-Way Radios', 'Is Discontinued By Manufacturer': 'No', 'Special features': '9 Foot Cord', 'Other display features': 'Car Audio or Theater', 'Color': 'black/silver', 'Whats in the box': "Cobra 25 LTD Mounting bracket Powercord Installation hardware Owner's manual", 'Department': 'OUTDOOR PRODUCTS -> CB RADIOS & ACCESSORIES', 'Manufacturer': 'Cobra', 'Date First Available': 'February 18, 2006', 'product_title': 'Cobra 25LTD Professional CB Radio - Emergency Radio, Travel Essentials, Instant Channel 9, 4 Watt Output, Full 40 Channels, 9 Foot Cord, 4 Pin Connector'},
    {'Brand': 'MECO', 'Shape': 'Square', 'Seating Capacity': '4', 'Room Type': 'Kitchen',
     'Included Components': 'Assembly Guide', 'Color': 'Fruitwood', 'Model Name': 'STAKMORE',
     'Model Number': '0056.00841', 'Target Gender': 'Unisex',
     'Customer Reviews': '4.6 out of 5 stars        6,543    4.6 out of 5 stars', 'ASIN': 'B00OYJCM0O',
     'Style': 'Traditional', 'Table design': 'Dining Table', 'Pattern': 'Table', 'Assembly required': 'No',
     'Assembly Instructions': 'Already Assembled', 'Warranty Type': '5-YEAR LIMITED WARRANTY',
     'Specific instructions for use': 'Residential Use', 'Product Dimensions': '32"D x 32"W x 32"H',
     'Item Width': '32 inches', 'Tabletop Thickness': '0.75 Inches', 'Size': '32 in x 32 in x 29.5 in (D x W x H)',
     'Item Weight': '28.8 Pounds', 'Maximum recommended load': '150 Pounds', 'Number of Items': '1',
     'Number of shelves': '1', 'Unit Count': '1.0 Count', 'Base Material': 'Rubberwood,Solid Wood',
     'Frame Material': 'Wood', 'Top Material Type': 'Rubberwood,Solid Wood', 'Is Stain Resistant': 'No',
     'Special Feature': 'Storage', 'Is Foldable': 'Yes', 'Base Type': 'Leg Glides', 'Indoor/Outdoor Usage': 'Indoor',
     'product_title': 'Meco STAKMORE Straight Edge Folding Card Table Fruitwood Finish, 32 in x 32 in x 29.5 in (D x W x H)'},

]

# Convert dictionaries to JSON strings
json_data1 = json.dumps(data1, sort_keys=True)
json_data2 = json.dumps(data2, sort_keys=True)

# Convert JSON strings back to dictionaries
data1_dict = json.loads(json_data1)
data2_dict = json.loads(json_data2)

# Find the differences between data1 and data2
diff = DeepDiff(data1_dict, data2_dict, ignore_order=True)

# Print the differences
print("Differences between data1 and data2:")
print(json.dumps(diff, indent=4))
