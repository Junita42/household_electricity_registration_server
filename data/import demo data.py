import csv

def generate_sql_inserts(csv_filepath, sql_filepath):
    with open(csv_filepath, 'r') as csvfile, open(sql_filepath, 'w') as sqlfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row

        for row in reader:
            try:
                postal_code, city, state, latitude, longitude = row
                sql = f"INSERT INTO Valid_Postal (postal_code, city, state, latitude, longitude) VALUES ('{postal_code}', '{city}', '{state}', {latitude}, {longitude});\n"
                sqlfile.write(sql)
            except Exception as e:
                print(f"Error processing row {row}: {e}")

if __name__ == "__main__":
    csv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/postal_codes.csv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/postal_codes_inserts.sql'
    generate_sql_inserts(csv_path, sql_path)

import csv
def generate_household_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')

        for row in reader:
            email = row['email'].replace("'", "''")  # Escape single quotes
            household_type = row['household_type']
            postal = row['postal_code']
            sqft = row['footage']
            offgrid_flag = 1 if row['utilities'] else 0

            sql_insert = f"INSERT INTO Household (email, household_type, postal, sqft, offgrid_flag) VALUES ('{email}', '{household_type}', '{postal}', {sqft}, {offgrid_flag});\n"
            sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Household.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_household.sql'

    generate_household_inserts(tsv_path, sql_path)


def generate_appliance_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')

        for row in reader:
            email = row['household_email'].replace("'", "''")  # Escape single quotes
            seq_num = row['appliance_number']
            manufacturer = row['manufacturer_name'].replace("'", "''")
            model_name = row['model'].replace("'", "''") if row['model'] else ''
            btu = row['btu']

            sql_insert = f"INSERT INTO Appliance (email, seq_num, manufacturer, model_name, BTU) VALUES ('{email}', {seq_num}, '{manufacturer}', '{model_name}', {btu});\n"
            sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Appliance.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_appliance.sql'

    generate_appliance_inserts(tsv_path, sql_path)

def generate_manufacturer_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')

        for row in reader:
            manufacturer_name = row['manufacturer_name'].replace("'", "''")  # Escape single quotes


            sql_insert = f"INSERT INTO Manufacturer (manufacturer_name) VALUES ('{manufacturer_name}');\n"
            sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Manufacturer.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_manufacturer.sql'

    generate_manufacturer_inserts(tsv_path, sql_path)

import csv

def generate_air_handler_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')

        for row in reader:
            if row['appliance_type'] == 'air_handler':
                email = row['household_email'].replace("'", "''")  # Escape single quotes
                seq_num = row['appliance_number'] 
                RPM = row['rpm']

                sql_insert = f"INSERT INTO Air_Handler (email, seq_num, RPM) VALUES ('{email}', {seq_num}, {RPM});\n"
                sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Appliance.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_air_handler.sql'

    generate_air_handler_inserts(tsv_path, sql_path)

def generate_ac_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')

        for row in reader:
            if row['appliance_type'] == 'air_handler' and 'air_conditioner' in row['air_handler_types']:
                email = row['household_email'].replace("'", "''")  # Escape single quotes
                air_handler_seq_num = row['appliance_number'] 
                EER = row['eer']

                sql_insert = f"INSERT INTO AC (email, air_handler_seq_num, EER) VALUES ('{email}', {air_handler_seq_num}, {EER});\n"
                sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Appliance.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_AC.sql'
    generate_ac_inserts(tsv_path, sql_path)


def generate_heater_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')

        for row in reader:
            if row['appliance_type'] == 'air_handler' and 'heater' in row['air_handler_types']:
                email = row['household_email'].replace("'", "''")  # Escape single quotes
                air_handler_seq_num = row['appliance_number'] 
                energy_source = row['energy_source']

                sql_insert = f"INSERT INTO Heater (email, air_handler_seq_num, energy_source) VALUES ('{email}', {air_handler_seq_num},'{energy_source}');\n"
                sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Appliance.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_heater.sql'
    
    generate_heater_inserts(tsv_path, sql_path)

