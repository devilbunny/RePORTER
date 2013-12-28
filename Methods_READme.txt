A collection of small scripts for answering the question of which residents get which grants and when.

Workflow (including program explanations)

1. RePorter-Wrangle.py
	takes a collection of .zip or .csv files in a given directory and puts them all into one
	large file.  only of subset of columns are taken to save on space.  this is also specified
	here.

2. Resident_Wrangle_____.py or Perimatch_Wrangle.py
	takes an ill-formatted list of graduates and attempts to extract information, including the 
	resident's name, institution, whether they have a PhD, graduation year, and subspecialty

3. Reporter_is_in.py
	takes the compiled RePorter .csv and the wrangled Resident list and does a merge, saving the
	file with the key 'RWG', meaning 'resident's with grants'  Matching is based on the last 
	name, and the first 3 letters of the first name.  Middle initials are not matched.

4, RWG_Wrangle
	Does two things, which should be separated.  First, it strips out non R, K, or F grants
	At this point, the file should be manually read to verify its validity
		For Perimatch, 36 residents with 102 grant*years were the result.
		Each resident was checked manually by searching the name of the resident and the 
		PI_NAME from RePorter using Google.  Searches either resulted in finding a 
		biography of the former resident on the website of the grant-hosting institution
		which included the training, or alternatively finding 2 biographies hosted on 
		the appropriate websites with different biographies or finding the biography of
		the PI listed in RePorter and verifying that the PI did not have the training 
		listed.  In general, spurious results were for 'R' type grants awarded shortly 
		after a trainee with no previous F or K grants, and the 'R' grants began their
		fellowship.

		Phillip Coffin seems to have been an investigator before begining his residency

		After checking, 13 residents remain with 23 grant*years
	
	Then the second stage can be run, which determines the year after/before graduation when
	a resident earned a grant, and the total grant money.  this can then be merged into the
	resident list.  this allows a comparison of grant-receiving and non-receiving graduates