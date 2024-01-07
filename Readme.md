1. Copy I2_Test data folder (which contains images) to docvisor/example/data/FullyAutomatic/I2/I2_Test/
2.a. Copy The prediction files to docvisor/example/data/FullyAutomatic/I2/I2_Test/
2.b. Set the ground truth and prediction file path in i2_to_docvisor_json_converter.py
3. To convert I2 json to Docvisor json, run python i2_to_docvisor_json_converter.py
4. To run docvisor, create and activate conda environment from requirments.txt
./run.sh