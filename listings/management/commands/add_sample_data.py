# listings/management/commands/add_sample_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random
from datetime import datetime

fake = Faker()

class Command(BaseCommand):
    help = 'Add sample data to database'

    def handle(self, *args, **kwargs):
        # Create test user if not exists
        user, created = User.objects.get_or_create(
            username='seller',
            defaults={
                'email': 'seller@example.com',
                'password': 'admin123'
            }
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS('Test user created: seller / admin123'))

        # Sample data for each category
        sample_items = {
            'electronics': [
                {
                    'title': 'iPhone 14 Pro Max',
                    'description': 'Like new condition, 256GB, Deep Purple color, with original box and charger',
                    'price_per_day': 1500,
                    'city': 'Karachi',
                    'image': 'electronics/iphone14.jpg'
                },
                {
                    'title': 'Samsung Galaxy S23 Ultra',
                    'description': 'Excellent condition, 512GB, Phantom Black, with S Pen',
                    'price_per_day': 1200,
                    'city': 'Lahore',
                    'image': 'electronics/samsung_s23.jpg'
                },
                {
                    'title': 'MacBook Pro M2',
                    'description': '16-inch, 512GB SSD, 16GB RAM, Apple Care till 2025',
                    'price_per_day': 2500,
                    'city': 'Islamabad',
                    'image': 'electronics/macbook.jpg'
                },
                {
                    'title': 'Sony WH-1000XM5 Headphones',
                    'description': 'Noise cancelling, 30hr battery, like new',
                    'price_per_day': 500,
                    'city': 'Karachi',
                    'image': 'electronics/sony_headphones.jpg'
                },
                {
                    'title': 'iPad Pro 12.9"',
                    'description': 'M1 chip, 256GB, with Apple Pencil 2',
                    'price_per_day': 1000,
                    'city': 'Rawalpindi',
                    'image': 'electronics/ipad_pro.jpg'
                },
                {
                    'title': 'PS5 Gaming Console',
                    'description': 'Disc edition, 2 controllers, 5 games included',
                    'price_per_day': 800,
                    'city': 'Lahore',
                    'image': 'electronics/ps5.jpg'
                }
            ],
            
            'furniture': [
                {
                    'title': 'Modern Sofa Set',
                    'description': '3+1+1, fabric, dark grey color, very comfortable',
                    'price_per_day': 1000,
                    'city': 'Karachi',
                    'image': 'furniture/sofa.jpg'
                },
                {
                    'title': 'King Size Bed',
                    'description': 'Wooden frame with storage, mattress included',
                    'price_per_day': 800,
                    'city': 'Lahore',
                    'image': 'furniture/bed.jpg'
                },
                {
                    'title': 'Dining Table Set',
                    'description': '6 seater, glass top, modern design',
                    'price_per_day': 700,
                    'city': 'Islamabad',
                    'image': 'furniture/dining_table.jpg'
                },
                {
                    'title': 'Office Chair',
                    'description': 'Ergonomic, mesh back, adjustable height',
                    'price_per_day': 300,
                    'city': 'Karachi',
                    'image': 'furniture/office_chair.jpg'
                },
                {
                    'title': 'Bookshelf',
                    'description': '5 shelves, solid wood, dark brown',
                    'price_per_day': 200,
                    'city': 'Rawalpindi',
                    'image': 'furniture/bookshelf.jpg'
                },
                {
                    'title': 'Study Table',
                    'description': 'With drawer, modern design, white color',
                    'price_per_day': 250,
                    'city': 'Lahore',
                    'image': 'furniture/study_table.jpg'
                }
            ],
            
            'vehicles': [
                {
                    'title': 'Toyota Corolla 2023',
                    'description': 'Automatic, AC, Power windows, excellent condition',
                    'price_per_day': 5000,
                    'city': 'Karachi',
                    'image': 'vehicles/corolla.jpg'
                },
                {
                    'title': 'Honda Civic 2022',
                    'description': 'Turbo, sunroof, leather seats',
                    'price_per_day': 6000,
                    'city': 'Lahore',
                    'image': 'vehicles/civic.jpg'
                },
                {
                    'title': 'Suzuki Mehran',
                    'description': 'Good condition, fuel efficient, AC',
                    'price_per_day': 2000,
                    'city': 'Islamabad',
                    'image': 'vehicles/mehran.jpg'
                },
                {
                    'title': 'Toyota Yaris 2023',
                    'description': 'Automatic, low mileage, like new',
                    'price_per_day': 4500,
                    'city': 'Karachi',
                    'image': 'vehicles/yaris.jpg'
                },
                {
                    'title': 'Honda CD 70 Bike',
                    'description': 'Excellent condition, low fuel consumption',
                    'price_per_day': 500,
                    'city': 'Lahore',
                    'image': 'vehicles/cd70.jpg'
                },
                {
                    'title': 'Yamaha YBR 125',
                    'description': 'Sporty look, good condition, well maintained',
                    'price_per_day': 800,
                    'city': 'Rawalpindi',
                    'image': 'vehicles/ybr.jpg'
                }
            ],
            
            'clothing': [
                {
                    'title': 'Designer Lawn Suit',
                    'description': '3 piece, summer collection, size medium',
                    'price_per_day': 500,
                    'city': 'Karachi',
                    'image': 'clothing/lawn.jpg'
                },
                {
                    'title': 'Men\'s Sherwani',
                    'description': 'Wedding collection, size 40, with waistcoat',
                    'price_per_day': 1500,
                    'city': 'Lahore',
                    'image': 'clothing/sherwani.jpg'
                },
                {
                    'title': 'Women\'s Formal Dress',
                    'description': 'Office wear, size small, brand new',
                    'price_per_day': 800,
                    'city': 'Islamabad',
                    'image': 'clothing/formal_dress.jpg'
                },
                {
                    'title': 'Leather Jacket',
                    'description': 'Genuine leather, black color, size large',
                    'price_per_day': 600,
                    'city': 'Karachi',
                    'image': 'clothing/jacket.jpg'
                },
                {
                    'title': 'Designer Lehenga',
                    'description': 'Wedding special, heavy work, size medium',
                    'price_per_day': 2000,
                    'city': 'Lahore',
                    'image': 'clothing/lehenga.jpg'
                },
                {
                    'title': 'Men\'s Suit',
                    'description': 'Formal wear, navy blue, size 42',
                    'price_per_day': 1000,
                    'city': 'Rawalpindi',
                    'image': 'clothing/suit.jpg'
                }
            ],
            
            'books': [
                {
                    'title': 'Rich Dad Poor Dad',
                    'description': 'Robert Kiyosaki - Financial wisdom book',
                    'price_per_day': 50,
                    'city': 'Karachi',
                    'image': 'books/rich_dad.jpg'
                },
                {
                    'title': 'Atomic Habits',
                    'description': 'James Clear - Build good habits',
                    'price_per_day': 50,
                    'city': 'Lahore',
                    'image': 'books/atomic_habits.jpg'
                },
                {
                    'title': 'Python Programming',
                    'description': 'Complete guide for beginners',
                    'price_per_day': 80,
                    'city': 'Islamabad',
                    'image': 'books/python.jpg'
                },
                {
                    'title': 'Urdu Novels Set',
                    'description': '5 novels by popular writers',
                    'price_per_day': 100,
                    'city': 'Karachi',
                    'image': 'books/urdu_novels.jpg'
                },
                {
                    'title': 'Quran Translation',
                    'description': 'With Urdu translation and Tafseer',
                    'price_per_day': 30,
                    'city': 'Lahore',
                    'image': 'books/quran.jpg'
                },
                {
                    'title': 'Django Web Framework',
                    'description': 'Build web apps with Python',
                    'price_per_day': 70,
                    'city': 'Rawalpindi',
                    'image': 'books/django.jpg'
                }
            ],
            
            'other': [
                {
                    'title': 'Camera Canon EOS',
                    'description': '18-55mm lens, memory card included',
                    'price_per_day': 1000,
                    'city': 'Karachi',
                    'image': 'other/camera.jpg'
                },
                {
                    'title': 'Tent for Camping',
                    'description': '4 person tent, waterproof, with sleeping bags',
                    'price_per_day': 500,
                    'city': 'Islamabad',
                    'image': 'other/tent.jpg'
                },
                {
                    'title': 'Guitar Yamaha',
                    'description': 'Acoustic guitar, with case and picks',
                    'price_per_day': 300,
                    'city': 'Lahore',
                    'image': 'other/guitar.jpg'
                },
                {
                    'title': 'Treadmill',
                    'description': 'Electric, home use, excellent condition',
                    'price_per_day': 400,
                    'city': 'Karachi',
                    'image': 'other/treadmill.jpg'
                },
                {
                    'title': 'Baby Stroller',
                    'description': 'Lightweight, foldable, safe for babies',
                    'price_per_day': 200,
                    'city': 'Rawalpindi',
                    'image': 'other/stroller.jpg'
                },
                {
                    'title': 'Laptop Bag',
                    'description': 'Waterproof, 15.6 inch, multiple pockets',
                    'price_per_day': 100,
                    'city': 'Lahore',
                    'image': 'other/laptop_bag.jpg'
                }
            ]
        }

        # Add data to database
        total_added = 0
        for category, items in sample_items.items():
            for item in items:
                listing, created = Listing.objects.get_or_create(
                    title=item['title'],
                    defaults={
                        'description': item['description'],
                        'price_per_day': item['price_per_day'],
                        'category': category,
                        'city': item['city'],
                        'owner': user,
                        'is_available': True
                    }
                )
                if created:
                    total_added += 1
                    self.stdout.write(f'Added: {item["title"]} ({category})')
                else:
                    self.stdout.write(f'Already exists: {item["title"]}')

        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully added {total_added} items to database!'))
        self.stdout.write(self.style.SUCCESS(f'📊 Total items now: {Listing.objects.count()}'))