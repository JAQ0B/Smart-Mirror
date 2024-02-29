from flask import Flask, request
from ClothingSuggestion import OutfitSelector
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
            usage = request_data.get('usage', 'Casual')
            weather = request_data.get('weather', 'Fall')
            outfit_selector.recommend_outfit(weather, gender, usage)
            return {'message': 'New outfit suggested.'}, 200            
        elif request_data['request_type'] == 'change_page':
            target_page = request_data.get('target_page', 1)
            page_controller.change_page(target_page)
            return {'message': f'Page changed to {target_page}'}, 200
        else:
            return {'message': 'Invalid request type.'}, 400
    else:
        return {'message': 'Request type not specified.'}, 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)


