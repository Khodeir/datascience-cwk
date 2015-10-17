def clean_dataset(my_dataset):
	del(my_dataset['THE TRAVEL AGENCY IN THE PARK'])
	del(my_dataset['TOTAL'])
	my_dataset['BELFER ROBERT'].update({'deferred_income':-102500,
										'expenses':3285, 
										'director_fees':102500, 
										'total_payments':3285, 
										'restricted_stock' : 44093, 
										'restricted_stock_deferred' : 44093})
	my_dataset['BHATNAGAR SANJAY'].update({'expenses':137864,
										'total_payments':137864,
										'exercised_stock_options': 15456290,
										'restricted_stock':2604490,
										'restricted_stock_deferred':-2604490,
										'total_stock_value': 15456290})
	return my_dataset

