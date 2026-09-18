"""Regenerate locations.data.js from locations.json.

locations.json is the source of truth. locations.data.js is a plain <script>-loadable
copy so the pages also work when opened directly from disk (file:// blocks fetch).
Run this after editing locations.json:  python make-data.py
"""
import json

with open('locations.json', encoding='utf-8') as f:
    data = json.load(f)

lines = [
    '// AUTO-GENERATED from locations.json — do not edit by hand.',
    '// Regenerate with: python make-data.py',
    'window.LOCATIONS = [',
]
lines += ['  { "id": "%s", "lat": %s, "lng": %s },' % (d['id'], d['lat'], d['lng']) for d in data]
lines += ['];', '']

with open('locations.data.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'wrote locations.data.js ({len(data)} locations)')
