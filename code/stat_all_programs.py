import json
import os

failed = 0
success = 0
results = []

for idx in range(0, 118389):
	if not os.path.exists('../data/all_programs/nt-{}.json'.format(idx)):
		print "nt-{}".format(idx)
"""
for prog in os.listdir('../data/all_programs/'):
	if prog.endswith('.json'):
		with open('../data/all_programs/' + prog, 'r') as f:
			data = json.load(f) 
		if len(data[3]) == 0:
			failed += 1
		else:
			success += 1

		results.append(data)
"""
#files = []
#with open('../READY/preprocessed_0.json') as f:
#	files.extend(json.load(f))
#with open('../READY/all_programs.json', 'w') as f:
#	json.dump(results, f)

#print "success: {}, failed: {}".format(success, failed)
