# Horrible horrible test db that should be replaced with a SQL server

import json
import os

# FIXME: Should be somewhere in e.g. /var or owned by a limited user
DEFAULT_PATH = 'patient-db.json'

# FIXME: This solution doesn't scale to large-scale concurrent usage.
#        (it will inevitably encounter data loss due to race conditions)
def insert_row(path, row):
    if os.path.exists(path):
        with open(path) as f:
            d = json.load(f)
    else:
        d = { 'patients': [] }

    # FIXME should validate fields of row

    patient_id = len(d['patients'])
    d['patients'].append(row)

    with open(path, 'w') as f:
        json.dump(d, f)

    return patient_id

def read_row(path, patient_id):
    with open(path) as f:
        d = json.load(f)

    return d['patients'][patient_id]

def find_patient_by_email(path, email):
    with open(path) as f:
        d = json.load(f)

    for patient_id, record in enumerate(d['patients']):
        if record['email'] == email:
            return patient_id

    raise ValueError(f'no patient with email: {email}')
