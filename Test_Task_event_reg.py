import json

class TEST:

    def test_task_event(self):
        registrant = [{
                  "registrant":
                     {
                        "name": "Tom Jones",
                        "email": "tom@jones.com",
                        "phone": "3211234567",
                     },

                },
                {
                    "registrant":
                        {
                            "name": "Lucy Liu",
                            "email": "lucy@liu.com",
                            "phone": "",
                        },

                },
                {
                    "registrant":
                        {
                            "name": "Doug",
                            "email": "doug@emmy.com",
                            "phone": "4564445556",
                        },

                },
              {
                    "registrant":
                        {
                            "name": "Uma Thurman",
                            "email": "uma@thurs.com",
                            "phone": "",
                        },

                },
           ]
        registrant_json = json.dumps(registrant)


        contact_list_model = {'contacts' :  [ { "name": "Alice Brown", "email": "","phone": "1231112223"},
                                              {"name": "Bob Crown","email": "bob@crowns.com", "phone": "", },
                                              {"name": "Carlos Drew","email": "carl@drewess.com", "phone": "3453334445", },
                                              {"name": "Doug Emerty","email": "", "phone": "4564445556", },
                                              {"name": "Egan Fair","email": "eg@fairness.com", "phone": "5675556667", },
                                             ] ,
                              'leads_list':[ { "name": "", "email": "kevin@keith.com","phone": ""},
                                              {"name": "Lucy","email": "lucy@liu.com", "phone": "3210001112", },
                                              {"name": "Mary Middle","email": "mary@middle.com", "phone": "3331112223", },
                                              {"name": "","email": "", "phone": "4442223334", },
                                              {"name": "","email": "ole@olson.com", "phone": "ole@olson.com", },
                                             ]
                              }
        data_of_registrant = json.loads(registrant_json)
        existed = []
        for data in data_of_registrant:
            email = data['registrant']['email'] if data['registrant']['email'] else  False
            phone  = data['registrant']['phone'] if data['registrant']['phone'] else  False
            is_existed = dict(existed=False)
            if email:
                email_exist = filter(lambda contact: contact['email'] == email , contact_list_model['contacts'])
                if email_exist:
                    is_existed.update(existed=True)
                existed += email_exist
            if phone:
                phone_exist = filter(lambda contact: contact['phone'] == phone, contact_list_model['contacts'])
                if phone_exist:
                    is_existed.update(existed=True)
                existed += phone_exist

            if  not is_existed['existed']:
                    leads_list = filter(lambda contact: contact['email'] == email and contact['email'] != False or \
                                                          contact['phone'] == phone and contact['phone'] != False
                                          , contact_list_model['leads_list'])
                    if leads_list:

                        existed += leads_list
                        if leads_list[0] in contact_list_model['leads_list']:

                            contact_list_model['leads_list'].remove(leads_list[0])

                            contact_list_model['contacts'].append(leads_list[0])

        return existed

