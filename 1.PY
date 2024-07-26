import pandas as pd
import numpy as np

# Load care areas and metadata
care_areas = pd.read_csv(r'C:\Users\ivsah\OneDrive\Documents\KLA\hackathon\Milestone1\Dataset-0\1st\CareAreas.csv', header=None)
care_areas.columns = ['id', 'x1', 'x2', 'y1', 'y2']

metadata = pd.read_csv(r'C:\Users\ivsah\OneDrive\Documents\KLA\hackathon\Milestone1\Dataset-0\1st\metadata.csv')
main_field_size = metadata['Main Field Size'].iloc[0]
sub_field_size = metadata['Sub Field size'].iloc[0]

# Generate main fields from care areas
def generate_main_fields_from_care_areas(care_areas, main_field_size):
    main_fields = []
    for _, row in care_areas.iterrows():
        x1, x2, y1, y2 = row['x1'], row['x2'], row['y1'], row['y2']
        main_fields.append([x1, x1 + main_field_size, y1, y1 + main_field_size])
    return pd.DataFrame(main_fields, columns=['x1', 'x2', 'y1', 'y2'])

main_fields_minimal = generate_main_fields_from_care_areas(care_areas, main_field_size)

def generate_sub_fields_from_care_areas(care_areas, sub_field_size):
    sub_fields = []
    sub_field_size = float(sub_field_size)  
    for _, row in care_areas.iterrows():
        x1, x2, y1, y2 = float(row['x1']), float(row['x2']), float(row['y1']), float(row['y2'])
        
        subfields_x = (x2 - x1) // sub_field_size
        if (x2 - x1) % sub_field_size != 0:
            subfields_x += 1
            
        subfields_y = (y2 - y1) // sub_field_size
        if (y2 - y1) % sub_field_size != 0:
            subfields_y += 1
        
        for i in range(int(subfields_x)):

            for j in range(int(subfields_y)):
                sub_x1 = x1 + i * sub_field_size
                sub_y1 = y1 + j * sub_field_size
                sub_x2 = (sub_x1 + sub_field_size, x2)
                sub_y2 = (sub_y1 + sub_field_size, y2)
                sub_fields.append([sub_x1, sub_x2, sub_y1, sub_y2, row['id']])
    
    return pd.DataFrame(sub_fields, columns=['x1', 'x2', 'y1', 'y2', 'CareArea ID'])

sub_fields = generate_sub_fields_from_care_areas(care_areas, sub_field_size)

# Output results without header
main_fields_minimal.to_csv(r'C:\Users\ivsah\OneDrive\Documents\KLA\hackathon\Milestone1\Dataset-0\1st\MainFieldsOP.csv', index_label='ID', header=False)
sub_fields.to_csv(r'C:\Users\ivsah\OneDrive\Documents\KLA\hackathon\Milestone1\Dataset-0\1st\SubFieldsOP.csv', index_label='ID', header=False)

# Print number of fields
print("Number of Main Fields:", len(main_fields_minimal))
print("Number of Sub Fields:", len(sub_fields))
