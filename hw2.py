import glob, json, sys

path_in = sys.argv[1]
path_out = sys.argv[2]

dump = {}
curent_v = 0



import_files = glob.glob(path_in+'*.json')


for file in import_files:
    fp = open(file)
    encod_file = json.load(fp)
    if float(encod_file['number']) > curent_v and encod_file['result'] != 0:
        dump["id"] = encod_file['id']
        dump["number"] = encod_file['number']
        dump["committer_name"] = encod_file['committer_name']
        dump["committer_email"] = encod_file['committer_email']
        curent_v = int(encod_file['number'])


with open(path_out, 'w') as outfile:
    json.dump(dump, outfile)


print('Create file %s with json necessary dump from folder %s*' %(path_out, path_in))
