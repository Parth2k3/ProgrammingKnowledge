
import googlemaps

# Provide your API key here
api_key = '############'  # Replace with your actual Google API key

# Initialize the Google Maps API client
gmaps = googlemaps.Client(key=api_key)

# Perform a place search (example: "restaurants in New York")
places_result = gmaps.places("restaurants in New York")

# Print the results
for place in places_result['results']:
    print(f"Name: {place['name']}")
    print(f"Address: {place.get('vicinity', 'N/A')}")
    print(f"Rating: {place.get('rating', 'N/A')}")
    print('-' * 30)

# Get details of a specific place by place ID
place_id = places_result['results'][0]['place_id']
place_details = gmaps.place(place_id)

# Print detailed information about the first place in the list
print("Detailed Information:")
print(f"Name: {place_details['result']['name']}")
print(f"Address: {place_details['result']['formatted_address']}")
print(f"Phone Number: {place_details['result'].get('formatted_phone_number', 'N/A')}")
print(f"Website: {place_details['result'].get('website', 'N/A')}")
