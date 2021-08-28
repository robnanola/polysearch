"""
Service area related tests
"""

import json

from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from providers.models import Provider
from .models import ServiceArea


class ServiceAreaTestCase(APITestCase):
    """
    Test cases for ServiceArea creation and search.
    """
    def setUp(self):
        """
        Setup initial providers and service areas
        """
        providers = [
            {"name": "Test Provider",
            "email": "user@test.com",
            "phone_number": "+639178872255",
            "language": "EN",
            "currency": "PHP"},
            {"name": "Test Provider 2",
            "email": "user2@test.com",
            "phone_number": "+639771166005",
            "language": "EN",
            "currency": "PHP"},
        ]
        for provider in providers:
            Provider.objects.create(**provider)

        service_areas = [
            {"provider": Provider.objects.get(name='Test Provider'),
            "name": "Zone 1",
            "price": "5.50",
            "zone": {
                "type":"Polygon",
                "coordinates": [[[9.531999799157633,55.70983677322995],
                    [9.5333087171569,55.7098488621418],
                    [9.535969468499674,55.70923232286865],
                    [9.535733434106364,55.707576080964074],
                    [9.532536240960612,55.70786623060356],
                    [9.531270238305583,55.70786623060356],
                    [9.531785222436442,55.70976423968035],
                    [9.531999799157633,55.70983677322995]]]
                }
            },
            {"provider": Provider.objects.get(name='Test Provider 2'),
            "name": "Zone 2",
            "price": "5.50",
            "zone": {
                "type":"Polygon",
                "coordinates": [[[9.528995725060954,55.70780578293966],
                    [9.532471867944254,55.70779369339567],
                    [9.532922479058756,55.70774533518228],
                    [9.532407494927897,55.70590767872433],
                    [9.528909894372477,55.705677965590375],
                    [9.528995725060954,55.70780578293966]]]
                }
            },
            {"provider": Provider.objects.get(name='Test Provider'),
            "name": "Zone 3",
            "price": "5.50",
            "zone": {
                "type":"Polygon",
                "coordinates": [[[9.528824063684,55.70779369339567],
                    [9.528738232995524,55.7056416949721],
                    [9.522687169457926,55.70542407055541],
                    [9.52260133876945,55.70654845032922],
                    [9.523051949883952,55.706560540258494],
                    [9.527729722405924,55.70785414107824],
                    [9.528824063684,55.70779369339567]]]
                }
            },
            {"provider": Provider.objects.get(name='Test Provider 2'),
            "name": "Zone 4",
            "price": "5.50",
            "zone": {
                "type":"Polygon",
                "coordinates": [[[9.523091985414561,55.711944878298056],
                    [9.52261991662794,55.706686130682144],
                    [9.52311344308668,55.706674040791704],
                    [9.524422361085948,55.707012556309614],
                    [9.525752736757335,55.707375248253],
                    [9.526911451051769,55.70770166812365],
                    [9.527748300264415,55.707919279855794],
                    [9.52888555688673,55.70790719034692],
                    [9.529164506624278,55.708620464970664],
                    [9.529486371706065,55.70887433923704],
                    [9.53038759393507,55.709333726573526],
                    [9.531052781770763,55.709684308012186],
                    [9.531524850557384,55.70993817536607],
                    [9.531696511934337,55.710034886305074],
                    [9.532468988130626,55.71120748739218],
                    [9.53313417596632,55.712513022453734],
                    [9.534202879589797,55.71446151042045],
                    [9.53413850657344,55.71454612270779],
                    [9.533494776409865,55.714739521533446],
                    [9.532936876934768,55.71488457002432],
                    [9.531220263165237,55.71315604047478],
                    [9.53089839808345,55.71297472175409],
                    [9.528838461560012,55.71201976260393],
                    [9.528731173199416,55.711874703475566],
                    [9.528495138806106,55.711874703475566],
                    [9.528323477429153,55.711959321365924],
                    [9.52615625254512,55.71193514484454],
                    [9.525426691693069,55.71191096830816],
                    [9.523538416546584,55.71198349787235],
                    [9.523091985414561,55.711944878298056]]]
                }
            },
            {"provider": Provider.objects.get(name='Test Provider'),
            "name": "Zone 5",
            "price": "5.50",
            "zone": {
                "type":"Polygon",
                "coordinates": [[[9.53437454096675,55.71449402071982],
                    [9.534224337261916,55.714300620678685],
                    [9.533301657360793,55.71253580107078],
                    [9.532851046246291,55.71167753806411],
                    [9.532250231426955,55.71060166062124],
                    [9.531928366345168,55.71003348866882],
                    [9.532035654705764,55.70991259995333],
                    [9.533301657360793,55.70992468884168],
                    [9.535232847851516,55.709453219423125],
                    [9.535983866375686,55.709296061685976],
                    [9.53613407008052,55.71020273224208],
                    [9.536284273785354,55.711085204710606],
                    [9.536434477490188,55.711314886056584],
                    [9.536799257916213,55.71145994726354],
                    [9.53735715739131,55.711617096296635],
                    [9.537657564800979,55.71167753806411],
                    [9.538279837292434,55.71172589141077],
                    [9.539095228832961,55.71179842131854],
                    [9.540189570111037,55.71224568610767],
                    [9.541455572766067,55.71298305741787],
                    [9.540232485455276,55.713212727606255],
                    [9.538151091259719,55.713684151657375],
                    [9.536906546276809,55.71396216830273],
                    [9.53660613886714,55.7140588692808],
                    [9.535490339916946,55.71420392029907],
                    [9.53437454096675,55.71449402071982]]]
                }
            },
            {"provider": Provider.objects.get(name='Test Provider 2'),
            "name": "Zone 6",
            "price": "5.50",
            "zone": {
                "type":"Polygon",
                "coordinates": [[[9.53159040833671,55.70979586615575],
                    [9.531735247623514,55.70976866606194],
                    [9.531536764156412,55.709167236927286],
                    [9.531306094181131,55.708275654090016],
                    [9.531166619312357,55.70785554529469],
                    [9.530276125919412,55.707867634819536],
                    [9.52935881043632,55.70786159005758],
                    [9.529171055805277,55.70786461243868],
                    [9.528983301174234,55.70787972434067],
                    [9.529149598133158,55.708396547870436],
                    [9.529278344165872,55.70860508876248],
                    [9.529653853427957,55.70886803003993],
                    [9.53034049893577,55.70923423370698],
                    [9.531053966533731,55.70960597176806],
                    [9.531268543254923,55.70966641664696],
                    [9.53159040833671,55.70979586615575]]]
                }
            },
        ]

        # load service_areas
        for service_area in service_areas:
            service_area['zone'] = json.dumps(service_area['zone'])
            ServiceArea.objects.create(**service_area)


    def test_viewset_get(self):
        """
        Test service list get without filters
        """
        response = self.client.get(reverse("servicearea-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['features']), ServiceArea.objects.all().count())


    def test_viewset_post_passed(self):
        """
        Tests service list post method with valid data
        """
        zone = [
            [
                [9.523050482755892,55.71576659960325],
                [9.52433794308304,55.71581494788879],
                [9.525732691770784,55.71585120906369],
                [9.527191813474886,55.715863296114506],
                [9.52785700131058,55.71585120906369],
                [9.530367548948519,55.715561118722064],
                [9.531440432554476,55.71540398555416],
                [9.53208416271805,55.71521059001827],
                [9.532856638914339,55.7149567569243],
                [9.531247313505403,55.713349109025195],
                [9.530989821439974,55.713107351738756],
                [9.529616530424349,55.71246668769403],
                [9.528801138883821,55.712055690133354],
                [9.52860801983475,55.71214030763166],
                [9.528436358457796,55.71206777835862],
                [9.525904353147737,55.711983160703205],
                [9.52410190868973,55.71200733719487],
                [9.52311485577225,55.71206777835862],
                [9.523200686460726,55.71427986060977],
                [9.523050482755892,55.71576659960325]
            ], [
                [9.529723818784944,55.71464248509411],
                [9.529037173277132,55.713880969788974],
                [9.528801138883821,55.713748005276905],
                [9.528221781736605,55.71368756671271],
                [9.528393443113558,55.71315570331575],
                [9.529165919309847,55.71315570331575],
                [9.52957361508011,55.71351833823549],
                [9.53058212566971,55.71435238577594],
                [9.529723818784944,55.71464248509411]
            ]
        ]

        data = {
            "provider": Provider.objects.first().pk,
            "name": "Test Zone",
            "price": "5.50",
            "zone": json.dumps(zone)
        }

        response = self.client.post(reverse("servicearea-list"), data, format='json')
        self.assertEqual(response.status_code, 201)


    def test_viewset_post_failed(self):
        """
        Test service list post method validations
        """
        zone = [
            [
                [9.523050482755892,55.71576659960325],
                [9.52433794308304,55.71581494788879],
                [9.523050482755892,55.71576659960325]
            ]
        ]

        data = {
            "provider": Provider.objects.first().pk,
            "name": "Test Zone Failed",
            "price": "5.50",
            "zone": zone
        }

        response = self.client.post(reverse("servicearea-list"), data, format='json')
        # we should get a bad request
        self.assertEqual(response.status_code, 400)

        # we should get a validation error "Not a valid string." for zone as we pass it as a list
        self.assertEqual(response.json()['zone'][0], 'Not a valid string.')

        # change data to an invalid Geometry string
        data['zone'] = 'invalid value'

        response = self.client.post(reverse("servicearea-list"), data, format='json')
        # we should get a bad request and an 'Invalid zone value.' error
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['zone'][0], 'Invalid zone value.')


    def test_viewset_list_filter(self):
        """
        Test service are list filter/serach
        """
        # valid coordinate within a zone
        data = {"coords": "55.710663495702725/9.52840811021021"}
        response = self.client.get(reverse("servicearea-list"), data, format='json')

        # we should get a http 200 and the zone
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['features']), 1)

        # valid coordinate but outside the zone
        data = {"coords": "55.71/22.52"}
        response = self.client.get(reverse("servicearea-list"), data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['features']), 0)

        # invalid coordinate format
        data = {"coords": "test"}
        response = self.client.get(reverse("servicearea-list"), data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['features']), 0)

        # invalid coordinate format
        data = {"coords": "lng/lat"}
        response = self.client.get(reverse("servicearea-list"), data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['features']), 0)


        # invalid coordinate format
        data = {"coords": 1}
        response = self.client.get(reverse("servicearea-list"), data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['features']), 0)
