import random
import subprocess
import json
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Produces JSON from images or PDFs of medical records.')
    parser.add_argument('PATH', help='path to document in image or PDF format')
    args = parser.parse_args()

    try:
        our_json = run(path=args.PATH)
        output = {
            'status': 'success',
            'result': our_json
        }
    except Exception as e:
        output = {
            'status': 'failure',
            'error': str(e),
        }
    json.dump(output, sys.stdout)
    print()

def run(path):
    api_json = parse_document(path, use_api=False)
    our_json = preprocess_json(api_json)
    return our_json

def parse_document(path, use_api=True):
    ''' Use IBM's Compare/Comply API to extract meaningful information from a document provided in image or PDF format. '''
    if use_api:
        apikey = open('api-keys/comply-compare').read().strip()
        ascii_bytes = subprocess.check_output([
            'curl',
            '-X', 'POST',
            '-u', f'apikey:{apikey}'
            '-F', f'file=@{path}',
            'https://gateway.watsonplatform.net/compare-comply/api/v1/element_classification?version=2018-10-15',
        ])
        return json.loads(ascii_bytes)
    else:
        return json.load(open('data/example-form.json'))

def preprocess_json(d):
    ''' Take JSON produced by IBM's compare/comply API, and produce the JSON we use in our database. '''
    # For now just produce randomized data, because IBM's document reader
    # doesn't give us the kind of fields we need. (it's for business contracts)
    _ = d

    allergies = []
    while True:
        if random.random() < 0.75:
            break
        allergies.append(random.choice(['peanuts', 'milk', 'tree nuts', 'soy', 'sea lions']))
    allergies = sorted(set(allergies))

    vaccines = []
    while True:
        if random.random() < 0.50:
            break
        vaccines.append({
            'vaccine': random.choice(['tetanus', 'polio', 'rabies', 'influenza', 'purple']),
            'date': f'{random.randrange(2000,2020)}-{random.randrange(1,13):02}-{random.randrange(1,28):02}',
        })
    vaccines = sorted(vaccines, key=lambda x: x['date'])

    return {
        'allergies': allergies,
        'vaccines': vaccines,
    }

if __name__ == '__main__':
    main()
