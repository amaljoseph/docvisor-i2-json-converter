import json
import os
import sys

# Load and Save Json Files
def load_json_file(file_path):
    json_file = open(file_path, 'r')
    json_data = json_file.read()
    return json.loads(json_data)

def save_json_file(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)

# Create DocVisor Specific Json Format
def create_region_dict(document_id, collection, region_label, ground_truth, model_prediction):
    # each region/polygon coordinates and metrics.
    region =  {
        'groundTruth': ground_truth, 
        'modelPrediction': model_prediction, 
        'regionLabel': region_label, 
        'metrics': {'iou': 0, 'hd': 0}, 
        'id': document_id, 
        'collection': collection,
        }
    # 'metrics': metric, 
    return region

def create_regions_list(document_id, collection, region_label, ground_truths, model_predictions):
    # A document/ image has multiple regions/ polygons.
    regions = []
    for ground_truth, model_prediction in zip(ground_truths, model_predictions):
        region = create_region_dict(document_id, collection, region_label, ground_truth, model_prediction)
        regions.append(region)
    return regions


# Load and Extract Data From I2 Dataset Json File.
def extract_gt_annotations(json_data):
    image_path = json_data['imgPath']
    ground_truths = json_data['gdPolygons']
    return image_path, ground_truths

def extract_prediction_annotations(json_data):
    model_predictions = json_data['predPolygons']
    metrics = json_data['score']
    return model_predictions, metrics

if __name__ == '__main__':
    gt_json_path = 'docvisor/example/data/FullyAutomatic/I2/I2_Test/I2_TEST.json'
    predictions_json_path = 'docvisor/example/data/FullyAutomatic/I2/I2_Test/V2-BIN-SCR-VIS.json'
    json_save_path = 'docvisor/example/jsonData/FullyAutomatic/I2/I2_TEST_converted.json'
    
    gt_json_data = load_json_file(gt_json_path)
    predictions_json_data = load_json_file(predictions_json_path)

    collection = 'I2'
    region_label = 'Character Line Segment'
    
    documents = {}
    for gt, predictions in zip(gt_json_data, predictions_json_data):
        # iterating through each document/ image in the json file.
        image_path, ground_truths = extract_gt_annotations(gt)
        image_path = 'example/data/FullyAutomatic/' + image_path[1:]
        document_id = image_path
        model_predictions, metrics = extract_prediction_annotations(predictions)
        regions = create_regions_list(document_id, collection, region_label, ground_truths, model_predictions)
        documents[document_id] = {
            'imagePath': image_path,
            'regions': regions
        }
    save_json_file(documents, json_save_path)