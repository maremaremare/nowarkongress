def loadmysigns():
	from content.models import Petition, OuterParticipant
	f = open('freedom.txt', 'r')
	pe = Petition.objects.get(id=6)
	fstr = f.read()
	flist = fstr.split(', ')
	for x in flist:
	    print x
	    namelist = x.split(' ')
	    first_name = namelist[0]
	    second_name = namelist[1]
	    try:
	        sign, created = OuterParticipant.objects.get_or_create(first_name=first_name, second_name=second_name)
	        pe.outerparticipants.add(sign)
	        pe.save()
	        print 'ok'
	    except:
	        raise
	f.close()

