from dataset import * 
from datetime import date
from math import ceil, floor
from random import choice

NONREPEAT_PERIOD = 62 # Goal of not wearing the same item more than once per two-month period, on average. User can set their nonrepeat period of choice.

def num_of_days(date1, date2):
  days_elapsed = (date2 - date1).days 
  return days_elapsed
  
days_elapsed = num_of_days(date(2018, 1, 1), date.today()) # Enters the date user started tracking wears and today's date

def get_items(dict): # Displays items from a given category that have been worn the least
  minimum = min(dict.values())
  print("Minimum Number of Wears: ", minimum)
  for key, value in dict.items():
    if value == minimum:
      print(key)
  return "****" # Aesthetic formatting 

def simple_sort(dict): # Lists in order of wears for one item category
  simple_sort = sorted(dict.items(), key = lambda x: x[1], reverse = False)
  return simple_sort

# Option 1 for creating outfits: using the least-worn items
def get_stats(category, dict1, dict2, max_wears):
  vals1 = [v for _, v in dict1.items()]
  vals2 = [v for _, v in dict2.items()]

  total_wears = sum(vals1) + sum(vals2)
  minimum_requirement = ceil(total_wears / max_wears)
  # Minimum number of items from a category required to not wear the same item twice per two-month period (or other length of time chosen by the user). Ceil is a conservative measure of how many items the user needs. For example, if they technically need half an item, to say they need 1 item instead of 0 errs on the side of caution. 
  for key, value in dict1.items():
    if key == "None":
      average = round(total_wears / len(dict2), 2)
      surplus = floor(-minimum_requirement) 
  # for key, value in dict2.items():
  #   if value == "None": 
  #     average = total_wears / len(dict1)
  #     surplus = 
    else:
      average = round(total_wears / (len(dict1) + len(dict2)), 2)
      surplus = floor(len(dict1) - minimum_requirement) # How many more items the user has versus what they need. A deficit would be displayed as a negative surplus. Floor function instead of rounding because fashion items are discrete, and floor is a more conservative measure than ceil (i.e., if you technically need half an item, having a -1 surplus instead of a 0 surplus -- that is, needing 1 item instead of 0 items -- is erring on the side of caution).
    all_items = len(dict1) + len(dict2)
    loss = len(dict2)
    loss_proportion = round(len(dict2) / all_items, 2)
    proportional_surplus = round(surplus / minimum_requirement, 2) 
  # Setting floating-point number precision to 2 decimal places for readability
  # The surplus as a proportion of the minimum items required is a standardized approach that weighs, for example, having two pairs of gloves when you only need one differently from having 10 dresses when you only need nine, despite the surpluses in each example being the same number of items.
    frequency = round(days_elapsed / total_wears, 2)
    if len(dict1) >= 61:
      years_until_new_buy = float('inf')
    elif proportional_surplus < 0:
      years_until_new_buy = 0
    else:
      years_until_new_buy = round ((frequency * ((NONREPEAT_PERIOD * total_wears - (len(dict1) + 1) * days_elapsed) / ((len(dict1) + 1) - NONREPEAT_PERIOD)) / 365), 2)
  print(category)
  print()
  print(get_items(dict1))
  for key, value in dict1.items():
    if value == "None":
      print("Total Items: 0")
    else:
      print("Total Items: ", len(dict1))
      break
  print("All Items: ", all_items)
  print("Loss: ", loss)
  print("Loss Percentage:", loss_proportion)
  print("Total Wears: ", total_wears)
  print("Average Wears: ", average)
  print("Minimum Requirement: ", minimum_requirement)
  print("Surplus: ", surplus)
  print("Proportional Surplus: ", proportional_surplus)
  print("Frequency: once every ", frequency, "days")
  print("Years Until New Buy: ", years_until_new_buy, "\n")
  print(simple_sort(dict1), "\n")
  return proportional_surplus

# Option 2 for creating outfits: random items
def outfit_generator(max_wears, *args): #which categories to include in the outfit
  for arg in args:
    item = choice(list(arg.items())) #selects a random item from each category
    print(item) 
  print("Max Wears: ", max_wears) #user can compare each item's wears to max_wears and choose not to wear those items that have already been worn the maximum number of times 

def what_to_buy(dict):
  sort = sorted(dict.items(), key = lambda x: x[1], reverse = False)
  print("What to Buy Next: ", sort)

