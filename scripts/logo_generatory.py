from random import shuffle
from urllib.parse import quote
from palettable.tableau import Tableau_20 as palette

tools = [('IntelliJ IDEA', 'intellijidea'), ('AWS', 'amazonaws'), ('GCP', 'googlecloud'), ('Azure', 'microsoftazure'), 
('scikit-learn', 'scikitlearn'), ('TensorFlow', 'tensorflow'), ('PyTorch', 'pytorch'), ('Apache Spark', 'apachespark'),
('Jupyter', 'jupyter'), ('Terraform', 'terraform')]

colors = [x.replace('#', '').lower() for x in palette.hex_colors]
shuffle(colors)


for i, (message, logo) in enumerate(tools):
    print(f'![{message}](https://img.shields.io/static/v1?style=for-the-badge&logo={quote(logo)}&message={quote(message)}&label=&color={colors[i]}&labelColor=000000)')
    
