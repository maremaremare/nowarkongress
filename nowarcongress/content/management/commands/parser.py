from content.models import *
f = open('myfile.txt', 'r')


for line in f:
	try:
	    name = line.split(',')[0]
	    first_name = name.split(' ')[0]
	    second_name = name.split(' ')[1]
	    occupationlist = line.split(',')[1:]
	    occupation = ",".join(occupationlist)[1:].replace('\n','')
	    signature, created = OuterParticipant.objects.get_or_create(first_name=first_name, second_name=second_name, occupation=occupation)
	    
	    petition = Petition.objects.get(id=5)
	    petition.outerparticipants.add(signature)
	    petition.save()
	except:
		raise


f.close()