def generate_heatpump_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')

        for row in reader:
            if row['appliance_type'] == 'air_handler' and 'heatpump' in row['air_handler_types']:
                email = row['household_email'].replace("'", "''")  # Escape single quotes
                air_handler_seq_num = row['appliance_number'] 
                SEER = row['seer']
                HSPF = row['hspf']

                sql_insert = f"INSERT INTO Heat_Pump (email, air_handler_seq_num, SEER, HSPF) VALUES ('{email}', {air_handler_seq_num},{SEER}, {HSPF});\n"
                sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Appliance.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_heatpump.sql'
    
    generate_heatpump_inserts(tsv_path, sql_path)

def generate_water_heater_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')

        for row in reader:
            if row['appliance_type'] == 'water_heater':
                email = row['household_email'].replace("'", "''")
                seq_num = row['appliance_number']
                tank_size = row['tank_size']
                energy_source = row['energy_source'].replace(" ", "_")
                current_temp = row['temperature'] if row['temperature'] else 'NULL'
            
                sql_insert =f"INSERT INTO Water_Heater (email, seq_num, tank_size, energy_source, current_temp) VALUES ('{email}', {seq_num}, {tank_size}, '{energy_source}', {current_temp});\n"
                sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Appliance.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_water_heater.sql'
    
    generate_water_heater_inserts(tsv_path, sql_path)


def generate_power_generator_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.reader(tsv_file, delimiter='\t')
        next(reader)  # Skip the header row

        for row in reader:
            email = row[0].replace("'", "''")  # Escape single quotes
            seq_num = row[1]
            energy_source = row[2].replace("'", "''")
            kilowatt_hours = row[3]
            battery_storage = row[4] if row[4] else 'NULL'

            sql_insert = f"INSERT INTO Power_Generator (email, seq_num, energy_source, kilowatt_hours, battery_storage) VALUES ('{email}', {seq_num}, '{energy_source}', {kilowatt_hours}, {battery_storage});\n"   
            sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Power.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_power_generator.sql'
    
    generate_power_generator_inserts(tsv_path, sql_path)

def generate_public_utility_inserts(tsv_file_path, output_sql_file_path):
    with open(tsv_file_path, 'r') as tsv_file, open(output_sql_file_path, 'w') as sql_file:
        reader = csv.DictReader(tsv_file, delimiter='\t')
        next(reader)  # Skip the header row

        for row in reader:
            email = row['email'].replace("'", "''")  # Escape single quotes
            utilities_type =row['utilities']

            sql_insert = f"INSERT INTO Public_Utilities (email, utilities_type) VALUES ('{email}', '{utilities_type}');\n"        
            sql_file.write(sql_insert)

if __name__ == "__main__":
    tsv_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data/Household.tsv'
    sql_path = '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_public_utility.sql'
    
    generate_public_utility_inserts(tsv_path, sql_path)




def combine_sql_files(file_paths, combined_file_path):
    with open(combined_file_path, 'w') as combined_file:
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                combined_file.write(file.read() + "\n\n")

if __name__ == "__main__":
    file_paths = [
        '/Users/junita/Documents/projects/electricity_fastapi/data/postal_codes_inserts.sql',
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_manufacturer.sql',
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_household.sql',
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_appliance.sql',
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_water_heater.sql',
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_air_handler.sql',
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_AC.sql',
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_heatpump.sql',
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_heater.sql',
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_power_generator.sql',  
        '/Users/junita/Documents/projects/electricity_fastapi/data/Demo_Data_public_utility.sql', 
    ]
    combined_file_path ='/Users/junita/Documents/projects/electricity_fastapi/data/demo_data.sql'

    combine_sql_files(file_paths, combined_file_path)
