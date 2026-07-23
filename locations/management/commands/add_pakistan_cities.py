from django.core.management.base import BaseCommand
from locations.models import Province, City

class Command(BaseCommand):
    help = 'Add Pakistan provinces and cities to database'

    def handle(self, *args, **kwargs):
        # Pakistan Provinces with cities
        pakistan_data = {
            'Punjab': {
                'code': 'PB',
                'cities': [
                    'Lahore', 'Rawalpindi', 'Faisalabad', 'Multan', 'Gujranwala',
                    'Sialkot', 'Bahawalpur', 'Sargodha', 'Sheikhupura', 'Rahim Yar Khan',
                    'Jhang', 'Dera Ghazi Khan', 'Sahiwal', 'Okara', 'Wah Cantonment',
                    'Kasur', 'Gujrat', 'Chiniot', 'Hafizabad', 'Mandi Bahauddin',
                    'Nankana Sahib', 'Layyah', 'Muzaffargarh', 'Khanewal', 'Vehari',
                    'Pakpattan', 'Toba Tek Singh', 'Jhelum', 'Attock', 'Chakwal',
                    'Narowal', 'Khushab', 'Bhakkar', 'Mianwali', 'Talagang'
                ]
            },
            'Sindh': {
                'code': 'SD',
                'cities': [
                    'Karachi', 'Hyderabad', 'Sukkur', 'Larkana', 'Nawabshah',
                    'Mirpur Khas', 'Dadu', 'Khairpur', 'Badin', 'Thatta',
                    'Ghotki', 'Shikarpur', 'Jacobabad', 'Kashmore', 'Umerkot',
                    'Tando Allahyar', 'Tando Muhammad Khan', 'Matiari', 'Sanghar',
                    'Jamshoro', 'Qambar Shahdadkot', 'Sujawal'
                ]
            },
            'Khyber Pakhtunkhwa': {
                'code': 'KP',
                'cities': [
                    'Peshawar', 'Abbottabad', 'Mardan', 'Swat', 'Dera Ismail Khan',
                    'Kohat', 'Mansehra', 'Charsadda', 'Nowshera', 'Swabi',
                    'Bannu', 'Haripur', 'Malakand', 'Chitral', 'Timergara',
                    'Batkhela', 'Mingora', 'Tank', 'Lakki Marwat', 'Hangu',
                    'Karak', 'Buner', 'Shangla', 'Kohistan', 'Torghar'
                ]
            },
            'Balochistan': {
                'code': 'BL',
                'cities': [
                    'Quetta', 'Gwadar', 'Turbat', 'Khuzdar', 'Chaman',
                    'Sibi', 'Loralai', 'Zhob', 'Nushki', 'Mastung',
                    'Kalat', 'Kharan', 'Panjgur', 'Awaran', 'Lasbela',
                    'Jhal Magsi', 'Kech', 'Washuk', 'Shaheed Sikandarabad'
                ]
            },
            'Islamabad': {
                'code': 'ISB',
                'cities': [
                    'Islamabad', 'Rawalpindi (ICT)', 'Golra Sharif', 'Bhara Kahu'
                ]
            },
            'Gilgit-Baltistan': {
                'code': 'GB',
                'cities': [
                    'Gilgit', 'Skardu', 'Hunza', 'Nagar', 'Ghanche',
                    'Astore', 'Diamer', 'Ghizer', 'Kharmang', 'Shigar'
                ]
            },
            'Azad Kashmir': {
                'code': 'AJK',
                'cities': [
                    'Muzaffarabad', 'Mirpur', 'Bhimber', 'Kotli', 'Rawalakot',
                    'Bagh', 'Haveli', 'Sudhanoti', 'Neelum', 'Poonch'
                ]
            }
        }

        for province_name, data in pakistan_data.items():
            province, created = Province.objects.get_or_create(
                name=province_name,
                defaults={'code': data['code']}
            )
            
            if created:
                self.stdout.write(f'✅ Added province: {province_name}')
            
            for city_name in data['cities']:
                city, created = City.objects.get_or_create(
                    name=city_name,
                    province=province
                )
                if created:
                    self.stdout.write(f'  📍 Added city: {city_name}')
        
        self.stdout.write(self.style.SUCCESS('✅ All Pakistan cities added successfully!'))