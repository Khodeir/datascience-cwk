
def feature_engineering(data_dict):
    feature_names = ['poi','salary',
     'to_messages',
     'deferral_payments',
     'total_payments',
     'exercised_stock_options',
     'bonus',
     'director_fees',
     'restricted_stock_deferred',
     'total_stock_value',
     'expenses',
     'from_poi_to_this_person',
     'loan_advances',
     'from_messages',
     'other',
     'from_this_person_to_poi',
     'deferred_income',
     'shared_receipt_with_poi',
     'restricted_stock',
     'long_term_incentive']
    def add_feature(name, ffun):
        feature_names.append(name)
        for p, pdata in data_dict.items():
            try:
                pdata[name] = ffun(pdata)
            except TypeError:
                pdata[name] = 'NaN'
    # the proportion of sent emails addressed to pois
    add_feature('prop_to_poi', 
            lambda x: 1. * x['from_this_person_to_poi'] / x['from_messages'])

    # the proporiton of received emails from pois
    add_feature('prop_from_poi', 
            lambda x: 1. * x['from_poi_to_this_person'] / x['to_messages'])

    # the proporiton of received emails shared with pois
    add_feature('prop_shared_with_poi', 
            lambda x: 1. * x['shared_receipt_with_poi'] / x['to_messages'])

    # the proporiton of exercised stock options
    add_feature('prop_exercised_stock', 
            lambda x: 1. * x['exercised_stock_options'] / x['total_stock_value'])

    # the proporiton of exercised stock to restricted stock
    add_feature('prop_rest_stock', 
            lambda x: 1. * x['exercised_stock_options'] / x['restricted_stock'])

    return data_dict, feature_names
