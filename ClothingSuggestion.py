import pandas as pd
import random
import matplotlib.pyplot as plt
from PIL import Image

class ClothingItem:
    def __init__(self, name, masterCategory, subCategory, season, usage, gender, id):
        self.name = name
        self.masterCategory = masterCategory
        self.subCategory = subCategory
        self.season = season
        self.usage = usage
        self.gender = gender
        self.id = id
        self.image_path = f"F:/Programming/Smart_Mirror/images/{self.id}.jpg"

class OutfitSelector:
    def __init__(self, dataset_file):
        self.dataset = self.load_dataset(dataset_file)
        self.outfit_options = []

    def load_dataset(self, dataset_file):
        df = pd.read_csv(dataset_file)
        dataset = []
        for _, row in df.iterrows():
            item = ClothingItem(row['productDisplayName'], row['masterCategory'], row['subCategory'], 
                                row['season'], row['usage'], row['gender'], row['id'])
            dataset.append(item)
        return dataset



    def select_outfit(self, gender, usage, weather):
        # Filter dataset based on gender, usage, and season
        filtered_clothes = [item for item in self.dataset if item.gender == gender 
                            and item.usage == usage 
                            and item.season == weather]
        
        # Select items for outfit (at least one topwear, one bottomwear, one footwear)
        topwear = random.choice([item for item in filtered_clothes 
                                if item.masterCategory == 'Apparel' 
                                and item.subCategory == 'Topwear'])
        bottomwear = random.choice([item for item in filtered_clothes 
                                    if item.masterCategory == 'Apparel' 
                                    and item.subCategory == 'Bottomwear'])
        footwear = random.choice([item for item in filtered_clothes 
                                if item.masterCategory == 'Footwear' 
                                and item.subCategory == 'Shoes'])
        
        # Always recommend one watch
        watch = random.choice([item for item in self.dataset if item.gender == gender
                            if item.masterCategory == 'Accessories' 
                            and item.subCategory == 'Watches'])

        # Randomly select one additional accessory
        additional_accessories = ['Caps', 'Handbags', 'Belts', 'Sunglasses']
        if gender == 'Women':
            additional_accessories.append('Earrings')
        accessory = random.choice([item for item in self.dataset if item.gender == gender
                                if item.masterCategory == 'Accessories' 
                                and item.subCategory in additional_accessories])

        return topwear, bottomwear, footwear, watch, accessory


    def show_outfit_collage(self, outfit):
        fig, axes = plt.subplots(1, len(outfit), figsize=(12, 4))
        fig.suptitle('Outfit of the Day', fontsize=16, weight='bold')
        plt.subplots_adjust(wspace=0.3)

        max_name_length = 25  # Maximum length for the name of the clothing item
        max_fontsize = 12  # Maximum font size for the title

        for ax, item in zip(axes, outfit):
            img = Image.open(item.image_path)
            ax.imshow(img)
            ax.axis('off')

            # Truncate the name of the clothing item if it exceeds the maximum length
            truncated_name = item.name[:max_name_length] + '...' if len(item.name) > max_name_length else item.name

            # Calculate font size based on the length of the truncated name
            fontsize = max_fontsize - len(truncated_name) * 0.8
            fontsize = max(fontsize, 8)  # Ensure minimum font size

            ax.set_title(truncated_name, fontsize=fontsize, weight='bold', pad=2)
            ax.set_aspect('auto')

            # Add transparent overlay with text for better readability
            ax.text(0.5, 0.5, item.subCategory, ha='center', va='center', fontsize=8, weight='bold',
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

        plt.show()


# Example usage:
outfit_selector = OutfitSelector('clothing_dataset.csv')

# Get today's weather (assumed here)
weather_today = 'Fall'
gender = 'Men'
usage = 'Sports'

# Select outfit based on gender, usage, and weather
topwear, bottomwear, footwear, watch, accessory = outfit_selector.select_outfit(gender, usage, weather_today)

if topwear and bottomwear and footwear and watch and accessory:
    outfit = [topwear, bottomwear, footwear, watch, accessory]
    print("Recommended outfit for today's", gender, usage, "and", weather_today, "weather:")
    for item in outfit:
        print("Item:", item.name)
        print("Category:", item.subCategory)
    outfit_selector.show_outfit_collage(outfit)
else:
    print("No suitable outfit found for today's", gender, usage, "and", weather_today, "weather.")
