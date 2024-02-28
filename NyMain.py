from flask import Flask, request
from ClothingSuggestion import OutfitSelector
from SendRequest import PageController

app = Flask(__name__)
outfit_selector = OutfitSelector('clothing_dataset.csv')
page_controller = PageController()

@app.route('/api/request', methods=['POST'])
def handle_request():
    request_data = request.json
    if 'request_type' in request_data:
        if request_data['request_type'] == 'new_outfit':
            gender = request_data.get('gender', 'Men')
            usage = request_data.get('usage', 'Sports')
            weather = request_data.get('weather', 'Fall')
            topwear, bottomwear, footwear, watch, accessory = outfit_selector.select_outfit(gender, usage, weather)
            if topwear and bottomwear and footwear and watch and accessory:
                outfit = [topwear, bottomwear, footwear, watch, accessory]
                outfit_selector.save_outfit_collage(outfit, 'outfitPic')
                return {'message': 'New outfit suggested.', 'outfit': [item.name for item in outfit]}, 200
            else:
                return {'message': 'No suitable outfit found for the specified criteria.'}, 404
        elif request_data['request_type'] == 'change_page':
            target_page = request_data.get('target_page', 1)
            page_controller.change_page(target_page)
            return {'message': f'Page changed to {target_page}'}, 200
        else:
            return {'message': 'Invalid request type.'}, 400
    else:
        return {'message': 'Request type not specified.'}, 400

if __name__ == "__main__":
    app.run(debug=True)
