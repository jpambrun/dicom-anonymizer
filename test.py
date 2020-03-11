import dicomanonymizer.anonymizer


def ActionNameNotReferenced(dataset, tag, seed):
  pass
	# print('here', seed)

actionsTagMap = {
	(0x0002, 0x0002): ActionNameNotReferenced,
  (0x0010, 0x0010): ActionNameNotReferenced,
}
actionsMap = dicomanonymizer.anonymizer.generateActionsDictionary(actionsTagMap)


dicomanonymizer.anonymizer.anonymize('in/', 'out/', actionsMap)