def main():
  print("Days Elapsed: ", days_elapsed)
  #print("Worn every ", ceil(days_elapsed / total_wears))
  print("Nonrepeat Period: ", NONREPEAT_PERIOD, " days")
  max_wears = ceil(days_elapsed / NONREPEAT_PERIOD) # Maximum number of times the same item could be worn during the entire period, if it was worn only an average of once per two-month period
  print("Max Wears: ", max_wears)
  print()
  #variable_of_interest = input("Rank by: ")
  # Storing the proportional surplus stat as its own variable outside get_stats allows the what_to_buy function to use it later
  # Including items that were worn, but are no longer available to be worn now (damaged, lost, etc.) is important for accuracy of the number of wears in a category and the number of new items needed (i.e., how many unavailable items need to be replaced)
  dress_proportional_surplus = get_stats("Dresses", dresses, dresses_not_available, max_wears)
  jumpsuit_proportional_surplus = get_stats("Jumpsuits", jumpsuits, jumpsuits_not_available, max_wears)
  top_proportional_surplus = get_stats("Tops", tops, tops_not_available, max_wears)
  sweater_proportional_surplus = get_stats("Sweaters", sweaters, sweaters_not_available, max_wears)
  skirt_proportional_surplus = get_stats("Skirts", skirts, skirts_not_available, max_wears)
  shorts_proportional_surplus = get_stats("Shorts", shorts, shorts_not_available, max_wears)
  jeans_proportional_surplus = get_stats("Jeans", jeans, jeans_not_available, max_wears)
  pants_proportional_surplus = get_stats("Pants", pants, pants_not_available, max_wears)
  socks_proportional_surplus = get_stats("Socks", socks, socks_not_available, max_wears)
  hosiery_proportional_surplus = get_stats("Hosiery", hosiery, hosiery_not_available, max_wears)
  jacket_proportional_surplus = get_stats("Jackets", jackets, jackets_not_available, max_wears)
  light_coat_proportional_surplus = get_stats("Light Coats", light_coats, light_coats_not_available, max_wears)
  heavy_coat_proportional_surplus = get_stats("Heavy Coats", heavy_coats, heavy_coats_not_available, max_wears)
  shoes_proportional_surplus = get_stats("Shoes", shoes, shoes_not_available, max_wears)
  boots_proportional_surplus = get_stats("Boots", boots, boots_not_available, max_wears)
  ankle_boots_proportional_surplus = get_stats("Ankle Boots", ankle_boots, ankle_boots_not_available, max_wears)
  heels_proportional_surplus = get_stats("Heels", heels, heels_not_available, max_wears)
  flats_proportional_surplus = get_stats("Flats", flats, flats_not_available, max_wears)
  sandals_proportional_surplus = get_stats("Sandals", sandals, sandals_not_available, max_wears)
  sneakers_proportional_surplus = get_stats("Sneakers", sneakers, sneakers_not_available, max_wears)
  earrings_proportional_surplus = get_stats("Earrings", earrings, earrings_not_available, max_wears)
  necklaces_proportional_surplus = get_stats("Necklaces", necklaces, necklaces_not_available, max_wears)
  brooches_proportional_surplus = get_stats("Brooches", brooches, brooches_not_available, max_wears)
  ties_proportional_surplus = get_stats("Ties", ties, ties_not_available, max_wears)
  spring_scarves_proportional_surplus = get_stats("Spring Scarves", spring_scarves, spring_scarves_not_available, max_wears)
  winter_scarves_proportional_surplus = get_stats("Winter Scarves", winter_scarves, winter_scarves_not_available, max_wears)
  belts_proportional_surplus = get_stats("Belts", belts, belts_not_available, max_wears)
  bracelets_proportional_surplus = get_stats("Bracelets", bracelets, bracelets_not_available, max_wears)
  watches_proportional_surplus = get_stats("Watches", watches, watches_not_available, max_wears)
  rings_proportional_surplus = get_stats("Rings", rings, rings_not_available, max_wears)
  ponytail_proportional_surplus = get_stats("Ponytail", ponytail, ponytail_not_available, max_wears)
  clips_proportional_surplus = get_stats("Clips", clips, clips_not_available, max_wears)
  headbands_proportional_surplus = get_stats("Headbands", headbands, headbands_not_available, max_wears)
  utilitarian_headbands_proportional_surplus = get_stats("Utilitarian Headbands", utilitarian_headbands, utilitarian_headbands_not_available, max_wears)
  summer_hats_proportional_surplus = get_stats("Summer Hats", summer_hats, summer_hats_not_available, max_wears)
  winter_hats_proportional_surplus = get_stats("Winter Hats", winter_hats, winter_hats_not_available, max_wears)
  glasses_proportional_surplus = get_stats("Glasses", glasses, glasses_not_available, max_wears)
  eyeglasses_proportional_surplus = get_stats("Eyeglasses", eyeglasses, eyeglasses_not_available, max_wears)
  sunglasses_proportional_surplus = get_stats("Sunglasses", sunglasses, sunglasses_not_available, max_wears)
  masks_proportional_surplus = get_stats("Masks", masks, masks_not_available, max_wears)
  gloves_proportional_surplus = get_stats("Gloves", gloves, gloves_not_available, max_wears)
  umbrellas_proportional_surplus = get_stats("Umbrellas", umbrellas, umbrellas_not_available, max_wears)
  phone_cases_proportional_surplus = get_stats("Phone Cases", phone_cases, phone_cases_not_available, max_wears)
  handbags_proportional_surplus = get_stats("Handbags", handbags, handbags_not_available, max_wears)
  totes_proportional_surplus = get_stats("Totes", totes, totes_not_available, max_wears)
  shopping_totes_proportional_surplus = get_stats("Shopping Totes", shopping_totes, shopping_totes_not_available, max_wears)
  wallets_proportional_surplus = get_stats ("Wallets", wallets, wallets_not_available, max_wears)
  cosmetics_bags_proportional_surplus = get_stats("Cosmetics Bags", cosmetics_bags, cosmetics_bags_not_available, max_wears)
  coin_purses_proportional_surplus = get_stats("Coin Purses", coin_purses, coin_purses_not_available, max_wears)
  club_dresses_proportional_surplus = get_stats("Club Dresses", club_dresses, club_dresses_not_available, max_wears)
  evening_dresses_proportional_surplus = get_stats("Evening Dresses", evening_dresses, evening_dresses_not_available, max_wears)
  evening_jumpsuits_proportional_surplus = get_stats("Evening Jumpsuits", evening_jumpsuits, evening_jumpsuits_not_available, max_wears)
  evening_tops_proportional_surplus = get_stats("Evening Tops", evening_tops, evening_tops_not_available, max_wears)
  evening_skirts_proportional_surplus = get_stats("Evening Skirts", evening_skirts, evening_skirts_not_available, max_wears)
  evening_jackets_proportional_surplus = get_stats("Evening Jackets", evening_jackets, evening_jackets_not_available, max_wears)
  evening_shoes_proportional_surplus = get_stats("Evening Shoes", evening_shoes, evening_shoes_not_available, max_wears)
  evening_accessories_proportional_surplus = get_stats("Evening Accessories", evening_accessories, evening_accessories_not_available, max_wears)
  evening_bags_proportional_surplus = get_stats("Evening Bags", evening_bags, evening_bags_not_available, max_wears)
  workout_tops_proportional_surplus = get_stats("Workout Tops", workout_tops, workout_tops_not_available, max_wears)
  workout_bottoms_proportional_surplus = get_stats("Workout Bottoms", workout_bottoms, workout_bottoms_not_available, max_wears)
  swim_tops_proportional_surplus = get_stats("Swim Tops", swim_tops, swim_tops_not_available, max_wears)
  swim_bottoms_proportional_surplus = get_stats("Swim Bottoms", swim_bottoms, swim_bottoms_not_available, max_wears)
  beach_shoes_proportional_surplus = get_stats("Beach Shoes", beach_shoes, beach_shoes_not_available, max_wears)
  festival_proportional_surplus = get_stats("Festival", festival, festival_not_available, max_wears)
  st_patricks_day_proportional_surplus = get_stats("St. Patrick's Day", st_patricks_day, st_patricks_day_not_available, max_wears)
  easter_proportional_surplus = get_stats("Easter", easter, easter_not_available, max_wears)
  halloween_proportional_surplus = get_stats("Halloween", halloween, halloween_not_available, max_wears)
  christmas_proportional_surplus = get_stats("Christmas", christmas, christmas_not_available, max_wears)
  new_years_proportional_surplus = get_stats("New Year's", new_years, new_years_not_available, max_wears)

  print("Outfit 1\n")
  outfit_generator(max_wears, dresses, jackets, heels, earrings, necklaces, bracelets, watches, rings, ponytail, sunglasses, masks, totes)
  print("\n") # Creates space between sample outfits for readability

  print("Outfit 2\n")
  outfit_generator(max_wears, tops, skirts, light_coats, flats, earrings, spring_scarves, sunglasses, masks, totes)
  print("\n")

  print("Outfit 3\n")
  outfit_generator(max_wears, sweaters, pants, heavy_coats, boots, earrings, winter_scarves, winter_hats, sunglasses, masks, gloves, umbrellas, totes)
  print("\n")

  print("Outfit 4\n")
  outfit_generator(max_wears, tops, jeans, heavy_coats, sneakers, earrings, ponytail, sunglasses, masks, handbags, coin_purses)
  print("\n")

  print("Outfit 5\n")
  outfit_generator(max_wears, jumpsuits, ankle_boots, earrings, brooches, eyeglasses, masks, handbags)
  print("\n")

  print("Outfit 6\n")
  outfit_generator(max_wears, dresses, hosiery, flats, earrings, belts, headbands, glasses, sunglasses, masks, handbags)
  print("\n")

  print("Outfit 7\n")
  outfit_generator(max_wears, tops, pants, flats, earrings, ties, sunglasses, masks, totes)
  print("\n")

  print("Outfit 8\n")
  outfit_generator(max_wears, swim_tops, swim_bottoms, beach_shoes, summer_hats, sunglasses, shopping_totes)
  print("\n")

  print("Outfit 9\n")
  outfit_generator(max_wears, dresses, sandals, earrings, sunglasses, masks, handbags)
  print("\n")

  print("Outfit 10\n")
  outfit_generator(max_wears, evening_dresses, evening_jackets, evening_shoes, evening_accessories, evening_bags)
  print("\n")

  print("Outfit 11\n")
  outfit_generator(max_wears, evening_tops, evening_skirts, evening_shoes, evening_bags)
  print("\n")

  print("Outfit 12\n")
  outfit_generator(max_wears, evening_jumpsuits, evening_shoes, evening_bags)
  print("\n")

  categories = {"dresses": dress_proportional_surplus, "jumpsuits": jumpsuit_proportional_surplus, "tops": top_proportional_surplus, "sweaters": sweater_proportional_surplus, "skirts": skirt_proportional_surplus, "shorts": shorts_proportional_surplus, "jeans": jeans_proportional_surplus, "pants": pants_proportional_surplus, "socks": socks_proportional_surplus, "hosiery": hosiery_proportional_surplus, "jackets": jacket_proportional_surplus, "light coats": light_coat_proportional_surplus, "heavy coats": heavy_coat_proportional_surplus, "shoes": shoes_proportional_surplus, "ankle boots": ankle_boots_proportional_surplus, "heels": heels_proportional_surplus, "boots": boots_proportional_surplus, "flats": flats_proportional_surplus, "sandals": sandals_proportional_surplus, "sneakers": sneakers_proportional_surplus, "earrings": earrings_proportional_surplus, "necklaces": necklaces_proportional_surplus, "brooches": brooches_proportional_surplus, "ties": ties_proportional_surplus, "spring scarves": spring_scarves_proportional_surplus, "winter scarves": winter_scarves_proportional_surplus, "belts": belts_proportional_surplus, "bracelets": bracelets_proportional_surplus, "watches": watches_proportional_surplus, "rings": rings_proportional_surplus, "ponytail": ponytail_proportional_surplus, "clips": clips_proportional_surplus, "headbands": headbands_proportional_surplus, "utilitarian headbands": utilitarian_headbands_proportional_surplus, "summer hats": summer_hats_proportional_surplus, "winter hats": winter_hats_proportional_surplus, "glasses": glasses_proportional_surplus, "eyeglasses": eyeglasses_proportional_surplus, "sunglasses": sunglasses_proportional_surplus, "masks": masks_proportional_surplus, "gloves": gloves_proportional_surplus, "umbrellas": umbrellas_proportional_surplus, "phone cases": phone_cases_proportional_surplus, "handbags": handbags_proportional_surplus, "totes": totes_proportional_surplus, "shopping totes": shopping_totes_proportional_surplus, "wallets": wallets_proportional_surplus, "cosmetics bags": cosmetics_bags_proportional_surplus, "coin purses": coin_purses_proportional_surplus, "club dresses": club_dresses_proportional_surplus, "evening dresses": evening_dresses_proportional_surplus, "evening jumpsuits": evening_jumpsuits_proportional_surplus, "evening tops": evening_tops_proportional_surplus, "evening skirts": evening_skirts_proportional_surplus, "evening jackets": evening_jackets_proportional_surplus, "evening shoes": evening_shoes_proportional_surplus, "evening accessories": evening_accessories_proportional_surplus, "evening bags": evening_bags_proportional_surplus, "workout tops": workout_tops_proportional_surplus, "workout bottoms": workout_bottoms_proportional_surplus, "swim tops": swim_tops_proportional_surplus, "swim bottoms": swim_bottoms_proportional_surplus, "beach shoes": beach_shoes_proportional_surplus, "festival": festival_proportional_surplus, "St. Patrick's Day": st_patricks_day_proportional_surplus, "Easter": easter_proportional_surplus, "Halloween": halloween_proportional_surplus, "Christmas": christmas_proportional_surplus, "New Year's": new_years_proportional_surplus}

  # Write results to file
  with open('output.txt', 'w') as f:
    f.write("What to Buy Next:\n")
    what_to_buy_results = what_to_buy(categories)
    f.write(str(what_to_buy_results)) 

if __name__ == "__main__":
    main()