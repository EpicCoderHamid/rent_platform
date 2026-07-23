# add_rental_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rent_platform.settings')
django.setup()

from django.contrib.auth.models import User
from listings.models import Listing

print("=" * 60)
print("🇵🇰 Adding PAKISTAN RENTAL DATA to Rentify Platform")
print("=" * 60)

# Create test users
seller, created = User.objects.get_or_create(
    username='renter',
    defaults={
        'email': 'renter@example.com',
        'first_name': 'Rental',
        'last_name': 'Provider'
    }
)
if created:
    seller.set_password('renter123')
    seller.save()
    print("✅ Rental provider created: renter / renter123")

# PAKISTAN SPECIFIC RENTAL DATA
rental_data = [
    
    # ========== WEDDING/EVENT CLOTHING ==========
    {
        'title': 'Sherwani for Wedding - Premium',
        'desc': 'Designer sherwani with waistcoat and shalwar, size 38-44 adjustable, perfect for groom/baraat. Includes turban and khussa.',
        'price': 3000,
        'cat': 'clothing',
        'city': 'Karachi'
    },
    {'title': 'Sherwani for Wedding - Premium Gold', 'desc': 'Designer sherwani with waistcoat and shalwar, size 38-44 adjustable, perfect for groom/baraat. Includes turban and khussa.', 'price': 3000, 'cat': 'clothing', 'city': 'Karachi'},
{'title': 'Bridal Lehenga - Heavy Work', 'desc': 'Red color bridal lehenga with dupatta, heavy embroidery, size M/L. Perfect for wedding functions. Security deposit required.', 'price': 5000, 'cat': 'clothing', 'city': 'Karachi'},
{'title': 'Men\'s Shalwar Kameez - 3 Piece', 'desc': 'Premium lawn/cambric, stitched, size 40-44, multiple colors available. For Eid and events.', 'price': 800, 'cat': 'clothing', 'city': 'Karachi'},
{'title': 'Women\'s Formal Dress - Office Wear', 'desc': 'Designer formal trouser suit, size S/M/L, professional look for job interviews/office.', 'price': 500, 'cat': 'clothing', 'city': 'Karachi'},
{'title': 'Waistcoat for Barat', 'desc': 'Designer waistcoat, velvet material, size 38-42, multiple colors.', 'price': 1000, 'cat': 'clothing', 'city': 'Karachi'},
{'title': 'Mehndi Outfit - Yellow Traditional', 'desc': 'Traditional yellow/orange outfit for mehndi function, with dupatta, size M.', 'price': 1500, 'cat': 'clothing', 'city': 'Karachi'},

# ========== WEDDING/EVENT CLOTHING - Lahore ==========
{'title': 'Sherwani for Wedding - Royal Blue', 'desc': 'Royal blue sherwani with golden embroidery, size 38-44, includes matching khussa and turban.', 'price': 3500, 'cat': 'clothing', 'city': 'Lahore'},
{'title': 'Bridal Lehenga - Maroon Velvet', 'desc': 'Maroon velvet bridal lehenga with gotta patti work, size M/L, dupatta included.', 'price': 5500, 'cat': 'clothing', 'city': 'Lahore'},
{'title': 'Men\'s Shalwar Kameez - Wash and Wear', 'desc': 'Stitched wash and wear shalwar kameez, size 38-44, for casual events and Jumma prayers.', 'price': 600, 'cat': 'clothing', 'city': 'Lahore'},
{'title': 'Women\'s Party Wear Gown', 'desc': 'Designer party gown for valima and receptions, size S/M/L, with sequence work.', 'price': 1200, 'cat': 'clothing', 'city': 'Lahore'},
{'title': 'Prince Coat - Black Formal', 'desc': 'Classic black prince coat for formal occasions, size 40-44, with sherwani style buttons.', 'price': 1500, 'cat': 'clothing', 'city': 'Lahore'},
{'title': 'Nikkah Dress - White Elegant', 'desc': 'White elegant nikkah dress with lace detailing, size S/M, includes hijab.', 'price': 1800, 'cat': 'clothing', 'city': 'Lahore'},

# ========== WEDDING/EVENT CLOTHING - Islamabad ==========
{'title': 'Sherwani for Engagement - Beige', 'desc': 'Beige color engagement sherwani with light embroidery, size 38-44, includes waistcoat.', 'price': 2800, 'cat': 'clothing', 'city': 'Islamabad'},
{'title': 'Bridal Lehenga - Pink Pastel', 'desc': 'Pastel pink bridal lehenga for daytime weddings, size M/L, with net dupatta.', 'price': 4800, 'cat': 'clothing', 'city': 'Islamabad'},
{'title': 'Men\'s Shalwar Kameez - Karandi', 'desc': 'Karandi fabric shalwar kameez for winter events, size 40-44, warm and comfortable.', 'price': 900, 'cat': 'clothing', 'city': 'Islamabad'},
{'title': 'Women\'s Formal Suit - Office', 'desc': 'Two-piece formal suit for office wear, size S/M/L, professional colors available.', 'price': 550, 'cat': 'clothing', 'city': 'Islamabad'},
{'title': 'Kids Sherwani - Age 3-8', 'desc': 'Kids sherwani with shalwar for wedding functions, multiple sizes, colorful options.', 'price': 400, 'cat': 'clothing', 'city': 'Islamabad'},
{'title': 'Mayun Dress - Yellow Organza', 'desc': 'Yellow organza mayun dress with floral work, size M/L, includes dupatta and jewelry.', 'price': 1300, 'cat': 'clothing', 'city': 'Islamabad'},

# ========== WEDDING/EVENT CLOTHING - Rawalpindi ==========
{'title': 'Sherwani for Barat - Black', 'desc': 'Black sherwani with silver embroidery, size 38-44, perfect for night events and receptions.', 'price': 3200, 'cat': 'clothing', 'city': 'Rawalpindi'},
{'title': 'Bridal Dress - Red Traditional', 'desc': 'Traditional red bridal dress with heavy zari work, size M/L, full set with dupatta.', 'price': 4500, 'cat': 'clothing', 'city': 'Rawalpindi'},
{'title': 'Men\'s Kurta Pajama - Cotton', 'desc': 'Simple cotton kurta pajama for casual events and Eid, size 38-44, multiple colors.', 'price': 400, 'cat': 'clothing', 'city': 'Rawalpindi'},
{'title': 'Women\'s Maxi Dress - Formal', 'desc': 'Long maxi dress for formal dinners, size S/M/L, elegant design with belt.', 'price': 700, 'cat': 'clothing', 'city': 'Rawalpindi'},
{'title': 'Jinnah Cap - Karakul', 'desc': 'Traditional Karakul cap for formal events and Jumma, one size fits all, black color.', 'price': 250, 'cat': 'clothing', 'city': 'Rawalpindi'},
{'title': 'Dholki Dress - Printed Lawn', 'desc': 'Printed lawn dholki dress with embroidery, size M/L, comfortable for long functions.', 'price': 650, 'cat': 'clothing', 'city': 'Rawalpindi'},

# ========== WEDDING/EVENT CLOTHING - Faisalabad ==========
{'title': 'Sherwani for Waliima - White', 'desc': 'White waliima sherwani with pearl work, size 38-44, elegant and simple design.', 'price': 2700, 'cat': 'clothing', 'city': 'Faisalabad'},
{'title': 'Bridal Lehenga - Orange Heavy', 'desc': 'Orange bridal lehenga for mehndi/barat, size M/L, heavy gotta patti border.', 'price': 4200, 'cat': 'clothing', 'city': 'Faisalabad'},
{'title': 'Men\'s Shalwar Kameez - Boski', 'desc': 'Boski fabric shalwar kameez for formal events, size 40-44, shiny finish.', 'price': 750, 'cat': 'clothing', 'city': 'Faisalabad'},
{'title': 'Women\'s Kameez Shalwar - Casual', 'desc': 'Simple kameez shalwar for daily wear and small functions, size S/M/L.', 'price': 350, 'cat': 'clothing', 'city': 'Faisalabad'},
{'title': 'Safa/Turban for Groom', 'desc': 'Ready-made safa/pagri for groom, multiple colors, with kalgi pin included.', 'price': 500, 'cat': 'clothing', 'city': 'Faisalabad'},
{'title': 'Teen Girl Lehenga - Age 12-16', 'desc': 'Stylish lehenga for teenage girls, perfect for cousin weddings, size adjustable.', 'price': 850, 'cat': 'clothing', 'city': 'Faisalabad'},

# ========== WEDDING/EVENT CLOTHING - Multan ==========
{'title': 'Sherwani for Nikkah - Cream', 'desc': 'Cream color nikkah sherwani with minimal embroidery, size 38-44, lightweight fabric.', 'price': 2500, 'cat': 'clothing', 'city': 'Multan'},
{'title': 'Bridal Lehenga - Multani Style', 'desc': 'Traditional Multani style bridal lehenga with mirror work, size M/L, unique design.', 'price': 4000, 'cat': 'clothing', 'city': 'Multan'},
{'title': 'Men\'s Shalwar Kameez - Latha', 'desc': 'Latha fabric shalwar kameez for summer events, size 40-44, cool and breathable.', 'price': 550, 'cat': 'clothing', 'city': 'Multan'},
{'title': 'Women\'s Saree - Party Wear', 'desc': 'Designer saree for weddings and parties, with blouse piece, multiple colors available.', 'price': 900, 'cat': 'clothing', 'city': 'Multan'},
{'title': 'Khussa for Groom - Embroidered', 'desc': 'Handmade embroidered khussa for groom, size 7-11, gold/silver work.', 'price': 450, 'cat': 'clothing', 'city': 'Multan'},
{'title': 'Girls Frocks - Party Wear', 'desc': 'Party frocks for girls age 3-10, with sequence and net, perfect for mehndi functions.', 'price': 350, 'cat': 'clothing', 'city': 'Multan'},

# ========== WEDDING/EVENT CLOTHING - Peshawar ==========
{'title': 'Sherwani for Barat - Maroon', 'desc': 'Maroon sherwani with golden embroidery, size 38-44, includes matching waistcoat.', 'price': 3100, 'cat': 'clothing', 'city': 'Peshawar'},
{'title': 'Bridal Dress - Afghan Style', 'desc': 'Afghan inspired bridal dress with heavy embroidery, size M/L, unique traditional look.', 'price': 4600, 'cat': 'clothing', 'city': 'Peshawar'},
{'title': 'Men\'s Shalwar Kameez - Peshawari', 'desc': 'Traditional Peshawari style shalwar kameez, size 40-44, with waistcoat.', 'price': 700, 'cat': 'clothing', 'city': 'Peshawar'},
{'title': 'Women\'s Abaya - Formal', 'desc': 'Formal abaya for events, with embroidery, size M/L/XL, multiple colors.', 'price': 600, 'cat': 'clothing', 'city': 'Peshawar'},
{'title': 'Peshawari Chappal - Formal', 'desc': 'Traditional Peshawari chappal for men, size 7-11, perfect with shalwar kameez.', 'price': 300, 'cat': 'clothing', 'city': 'Peshawar'},
{'title': 'Kids Waistcoat Set', 'desc': 'Boys waistcoat with shalwar kameez, age 4-12, perfect for family weddings.', 'price': 450, 'cat': 'clothing', 'city': 'Peshawar'},

# ========== WEDDING/EVENT CLOTHING - Quetta ==========
{'title': 'Sherwani for Reception - Navy Blue', 'desc': 'Navy blue sherwani with light embroidery, size 38-44, perfect for reception dinners.', 'price': 2900, 'cat': 'clothing', 'city': 'Quetta'},
{'title': 'Bridal Lehenga - Green Heavy', 'desc': 'Green bridal lehenga with golden zari work, size M/L, traditional Balochi inspired.', 'price': 4300, 'cat': 'clothing', 'city': 'Quetta'},
{'title': 'Men\'s Shalwar Kameez - Winter', 'desc': 'Warm shalwar kameez for winter weddings, size 40-44, with shawl included.', 'price': 850, 'cat': 'clothing', 'city': 'Quetta'},
{'title': 'Women\'s Shawl - Pashmina Style', 'desc': 'Warm pashmina style shawl for winter events, multiple colors, elegant design.', 'price': 400, 'cat': 'clothing', 'city': 'Quetta'},
{'title': 'Kids Party Dress - Boys', 'desc': 'Formal party dress for boys age 5-12, with coat and pants, wedding appropriate.', 'price': 550, 'cat': 'clothing', 'city': 'Quetta'},
{'title': 'Bridal Dupatta - Separate', 'desc': 'Heavy embroidered dupatta for bridal wear, 2.5 yards, can match any dress.', 'price': 700, 'cat': 'clothing', 'city': 'Quetta'},

# ========== WEDDING/EVENT CLOTHING - Gujranwala ==========
{'title': 'Sherwani for Mayun - Light Gold', 'desc': 'Light gold sherwani for mayun function, size 38-44, comfortable for long wear.', 'price': 2600, 'cat': 'clothing', 'city': 'Gujranwala'},
{'title': 'Bridal Dress - Purple Velvet', 'desc': 'Purple velvet bridal dress with sequence work, size M/L, includes dupatta and jewelry.', 'price': 4100, 'cat': 'clothing', 'city': 'Gujranwala'},
{'title': 'Men\'s Waistcoat - Designer', 'desc': 'Designer waistcoat for formal events, size 38-44, multiple fabrics and colors.', 'price': 650, 'cat': 'clothing', 'city': 'Gujranwala'},
{'title': 'Women\'s Trouser Suit - Party', 'desc': 'Stylish trouser suit for parties and events, size S/M/L, with dupatta.', 'price': 750, 'cat': 'clothing', 'city': 'Gujranwala'},
{'title': 'Boys Sherwani - Age 8-14', 'desc': 'Sherwani for teenage boys, size adjustable, perfect for family weddings.', 'price': 600, 'cat': 'clothing', 'city': 'Gujranwala'},
{'title': 'Mehndi Jewelry Set', 'desc': 'Artificial jewelry set for mehndi function, includes necklace, earrings, bangles.', 'price': 300, 'cat': 'clothing', 'city': 'Gujranwala'},

# ========== WEDDING/EVENT CLOTHING - Sialkot ==========
{'title': 'Sherwani for Dholki - Silver', 'desc': 'Silver sherwani for dholki function, size 38-44, lightweight and stylish.', 'price': 2400, 'cat': 'clothing', 'city': 'Sialkot'},
{'title': 'Bridal Lehenga - Peach', 'desc': 'Peach color bridal lehenga for day events, size M/L, with net dupatta.', 'price': 3900, 'cat': 'clothing', 'city': 'Sialkot'},
{'title': 'Men\'s Shalwar Kameez - Simple', 'desc': 'Simple cotton shalwar kameez for daily events, size 40-44, comfortable fit.', 'price': 450, 'cat': 'clothing', 'city': 'Sialkot'},
{'title': 'Women\'s Gharara - Traditional', 'desc': 'Traditional gharara for weddings, size M/L, with short kameez and dupatta.', 'price': 950, 'cat': 'clothing', 'city': 'Sialkot'},
{'title': 'Groom\'s Sehra - Fresh Flowers', 'desc': 'Sehra made of fresh flowers for groom, custom made on order.', 'price': 800, 'cat': 'clothing', 'city': 'Sialkot'},
{'title': 'Girls Lehenga - Age 5-10', 'desc': 'Beautiful lehenga for girls, perfect for flower girls and family weddings.', 'price': 500, 'cat': 'clothing', 'city': 'Sialkot'},

# ========== WEDDING/EVENT CLOTHING - Bahawalpur ==========
{'title': 'Sherwani for Waliima - Off White', 'desc': 'Off white waliima sherwani with pearl buttons, size 38-44, elegant look.', 'price': 2700, 'cat': 'clothing', 'city': 'Bahawalpur'},
{'title': 'Bridal Dress - Yellow Mustard', 'desc': 'Yellow mustard bridal dress for mehndi, size M/L, with heavy gotta work.', 'price': 3800, 'cat': 'clothing', 'city': 'Bahawalpur'},
{'title': 'Men\'s Kurta - Eid Special', 'desc': 'Special Eid kurta with pajama, size 40-44, embroidered neckline.', 'price': 500, 'cat': 'clothing', 'city': 'Bahawalpur'},
{'title': 'Women\'s Farshi Shalwar', 'desc': 'Traditional farshi shalwar with kameez, size M/L, royal look for weddings.', 'price': 1100, 'cat': 'clothing', 'city': 'Bahawalpur'},
{'title': 'Safa - Rajasthani Style', 'desc': 'Rajasthani style safa for groom, multiple colors, with brooch included.', 'price': 600, 'cat': 'clothing', 'city': 'Bahawalpur'},
{'title': 'Kids Lehenga - Girls', 'desc': 'Lehenga choli for girls age 4-10, with sequence and gotta work.', 'price': 450, 'cat': 'clothing', 'city': 'Bahawalpur'},

# ========== WEDDING/EVENT CLOTHING - Hyderabad ==========
{'title': 'Sherwani for Mehndi - Green', 'desc': 'Green sherwani for mehndi function, size 38-44, with light embroidery.', 'price': 2300, 'cat': 'clothing', 'city': 'Hyderabad'},
{'title': 'Bridal Lehenga - Sindhi Style', 'desc': 'Traditional Sindhi style bridal lehenga with mirror work, size M/L, unique pattern.', 'price': 3600, 'cat': 'clothing', 'city': 'Hyderabad'},
{'title': 'Men\'s Ajrak Waistcoat', 'desc': 'Ajrak print waistcoat for cultural events, size 38-44, traditional Sindhi design.', 'price': 550, 'cat': 'clothing', 'city': 'Hyderabad'},
{'title': 'Women\'s Ajrak Dress', 'desc': 'Ajrak print dress for cultural functions, size S/M/L, with dupatta.', 'price': 650, 'cat': 'clothing', 'city': 'Hyderabad'},
{'title': 'Sindhi Topi - Traditional', 'desc': 'Traditional Sindhi topi for men, embroidered, perfect for cultural events.', 'price': 200, 'cat': 'clothing', 'city': 'Hyderabad'},
{'title': 'Kids Ajrak Outfit', 'desc': 'Ajrak outfit for kids age 3-10, cultural dress for family events.', 'price': 350, 'cat': 'clothing', 'city': 'Hyderabad'},

# ========== WEDDING/EVENT CLOTHING - Sukkur ==========
{'title': 'Sherwani for Barat - Brown', 'desc': 'Brown sherwani with golden buttons, size 38-44, unique color for groom.', 'price': 2500, 'cat': 'clothing', 'city': 'Sukkur'},
{'title': 'Bridal Dress - Red Sindhi', 'desc': 'Red Sindhi bridal dress with embroidery, size M/L, traditional and elegant.', 'price': 3500, 'cat': 'clothing', 'city': 'Sukkur'},
{'title': 'Men\'s Shalwar Kameez - Summer', 'desc': 'Lightweight summer shalwar kameez, size 40-44, perfect for hot weather events.', 'price': 400, 'cat': 'clothing', 'city': 'Sukkur'},
{'title': 'Women\'s Churidar Suit', 'desc': 'Churidar suit for formal events, size S/M/L, with long kameez and dupatta.', 'price': 550, 'cat': 'clothing', 'city': 'Sukkur'},
{'title': 'Groom\'s Mojari - Handmade', 'desc': 'Handmade mojari for groom, size 7-11, with embroidery and beads.', 'price': 400, 'cat': 'clothing', 'city': 'Sukkur'},
{'title': 'Girls Sharara - Party', 'desc': 'Sharara for girls age 5-12, with sequence top and dupatta.', 'price': 400, 'cat': 'clothing', 'city': 'Sukkur'},

# ========== WEDDING/EVENT CLOTHING - Larkana ==========
{'title': 'Sherwani for Reception - Grey', 'desc': 'Grey sherwani with black buttons, size 38-44, modern and stylish.', 'price': 2600, 'cat': 'clothing', 'city': 'Larkana'},
{'title': 'Bridal Lehenga - Pink Heavy', 'desc': 'Pink heavy bridal lehenga for valima, size M/L, with stone work.', 'price': 3700, 'cat': 'clothing', 'city': 'Larkana'},
{'title': 'Men\'s Shalwar - Separate', 'desc': 'Stitched shalwar only, size 38-44, multiple colors, can match with any kameez.', 'price': 200, 'cat': 'clothing', 'city': 'Larkana'},
{'title': 'Women\'s Kameez - Designer', 'desc': 'Designer kameez for parties, size S/M/L, without shalwar.', 'price': 400, 'cat': 'clothing', 'city': 'Larkana'},
{'title': 'Bridal Clutch - Embroidered', 'desc': 'Embroidered bridal clutch for wedding, matches with bridal dress.', 'price': 300, 'cat': 'clothing', 'city': 'Larkana'},
{'title': 'Boys Kurta Pajama', 'desc': 'Simple kurta pajama for boys age 3-10, comfortable for long events.', 'price': 250, 'cat': 'clothing', 'city': 'Larkana'},

# ========== WEDDING/EVENT CLOTHING - Mirpur Khas ==========
{'title': 'Sherwani for Nikkah - White Gold', 'desc': 'White sherwani with gold buttons, size 38-44, simple and elegant for nikkah.', 'price': 2200, 'cat': 'clothing', 'city': 'Mirpur Khas'},
{'title': 'Bridal Dress - Orange Sindhi', 'desc': 'Orange Sindhi bridal dress with mirror work, size M/L, vibrant and beautiful.', 'price': 3400, 'cat': 'clothing', 'city': 'Mirpur Khas'},
{'title': 'Men\'s Kameez - Embroidered', 'desc': 'Embroidered kameez for men, size 40-44, neckline work, without shalwar.', 'price': 450, 'cat': 'clothing', 'city': 'Mirpur Khas'},
{'title': 'Women\'s Lehenga - Simple', 'desc': 'Simple lehenga for small functions, size M/L, with blouse and dupatta.', 'price': 800, 'cat': 'clothing', 'city': 'Mirpur Khas'},
{'title': 'Khusa - Simple', 'desc': 'Simple khussa for men, size 7-11, without embroidery, comfortable.', 'price': 250, 'cat': 'clothing', 'city': 'Mirpur Khas'},
{'title': 'Kids Traditional Dress', 'desc': 'Traditional dress for kids age 4-12, both boys and girls options.', 'price': 300, 'cat': 'clothing', 'city': 'Mirpur Khas'},

# ========== WEDDING/EVENT CLOTHING - Nawabshah ==========
{'title': 'Sherwani for Mayun - Peach', 'desc': 'Peach color sherwani for mayun, size 38-44, with light work.', 'price': 2100, 'cat': 'clothing', 'city': 'Nawabshah'},
{'title': 'Bridal Lehenga - Golden', 'desc': 'Golden bridal lehenga for reception, size M/L, with heavy border.', 'price': 3300, 'cat': 'clothing', 'city': 'Nawabshah'},
{'title': 'Men\'s Formal Suit - 2 Piece', 'desc': 'Two-piece formal suit for men, size 40-44, coat and trouser.', 'price': 1200, 'cat': 'clothing', 'city': 'Nawabshah'},
{'title': 'Women\'s Blouse - Designer', 'desc': 'Designer blouse for saree or lehenga, size S/M/L, with embroidery.', 'price': 300, 'cat': 'clothing', 'city': 'Nawabshah'},
{'title': 'Pagri - Ready Made', 'desc': 'Ready made pagri for groom, multiple colors, easy to wear.', 'price': 350, 'cat': 'clothing', 'city': 'Nawabshah'},
{'title': 'Girls Party Suit', 'desc': 'Party suit for girls age 5-12, with trouser and dupatta.', 'price': 350, 'cat': 'clothing', 'city': 'Nawabshah'},

# ========== WEDDING/EVENT CLOTHING - Rahim Yar Khan ==========
{'title': 'Sherwani for Waliima - Sky Blue', 'desc': 'Sky blue waliima sherwani, size 38-44, with silver embroidery.', 'price': 2400, 'cat': 'clothing', 'city': 'Rahim Yar Khan'},
{'title': 'Bridal Dress - Ferozi', 'desc': 'Ferozi color bridal dress with zari work, size M/L, unique and royal.', 'price': 3600, 'cat': 'clothing', 'city': 'Rahim Yar Khan'},
{'title': 'Men\'s Shalwar Kameez - Sada', 'desc': 'Sada shalwar kameez for daily prayers, size 40-44, simple design.', 'price': 300, 'cat': 'clothing', 'city': 'Rahim Yar Khan'},
{'title': 'Women\'s Pishwas - Traditional', 'desc': 'Traditional pishwas for weddings, size M/L, with chooridar and dupatta.', 'price': 850, 'cat': 'clothing', 'city': 'Rahim Yar Khan'},
{'title': 'Necklace Set - Bridal', 'desc': 'Artificial bridal necklace set with earrings and tikka.', 'price': 500, 'cat': 'clothing', 'city': 'Rahim Yar Khan'},
{'title': 'Boys Coat Pant', 'desc': 'Formal coat pant for boys age 5-12, perfect for wedding receptions.', 'price': 400, 'cat': 'clothing', 'city': 'Rahim Yar Khan'},

# ========== WEDDING/EVENT CLOTHING - Sargodha ==========
{'title': 'Sherwani for Dholki - Purple', 'desc': 'Purple sherwani for dholki night, size 38-44, with light sequence work.', 'price': 2300, 'cat': 'clothing', 'city': 'Sargodha'},
{'title': 'Bridal Lehenga - Dark Green', 'desc': 'Dark green bridal lehenga for barat, size M/L, heavy embroidery.', 'price': 3500, 'cat': 'clothing', 'city': 'Sargodha'},
{'title': 'Men\'s Waistcoat - Plain', 'desc': 'Plain waistcoat for formal wear, size 38-44, multiple colors.', 'price': 400, 'cat': 'clothing', 'city': 'Sargodha'},
{'title': 'Women\'s Maxi - Embroidered', 'desc': 'Embroidered maxi dress for parties, size S/M/L, elegant and comfortable.', 'price': 700, 'cat': 'clothing', 'city': 'Sargodha'},
{'title': 'Groom\'s Kalgi - Pearl', 'desc': 'Pearl kalgi for groom turban, elegant design.', 'price': 300, 'cat': 'clothing', 'city': 'Sargodha'},
{'title': 'Kids Frock - Wedding', 'desc': 'Wedding frock for girls age 3-8, with net and sequence.', 'price': 300, 'cat': 'clothing', 'city': 'Sargodha'},

# ========== WEDDING/EVENT CLOTHING - Jhang ==========
{'title': 'Sherwani for Engagement - Light Pink', 'desc': 'Light pink engagement sherwani, size 38-44, unique and modern.', 'price': 2200, 'cat': 'clothing', 'city': 'Jhang'},
{'title': 'Bridal Dress - Magenta', 'desc': 'Magenta bridal dress for mehndi, size M/L, with gotta work.', 'price': 3400, 'cat': 'clothing', 'city': 'Jhang'},
{'title': 'Men\'s Kurta - Simple', 'desc': 'Simple kurta for men, size 40-44, cotton fabric, without shalwar.', 'price': 250, 'cat': 'clothing', 'city': 'Jhang'},
{'title': 'Women\'s Saree - Banarsi', 'desc': 'Banarsi saree for weddings, with blouse piece, rich look.', 'price': 1000, 'cat': 'clothing', 'city': 'Jhang'},
    {
        'title': 'Bridal Lehenga - Heavy Work',
        'desc': 'Red color bridal lehenga with dupatta, heavy embroidery, size M/L. Perfect for wedding functions. Security deposit required.',
        'price': 5000,
        'cat': 'clothing',
        'city': 'Lahore'
    },
    {
        'title': 'Men\'s Shalwar Kameez - 3 Piece',
        'desc': 'Premium lawn/cambric, stitched, size 40-44, multiple colors available. For Eid and events.',
        'price': 800,
        'cat': 'clothing',
        'city': 'Islamabad'
    },
    {
        'title': 'Women\'s Formal Dress - Office Wear',
        'desc': 'Designer formal trouser suit, size S/M/L, professional look for job interviews/office.',
        'price': 500,
        'cat': 'clothing',
        'city': 'Karachi'
    },
    {
        'title': 'Waistcoat for Barat',
        'desc': 'Designer waistcoat, velvet material, size 38-42, multiple colors.',
        'price': 1000,
        'cat': 'clothing',
        'city': 'Rawalpindi'
    },
    {
        'title': 'Mehndi Outfit - Yellow',
        'desc': 'Traditional yellow/orange outfit for mehndi function, with dupatta, size M.',
        'price': 1500,
        'cat': 'clothing',
        'city': 'Lahore'
    },
    {
        'title': 'Nikkah Dress - White',
        'desc': 'Simple elegant white dress for nikkah ceremony, size S/M.',
        'price': 2000,
        'cat': 'clothing',
        'city': 'Karachi'
    },
    {
        'title': 'Kids Wedding Wear',
        'desc': 'Sherwani and shalwar for boys age 5-12, perfect for family weddings.',
        'price': 500,
        'cat': 'clothing',
        'city': 'Islamabad'
    },
    
    # ========== VEHICLES FOR RENT ==========
    {
        'title': 'Toyota Corolla - Wedding Car',
        'desc': '2022 model, white color, AC, clean interior. Perfect for wedding/baraat. Driver included.',
        'price': 5000,
        'cat': 'vehicles',
        'city': 'Karachi'
    },
    {'title': 'Toyota Corolla GLI - 2022 Model', 'desc': 'White Corolla GLI automatic, perfect for weddings and family trips. AC, power steering, clean interior. Driver optional.', 'price': 5000, 'cat': 'vehicles', 'city': 'Karachi'},
{'title': 'Honda Civic Oriel - 2021', 'desc': 'Black Civic Oriel with sunroof, leather seats, perfect for valima and receptions. Self or with driver.', 'price': 6000, 'cat': 'vehicles', 'city': 'Karachi'},
{'title': 'Suzuki Alto VXL - 2023', 'desc': 'Brand new Alto VXL, fuel efficient, perfect for city travel and small events. AC, power windows.', 'price': 2500, 'cat': 'vehicles', 'city': 'Karachi'},
{'title': 'Toyota Hiace Grand Cabin - 2020', 'desc': '14-seater Hiace for family trips and wedding guests transport. AC, comfortable seats, with driver.', 'price': 8000, 'cat': 'vehicles', 'city': 'Karachi'},
{'title': 'Honda BR-V - 7 Seater', 'desc': '7-seater BR-V for family outings and airport pickup. AC, spacious, luggage space available.', 'price': 4500, 'cat': 'vehicles', 'city': 'Karachi'},
{'title': 'Suzuki Wagon R - 2022', 'desc': 'Wagon R VXL, perfect for small family trips and daily rental. AC, CNG option, economical.', 'price': 2000, 'cat': 'vehicles', 'city': 'Karachi'},

# ========== VEHICLES FOR RENT - Lahore ==========
{'title': 'Toyota Corolla Altis - 2023', 'desc': 'Silver Altis Grande, top model with sunroof, leather interior. Perfect for weddings and corporate events.', 'price': 7000, 'cat': 'vehicles', 'city': 'Lahore'},
{'title': 'Honda City Aspire - 2022', 'desc': 'White City Aspire Prosmatec, sunroof, cruise control. Ideal for outstation trips and weddings.', 'price': 4500, 'cat': 'vehicles', 'city': 'Lahore'},
{'title': 'Suzuki Cultus VXL - 2023', 'desc': 'New model Cultus VXL, automatic, fuel efficient. Perfect for city tours and shopping trips.', 'price': 2800, 'cat': 'vehicles', 'city': 'Lahore'},
{'title': 'Toyota Fortuner Legender - 2022', 'desc': 'Black Fortuner Legender, 7-seater luxury SUV. Perfect for VIP events, weddings, and corporate guests.', 'price': 15000, 'cat': 'vehicles', 'city': 'Lahore'},
{'title': 'Honda Civic X - 2020', 'desc': 'Civic X Oriel, 1.8 i-VTEC, sunroof, paddle shifters. Sports look for young couples.', 'price': 5500, 'cat': 'vehicles', 'city': 'Lahore'},
{'title': 'Suzuki Swift - 2021', 'desc': 'Swift DLX automatic, sporty look, perfect for couples and small families. AC, music system.', 'price': 3500, 'cat': 'vehicles', 'city': 'Lahore'},

# ========== VEHICLES FOR RENT - Islamabad ==========
{'title': 'Toyota Prado TX - 2021', 'desc': 'White Prado TX, 7-seater luxury SUV. 4x4, perfect for northern areas trip and VIP guests.', 'price': 18000, 'cat': 'vehicles', 'city': 'Islamabad'},
{'title': 'Honda HR-V - 2023', 'desc': 'HR-V VTI-S, sunroof, Honda sensing. Perfect for Murree/Nathia Gali trips and family outings.', 'price': 8000, 'cat': 'vehicles', 'city': 'Islamabad'},
{'title': 'Suzuki Jimny - 2024', 'desc': 'Brand new Jimny, 4x4, perfect for off-roading and hilly areas. AC, power steering.', 'price': 6000, 'cat': 'vehicles', 'city': 'Islamabad'},
{'title': 'Toyota Yaris Ativ X - 2023', 'desc': 'Yaris Ativ X CVT, sunroof, 7 airbags. Safe and comfortable for family trips.', 'price': 4000, 'cat': 'vehicles', 'city': 'Islamabad'},
{'title': 'Kia Sportage Alpha - 2022', 'desc': 'Sportage Alpha, panoramic sunroof, ventilated seats. Luxury compact SUV for events.', 'price': 9000, 'cat': 'vehicles', 'city': 'Islamabad'},
{'title': 'Suzuki Mehran - 2018', 'desc': 'Budget-friendly Mehran for daily city use. AC, CNG, economical for students and small errands.', 'price': 1500, 'cat': 'vehicles', 'city': 'Islamabad'},

# ========== VEHICLES FOR RENT - Rawalpindi ==========
{'title': 'Toyota Corolla XLI - 2021', 'desc': 'Silver XLI manual, AC, power windows. Perfect for weddings and city travel.', 'price': 3500, 'cat': 'vehicles', 'city': 'Rawalpindi'},
{'title': 'Honda Civic Rebirth - 2019', 'desc': 'White Civic Rebirth, sunroof, leather seats. Popular for weddings and receptions.', 'price': 4000, 'cat': 'vehicles', 'city': 'Rawalpindi'},
{'title': 'Suzuki Bolan - 2020', 'desc': 'Bolan van, 7-seater, perfect for small family trips and luggage transport. AC, economical.', 'price': 2500, 'cat': 'vehicles', 'city': 'Rawalpindi'},
{'title': 'Toyota Vitz - 2018', 'desc': 'Imported Vitz, automatic, fuel efficient. Perfect for city use and small families.', 'price': 3000, 'cat': 'vehicles', 'city': 'Rawalpindi'},
{'title': 'Honda BR-V - 2021', 'desc': '7-seater BR-V, perfect for Murree trips and family outings. AC, spacious.', 'price': 5000, 'cat': 'vehicles', 'city': 'Rawalpindi'},
{'title': 'Suzuki Ravi - 2019', 'desc': 'Ravi pickup for luggage shifting and small goods transport. Perfect for moving houses.', 'price': 2000, 'cat': 'vehicles', 'city': 'Rawalpindi'},

# ========== VEHICLES FOR RENT - Faisalabad ==========
{'title': 'Toyota Corolla GLI - 2020', 'desc': 'Grey GLI automatic, perfect for weddings and business meetings. AC, clean condition.', 'price': 4000, 'cat': 'vehicles', 'city': 'Faisalabad'},
{'title': 'Honda City - 2019', 'desc': 'White City 1.2L manual, fuel efficient, perfect for city tours and family visits.', 'price': 3000, 'cat': 'vehicles', 'city': 'Faisalabad'},
{'title': 'Suzuki Alto - 2022', 'desc': 'Alto VX, AC, CNG, economical for daily use. Perfect for students and small errands.', 'price': 1800, 'cat': 'vehicles', 'city': 'Faisalabad'},
{'title': 'Toyota Hiace - 2018', 'desc': 'Hiace van for wedding parties and family trips. 14-seater, AC, with driver.', 'price': 7000, 'cat': 'vehicles', 'city': 'Faisalabad'},
{'title': 'Honda Insight - 2019', 'desc': 'Hybrid Insight, fuel efficient, perfect for outstation trips and business travel.', 'price': 5000, 'cat': 'vehicles', 'city': 'Faisalabad'},
{'title': 'Suzuki Cultus - 2021', 'desc': 'Cultus VXL, automatic, AC, perfect for shopping trips and city events.', 'price': 2500, 'cat': 'vehicles', 'city': 'Faisalabad'},

# ========== VEHICLES FOR RENT - Multan ==========
{'title': 'Toyota Corolla Altis - 2021', 'desc': 'White Altis X automatic, sunroof, leather seats. Perfect for weddings and VIP guests.', 'price': 5500, 'cat': 'vehicles', 'city': 'Multan'},
{'title': 'Honda Civic Oriel - 2020', 'desc': 'Black Civic Oriel, sunroof, premium sound system. Popular for valima and receptions.', 'price': 5000, 'cat': 'vehicles', 'city': 'Multan'},
{'title': 'Suzuki Wagon R - 2023', 'desc': 'New Wagon R, spacious, AC, CNG option. Perfect for family trips and daily rental.', 'price': 2200, 'cat': 'vehicles', 'city': 'Multan'},
{'title': 'Toyota Fortuner - 2019', 'desc': 'White Fortuner 4x4, 7-seater, perfect for desert safari and VIP events.', 'price': 12000, 'cat': 'vehicles', 'city': 'Multan'},
{'title': 'Daihatsu Mira - 2020', 'desc': 'Imported Mira, automatic, fuel efficient. Perfect for city use and small families.', 'price': 2500, 'cat': 'vehicles', 'city': 'Multan'},
{'title': 'Suzuki Mehran - 2017', 'desc': 'Budget Mehran for city travel, AC, CNG, economical for students.', 'price': 1200, 'cat': 'vehicles', 'city': 'Multan'},

# ========== VEHICLES FOR RENT - Peshawar ==========
{'title': 'Toyota Corolla XLI - 2022', 'desc': 'White XLI automatic, perfect for weddings and family functions. AC, power steering.', 'price': 3800, 'cat': 'vehicles', 'city': 'Peshawar'},
{'title': 'Honda Civic - 2018', 'desc': 'Silver Civic 1.8 i-VTEC, sunroof, leather seats. Ideal for weddings and corporate events.', 'price': 4500, 'cat': 'vehicles', 'city': 'Peshawar'},
{'title': 'Suzuki Alto - 2021', 'desc': 'Alto VXL, AC, CNG, perfect for city tours and shopping. Economical and easy to park.', 'price': 2000, 'cat': 'vehicles', 'city': 'Peshawar'},
{'title': 'Toyota Hiace - 2021', 'desc': 'Hiace grand cabin, 14-seater, AC, comfortable. Perfect for wedding guests transport.', 'price': 7500, 'cat': 'vehicles', 'city': 'Peshawar'},
{'title': 'Honda Vezel - 2019', 'desc': 'Imported Vezel hybrid, sunroof, fuel efficient. Perfect for outstation trips and business.', 'price': 6000, 'cat': 'vehicles', 'city': 'Peshawar'},
{'title': 'Suzuki Bolan - 2022', 'desc': 'Bolan van, 7-seater, AC, perfect for family trips and luggage transport.', 'price': 2800, 'cat': 'vehicles', 'city': 'Peshawar'},

# ========== VEHICLES FOR RENT - Quetta ==========
{'title': 'Toyota Corolla GLI - 2020', 'desc': 'White GLI manual, AC, perfect for weddings and city travel. Well maintained.', 'price': 3500, 'cat': 'vehicles', 'city': 'Quetta'},
{'title': 'Honda City - 2021', 'desc': 'Grey City 1.2L, automatic, fuel efficient. Perfect for family trips and business.', 'price': 3200, 'cat': 'vehicles', 'city': 'Quetta'},
{'title': 'Suzuki Jimny - 2023', 'desc': 'Jimny 4x4, perfect for Ziarat trips and hilly areas. AC, reliable off-road.', 'price': 5500, 'cat': 'vehicles', 'city': 'Quetta'},
{'title': 'Toyota Land Cruiser - 2017', 'desc': 'Land Cruiser V8, 4x4, perfect for Ziarat/Hanna Lake trips and VIP guests.', 'price': 15000, 'cat': 'vehicles', 'city': 'Quetta'},
{'title': 'Suzuki Cultus - 2022', 'desc': 'Cultus VXL, automatic, AC, CNG. Perfect for city tours and small families.', 'price': 2400, 'cat': 'vehicles', 'city': 'Quetta'},
{'title': 'Suzuki Ravi - 2020', 'desc': 'Ravi pickup for goods transport and shifting. Perfect for moving household items.', 'price': 1800, 'cat': 'vehicles', 'city': 'Quetta'},

# ========== VEHICLES FOR RENT - Gujranwala ==========
{'title': 'Toyota Corolla Altis - 2020', 'desc': 'Black Altis 1.6 automatic, sunroof, leather seats. Perfect for weddings and VIP events.', 'price': 5000, 'cat': 'vehicles', 'city': 'Gujranwala'},
{'title': 'Honda Civic X - 2021', 'desc': 'Civic X Oriel, white, sunroof, sporty look. Ideal for young couples and events.', 'price': 5200, 'cat': 'vehicles', 'city': 'Gujranwala'},
{'title': 'Suzuki Wagon R - 2022', 'desc': 'Wagon R VXL, AC, spacious, CNG. Perfect for family trips and shopping.', 'price': 2100, 'cat': 'vehicles', 'city': 'Gujranwala'},
{'title': 'Toyota Hiace - 2019', 'desc': 'Hiace van, 14-seater, AC, comfortable seats. For wedding guests and family trips.', 'price': 6500, 'cat': 'vehicles', 'city': 'Gujranwala'},
{'title': 'Honda N-WGN - 2018', 'desc': 'Imported N-WGN, automatic, fuel efficient. Perfect for city use and small families.', 'price': 2200, 'cat': 'vehicles', 'city': 'Gujranwala'},
{'title': 'Suzuki Mehran - 2019', 'desc': 'Mehran Euro II, AC, CNG, budget-friendly for daily use and students.', 'price': 1300, 'cat': 'vehicles', 'city': 'Gujranwala'},

# ========== VEHICLES FOR RENT - Sialkot ==========
{'title': 'Toyota Corolla XLI - 2023', 'desc': 'New model XLI automatic, silver, AC, power windows. Perfect for weddings and business.', 'price': 4200, 'cat': 'vehicles', 'city': 'Sialkot'},
{'title': 'Honda Civic Rebirth - 2020', 'desc': 'Civic Rebirth, white, sunroof, premium audio. Popular for wedding events.', 'price': 4300, 'cat': 'vehicles', 'city': 'Sialkot'},
{'title': 'Suzuki Alto - 2023', 'desc': 'Alto VXL AGS, automatic, AC, fuel efficient. Perfect for city tours and shopping.', 'price': 2300, 'cat': 'vehicles', 'city': 'Sialkot'},
{'title': 'Toyota Fortuner - 2021', 'desc': 'Fortuner Sigma 4, black, 7-seater. Perfect for VIP events and corporate guests.', 'price': 13000, 'cat': 'vehicles', 'city': 'Sialkot'},
{'title': 'Honda Grace - 2019', 'desc': 'Imported Grace hybrid, fuel efficient, perfect for outstation trips and business.', 'price': 4800, 'cat': 'vehicles', 'city': 'Sialkot'},
{'title': 'Suzuki Bolan - 2021', 'desc': 'Bolan van, AC, 7-seater, perfect for family trips and airport pickup.', 'price': 2600, 'cat': 'vehicles', 'city': 'Sialkot'},

# ========== VEHICLES FOR RENT - Bahawalpur ==========
{'title': 'Toyota Corolla GLI - 2021', 'desc': 'White GLI automatic, AC, clean condition. Perfect for weddings and family functions.', 'price': 3800, 'cat': 'vehicles', 'city': 'Bahawalpur'},
{'title': 'Honda City - 2020', 'desc': 'Silver City 1.2L manual, fuel efficient. Perfect for city travel and family visits.', 'price': 2800, 'cat': 'vehicles', 'city': 'Bahawalpur'},
{'title': 'Suzuki Cultus - 2023', 'desc': 'New Cultus VXL, automatic, AC, CNG. Perfect for shopping trips and city events.', 'price': 2600, 'cat': 'vehicles', 'city': 'Bahawalpur'},
{'title': 'Toyota Prado - 2018', 'desc': 'Prado TX, 7-seater, 4x4, perfect for desert safari and Cholistan trips.', 'price': 14000, 'cat': 'vehicles', 'city': 'Bahawalpur'},
{'title': 'Daihatsu Move - 2019', 'desc': 'Imported Move, automatic, spacious small car. Perfect for city use and families.', 'price': 2200, 'cat': 'vehicles', 'city': 'Bahawalpur'},
{'title': 'Suzuki Ravi - 2021', 'desc': 'Ravi pickup for goods transport and luggage shifting. Perfect for moving purposes.', 'price': 1900, 'cat': 'vehicles', 'city': 'Bahawalpur'},

# ========== VEHICLES FOR RENT - Hyderabad ==========
{'title': 'Toyota Corolla Altis - 2019', 'desc': 'White Altis 1.6 automatic, sunroof, leather seats. Perfect for weddings and events.', 'price': 4500, 'cat': 'vehicles', 'city': 'Hyderabad'},
{'title': 'Honda Civic - 2019', 'desc': 'Black Civic Oriel, sunroof, paddle shifters. Ideal for valima and receptions.', 'price': 4200, 'cat': 'vehicles', 'city': 'Hyderabad'},
{'title': 'Suzuki Wagon R - 2021', 'desc': 'Wagon R VXL, AC, CNG, spacious interior. Perfect for family trips and shopping.', 'price': 2000, 'cat': 'vehicles', 'city': 'Hyderabad'},
{'title': 'Toyota Hiace - 2020', 'desc': 'Hiace van, 14-seater, AC, comfortable. For wedding parties and family trips.', 'price': 6800, 'cat': 'vehicles', 'city': 'Hyderabad'},
{'title': 'Honda N-One - 2018', 'desc': 'Imported N-One, automatic, fuel efficient. Perfect for city use and small errands.', 'price': 2000, 'cat': 'vehicles', 'city': 'Hyderabad'},
{'title': 'Suzuki Mehran - 2018', 'desc': 'Mehran VX, AC, CNG, budget-friendly for students and daily use.', 'price': 1100, 'cat': 'vehicles', 'city': 'Hyderabad'},

# ========== VEHICLES FOR RENT - Sukkur ==========
{'title': 'Toyota Corolla XLI - 2021', 'desc': 'Grey XLI manual, AC, power steering. Perfect for weddings and city travel.', 'price': 3400, 'cat': 'vehicles', 'city': 'Sukkur'},
{'title': 'Honda City - 2019', 'desc': 'White City 1.2L automatic, fuel efficient. Perfect for family trips and business.', 'price': 2900, 'cat': 'vehicles', 'city': 'Sukkur'},
{'title': 'Suzuki Alto - 2022', 'desc': 'Alto VX, AC, CNG, economical for daily use. Perfect for shopping and errands.', 'price': 1900, 'cat': 'vehicles', 'city': 'Sukkur'},
{'title': 'Toyota Vitz - 2017', 'desc': 'Imported Vitz, automatic, fuel efficient. Perfect for city use and small families.', 'price': 2700, 'cat': 'vehicles', 'city': 'Sukkur'},
{'title': 'Honda BR-V - 2020', 'desc': 'BR-V 7-seater, AC, perfect for family outings and airport pickup.', 'price': 4600, 'cat': 'vehicles', 'city': 'Sukkur'},
{'title': 'Suzuki Bolan - 2019', 'desc': 'Bolan van, 7-seater, AC, economical for family trips and luggage.', 'price': 2400, 'cat': 'vehicles', 'city': 'Sukkur'},

# ========== VEHICLES FOR RENT - Larkana ==========
{'title': 'Toyota Corolla GLI - 2019', 'desc': 'White GLI automatic, AC, well maintained. Perfect for weddings and family events.', 'price': 3600, 'cat': 'vehicles', 'city': 'Larkana'},
{'title': 'Honda Civic - 2017', 'desc': 'Silver Civic 1.8, sunroof, leather seats. Ideal for wedding receptions and events.', 'price': 3800, 'cat': 'vehicles', 'city': 'Larkana'},
{'title': 'Suzuki Cultus - 2021', 'desc': 'Cultus VXL, automatic, AC, CNG. Perfect for city tours and family visits.', 'price': 2300, 'cat': 'vehicles', 'city': 'Larkana'},
{'title': 'Toyota Hiace - 2018', 'desc': 'Hiace van for wedding guests, 14-seater, AC, with driver included.', 'price': 6000, 'cat': 'vehicles', 'city': 'Larkana'},
{'title': 'Daihatsu Mira - 2020', 'desc': 'Imported Mira, automatic, fuel efficient. Perfect for city use and small errands.', 'price': 2400, 'cat': 'vehicles', 'city': 'Larkana'},
{'title': 'Suzuki Ravi - 2019', 'desc': 'Ravi pickup for goods transport, perfect for shifting and luggage.', 'price': 1700, 'cat': 'vehicles', 'city': 'Larkana'},

# ========== VEHICLES FOR RENT - Mirpur Khas ==========
{'title': 'Toyota Corolla XLI - 2020', 'desc': 'White XLI manual, AC, power windows. Perfect for weddings and business travel.', 'price': 3300, 'cat': 'vehicles', 'city': 'Mirpur Khas'},
{'title': 'Honda City - 2018', 'desc': 'Grey City 1.2L manual, fuel efficient. Perfect for city tours and family visits.', 'price': 2600, 'cat': 'vehicles', 'city': 'Mirpur Khas'},
{'title': 'Suzuki Wagon R - 2020', 'desc': 'Wagon R VX, AC, CNG, spacious. Perfect for family trips and shopping.', 'price': 1900, 'cat': 'vehicles', 'city': 'Mirpur Khas'},
{'title': 'Suzuki Mehran - 2019', 'desc': 'Mehran VX, AC, CNG, budget-friendly for students and daily use.', 'price': 1000, 'cat': 'vehicles', 'city': 'Mirpur Khas'},
{'title': 'Honda Vezel - 2017', 'desc': 'Imported Vezel hybrid, sunroof, fuel efficient. Perfect for outstation trips.', 'price': 5500, 'cat': 'vehicles', 'city': 'Mirpur Khas'},
{'title': 'Suzuki Bolan - 2020', 'desc': 'Bolan van, 7-seater, AC, perfect for small family trips.', 'price': 2300, 'cat': 'vehicles', 'city': 'Mirpur Khas'},

# ========== VEHICLES FOR RENT - Nawabshah ==========
{'title': 'Toyota Corolla GLI - 2018', 'desc': 'White GLI automatic, AC, clean condition. Perfect for weddings and events.', 'price': 3200, 'cat': 'vehicles', 'city': 'Nawabshah'},
{'title': 'Honda Civic - 2016', 'desc': 'White Civic 1.8 i-VTEC, sunroof. Ideal for wedding functions and receptions.', 'price': 3500, 'cat': 'vehicles', 'city': 'Nawabshah'},
{'title': 'Suzuki Alto - 2021', 'desc': 'Alto VX, AC, CNG, fuel efficient. Perfect for city travel and shopping.', 'price': 1800, 'cat': 'vehicles', 'city': 'Nawabshah'},
{'title': 'Toyota Vitz - 2016', 'desc': 'Imported Vitz, automatic, fuel efficient. Perfect for city use and small families.', 'price': 2500, 'cat': 'vehicles', 'city': 'Nawabshah'},
{'title': 'Suzuki Cultus - 2020', 'desc': 'Cultus VXL, AC, CNG, perfect for daily rental and family visits.', 'price': 2200, 'cat': 'vehicles', 'city': 'Nawabshah'},
{'title': 'Suzuki Ravi - 2020', 'desc': 'Ravi pickup for goods transport and shifting purposes.', 'price': 1600, 'cat': 'vehicles', 'city': 'Nawabshah'},

# ========== VEHICLES FOR RENT - Rahim Yar Khan ==========
{'title': 'Toyota Corolla Altis - 2020', 'desc': 'Black Altis 1.6 automatic, sunroof, leather seats. Perfect for weddings and VIP events.', 'price': 4800, 'cat': 'vehicles', 'city': 'Rahim Yar Khan'},
{'title': 'Honda Civic X - 2019', 'desc': 'Civic X Oriel, white, sunroof, sporty look. Ideal for young couples and events.', 'price': 4600, 'cat': 'vehicles', 'city': 'Rahim Yar Khan'},
{'title': 'Suzuki Wagon R - 2022', 'desc': 'Wagon R VXL, AC, CNG, spacious. Perfect for family trips and shopping.', 'price': 2100, 'cat': 'vehicles', 'city': 'Rahim Yar Khan'},
{'title': 'Toyota Fortuner - 2018', 'desc': 'Fortuner 4x4, 7-seater, perfect for desert trips and VIP guests.', 'price': 11000, 'cat': 'vehicles', 'city': 'Rahim Yar Khan'},
{'title': 'Daihatsu Move - 2020', 'desc': 'Imported Move, automatic, spacious. Perfect for city use and families.', 'price': 2300, 'cat': 'vehicles', 'city': 'Rahim Yar Khan'},
{'title': 'Suzuki Bolan - 2021', 'desc': 'Bolan van, AC, 7-seater, perfect for family outings and airport pickup.', 'price': 2500, 'cat': 'vehicles', 'city': 'Rahim Yar Khan'},

# ========== VEHICLES FOR RENT - Sargodha ==========
{'title': 'Toyota Corolla XLI - 2021', 'desc': 'Silver XLI automatic, AC, power windows. Perfect for weddings and business.', 'price': 3700, 'cat': 'vehicles', 'city': 'Sargodha'},
{'title': 'Honda City - 2020', 'desc': 'White City 1.2L automatic, fuel efficient. Perfect for family trips and city travel.', 'price': 3000, 'cat': 'vehicles', 'city': 'Sargodha'},
{'title': 'Suzuki Alto - 2023', 'desc': 'Alto VXL AGS, automatic, AC, fuel efficient. Perfect for shopping and errands.', 'price': 2200, 'cat': 'vehicles', 'city': 'Sargodha'},
{'title': 'Toyota Hiace - 2019', 'desc': 'Hiace van, 14-seater, AC, comfortable. For wedding parties and family trips.', 'price': 6200, 'cat': 'vehicles', 'city': 'Sargodha'},
{'title': 'Honda N-WGN - 2019', 'desc': 'Imported N-WGN, automatic, fuel efficient. Perfect for city use and small errands.', 'price': 2100, 'cat': 'vehicles', 'city': 'Sargodha'},
{'title': 'Suzuki Mehran - 2020', 'desc': 'Mehran VXR, AC, CNG, budget-friendly for students and daily use.', 'price': 1200, 'cat': 'vehicles', 'city': 'Sargodha'},

# ========== VEHICLES FOR RENT - Jhang ==========
{'title': 'Toyota Corolla GLI - 2019', 'desc': 'White GLI manual, AC, well maintained. Perfect for weddings and family functions.', 'price': 3100, 'cat': 'vehicles', 'city': 'Jhang'},
{'title': 'Honda Civic - 2017', 'desc': 'Grey Civic 1.8, sunroof, leather seats. Ideal for wedding receptions.', 'price': 3600, 'cat': 'vehicles', 'city': 'Jhang'},
{'title': 'Suzuki Cultus - 2021', 'desc': 'Cultus VX, AC, CNG, fuel efficient. Perfect for city tours and family visits.', 'price': 2000, 'cat': 'vehicles', 'city': 'Jhang'},
{'title': 'Suzuki Wagon R - 2020', 'desc': 'Wagon R VX, AC, spacious, perfect for small family trips.', 'price': 1800, 'cat': 'vehicles', 'city': 'Jhang'},
{'title': 'Daihatsu Mira - 2018', 'desc': 'Imported Mira, automatic, fuel efficient. Perfect for city use.', 'price': 2200, 'cat': 'vehicles', 'city': 'Jhang'},
{'title': 'Suzuki Bolan - 2018', 'desc': 'Bolan van, 7-seater, AC, economical for family trips.', 'price': 2200, 'cat': 'vehicles', 'city': 'Jhang'},

# ========== VEHICLES FOR RENT - Sahiwal ==========
{'title': 'Toyota Corolla XLI - 2020', 'desc': 'White XLI manual, AC, power steering. Perfect for weddings and city travel.', 'price': 3000, 'cat': 'vehicles', 'city': 'Sahiwal'},
{'title': 'Honda City - 2019', 'desc': 'Silver City 1.2L manual, fuel efficient. Perfect for family trips and business.', 'price': 2700, 'cat': 'vehicles', 'city': 'Sahiwal'},
{'title': 'Suzuki Alto - 2022', 'desc': 'Alto VX, AC, CNG, economical for daily use and shopping.', 'price': 1700, 'cat': 'vehicles', 'city': 'Sahiwal'},
{'title': 'Toyota Vitz - 2017', 'desc': 'Imported Vitz, automatic, fuel efficient. Perfect for city use and small families.', 'price': 2400, 'cat': 'vehicles', 'city': 'Sahiwal'},
{'title': 'Suzuki Mehran - 2019', 'desc': 'Mehran VX, AC, CNG, budget-friendly for students.', 'price': 1100, 'cat': 'vehicles', 'city': 'Sahiwal'},
{'title': 'Suzuki Ravi - 2020', 'desc': 'Ravi pickup for goods transport and shifting purposes.', 'price': 1500, 'cat': 'vehicles', 'city': 'Sahiwal'},
    {
        'title': 'Honda Civic - Luxury Rent',
        'desc': '2023 model, automatic, sunroof, leather seats. For family trips/events.',
        'price': 6000,
        'cat': 'vehicles',
        'city': 'Lahore'
    },
    {
        'title': 'Suzuki Wagon R - Family Use',
        'desc': 'Spacious, fuel efficient, AC. Perfect for family travel and daily use.',
        'price': 3000,
        'cat': 'vehicles',
        'city': 'Islamabad'
    },
    {
        'title': 'Honda CD 70 Bike',
        'desc': '2023 model, low fuel consumption, well maintained. Daily rental.',
        'price': 500,
        'cat': 'vehicles',
        'city': 'Karachi'
    },
    {
        'title': 'Toyota HiAce - 12 Seater',
        'desc': 'For family trips, picnics, events. 12 seats with AC. Driver available.',
        'price': 8000,
        'cat': 'vehicles',
        'city': 'Lahore'
    },
    {
        'title': 'Suzuki Alto - City Use',
        'desc': '2023 model, automatic, AC. Perfect for city driving.',
        'price': 2500,
        'cat': 'vehicles',
        'city': 'Rawalpindi'
    },
    {
        'title': 'Yamaha YBR 125 Bike',
        'desc': 'Sporty look, good condition, helmet included.',
        'price': 800,
        'cat': 'vehicles',
        'city': 'Karachi'
    },
    {
        'title': 'Cultus - Daily Rent',
        'desc': 'AC, power steering, good fuel average. For daily commute.',
        'price': 2500,
        'cat': 'vehicles',
        'city': 'Islamabad'
    },
    
    # ========== EVENT EQUIPMENT ==========
    {
        'title': 'Sound System for Wedding',
        'desc': '2 speakers + amplifier + microphones. 1000W power. Perfect for wedding/party.',
        'price': 4000,
        'cat': 'electronics',
        'city': 'Karachi'
    },
    {
        'title': 'LED Wall Display',
        'desc': '10x6 feet LED screen for wedding/birthday. Perfect for backdrop.',
        'price': 8000,
        'cat': 'electronics',
        'city': 'Lahore'
    },
    {
        'title': 'Projector for Event',
        'desc': 'HD projector with screen. For presentations/events.',
        'price': 2000,
        'cat': 'electronics',
        'city': 'Islamabad'
    },
    {
        'title': 'Camera for Wedding Photography',
        'desc': 'Canon EOS 1500D with lens, tripod, memory card. Professional photography.',
        'price': 2500,
        'cat': 'electronics',
        'city': 'Karachi'
    },
    {
        'title': 'DJI Drone - Aerial Shooting',
        'desc': 'For wedding aerial photography/videography. With extra batteries.',
        'price': 5000,
        'cat': 'electronics',
        'city': 'Lahore'
    },
    {
        'title': 'Microphone Set - Wireless',
        'desc': '2 wireless mics for events/nikkah. Clear sound.',
        'price': 1000,
        'cat': 'electronics',
        'city': 'Rawalpindi'
    },
    
    # ========== FURNITURE FOR RENT ==========
    {
        'title': 'Wedding Stage Furniture',
        'desc': 'Royal sofa set for barat stage. 3 pieces with covers.',
        'price': 3000,
        'cat': 'furniture',
        'city': 'Karachi'
    },
    # ========== FURNITURE FOR RENT - Karachi ==========
{'title': 'Sofa Set - 5 Seater L Shape', 'desc': 'Premium L-shaped sofa set, beige fabric, comfortable for living room. Perfect for events and temporary accommodation.', 'price': 3500, 'cat': 'furniture', 'city': 'Karachi'},
{'title': 'Double Bed with Mattress', 'desc': 'Queen size bed with orthopedic mattress, wooden frame. Perfect for guests and temporary stays.', 'price': 2000, 'cat': 'furniture', 'city': 'Karachi'},
{'title': 'Dining Table - 6 Seater', 'desc': 'Wooden dining table with 6 chairs, elegant design. Perfect for family gatherings and events.', 'price': 2500, 'cat': 'furniture', 'city': 'Karachi'},
{'title': 'Wardrobe - 3 Door Wooden', 'desc': 'Large wooden wardrobe with mirror, ample storage space. Perfect for temporary accommodation.', 'price': 1800, 'cat': 'furniture', 'city': 'Karachi'},
{'title': 'Fridge - Haier Double Door', 'desc': 'Double door refrigerator, 14 cubic feet, energy efficient. Perfect for temporary housing and events.', 'price': 1500, 'cat': 'furniture', 'city': 'Karachi'},
{'title': 'LED TV 43 Inch with Stand', 'desc': 'Samsung 43" Smart LED TV with wall mount stand. Perfect for temporary accommodation and events.', 'price': 1200, 'cat': 'furniture', 'city': 'Karachi'},

# ========== FURNITURE FOR RENT - Lahore ==========
{'title': 'Sofa Set - 7 Seater Velvet', 'desc': 'Royal velvet sofa set, burgundy color, 3+2+1+1 configuration. Perfect for weddings and VIP events.', 'price': 5000, 'cat': 'furniture', 'city': 'Lahore'},
{'title': 'King Size Bed with Storage', 'desc': 'King size bed with hydraulic storage, premium mattress included. Perfect for bridal room and guests.', 'price': 3000, 'cat': 'furniture', 'city': 'Lahore'},
{'title': 'Dining Table - 8 Seater Glass', 'desc': 'Glass top dining table with 8 cushioned chairs, modern design. Perfect for dinner parties.', 'price': 3500, 'cat': 'furniture', 'city': 'Lahore'},
{'title': 'Dressing Table with Mirror', 'desc': 'Wooden dressing table with large mirror, 4 drawers, stool included. Perfect for bridal room.', 'price': 1200, 'cat': 'furniture', 'city': 'Lahore'},
{'title': 'Washing Machine - Automatic', 'desc': 'Dawlance automatic washing machine, 8kg capacity. Perfect for temporary accommodation.', 'price': 1000, 'cat': 'furniture', 'city': 'Lahore'},
{'title': 'Air Conditioner - 1.5 Ton', 'desc': 'Gree 1.5 ton split AC, cooling/heating, energy efficient. Perfect for events and temporary stays.', 'price': 2000, 'cat': 'furniture', 'city': 'Lahore'},

# ========== FURNITURE FOR RENT - Islamabad ==========
{'title': 'Sofa Set - Italian Leather', 'desc': 'Premium Italian leather sofa set, 3+2 configuration, black color. Perfect for corporate events and VIP stays.', 'price': 6000, 'cat': 'furniture', 'city': 'Islamabad'},
{'title': 'Bed Set - Complete Bedroom', 'desc': 'Complete bedroom set including bed, side tables, dressing table, and wardrobe. Premium quality.', 'price': 5000, 'cat': 'furniture', 'city': 'Islamabad'},
{'title': 'Office Furniture Package', 'desc': 'Complete office setup: 2 desks, 2 chairs, filing cabinet, and bookshelf. Perfect for temporary offices.', 'price': 4000, 'cat': 'furniture', 'city': 'Islamabad'},
{'title': 'Center Table - Designer', 'desc': 'Designer wooden center table with glass top, modern design. Perfect for living room setup.', 'price': 800, 'cat': 'furniture', 'city': 'Islamabad'},
{'title': 'Microwave Oven - LG', 'desc': 'LG microwave oven, 28L capacity, grill function. Perfect for temporary kitchen setup.', 'price': 500, 'cat': 'furniture', 'city': 'Islamabad'},
{'title': 'Water Dispenser - Hot/Cold', 'desc': 'Nova water dispenser with hot and cold options. Perfect for events and temporary offices.', 'price': 400, 'cat': 'furniture', 'city': 'Islamabad'},

# ========== FURNITURE FOR RENT - Rawalpindi ==========
{'title': 'Sofa Set - 5 Seater Fabric', 'desc': 'Comfortable fabric sofa set, grey color, 3+2 configuration. Perfect for temporary accommodation.', 'price': 3000, 'cat': 'furniture', 'city': 'Rawalpindi'},
{'title': 'Single Bed with Mattress', 'desc': 'Single bed with foam mattress, wooden frame. Perfect for guests and single occupancy.', 'price': 1000, 'cat': 'furniture', 'city': 'Rawalpindi'},
{'title': 'Dining Table - 4 Seater', 'desc': 'Compact wooden dining table with 4 chairs. Perfect for small families and temporary setup.', 'price': 1500, 'cat': 'furniture', 'city': 'Rawalpindi'},
{'title': 'Cupboard - 2 Door Steel', 'desc': 'Steel cupboard with lock, ample storage for clothes and items. Perfect for temporary stays.', 'price': 1200, 'cat': 'furniture', 'city': 'Rawalpindi'},
{'title': 'Deep Freezer - Waves', 'desc': 'Waves deep freezer, 300L capacity. Perfect for events and food storage.', 'price': 1000, 'cat': 'furniture', 'city': 'Rawalpindi'},
{'title': 'Iron with Ironing Board', 'desc': 'Philips steam iron with adjustable ironing board. Essential for temporary accommodation.', 'price': 200, 'cat': 'furniture', 'city': 'Rawalpindi'},

# ========== FURNITURE FOR RENT - Faisalabad ==========
{'title': 'Sofa Set - 3+1+1 Design', 'desc': 'Elegant sofa set with center table, fabric upholstery. Perfect for living room setup.', 'price': 2800, 'cat': 'furniture', 'city': 'Faisalabad'},
{'title': 'Double Bed - Iron Frame', 'desc': 'Iron frame double bed with spring mattress, durable and comfortable. Perfect for temporary stays.', 'price': 1800, 'cat': 'furniture', 'city': 'Faisalabad'},
{'title': 'Dining Table - 6 Seater Wooden', 'desc': 'Solid wood dining table with 6 chairs, traditional design. Perfect for family gatherings.', 'price': 2200, 'cat': 'furniture', 'city': 'Faisalabad'},
{'title': 'Computer Table with Chair', 'desc': 'Study table with drawer and comfortable chair. Perfect for students and temporary work setup.', 'price': 600, 'cat': 'furniture', 'city': 'Faisalabad'},
{'title': 'Electric Kettle - Philips', 'desc': 'Philips electric kettle 1.7L, quick boil. Essential for temporary kitchen.', 'price': 150, 'cat': 'furniture', 'city': 'Faisalabad'},
{'title': 'Room Cooler - 40L', 'desc': 'Large room cooler with 3-speed fan, perfect for summer temporary accommodation.', 'price': 800, 'cat': 'furniture', 'city': 'Faisalabad'},

# ========== FURNITURE FOR RENT - Multan ==========
{'title': 'Sofa Set - Traditional Style', 'desc': 'Traditional Multani style sofa set, wooden frame with cushions. Perfect for events.', 'price': 3200, 'cat': 'furniture', 'city': 'Multan'},
{'title': 'Bed with Side Tables', 'desc': 'Queen size bed with two side tables, wooden finish. Complete sleeping setup.', 'price': 2200, 'cat': 'furniture', 'city': 'Multan'},
{'title': 'Dining Table - 8 Seater', 'desc': 'Large wooden dining table with 8 chairs, perfect for big families and events.', 'price': 3000, 'cat': 'furniture', 'city': 'Multan'},
{'title': 'Almirah - Wooden Large', 'desc': 'Traditional wooden almirah with 4 shelves, perfect for storage.', 'price': 1500, 'cat': 'furniture', 'city': 'Multan'},
{'title': 'Gas Stove - 4 Burner', 'desc': 'Cannon 4 burner gas stove with oven. Perfect for temporary kitchen setup.', 'price': 700, 'cat': 'furniture', 'city': 'Multan'},
{'title': 'Ceiling Fan - 56 Inch', 'desc': 'GFC ceiling fan, 56 inch, 3-speed. Essential for summer temporary stays.', 'price': 300, 'cat': 'furniture', 'city': 'Multan'},

# ========== FURNITURE FOR RENT - Peshawar ==========
{'title': 'Sofa Set - Peshawari Style', 'desc': 'Traditional Peshawari style sofa set with intricate woodwork, cushions included.', 'price': 4000, 'cat': 'furniture', 'city': 'Peshawar'},
{'title': 'Bed Set - Walnut Wood', 'desc': 'Beautiful walnut wood bed with carved headboard, mattress included.', 'price': 2800, 'cat': 'furniture', 'city': 'Peshawar'},
{'title': 'Carpet - Afghan Style', 'desc': 'Large Afghan style carpet, 12x15 feet, perfect for living room and events.', 'price': 2000, 'cat': 'furniture', 'city': 'Peshawar'},
{'title': 'Dining Table - 6 Seater', 'desc': 'Solid wood dining table with 6 chairs, traditional design.', 'price': 2500, 'cat': 'furniture', 'city': 'Peshawar'},
{'title': 'Gas Heater - Winter', 'desc': 'Large gas heater for winter, perfect for temporary accommodation in cold weather.', 'price': 600, 'cat': 'furniture', 'city': 'Peshawar'},
{'title': 'Wardrobe - 2 Door', 'desc': 'Wooden wardrobe with 2 doors and drawer, ample storage space.', 'price': 1400, 'cat': 'furniture', 'city': 'Peshawar'},

# ========== FURNITURE FOR RENT - Quetta ==========
{'title': 'Sofa Set - Warm Fabric', 'desc': 'Cozy fabric sofa set, warm colors, perfect for Quetta winters. 3+2 configuration.', 'price': 3500, 'cat': 'furniture', 'city': 'Quetta'},
{'title': 'Bed with Woolen Mattress', 'desc': 'Queen size bed with woolen mattress topper, perfect for cold weather stays.', 'price': 2300, 'cat': 'furniture', 'city': 'Quetta'},
{'title': 'Bukhari - Heating Stove', 'desc': 'Traditional bukhari heating stove, perfect for winter accommodation. Wood/coal fuel.', 'price': 500, 'cat': 'furniture', 'city': 'Quetta'},
{'title': 'Dining Table - 4 Seater', 'desc': 'Compact wooden dining table with 4 chairs, perfect for small families.', 'price': 1600, 'cat': 'furniture', 'city': 'Quetta'},
{'title': 'Carpet - Thick Wool', 'desc': 'Thick wool carpet, 10x12 feet, warm and comfortable for winters.', 'price': 1800, 'cat': 'furniture', 'city': 'Quetta'},
{'title': 'Electric Heater - 2000W', 'desc': 'Electric room heater with thermostat, perfect for quick heating.', 'price': 400, 'cat': 'furniture', 'city': 'Quetta'},

# ========== FURNITURE FOR RENT - Gujranwala ==========
{'title': 'Sofa Set - Modern Design', 'desc': 'Modern L-shaped sofa set, grey fabric, comfortable and stylish.', 'price': 3300, 'cat': 'furniture', 'city': 'Gujranwala'},
{'title': 'Double Bed - Steel Frame', 'desc': 'Steel frame double bed with premium mattress, durable and rust-proof.', 'price': 1900, 'cat': 'furniture', 'city': 'Gujranwala'},
{'title': 'Dining Table - Glass Top', 'desc': 'Glass top dining table with 6 steel chairs, modern look.', 'price': 2400, 'cat': 'furniture', 'city': 'Gujranwala'},
{'title': 'Washing Machine - Semi Auto', 'desc': 'Semi-automatic washing machine, 7kg capacity, perfect for temporary stays.', 'price': 600, 'cat': 'furniture', 'city': 'Gujranwala'},
{'title': 'Book Shelf - 5 Tier', 'desc': 'Wooden book shelf with 5 tiers, perfect for students and temporary offices.', 'price': 700, 'cat': 'furniture', 'city': 'Gujranwala'},
{'title': 'Pedestal Fan - 18 Inch', 'desc': 'Large pedestal fan, 3-speed, perfect for summer cooling.', 'price': 250, 'cat': 'furniture', 'city': 'Gujranwala'},

# ========== FURNITURE FOR RENT - Sialkot ==========
{'title': 'Sofa Set - Executive Style', 'desc': 'Executive sofa set, black leather finish, 3+2 configuration. Perfect for offices and VIP stays.', 'price': 4500, 'cat': 'furniture', 'city': 'Sialkot'},
{'title': 'Bed Set - Complete', 'desc': 'Complete bed set with mattress, side tables, and lamp. Ready to use.', 'price': 2500, 'cat': 'furniture', 'city': 'Sialkot'},
{'title': 'Office Chair - Ergonomic', 'desc': 'Premium ergonomic office chair with lumbar support. Perfect for work from home setup.', 'price': 800, 'cat': 'furniture', 'city': 'Sialkot'},
{'title': 'Dining Table - 6 Seater', 'desc': 'Elegant dining table with 6 chairs, wooden finish.', 'price': 2600, 'cat': 'furniture', 'city': 'Sialkot'},
{'title': 'Air Cooler - 60L', 'desc': 'Large air cooler with remote control, perfect for summer events and temporary stays.', 'price': 1000, 'cat': 'furniture', 'city': 'Sialkot'},
{'title': 'Juicer Blender - Westpoint', 'desc': 'Westpoint juicer blender with 3 jars, perfect for temporary kitchen.', 'price': 300, 'cat': 'furniture', 'city': 'Sialkot'},

# ========== FURNITURE FOR RENT - Bahawalpur ==========
{'title': 'Sofa Set - Royal Style', 'desc': 'Royal style sofa set with wooden carvings, velvet cushions. Perfect for weddings and events.', 'price': 4200, 'cat': 'furniture', 'city': 'Bahawalpur'},
{'title': 'Bed - Nawabi Style', 'desc': 'Traditional Nawabi style bed with carved headboard, mattress included.', 'price': 2700, 'cat': 'furniture', 'city': 'Bahawalpur'},
{'title': 'Dining Table - 8 Seater Wood', 'desc': 'Large wooden dining table with 8 chairs, traditional design.', 'price': 3200, 'cat': 'furniture', 'city': 'Bahawalpur'},
{'title': 'Chest of Drawers', 'desc': 'Wooden chest with 5 drawers, perfect for clothes storage.', 'price': 1000, 'cat': 'furniture', 'city': 'Bahawalpur'},
{'title': 'Desert Cooler - 80L', 'desc': 'Heavy duty desert cooler, perfect for Cholistan heat. Large water capacity.', 'price': 1200, 'cat': 'furniture', 'city': 'Bahawalpur'},
{'title': 'Carpet - Traditional', 'desc': 'Traditional Bahawalpuri carpet, 8x10 feet, beautiful patterns.', 'price': 1500, 'cat': 'furniture', 'city': 'Bahawalpur'},

# ========== FURNITURE FOR RENT - Hyderabad ==========
{'title': 'Sofa Set - 5 Seater', 'desc': 'Comfortable 5-seater sofa set, brown fabric, perfect for temporary accommodation.', 'price': 3000, 'cat': 'furniture', 'city': 'Hyderabad'},
{'title': 'Double Bed - Simple', 'desc': 'Simple double bed with foam mattress, affordable and comfortable.', 'price': 1600, 'cat': 'furniture', 'city': 'Hyderabad'},
{'title': 'Dining Table - 4 Seater', 'desc': 'Compact dining table with 4 chairs, perfect for small spaces.', 'price': 1400, 'cat': 'furniture', 'city': 'Hyderabad'},
{'title': 'Fridge - Single Door', 'desc': 'Single door refrigerator, 10 cubic feet, energy efficient.', 'price': 900, 'cat': 'furniture', 'city': 'Hyderabad'},
{'title': 'Wardrobe - Steel', 'desc': 'Steel wardrobe with 2 doors and lock, durable and secure.', 'price': 1100, 'cat': 'furniture', 'city': 'Hyderabad'},
{'title': 'Table Fan - 16 Inch', 'desc': 'Orient table fan, 16 inch, 3-speed, perfect for personal cooling.', 'price': 150, 'cat': 'furniture', 'city': 'Hyderabad'},

# ========== FURNITURE FOR RENT - Sukkur ==========
{'title': 'Sofa Set - 3+2 Fabric', 'desc': 'Fabric sofa set, 3+2 configuration, beige color. Perfect for living room.', 'price': 2800, 'cat': 'furniture', 'city': 'Sukkur'},
{'title': 'Single Bed with Storage', 'desc': 'Single bed with storage drawer, mattress included. Perfect for single occupancy.', 'price': 900, 'cat': 'furniture', 'city': 'Sukkur'},
{'title': 'Dining Table - 6 Seater', 'desc': 'Wooden dining table with 6 chairs, simple and functional.', 'price': 2000, 'cat': 'furniture', 'city': 'Sukkur'},
{'title': 'Deep Freezer - 200L', 'desc': 'Deep freezer 200L capacity, perfect for events and bulk storage.', 'price': 800, 'cat': 'furniture', 'city': 'Sukkur'},
{'title': 'Water Cooler - 50L', 'desc': 'Large water cooler with tap, perfect for events and gatherings.', 'price': 400, 'cat': 'furniture', 'city': 'Sukkur'},
{'title': 'Iron - Dry Iron', 'desc': 'Simple dry iron, 1000W, essential for temporary stays.', 'price': 100, 'cat': 'furniture', 'city': 'Sukkur'},

# ========== FURNITURE FOR RENT - Larkana ==========
{'title': 'Sofa Set - Traditional', 'desc': 'Traditional Sindhi style sofa set, wooden frame with bright cushions.', 'price': 3200, 'cat': 'furniture', 'city': 'Larkana'},
{'title': 'Bed - Wooden Simple', 'desc': 'Simple wooden bed with cotton mattress, comfortable for Sindh weather.', 'price': 1500, 'cat': 'furniture', 'city': 'Larkana'},
{'title': 'Dining Table - 4 Seater Wood', 'desc': 'Wooden dining table with 4 chairs, compact and sturdy.', 'price': 1300, 'cat': 'furniture', 'city': 'Larkana'},
{'title': 'Almirah - 2 Door', 'desc': 'Wooden almirah with 2 doors, perfect for clothes storage.', 'price': 1000, 'cat': 'furniture', 'city': 'Larkana'},
{'title': 'Gas Stove - 2 Burner', 'desc': 'Simple 2 burner gas stove, perfect for small kitchen setup.', 'price': 400, 'cat': 'furniture', 'city': 'Larkana'},
{'title': 'Ceiling Fan - 48 Inch', 'desc': 'Pak fan, 48 inch, 3-speed, essential for hot weather.', 'price': 250, 'cat': 'furniture', 'city': 'Larkana'},

# ========== FURNITURE FOR RENT - Mirpur Khas ==========
{'title': 'Sofa Set - 3 Seater', 'desc': 'Simple 3-seater sofa, fabric upholstery, comfortable for small spaces.', 'price': 2000, 'cat': 'furniture', 'city': 'Mirpur Khas'},
{'title': 'Double Bed - Iron', 'desc': 'Iron frame double bed with mattress, durable and affordable.', 'price': 1400, 'cat': 'furniture', 'city': 'Mirpur Khas'},
{'title': 'Dining Table - 6 Seater Simple', 'desc': 'Simple wooden dining table with 6 chairs, functional design.', 'price': 1800, 'cat': 'furniture', 'city': 'Mirpur Khas'},
{'title': 'Fridge - Haier Single Door', 'desc': 'Haier single door fridge, 12 cubic feet, reliable and efficient.', 'price': 1000, 'cat': 'furniture', 'city': 'Mirpur Khas'},
{'title': 'Washing Machine - Twin Tub', 'desc': 'Twin tub washing machine, 6kg wash capacity.', 'price': 500, 'cat': 'furniture', 'city': 'Mirpur Khas'},
{'title': 'Bracket Fan - 18 Inch', 'desc': 'Wall bracket fan, 18 inch, 3-speed, saves floor space.', 'price': 200, 'cat': 'furniture', 'city': 'Mirpur Khas'},

# ========== FURNITURE FOR RENT - Nawabshah ==========
{'title': 'Sofa Set - Simple 3+2', 'desc': 'Simple 3+2 sofa set, cotton fabric, easy to maintain.', 'price': 2500, 'cat': 'furniture', 'city': 'Nawabshah'},
{'title': 'Bed Set - Complete', 'desc': 'Complete bed set with mattress, pillow, and bed sheet.', 'price': 1700, 'cat': 'furniture', 'city': 'Nawabshah'},
{'title': 'Dining Table - 4 Seater', 'desc': 'Compact dining table with 4 chairs, perfect for families.', 'price': 1200, 'cat': 'furniture', 'city': 'Nawabshah'},
{'title': 'Cupboard - Steel Small', 'desc': 'Small steel cupboard with lock, perfect for valuable storage.', 'price': 800, 'cat': 'furniture', 'city': 'Nawabshah'},
{'title': 'Microwave Oven - Dawlance', 'desc': 'Dawlance microwave oven, 20L capacity, essential for quick meals.', 'price': 400, 'cat': 'furniture', 'city': 'Nawabshah'},
{'title': 'Pedestal Fan - 20 Inch', 'desc': 'Large pedestal fan, 20 inch, powerful airflow for hot weather.', 'price': 300, 'cat': 'furniture', 'city': 'Nawabshah'},

# ========== FURNITURE FOR RENT - Rahim Yar Khan ==========
{'title': 'Sofa Set - Premium Fabric', 'desc': 'Premium fabric sofa set, 3+2+1 configuration, elegant design.', 'price': 3800, 'cat': 'furniture', 'city': 'Rahim Yar Khan'},
{'title': 'King Size Bed - Luxury', 'desc': 'King size bed with luxury mattress, headboard with lights.', 'price': 3000, 'cat': 'furniture', 'city': 'Rahim Yar Khan'},
{'title': 'Dining Table - 8 Seater Glass', 'desc': 'Glass top dining table with 8 chairs, modern and elegant.', 'price': 3500, 'cat': 'furniture', 'city': 'Rahim Yar Khan'},
{'title': 'Air Conditioner - 1 Ton', 'desc': 'Haier 1 ton AC, cooling only, energy saver. Perfect for summer stays.', 'price': 1800, 'cat': 'furniture', 'city': 'Rahim Yar Khan'},
{'title': 'Wardrobe - 4 Door', 'desc': 'Large wooden wardrobe with 4 doors and mirror, ample storage.', 'price': 2000, 'cat': 'furniture', 'city': 'Rahim Yar Khan'},
{'title': 'TV Stand - Modern', 'desc': 'Modern TV stand with drawers, fits up to 55 inch TV.', 'price': 600, 'cat': 'furniture', 'city': 'Rahim Yar Khan'},

# ========== FURNITURE FOR RENT - Sargodha ==========
{'title': 'Sofa Set - 5 Seater Modern', 'desc': 'Modern 5-seater sofa set, grey fabric, comfortable cushions.', 'price': 3100, 'cat': 'furniture', 'city': 'Sargodha'},
{'title': 'Double Bed - Storage', 'desc': 'Double bed with storage drawers, mattress included.', 'price': 1800, 'cat': 'furniture', 'city': 'Sargodha'},
{'title': 'Dining Table - 6 Seater Simple', 'desc': 'Simple wooden dining table with 6 chairs, sturdy and functional.', 'price': 2100, 'cat': 'furniture', 'city': 'Sargodha'},
{'title': 'Fridge - Waves Double Door', 'desc': 'Waves double door fridge, 16 cubic feet, frost free.', 'price': 1600, 'cat': 'furniture', 'city': 'Sargodha'},
{'title': 'Dressing Table - Simple', 'desc': 'Simple dressing table with mirror and 2 drawers.', 'price': 700, 'cat': 'furniture', 'city': 'Sargodha'},
{'title': 'Room Cooler - 50L', 'desc': 'Large room cooler with honeycomb pads, efficient cooling.', 'price': 900, 'cat': 'furniture', 'city': 'Sargodha'},

# ========== FURNITURE FOR RENT - Jhang ==========
{'title': 'Sofa Set - Traditional Wood', 'desc': 'Traditional wooden sofa set with cushions, 3+2 configuration.', 'price': 2900, 'cat': 'furniture', 'city': 'Jhang'},
{'title': 'Single Bed - Iron', 'desc': 'Iron single bed with mattress, perfect for single person.', 'price': 800, 'cat': 'furniture', 'city': 'Jhang'},
{'title': 'Dining Table - 4 Seater Simple', 'desc': 'Simple 4-seater dining table with chairs, affordable option.', 'price': 1100, 'cat': 'furniture', 'city': 'Jhang'},
{'title': 'Cupboard - Wooden Small', 'desc': 'Small wooden cupboard with 2 shelves, perfect for small spaces.', 'price': 700, 'cat': 'furniture', 'city': 'Jhang'},
{'title': 'Electric Kettle - Simple', 'desc': 'Simple electric kettle, 1.5L, quick boiling.', 'price': 120, 'cat': 'furniture', 'city': 'Jhang'},
{'title': 'Ceiling Fan - 56 Inch', 'desc': 'Lahore fan, 56 inch, 3-speed, reliable and durable.', 'price': 280, 'cat': 'furniture', 'city': 'Jhang'},

# ========== FURNITURE FOR RENT - Sahiwal ==========
{'title': 'Sofa Set - 3+2 Simple', 'desc': 'Simple 3+2 sofa set, fabric upholstery, comfortable and affordable.', 'price': 2600, 'cat': 'furniture', 'city': 'Sahiwal'},
{'title': 'Double Bed - Simple Wood', 'desc': 'Simple wooden double bed with mattress, basic and functional.', 'price': 1500, 'cat': 'furniture', 'city': 'Sahiwal'},
{'title': 'Dining Table - 6 Seater', 'desc': 'Wooden dining table with 6 chairs, perfect for family meals.', 'price': 1900, 'cat': 'furniture', 'city': 'Sahiwal'},
{'title': 'Wardrobe - 2 Door Simple', 'desc': 'Simple 2-door wardrobe, wooden finish, adequate storage.', 'price': 1200, 'cat': 'furniture', 'city': 'Sahiwal'},
{'title': 'Gas Heater - Small', 'desc': 'Small gas heater for winter, perfect for room heating.', 'price': 350, 'cat': 'furniture', 'city': 'Sahiwal'},
{'title': 'Table Fan - 12 Inch', 'desc': 'Small table fan, 12 inch, perfect for personal use.', 'price': 130, 'cat': 'furniture', 'city': 'Sahiwal'},
    {
        'title': 'Chairs for Event - 100 pcs',
        'desc': '100 plastic chairs for wedding/event. Delivery and pickup included.',
        'price': 5000,
        'cat': 'furniture',
        'city': 'Lahore'
    },
    {
        'title': 'Tables for Event - 20 pcs',
        'desc': '20 rectangular tables for food/guests.',
        'price': 4000,
        'cat': 'furniture',
        'city': 'Islamabad'
    },
    {
        'title': 'Bed for Guest Room',
        'desc': 'Single bed with mattress. For temporary guests.',
        'price': 1000,
        'cat': 'furniture',
        'city': 'Karachi'
    },
    {
        'title': 'Sofa Set - 3+2+1',
        'desc': 'Fabric sofa set for event or temporary use.',
        'price': 2000,
        'cat': 'furniture',
        'city': 'Lahore'
    },
    {
        'title': 'Carpet - Large Size',
        'desc': '20x15 feet carpet for wedding/event.',
        'price': 1500,
        'cat': 'furniture',
        'city': 'Rawalpindi'
    },
    
    # ========== GENERATORS & TOOLS ==========
    {
        'title': 'Generator - 5kVA',
        'desc': 'For wedding/events. Petrol generator with fuel.',
        'price': 3000,
        'cat': 'other',
        'city': 'Karachi'
    },
    # ========== GENERATORS & TOOLS - Karachi ==========
{'title': 'Generator - Honda 20 KVA', 'desc': 'Honda 20 KVA diesel generator, silent type, perfect for weddings and commercial events. Fuel efficient, 8 hours backup.', 'price': 8000, 'cat': 'generators_tools', 'city': 'Karachi'},
{'title': 'Generator - Yamaha 5 KVA', 'desc': 'Yamaha 5 KVA petrol generator, portable, ideal for home backup and small events. Easy start, low noise.', 'price': 2500, 'cat': 'generators_tools', 'city': 'Karachi'},
{'title': 'Drill Machine - Bosch Professional', 'desc': 'Bosch impact drill 850W with bits set, perfect for wall drilling and home repairs. Includes carrying case.', 'price': 400, 'cat': 'generators_tools', 'city': 'Karachi'},
{'title': 'Welding Machine - 200 Amp', 'desc': '200 Amp arc welding machine with cables and holder, perfect for gate/window repair and fabrication work.', 'price': 600, 'cat': 'generators_tools', 'city': 'Karachi'},
{'title': 'Marble Cutter - Makita', 'desc': 'Makita marble cutter 4 inch, with diamond blade, perfect for tile and marble cutting. Professional grade.', 'price': 350, 'cat': 'generators_tools', 'city': 'Karachi'},
{'title': 'Scaffolding Set - Complete', 'desc': 'Complete scaffolding set, 10ft height, with wheels and platforms. Perfect for painting and construction work.', 'price': 1500, 'cat': 'generators_tools', 'city': 'Karachi'},

# ========== GENERATORS & TOOLS - Lahore ==========
{'title': 'Generator - Perkins 30 KVA', 'desc': 'Perkins 30 KVA diesel generator, soundproof canopy, ideal for large weddings and corporate events. 12 hours runtime.', 'price': 12000, 'cat': 'generators_tools', 'city': 'Lahore'},
{'title': 'Generator - Honda EU70is', 'desc': 'Honda EU70is 7 KVA inverter generator, ultra silent, perfect for residential backup and small functions.', 'price': 3500, 'cat': 'generators_tools', 'city': 'Lahore'},
{'title': 'Angle Grinder - Bosch 7 Inch', 'desc': 'Bosch 7 inch angle grinder 2200W, with cutting and grinding discs. Perfect for metal work.', 'price': 450, 'cat': 'generators_tools', 'city': 'Lahore'},
{'title': 'Air Compressor - 50L', 'desc': '50L air compressor with spray gun and hose, 2HP motor. Perfect for painting and tire inflation.', 'price': 700, 'cat': 'generators_tools', 'city': 'Lahore'},
{'title': 'Concrete Mixer - Small', 'desc': 'Small concrete mixer machine, electric, perfect for small construction and renovation work.', 'price': 1000, 'cat': 'generators_tools', 'city': 'Lahore'},
{'title': 'Pressure Washer - Karcher', 'desc': 'Karcher pressure washer K3, 1800 PSI, perfect for car washing and floor cleaning.', 'price': 500, 'cat': 'generators_tools', 'city': 'Lahore'},

# ========== GENERATORS & TOOLS - Islamabad ==========
{'title': 'Generator - Cummins 60 KVA', 'desc': 'Cummins 60 KVA diesel generator, soundproof, automatic transfer switch. Perfect for large events and commercial use.', 'price': 20000, 'cat': 'generators_tools', 'city': 'Islamabad'},
{'title': 'Generator - Honda EM6500', 'desc': 'Honda EM6500 6.5 KVA petrol generator, reliable and quiet. Perfect for home backup and outdoor events.', 'price': 3000, 'cat': 'generators_tools', 'city': 'Islamabad'},
{'title': 'Demolition Hammer - Hilti', 'desc': 'Hilti TE 1000 demolition hammer, 1700W, perfect for breaking concrete and tiles. Professional use.', 'price': 1200, 'cat': 'generators_tools', 'city': 'Islamabad'},
{'title': 'Tile Cutter - Manual 600mm', 'desc': 'Manual tile cutter 600mm with tungsten carbide wheel, perfect for precise tile cutting.', 'price': 250, 'cat': 'generators_tools', 'city': 'Islamabad'},
{'title': 'Generator - Small 2 KVA', 'desc': 'Small 2 KVA petrol generator, portable, perfect for camping and outdoor activities.', 'price': 1200, 'cat': 'generators_tools', 'city': 'Islamabad'},
{'title': 'Circular Saw - Dewalt', 'desc': 'Dewalt 7-1/4 inch circular saw, 1800W, with wood cutting blade. Perfect for carpentry work.', 'price': 400, 'cat': 'generators_tools', 'city': 'Islamabad'},

# ========== GENERATORS & TOOLS - Rawalpindi ==========
{'title': 'Generator - Honda 10 KVA', 'desc': 'Honda 10 KVA diesel generator, reliable performance, perfect for medium events and shops.', 'price': 5000, 'cat': 'generators_tools', 'city': 'Rawalpindi'},
{'title': 'Generator - Robin 3 KVA', 'desc': 'Robin 3 KVA petrol generator, portable and lightweight. Perfect for small shops and home backup.', 'price': 1800, 'cat': 'generators_tools', 'city': 'Rawalpindi'},
{'title': 'Rotary Hammer - Bosch', 'desc': 'Bosch rotary hammer drill 800W, SDS plus, perfect for concrete drilling. With 3 drill bits.', 'price': 350, 'cat': 'generators_tools', 'city': 'Rawalpindi'},
{'title': 'Chain Saw - Stihl', 'desc': 'Stihl MS 180 chain saw, 14 inch bar, perfect for tree cutting and wood work.', 'price': 600, 'cat': 'generators_tools', 'city': 'Rawalpindi'},
{'title': 'Ladder - Aluminum 12ft', 'desc': 'Aluminum ladder 12 feet, lightweight and sturdy, perfect for painting and electrical work.', 'price': 200, 'cat': 'generators_tools', 'city': 'Rawalpindi'},
{'title': 'Electric Planer - Makita', 'desc': 'Makita electric planer 82mm, 850W, perfect for wood smoothing and carpentry.', 'price': 300, 'cat': 'generators_tools', 'city': 'Rawalpindi'},

# ========== GENERATORS & TOOLS - Faisalabad ==========
{'title': 'Generator - Atlas Copco 15 KVA', 'desc': 'Atlas Copco 15 KVA diesel generator, silent type, perfect for textile industry backup and events.', 'price': 6500, 'cat': 'generators_tools', 'city': 'Faisalabad'},
{'title': 'Generator - Honda EU30is', 'desc': 'Honda EU30is 3 KVA inverter generator, super quiet, ideal for residential use and small functions.', 'price': 2200, 'cat': 'generators_tools', 'city': 'Faisalabad'},
{'title': 'Power Drill - Black & Decker', 'desc': 'Black & Decker power drill 550W, with 20 piece accessory kit. Perfect for home DIY projects.', 'price': 250, 'cat': 'generators_tools', 'city': 'Faisalabad'},
{'title': 'Jigsaw - Bosch GST 650', 'desc': 'Bosch jigsaw 650W, with wood and metal blades. Perfect for curved cutting and crafts.', 'price': 300, 'cat': 'generators_tools', 'city': 'Faisalabad'},
{'title': 'Water Pump - 1 HP', 'desc': '1 HP water pump motor, perfect for water tank filling and garden irrigation.', 'price': 350, 'cat': 'generators_tools', 'city': 'Faisalabad'},
{'title': 'Tool Kit - Complete Set', 'desc': 'Complete tool kit with spanners, screwdrivers, pliers, and hammer. 50 pieces, perfect for home use.', 'price': 400, 'cat': 'generators_tools', 'city': 'Faisalabad'},

# ========== GENERATORS & TOOLS - Multan ==========
{'title': 'Generator - FG Wilson 25 KVA', 'desc': 'FG Wilson 25 KVA diesel generator, Perkins engine, soundproof. Perfect for weddings and industrial use.', 'price': 9500, 'cat': 'generators_tools', 'city': 'Multan'},
{'title': 'Generator - Honda 2.5 KVA', 'desc': 'Honda 2.5 KVA petrol generator, portable, easy start. Perfect for small shops and home backup.', 'price': 1500, 'cat': 'generators_tools', 'city': 'Multan'},
{'title': 'Heat Gun - 2000W', 'desc': 'Heat gun 2000W with temperature control, perfect for paint removal and plastic welding.', 'price': 200, 'cat': 'generators_tools', 'city': 'Multan'},
{'title': 'Sander Machine - Orbital', 'desc': 'Orbital sander 300W, with 10 sanding sheets. Perfect for wood finishing and paint preparation.', 'price': 250, 'cat': 'generators_tools', 'city': 'Multan'},
{'title': 'Welding Machine - 300 Amp', 'desc': '300 Amp heavy duty welding machine, with full accessories. Perfect for industrial fabrication.', 'price': 800, 'cat': 'generators_tools', 'city': 'Multan'},
{'title': 'Electric Hoist - 1 Ton', 'desc': '1 Ton electric hoist with remote control, perfect for lifting heavy items and construction.', 'price': 1000, 'cat': 'generators_tools', 'city': 'Multan'},

# ========== GENERATORS & TOOLS - Peshawar ==========
{'title': 'Generator - Caterpillar 40 KVA', 'desc': 'Caterpillar 40 KVA diesel generator, industrial grade, soundproof. Perfect for large events and commercial use.', 'price': 15000, 'cat': 'generators_tools', 'city': 'Peshawar'},
{'title': 'Generator - Honda EG4000', 'desc': 'Honda EG4000 4 KVA petrol generator, reliable and fuel efficient. Perfect for home and small business.', 'price': 2000, 'cat': 'generators_tools', 'city': 'Peshawar'},
{'title': 'Jack Hammer - Electric', 'desc': 'Electric jack hammer 1700W, perfect for breaking concrete roads and foundations. Heavy duty.', 'price': 1100, 'cat': 'generators_tools', 'city': 'Peshawar'},
{'title': 'Spray Gun - Paint', 'desc': 'Electric paint spray gun 800W, with 3 nozzles. Perfect for wall and furniture painting.', 'price': 300, 'cat': 'generators_tools', 'city': 'Peshawar'},
{'title': 'Bench Grinder - 8 Inch', 'desc': '8 inch bench grinder 550W, with grinding and buffing wheels. Perfect for metal sharpening.', 'price': 350, 'cat': 'generators_tools', 'city': 'Peshawar'},
{'title': 'Cable Tester - Network', 'desc': 'Network cable tester with toner, perfect for LAN cable testing and tracing.', 'price': 150, 'cat': 'generators_tools', 'city': 'Peshawar'},

# ========== GENERATORS & TOOLS - Quetta ==========
{'title': 'Generator - Honda 15 KVA', 'desc': 'Honda 15 KVA diesel generator, reliable cold start, perfect for winter events and backup.', 'price': 7000, 'cat': 'generators_tools', 'city': 'Quetta'},
{'title': 'Generator - Robin 5 KVA', 'desc': 'Robin 5 KVA petrol generator, robust design, perfect for high altitude areas and home backup.', 'price': 2800, 'cat': 'generators_tools', 'city': 'Quetta'},
{'title': 'Hammer Drill - Stanley', 'desc': 'Stanley hammer drill 650W, with 13 drill bits. Perfect for concrete and masonry drilling.', 'price': 350, 'cat': 'generators_tools', 'city': 'Quetta'},
{'title': 'Soldering Iron - 60W', 'desc': '60W soldering iron with stand and solder wire. Perfect for electronics repair.', 'price': 100, 'cat': 'generators_tools', 'city': 'Quetta'},
{'title': 'Multimeter - Digital', 'desc': 'Digital multimeter with probes, perfect for electrical testing and troubleshooting.', 'price': 150, 'cat': 'generators_tools', 'city': 'Quetta'},
{'title': 'Tool Box - Empty', 'desc': 'Empty metal tool box with compartments, perfect for storing and carrying tools.', 'price': 100, 'cat': 'generators_tools', 'city': 'Quetta'},

# ========== GENERATORS & TOOLS - Gujranwala ==========
{'title': 'Generator - Honda 12 KVA', 'desc': 'Honda 12 KVA diesel generator, silent canopy, perfect for wedding halls and events.', 'price': 6000, 'cat': 'generators_tools', 'city': 'Gujranwala'},
{'title': 'Generator - Yamaha 6 KVA', 'desc': 'Yamaha 6 KVA petrol generator, lightweight and powerful. Perfect for home and small industry.', 'price': 2600, 'cat': 'generators_tools', 'city': 'Gujranwala'},
{'title': 'Pipe Wrench - Heavy Duty', 'desc': 'Heavy duty pipe wrench 18 inch, perfect for plumbing and pipe fitting work.', 'price': 150, 'cat': 'generators_tools', 'city': 'Gujranwala'},
{'title': 'Cordless Drill - 18V', 'desc': 'Cordless drill 18V with 2 batteries and charger, 13mm chuck. Perfect for mobile work.', 'price': 400, 'cat': 'generators_tools', 'city': 'Gujranwala'},
{'title': 'Electric Blower - 600W', 'desc': 'Electric blower 600W, perfect for dust cleaning and workshop use.', 'price': 200, 'cat': 'generators_tools', 'city': 'Gujranwala'},
{'title': 'Vice - 4 Inch Bench', 'desc': '4 inch bench vice, cast iron, perfect for holding work pieces during filing and cutting.', 'price': 180, 'cat': 'generators_tools', 'city': 'Gujranwala'},

# ========== GENERATORS & TOOLS - Sialkot ==========
{'title': 'Generator - Perkins 20 KVA', 'desc': 'Perkins 20 KVA diesel generator, UK engine, reliable performance. Perfect for surgical industry and events.', 'price': 8500, 'cat': 'generators_tools', 'city': 'Sialkot'},
{'title': 'Generator - Honda 3 KVA', 'desc': 'Honda 3 KVA petrol generator, portable and quiet. Perfect for sports goods industry backup.', 'price': 1900, 'cat': 'generators_tools', 'city': 'Sialkot'},
{'title': 'Polisher Machine - 7 Inch', 'desc': '7 inch car polisher 1400W, with foam pads. Perfect for vehicle detailing and polishing.', 'price': 450, 'cat': 'generators_tools', 'city': 'Sialkot'},
{'title': 'Hydraulic Jack - 3 Ton', 'desc': '3 Ton hydraulic bottle jack, perfect for vehicle lifting and workshop use.', 'price': 250, 'cat': 'generators_tools', 'city': 'Sialkot'},
{'title': 'Rivet Gun - Manual', 'desc': 'Manual rivet gun with assorted rivets, perfect for sheet metal work.', 'price': 150, 'cat': 'generators_tools', 'city': 'Sialkot'},
{'title': 'Soldering Gun - 100W', 'desc': '100W soldering gun, instant heat, perfect for heavy soldering and electronics.', 'price': 180, 'cat': 'generators_tools', 'city': 'Sialkot'},

# ========== GENERATORS & TOOLS - Bahawalpur ==========
{'title': 'Generator - Cummins 35 KVA', 'desc': 'Cummins 35 KVA diesel generator, soundproof, automatic. Perfect for large weddings and industrial use.', 'price': 13000, 'cat': 'generators_tools', 'city': 'Bahawalpur'},
{'title': 'Generator - Honda 8 KVA', 'desc': 'Honda 8 KVA diesel generator, fuel efficient, perfect for home backup and medium events.', 'price': 4200, 'cat': 'generators_tools', 'city': 'Bahawalpur'},
{'title': 'Screwdriver Set - 20 Piece', 'desc': '20 piece screwdriver set, includes flat and Phillips heads. Perfect for electronics and general use.', 'price': 150, 'cat': 'generators_tools', 'city': 'Bahawalpur'},
{'title': 'Allen Key Set - Metric', 'desc': 'Metric Allen key set 1.5mm to 10mm, perfect for furniture assembly and bike repair.', 'price': 100, 'cat': 'generators_tools', 'city': 'Bahawalpur'},
{'title': 'Pliers Set - 3 Piece', 'desc': '3 piece pliers set: combination, long nose, and cutting pliers. Perfect for electrical work.', 'price': 200, 'cat': 'generators_tools', 'city': 'Bahawalpur'},
{'title': 'Measuring Tape - 5m', 'desc': '5 meter measuring tape with lock, perfect for construction and tailoring measurements.', 'price': 50, 'cat': 'generators_tools', 'city': 'Bahawalpur'},

# ========== GENERATORS & TOOLS - Hyderabad ==========
{'title': 'Generator - Honda 10 KVA', 'desc': 'Honda 10 KVA diesel generator, silent type, perfect for weddings and commercial backup.', 'price': 5500, 'cat': 'generators_tools', 'city': 'Hyderabad'},
{'title': 'Generator - Yamaha 2.8 KVA', 'desc': 'Yamaha 2.8 KVA petrol generator, portable, ideal for home use and small shops.', 'price': 1600, 'cat': 'generators_tools', 'city': 'Hyderabad'},
{'title': 'Cutter Machine - Steel', 'desc': 'Steel cutter machine 14 inch, 2200W, perfect for cutting steel bars and pipes.', 'price': 500, 'cat': 'generators_tools', 'city': 'Hyderabad'},
{'title': 'Spanner Set - 12 Piece', 'desc': '12 piece combination spanner set 6mm to 22mm, perfect for mechanical work.', 'price': 250, 'cat': 'generators_tools', 'city': 'Hyderabad'},
{'title': 'Water Pump - 2 HP', 'desc': '2 HP water pump motor, high pressure, perfect for large tanks and garden irrigation.', 'price': 500, 'cat': 'generators_tools', 'city': 'Hyderabad'},
{'title': 'Socket Set - 24 Piece', 'desc': '24 piece socket set with ratchet handle, 1/4 inch drive. Perfect for automotive work.', 'price': 350, 'cat': 'generators_tools', 'city': 'Hyderabad'},

# ========== GENERATORS & TOOLS - Sukkur ==========
{'title': 'Generator - Perkins 15 KVA', 'desc': 'Perkins 15 KVA diesel generator, reliable engine, perfect for events and commercial use.', 'price': 7000, 'cat': 'generators_tools', 'city': 'Sukkur'},
{'title': 'Generator - Honda EP2500', 'desc': 'Honda EP2500 2.5 KVA petrol generator, compact and lightweight. Perfect for small backup.', 'price': 1400, 'cat': 'generators_tools', 'city': 'Sukkur'},
{'title': 'Glue Gun - 40W', 'desc': '40W hot glue gun with 5 glue sticks, perfect for crafts and small repairs.', 'price': 100, 'cat': 'generators_tools', 'city': 'Sukkur'},
{'title': 'Staple Gun - Manual', 'desc': 'Manual staple gun with 1000 staples, perfect for upholstery and wood work.', 'price': 150, 'cat': 'generators_tools', 'city': 'Sukkur'},
{'title': 'Hacksaw - Adjustable', 'desc': 'Adjustable hacksaw frame with 5 blades, perfect for metal and PVC cutting.', 'price': 100, 'cat': 'generators_tools', 'city': 'Sukkur'},
{'title': 'Spirit Level - 24 Inch', 'desc': '24 inch aluminum spirit level with 3 vials, perfect for construction and alignment.', 'price': 120, 'cat': 'generators_tools', 'city': 'Sukkur'},

# ========== GENERATORS & TOOLS - Larkana ==========
{'title': 'Generator - Honda 7 KVA', 'desc': 'Honda 7 KVA diesel generator, compact design, perfect for home and small business.', 'price': 4000, 'cat': 'generators_tools', 'city': 'Larkana'},
{'title': 'Generator - Small 1.5 KVA', 'desc': 'Small 1.5 KVA petrol generator, ultra portable, perfect for camping and outdoor use.', 'price': 1000, 'cat': 'generators_tools', 'city': 'Larkana'},
{'title': 'Electric Tester - Digital', 'desc': 'Digital voltage tester with LCD display, perfect for electrical troubleshooting.', 'price': 80, 'cat': 'generators_tools', 'city': 'Larkana'},
{'title': 'Wire Stripper - Automatic', 'desc': 'Automatic wire stripper and cutter, perfect for electrical wiring work.', 'price': 120, 'cat': 'generators_tools', 'city': 'Larkana'},
{'title': 'Hammer - 2lb', 'desc': '2 lb hammer with wooden handle, perfect for general construction and demolition.', 'price': 100, 'cat': 'generators_tools', 'city': 'Larkana'},
{'title': 'Chisel Set - 3 Piece', 'desc': '3 piece wood chisel set 6mm, 12mm, 18mm. Perfect for carpentry work.', 'price': 120, 'cat': 'generators_tools', 'city': 'Larkana'},

# ========== GENERATORS & TOOLS - Mirpur Khas ==========
{'title': 'Generator - Honda 5 KVA', 'desc': 'Honda 5 KVA diesel generator, quiet operation, perfect for home backup and small shops.', 'price': 3500, 'cat': 'generators_tools', 'city': 'Mirpur Khas'},
{'title': 'Generator - Chinese 2 KVA', 'desc': 'Chinese 2 KVA petrol generator, budget friendly, perfect for basic home backup.', 'price': 1100, 'cat': 'generators_tools', 'city': 'Mirpur Khas'},
{'title': 'Hand Drill - Manual', 'desc': 'Manual hand drill with chuck, perfect for small drilling jobs without electricity.', 'price': 80, 'cat': 'generators_tools', 'city': 'Mirpur Khas'},
{'title': 'C-Clamp - 4 Inch', 'desc': '4 inch C-clamp, cast iron, perfect for holding work pieces during gluing and welding.', 'price': 100, 'cat': 'generators_tools', 'city': 'Mirpur Khas'},
{'title': 'File Set - 5 Piece', 'desc': '5 piece file set: flat, round, half-round, square, triangular. Perfect for metal work.', 'price': 150, 'cat': 'generators_tools', 'city': 'Mirpur Khas'},
{'title': 'Oil Can - 500ml', 'desc': '500ml oil can with flexible spout, perfect for lubricating machines and tools.', 'price': 60, 'cat': 'generators_tools', 'city': 'Mirpur Khas'},

# ========== GENERATORS & TOOLS - Nawabshah ==========
{'title': 'Generator - Honda 6 KVA', 'desc': 'Honda 6 KVA diesel generator, reliable and efficient, perfect for home and small business.', 'price': 3800, 'cat': 'generators_tools', 'city': 'Nawabshah'},
{'title': 'Generator - Yamaha 4 KVA', 'desc': 'Yamaha 4 KVA petrol generator, portable design, perfect for medium home backup.', 'price': 2100, 'cat': 'generators_tools', 'city': 'Nawabshah'},
{'title': 'Adjustable Wrench - 10 Inch', 'desc': '10 inch adjustable wrench, chrome vanadium steel, perfect for plumbing and mechanical work.', 'price': 120, 'cat': 'generators_tools', 'city': 'Nawabshah'},
{'title': 'Claw Hammer - 1lb', 'desc': '1 lb claw hammer with rubber grip, perfect for nail driving and removal.', 'price': 80, 'cat': 'generators_tools', 'city': 'Nawabshah'},
{'title': 'Utility Knife - Heavy Duty', 'desc': 'Heavy duty utility knife with 5 spare blades, perfect for cutting and scoring.', 'price': 70, 'cat': 'generators_tools', 'city': 'Nawabshah'},
{'title': 'Hex Key Set - Imperial', 'desc': 'Imperial hex key set 1/16 to 3/8 inch, perfect for imported machinery maintenance.', 'price': 100, 'cat': 'generators_tools', 'city': 'Nawabshah'},

# ========== GENERATORS & TOOLS - Rahim Yar Khan ==========
{'title': 'Generator - Cummins 50 KVA', 'desc': 'Cummins 50 KVA diesel generator, industrial grade, perfect for large events and factories.', 'price': 18000, 'cat': 'generators_tools', 'city': 'Rahim Yar Khan'},
{'title': 'Generator - Honda 9 KVA', 'desc': 'Honda 9 KVA diesel generator, super silent, perfect for residential and commercial use.', 'price': 4800, 'cat': 'generators_tools', 'city': 'Rahim Yar Khan'},
{'title': 'Air Impact Wrench - 1/2 Inch', 'desc': '1/2 inch air impact wrench, 600 ft-lbs torque, perfect for automotive repair.', 'price': 400, 'cat': 'generators_tools', 'city': 'Rahim Yar Khan'},
{'title': 'Engine Crane - 2 Ton', 'desc': '2 Ton hydraulic engine crane with wheels, perfect for engine removal and heavy lifting.', 'price': 800, 'cat': 'generators_tools', 'city': 'Rahim Yar Khan'},
{'title': 'Car Jack - Trolley 3 Ton', 'desc': '3 Ton trolley jack with wheels, perfect for garage and workshop vehicle lifting.', 'price': 400, 'cat': 'generators_tools', 'city': 'Rahim Yar Khan'},
{'title': 'Axle Stand - 3 Ton Pair', 'desc': 'Pair of 3 Ton axle stands, ratchet type, perfect for vehicle support during repairs.', 'price': 200, 'cat': 'generators_tools', 'city': 'Rahim Yar Khan'},

# ========== GENERATORS & TOOLS - Sargodha ==========
{'title': 'Generator - Honda 11 KVA', 'desc': 'Honda 11 KVA diesel generator, reliable power, perfect for events and commercial backup.', 'price': 5800, 'cat': 'generators_tools', 'city': 'Sargodha'},
{'title': 'Generator - Robin 2 KVA', 'desc': 'Robin 2 KVA petrol generator, compact and efficient, perfect for small shops.', 'price': 1300, 'cat': 'generators_tools', 'city': 'Sargodha'},
{'title': 'Caulking Gun - Manual', 'desc': 'Manual caulking gun for silicone and sealant tubes, perfect for waterproofing and sealing.', 'price': 80, 'cat': 'generators_tools', 'city': 'Sargodha'},
{'title': 'Putty Knife - Set of 3', 'desc': 'Set of 3 putty knives 2, 3, 4 inch, perfect for wall putty and paint scraping.', 'price': 90, 'cat': 'generators_tools', 'city': 'Sargodha'},
{'title': 'Pipe Cutter - 15-50mm', 'desc': 'Pipe cutter for 15-50mm pipes, perfect for PVC and CPVC pipe cutting.', 'price': 150, 'cat': 'generators_tools', 'city': 'Sargodha'},
{'title': 'Torch Light - LED Rechargeable', 'desc': 'LED rechargeable torch light, 2000 lumens, perfect for night work and emergencies.', 'price': 120, 'cat': 'generators_tools', 'city': 'Sargodha'},

# ========== GENERATORS & TOOLS - Jhang ==========
{'title': 'Generator - Honda 4 KVA', 'desc': 'Honda 4 KVA diesel generator, compact and quiet, perfect for home backup.', 'price': 3200, 'cat': 'generators_tools', 'city': 'Jhang'},
{'title': 'Generator - Chinese 3 KVA', 'desc': 'Chinese 3 KVA petrol generator, affordable option for basic power backup.', 'price': 1500, 'cat': 'generators_tools', 'city': 'Jhang'},
{'title': 'Trowel Set - Masonry', 'desc': 'Set of 3 masonry trowels, perfect for brick laying and plaster work.', 'price': 150, 'cat': 'generators_tools', 'city': 'Jhang'},
{'title': 'Plumb Bob - 400g', 'desc': '400g brass plumb bob with string, perfect for vertical alignment in construction.', 'price': 100, 'cat': 'generators_tools', 'city': 'Jhang'},
{'title': 'Crowbar - 5ft', 'desc': '5 foot crowbar, heavy duty, perfect for demolition and heavy lifting.', 'price': 250, 'cat': 'generators_tools', 'city': 'Jhang'},
{'title': 'Wire Brush - Set of 3', 'desc': 'Set of 3 wire brushes: steel, brass, and nylon. Perfect for rust removal and cleaning.', 'price': 80, 'cat': 'generators_tools', 'city': 'Jhang'},

# ========== GENERATORS & TOOLS - Sahiwal ==========
{'title': 'Generator - Honda 3.5 KVA', 'desc': 'Honda 3.5 KVA diesel generator, fuel efficient, perfect for small home backup.', 'price': 3000, 'cat': 'generators_tools', 'city': 'Sahiwal'},
{'title': 'Generator - Yamaha 1.5 KVA', 'desc': 'Yamaha 1.5 KVA petrol generator, ultra portable, perfect for camping and outdoor events.', 'price': 1100, 'cat': 'generators_tools', 'city': 'Sahiwal'},
{'title': 'Sledge Hammer - 8lb', 'desc': '8 lb sledge hammer with fiberglass handle, perfect for heavy demolition work.', 'price': 200, 'cat': 'generators_tools', 'city': 'Sahiwal'},
{'title': 'Pick Axe - Heavy Duty', 'desc': 'Heavy duty pick axe with wooden handle, perfect for digging and breaking hard soil.', 'price': 180, 'cat': 'generators_tools', 'city': 'Sahiwal'},
{'title': 'Shovel - Round Point', 'desc': 'Round point shovel with D-handle, perfect for digging and moving soil.', 'price': 120, 'cat': 'generators_tools', 'city': 'Sahiwal'},
{'title': 'Wheelbarrow - Heavy Duty', 'desc': 'Heavy duty wheelbarrow with pneumatic tire, perfect for construction material transport.', 'price': 350, 'cat': 'generators_tools', 'city': 'Sahiwal'},
    {
        'title': 'Generator - 10kVA',
        'desc': 'Heavy duty for big events. Diesel generator.',
        'price': 6000,
        'cat': 'other',
        'city': 'Lahore'
    },
    {
        'title': 'Drilling Machine',
        'desc': 'Hammer drill for construction/repair.',
        'price': 500,
        'cat': 'other',
        'city': 'Islamabad'
    },
    {
        'title': 'Pressure Washer',
        'desc': 'For car/building cleaning. Powerful.',
        'price': 800,
        'cat': 'other',
        'city': 'Karachi'
    },
    {
        'title': 'Cement Mixer',
        'desc': 'For construction work.',
        'price': 1500,
        'cat': 'other',
        'city': 'Lahore'
    },
    {
        'title': 'Ladder - 12 feet',
        'desc': 'Aluminum ladder for home repair.',
        'price': 300,
        'cat': 'other',
        'city': 'Rawalpindi'
    },
    
    # ========== ELECTRONICS FOR RENT ==========
    {
        'title': 'PS5 Gaming Console',
        'desc': 'For gaming events/birthday parties. 2 controllers + 5 games.',
        'price': 1500,
        'cat': 'electronics',
        'city': 'Karachi'
    },
    # ========== ELECTRONICS FOR RENT - Karachi ==========
{'title': 'DSLR Camera - Canon 200D', 'desc': 'Canon 200D with 18-55mm lens, 24MP, perfect for photography beginners and events. Includes bag, charger, 32GB SD card.', 'price': 1500, 'cat': 'electronics', 'city': 'Karachi'},
{'title': 'PlayStation 5 - Disc Edition', 'desc': 'PS5 console with 1 controller, 825GB SSD. Includes 5 games pre-installed. Security deposit: Rs. 50,000.', 'price': 2500, 'cat': 'electronics', 'city': 'Karachi'},
{'title': 'Projector - 1080p HD', 'desc': 'LED projector with 1080p support, 3000 lumens. Perfect for movie nights and cricket matches. HDMI/USB input.', 'price': 1000, 'cat': 'electronics', 'city': 'Karachi'},
{'title': 'Gaming Laptop - ASUS TUF A15', 'desc': 'Ryzen 7, RTX 3050, 16GB RAM, 512GB SSD. Perfect for gaming and video editing. Deposit required.', 'price': 3000, 'cat': 'electronics', 'city': 'Karachi'},
{'title': 'Sound System - 1000W', 'desc': 'Complete PA system with 2 speakers, mixer, and wireless mics. Perfect for small events and parties.', 'price': 2500, 'cat': 'electronics', 'city': 'Karachi'},
{'title': 'iPad 9th Generation', 'desc': 'iPad 9th Gen 64GB WiFi, with Apple Pencil support. Great for students and digital artists.', 'price': 1200, 'cat': 'electronics', 'city': 'Karachi'},

# ========== ELECTRONICS FOR RENT - Lahore ==========
{'title': 'GoPro Hero 11 Black', 'desc': 'Action camera with waterproof housing, 5.3K video, stabilization. Perfect for travel vlogs and adventure sports.', 'price': 1500, 'cat': 'electronics', 'city': 'Lahore'},
{'title': 'Xbox Series X - 1TB', 'desc': 'Xbox Series X with 1 controller, 1TB SSD, 4K gaming. Includes Game Pass Ultimate 3 months.', 'price': 2800, 'cat': 'electronics', 'city': 'Lahore'},
{'title': 'MacBook Air M1', 'desc': 'Apple M1 chip, 8GB RAM, 256GB SSD. Perfect for professionals and students. Security deposit required.', 'price': 3500, 'cat': 'electronics', 'city': 'Lahore'},
{'title': '4K Smart TV - 55 Inch', 'desc': 'Samsung 55" Crystal UHD 4K Smart TV. Includes wall mount. Great for events and cricket matches.', 'price': 2000, 'cat': 'electronics', 'city': 'Lahore'},
{'title': 'DJI Drone Mini 3 Pro', 'desc': '4K camera drone with obstacle avoidance, 34 min flight time. Perfect for aerial photography at events.', 'price': 2500, 'cat': 'electronics', 'city': 'Lahore'},
{'title': 'Wireless Microphone Set', 'desc': 'Dual wireless mic system with receiver, 50m range. Perfect for presentations and karaoke nights.', 'price': 500, 'cat': 'electronics', 'city': 'Lahore'},

# ========== ELECTRONICS FOR RENT - Islamabad ==========
{'title': 'Nikon D7500 DSLR', 'desc': 'Nikon D7500 with 18-140mm lens, 4K video, perfect for professional photography. Includes bag and 64GB card.', 'price': 2500, 'cat': 'electronics', 'city': 'Islamabad'},
{'title': 'Nintendo Switch OLED', 'desc': 'Nintendo Switch with 2 Joy-Cons, includes 5 popular games. Perfect for family entertainment and parties.', 'price': 1800, 'cat': 'electronics', 'city': 'Islamabad'},
{'title': 'Dell XPS 15 Laptop', 'desc': 'Intel i7, 16GB RAM, 512GB SSD, 4K touch display. Perfect for creative professionals. Deposit required.', 'price': 4000, 'cat': 'electronics', 'city': 'Islamabad'},
{'title': 'Studio Light Kit - 3 Point', 'desc': 'Professional 3-point lighting kit with softboxes and stands. Perfect for indoor photography and videography.', 'price': 1000, 'cat': 'electronics', 'city': 'Islamabad'},
{'title': 'DJ Controller - Pioneer DDJ-400', 'desc': 'Entry-level DJ controller compatible with rekordbox. Perfect for learning and small parties.', 'price': 1200, 'cat': 'electronics', 'city': 'Islamabad'},
{'title': 'Ring Light with Tripod', 'desc': '12-inch LED ring light with adjustable tripod stand, 3 color modes. For vlogging and makeup tutorials.', 'price': 300, 'cat': 'electronics', 'city': 'Islamabad'},

# ========== ELECTRONICS FOR RENT - Rawalpindi ==========
{'title': 'Sony Alpha A6400', 'desc': 'Sony A6400 mirrorless camera with 16-50mm lens, 4K video. Perfect for vlogging and events.', 'price': 2000, 'cat': 'electronics', 'city': 'Rawalpindi'},
{'title': 'PlayStation 4 Pro - 1TB', 'desc': 'PS4 Pro with 2 controllers, 1TB storage. Includes 10 popular games. Perfect for gaming nights.', 'price': 1500, 'cat': 'electronics', 'city': 'Rawalpindi'},
{'title': 'HP Pavilion Gaming Laptop', 'desc': 'Intel i5, GTX 1650, 8GB RAM, 512GB SSD. Perfect for casual gaming and work.', 'price': 2200, 'cat': 'electronics', 'city': 'Rawalpindi'},
{'title': 'Green Screen Backdrop', 'desc': 'Professional 6x9ft green screen with stand. Perfect for video production and photography.', 'price': 500, 'cat': 'electronics', 'city': 'Rawalpindi'},
{'title': 'Karaoke Machine', 'desc': 'Portable karaoke machine with 2 wireless mics, Bluetooth, LED lights. Perfect for parties.', 'price': 800, 'cat': 'electronics', 'city': 'Rawalpindi'},
{'title': 'Gaming Monitor - 144Hz', 'desc': '24 inch gaming monitor, 144Hz refresh rate, 1ms response. Perfect for competitive gaming.', 'price': 600, 'cat': 'electronics', 'city': 'Rawalpindi'},

# ========== ELECTRONICS FOR RENT - Faisalabad ==========
{'title': 'Canon EOS 1500D', 'desc': 'Canon 1500D with 18-55mm lens, perfect for beginners. Includes bag, charger, and 32GB card.', 'price': 1200, 'cat': 'electronics', 'city': 'Faisalabad'},
{'title': 'Xbox One X - 1TB', 'desc': 'Xbox One X with 2 controllers, 4K gaming. Includes 8 games pre-installed.', 'price': 1800, 'cat': 'electronics', 'city': 'Faisalabad'},
{'title': 'Lenovo ThinkPad Laptop', 'desc': 'Intel i5, 8GB RAM, 256GB SSD, perfect for office work and students. Reliable performance.', 'price': 1500, 'cat': 'electronics', 'city': 'Faisalabad'},
{'title': 'LED TV - 43 Inch', 'desc': 'TCL 43" Android Smart TV, 4K HDR. Perfect for temporary accommodation and events.', 'price': 1000, 'cat': 'electronics', 'city': 'Faisalabad'},
{'title': 'Bluetooth Speaker - JBL', 'desc': 'JBL PartyBox 310, 240W output, light show, portable. Perfect for parties and outdoor events.', 'price': 1200, 'cat': 'electronics', 'city': 'Faisalabad'},
{'title': 'Webcam - Logitech C920', 'desc': 'Logitech C920 HD Pro webcam, 1080p, perfect for video calls and streaming.', 'price': 200, 'cat': 'electronics', 'city': 'Faisalabad'},

# ========== ELECTRONICS FOR RENT - Multan ==========
{'title': 'Sony Handycam - 4K', 'desc': 'Sony 4K Handycam with 30x optical zoom, perfect for wedding videography. Includes 64GB card and bag.', 'price': 1800, 'cat': 'electronics', 'city': 'Multan'},
{'title': 'PlayStation VR Bundle', 'desc': 'PSVR headset with camera and 2 Move controllers. Includes 5 VR games. Immersive experience.', 'price': 2000, 'cat': 'electronics', 'city': 'Multan'},
{'title': 'Acer Predator Gaming Laptop', 'desc': 'Intel i7, RTX 3060, 16GB RAM, 1TB SSD. Ultimate gaming performance. Deposit required.', 'price': 3500, 'cat': 'electronics', 'city': 'Multan'},
{'title': 'Projector Screen - 100 Inch', 'desc': '100 inch portable projector screen with tripod stand. Perfect for movie nights and presentations.', 'price': 400, 'cat': 'electronics', 'city': 'Multan'},
{'title': 'Gaming Chair - Ergonomic', 'desc': 'Racing style gaming chair with lumbar support, adjustable height. Perfect for long gaming sessions.', 'price': 800, 'cat': 'electronics', 'city': 'Multan'},
{'title': 'Streaming Kit - Beginner', 'desc': 'Complete streaming kit: microphone, arm stand, pop filter, and webcam. Perfect for aspiring streamers.', 'price': 600, 'cat': 'electronics', 'city': 'Multan'},

# ========== ELECTRONICS FOR RENT - Peshawar ==========
{'title': 'Nikon D5600 DSLR', 'desc': 'Nikon D5600 with 18-55mm and 70-300mm lenses. Complete photography kit with bag and accessories.', 'price': 2000, 'cat': 'electronics', 'city': 'Peshawar'},
{'title': 'PlayStation 5 - Digital Edition', 'desc': 'PS5 Digital Edition with 2 controllers, 825GB SSD. Includes PlayStation Plus subscription.', 'price': 2200, 'cat': 'electronics', 'city': 'Peshawar'},
{'title': 'MSI Gaming Laptop', 'desc': 'Intel i7, RTX 3070, 32GB RAM, 1TB SSD. High-end gaming and rendering. Security deposit required.', 'price': 4500, 'cat': 'electronics', 'city': 'Peshawar'},
{'title': 'Smart TV - 50 Inch', 'desc': 'Sony 50" Bravia Android TV, 4K HDR. Perfect for events and temporary accommodation.', 'price': 1800, 'cat': 'electronics', 'city': 'Peshawar'},
{'title': 'Professional Camera Tripod', 'desc': 'Manfrotto professional tripod with fluid head, perfect for video and photography.', 'price': 500, 'cat': 'electronics', 'city': 'Peshawar'},
{'title': 'Gaming Headset - Razer', 'desc': 'Razer Kraken gaming headset with surround sound, perfect for competitive gaming.', 'price': 300, 'cat': 'electronics', 'city': 'Peshawar'},

# ========== ELECTRONICS FOR RENT - Quetta ==========
{'title': 'Canon EOS 1300D', 'desc': 'Canon 1300D with 18-55mm lens, perfect for beginners and events. Includes accessories.', 'price': 1000, 'cat': 'electronics', 'city': 'Quetta'},
{'title': 'Xbox Series S', 'desc': 'Xbox Series S 512GB with 1 controller. Includes Game Pass Ultimate 3 months. Compact and powerful.', 'price': 1600, 'cat': 'electronics', 'city': 'Quetta'},
{'title': 'HP EliteBook Laptop', 'desc': 'Intel i5, 8GB RAM, 256GB SSD, business grade laptop. Perfect for professional work.', 'price': 1400, 'cat': 'electronics', 'city': 'Quetta'},
{'title': 'Portable Generator - Battery', 'desc': 'Jackery portable power station 500W, perfect for camping and outdoor electronics.', 'price': 800, 'cat': 'electronics', 'city': 'Quetta'},
{'title': 'Camera Lens - 50mm Prime', 'desc': 'Canon 50mm f/1.8 STM lens, perfect for portraits and low light photography.', 'price': 300, 'cat': 'electronics', 'city': 'Quetta'},
{'title': 'Drone - DJI Mini SE', 'desc': 'DJI Mini SE drone, 2.7K camera, 30 min flight. Perfect for beginners and aerial photos.', 'price': 1200, 'cat': 'electronics', 'city': 'Quetta'},

# ========== ELECTRONICS FOR RENT - Gujranwala ==========
{'title': 'Sony ZV-1 Camera', 'desc': 'Sony ZV-1 vlogging camera with flip screen, 4K video. Perfect for content creators.', 'price': 1800, 'cat': 'electronics', 'city': 'Gujranwala'},
{'title': 'Nintendo Switch Lite', 'desc': 'Nintendo Switch Lite, handheld only, includes 5 games. Perfect for portable gaming.', 'price': 1000, 'cat': 'electronics', 'city': 'Gujranwala'},
{'title': 'Dell Inspiron Laptop', 'desc': 'Intel i3, 4GB RAM, 1TB HDD, perfect for basic work and students. Affordable option.', 'price': 800, 'cat': 'electronics', 'city': 'Gujranwala'},
{'title': 'Soundbar - Samsung', 'desc': 'Samsung 2.1 channel soundbar with wireless subwoofer. Perfect for TV and movie experience.', 'price': 600, 'cat': 'electronics', 'city': 'Gujranwala'},
{'title': 'Gaming Keyboard - Mechanical', 'desc': 'Redragon mechanical gaming keyboard, RGB backlit. Perfect for gaming and typing.', 'price': 250, 'cat': 'electronics', 'city': 'Gujranwala'},
{'title': 'USB Microphone - Blue Yeti', 'desc': 'Blue Yeti USB microphone, perfect for podcasting, streaming, and voice recording.', 'price': 400, 'cat': 'electronics', 'city': 'Gujranwala'},

# ========== ELECTRONICS FOR RENT - Sialkot ==========
{'title': 'Fujifilm Instax Camera', 'desc': 'Instax Mini 11 instant camera with 20 film sheets. Perfect for events and parties.', 'price': 500, 'cat': 'electronics', 'city': 'Sialkot'},
{'title': 'Gaming PC - Full Setup', 'desc': 'Complete gaming PC: Ryzen 5, RTX 3060, 16GB RAM, monitor, keyboard, mouse. Ready to play.', 'price': 3500, 'cat': 'electronics', 'city': 'Sialkot'},
{'title': 'MacBook Pro 2019', 'desc': 'Intel i5, 8GB RAM, 256GB SSD, Touch Bar. Perfect for creative work. Deposit required.', 'price': 3000, 'cat': 'electronics', 'city': 'Sialkot'},
{'title': 'Home Theater System', 'desc': 'Sony 5.1 channel home theater system, 1000W. Perfect for movie nights and events.', 'price': 1500, 'cat': 'electronics', 'city': 'Sialkot'},
{'title': 'Gaming Mouse - Logitech', 'desc': 'Logitech G502 gaming mouse, adjustable weights, programmable buttons.', 'price': 200, 'cat': 'electronics', 'city': 'Sialkot'},
{'title': 'Capture Card - Elgato', 'desc': 'Elgato HD60 S capture card, perfect for streaming console gameplay.', 'price': 500, 'cat': 'electronics', 'city': 'Sialkot'},

# ========== ELECTRONICS FOR RENT - Bahawalpur ==========
{'title': 'Canon PowerShot SX540', 'desc': 'Canon PowerShot with 50x optical zoom, perfect for wildlife and sports photography.', 'price': 900, 'cat': 'electronics', 'city': 'Bahawalpur'},
{'title': 'PS4 Slim - 500GB', 'desc': 'PS4 Slim with 2 controllers, includes 15 popular games. Perfect for family entertainment.', 'price': 1200, 'cat': 'electronics', 'city': 'Bahawalpur'},
{'title': 'Chromebook - Acer', 'desc': 'Acer Chromebook, 4GB RAM, 32GB storage, perfect for students and basic browsing.', 'price': 500, 'cat': 'electronics', 'city': 'Bahawalpur'},
{'title': 'Projector - Mini Portable', 'desc': 'Mini portable projector with Android OS, 720p. Perfect for small gatherings and bedroom use.', 'price': 600, 'cat': 'electronics', 'city': 'Bahawalpur'},
{'title': 'Bluetooth Speaker - Anker', 'desc': 'Anker Soundcore Bluetooth speaker, 24hr battery, waterproof. Perfect for outdoor use.', 'price': 300, 'cat': 'electronics', 'city': 'Bahawalpur'},
{'title': 'Action Camera - Akaso', 'desc': 'Akaso Brave 7 action camera, 4K, waterproof. Budget alternative to GoPro.', 'price': 400, 'cat': 'electronics', 'city': 'Bahawalpur'},

# ========== ELECTRONICS FOR RENT - Hyderabad ==========
{'title': 'Sony Cybershot Camera', 'desc': 'Sony Cybershot point and shoot, 20MP, perfect for casual photography and events.', 'price': 600, 'cat': 'electronics', 'city': 'Hyderabad'},
{'title': 'Xbox 360 - Kinect Bundle', 'desc': 'Xbox 360 with Kinect sensor, 2 controllers, 20+ games. Perfect for family fun.', 'price': 800, 'cat': 'electronics', 'city': 'Hyderabad'},
{'title': 'Tablet - Samsung Galaxy Tab', 'desc': 'Samsung Galaxy Tab A7, 10.4" display, 32GB. Perfect for entertainment and light work.', 'price': 700, 'cat': 'electronics', 'city': 'Hyderabad'},
{'title': 'Portable DVD Player', 'desc': 'Portable DVD player with 10" screen, perfect for kids and travel entertainment.', 'price': 300, 'cat': 'electronics', 'city': 'Hyderabad'},
{'title': 'Camera Stabilizer - Gimbal', 'desc': 'Zhiyun Smooth 4 gimbal for smartphones, perfect for smooth video recording.', 'price': 400, 'cat': 'electronics', 'city': 'Hyderabad'},
{'title': 'Echo Dot - Alexa', 'desc': 'Amazon Echo Dot 4th Gen with Alexa, perfect for smart home and music.', 'price': 150, 'cat': 'electronics', 'city': 'Hyderabad'},

# ========== ELECTRONICS FOR RENT - Sukkur ==========
{'title': 'Nikon Coolpix B500', 'desc': 'Nikon Coolpix with 40x zoom, perfect for travel and event photography.', 'price': 800, 'cat': 'electronics', 'city': 'Sukkur'},
{'title': 'PS3 Console - 320GB', 'desc': 'PS3 Super Slim with 2 controllers, includes 10 classic games. Budget gaming option.', 'price': 600, 'cat': 'electronics', 'city': 'Sukkur'},
{'title': 'Laptop - Dell Latitude', 'desc': 'Dell Latitude i5, 8GB RAM, 256GB SSD, business laptop. Perfect for work and study.', 'price': 1300, 'cat': 'electronics', 'city': 'Sukkur'},
{'title': 'LED TV - 32 Inch', 'desc': 'Changhong Ruba 32" LED TV, perfect for small rooms and temporary accommodation.', 'price': 600, 'cat': 'electronics', 'city': 'Sukkur'},
{'title': 'Wireless Earbuds - Samsung', 'desc': 'Samsung Galaxy Buds, wireless earbuds with charging case. Perfect for calls and music.', 'price': 200, 'cat': 'electronics', 'city': 'Sukkur'},
{'title': 'Power Bank - 20000mAh', 'desc': '20000mAh power bank with dual USB ports, perfect for charging devices on the go.', 'price': 100, 'cat': 'electronics', 'city': 'Sukkur'},

# ========== ELECTRONICS FOR RENT - Larkana ==========
{'title': 'Canon IXUS 185', 'desc': 'Canon IXUS compact camera, 20MP, perfect for casual photography and family events.', 'price': 500, 'cat': 'electronics', 'city': 'Larkana'},
{'title': 'PS2 Console - Classic', 'desc': 'PS2 with 2 controllers, includes 20+ classic games. Nostalgic gaming experience.', 'price': 400, 'cat': 'electronics', 'city': 'Larkana'},
{'title': 'Desktop Computer - Basic', 'desc': 'Basic desktop PC: Intel Dual Core, 4GB RAM, 500GB HDD, 19" monitor. For basic work.', 'price': 700, 'cat': 'electronics', 'city': 'Larkana'},
{'title': 'Multimedia Speaker - 2.1', 'desc': 'Creative 2.1 multimedia speakers, perfect for computer audio and music.', 'price': 250, 'cat': 'electronics', 'city': 'Larkana'},
{'title': 'USB Hub - 4 Port', 'desc': '4 port USB 3.0 hub with power adapter, perfect for connecting multiple devices.', 'price': 50, 'cat': 'electronics', 'city': 'Larkana'},
{'title': 'HDMI Cable - 10ft', 'desc': '10 feet high-speed HDMI cable, perfect for connecting devices to TV/projector.', 'price': 50, 'cat': 'electronics', 'city': 'Larkana'},

# ========== ELECTRONICS FOR RENT - Mirpur Khas ==========
{'title': 'Sony DSC-W830', 'desc': 'Sony compact camera, 20MP, Zeiss lens. Perfect for point and shoot photography.', 'price': 550, 'cat': 'electronics', 'city': 'Mirpur Khas'},
{'title': 'PSP Console - Portable', 'desc': 'PSP 3000 with 10 games pre-loaded on memory card. Perfect for portable gaming.', 'price': 350, 'cat': 'electronics', 'city': 'Mirpur Khas'},
{'title': 'Tablet - Lenovo Tab M8', 'desc': 'Lenovo Tab M8, 8" display, 32GB. Perfect for reading, browsing, and kids.', 'price': 400, 'cat': 'electronics', 'city': 'Mirpur Khas'},
{'title': 'Car Charger - Dual USB', 'desc': 'Dual USB car charger with fast charging, perfect for road trips.', 'price': 50, 'cat': 'electronics', 'city': 'Mirpur Khas'},
{'title': 'Bluetooth Adapter - Audio', 'desc': 'Bluetooth audio receiver, turns any speaker into wireless speaker.', 'price': 80, 'cat': 'electronics', 'city': 'Mirpur Khas'},
{'title': 'Memory Card Reader', 'desc': 'USB 3.0 multi card reader, supports SD, microSD, CF cards.', 'price': 50, 'cat': 'electronics', 'city': 'Mirpur Khas'},

# ========== ELECTRONICS FOR RENT - Nawabshah ==========
{'title': 'Panasonic Lumix Camera', 'desc': 'Panasonic Lumix point and shoot, 16MP, perfect for family events and travel.', 'price': 600, 'cat': 'electronics', 'city': 'Nawabshah'},
{'title': 'Xbox 360 - Standard', 'desc': 'Xbox 360 with 1 controller, includes 5 games. Budget gaming for kids.', 'price': 500, 'cat': 'electronics', 'city': 'Nawabshah'},
{'title': 'Kindle E-Reader', 'desc': 'Amazon Kindle Paperwhite, 6" display, backlit. Perfect for book lovers.', 'price': 300, 'cat': 'electronics', 'city': 'Nawabshah'},
{'title': 'WiFi Router - TP-Link', 'desc': 'TP-Link WiFi router, 300Mbps, perfect for temporary internet setup.', 'price': 100, 'cat': 'electronics', 'city': 'Nawabshah'},
{'title': 'Smart Watch - Mi Band', 'desc': 'Mi Band 6 fitness tracker with heart rate monitor, perfect for activity tracking.', 'price': 150, 'cat': 'electronics', 'city': 'Nawabshah'},
{'title': 'Extension Board - 4 Port', 'desc': '4 port extension board with surge protection, 5 meter cord.', 'price': 80, 'cat': 'electronics', 'city': 'Nawabshah'},

# ========== ELECTRONICS FOR RENT - Rahim Yar Khan ==========
{'title': 'DJI Osmo Mobile 3', 'desc': 'DJI Osmo Mobile 3 gimbal for smartphones, perfect for smooth video and vlogging.', 'price': 500, 'cat': 'electronics', 'city': 'Rahim Yar Khan'},
{'title': 'PS4 Pro - 1TB', 'desc': 'PS4 Pro with 2 controllers, 1TB, includes 10 games. 4K gaming experience.', 'price': 1600, 'cat': 'electronics', 'city': 'Rahim Yar Khan'},
{'title': 'Laptop - HP Stream', 'desc': 'HP Stream 11, 4GB RAM, 32GB storage, perfect for basic tasks and students.', 'price': 400, 'cat': 'electronics', 'city': 'Rahim Yar Khan'},
{'title': 'Smart TV - 40 Inch', 'desc': 'Haier 40" Android Smart TV, perfect for temporary accommodation and events.', 'price': 900, 'cat': 'electronics', 'city': 'Rahim Yar Khan'},
{'title': 'VR Headset - Oculus Go', 'desc': 'Oculus Go standalone VR headset, 32GB. Perfect for immersive entertainment.', 'price': 600, 'cat': 'electronics', 'city': 'Rahim Yar Khan'},
{'title': 'Dash Cam - Car Camera', 'desc': '1080p dash cam with night vision, perfect for road trips and car rental.', 'price': 200, 'cat': 'electronics', 'city': 'Rahim Yar Khan'},

# ========== ELECTRONICS FOR RENT - Sargodha ==========
{'title': 'Kodak PixPro Camera', 'desc': 'Kodak PixPro 16MP, 5x optical zoom. Budget friendly camera for events.', 'price': 450, 'cat': 'electronics', 'city': 'Sargodha'},
{'title': 'Gaming Console - Retro', 'desc': 'Retro gaming console with 500+ classic games, 2 controllers. Perfect for nostalgia.', 'price': 300, 'cat': 'electronics', 'city': 'Sargodha'},
{'title': 'Monitor - 22 Inch LED', 'desc': '22" Dell LED monitor, 1080p, perfect for temporary workstation setup.', 'price': 400, 'cat': 'electronics', 'city': 'Sargodha'},
{'title': 'FM Radio - Portable', 'desc': 'Portable FM radio with USB/SD card support, perfect for entertainment.', 'price': 100, 'cat': 'electronics', 'city': 'Sargodha'},
{'title': 'Graphing Calculator', 'desc': 'Casio graphing calculator, perfect for students and exams preparation.', 'price': 150, 'cat': 'electronics', 'city': 'Sargodha'},
{'title': 'External Hard Drive - 1TB', 'desc': '1TB external hard drive, USB 3.0, perfect for data backup and transfer.', 'price': 150, 'cat': 'electronics', 'city': 'Sargodha'},

# ========== ELECTRONICS FOR RENT - Jhang ==========
{'title': 'Olympus Tough Camera', 'desc': 'Olympus Tough waterproof camera, perfect for outdoor and beach events.', 'price': 700, 'cat': 'electronics', 'city': 'Jhang'},
{'title': 'PS3 - 160GB', 'desc': 'PS3 Slim with 1 controller, includes 5 games. Affordable gaming option.', 'price': 450, 'cat': 'electronics', 'city': 'Jhang'},
{'title': 'Netbook - Small Laptop', 'desc': 'Small netbook for basic browsing and typing, lightweight and portable.', 'price': 350, 'cat': 'electronics', 'city': 'Jhang'},
{'title': 'Computer Speakers - Basic', 'desc': 'Basic 2.0 computer speakers, perfect for desktop audio.', 'price': 100, 'cat': 'electronics', 'city': 'Jhang'},
{'title': 'DVD Writer - External', 'desc': 'External USB DVD writer, perfect for laptops without optical drive.', 'price': 80, 'cat': 'electronics', 'city': 'Jhang'},
{'title': 'Laptop Cooling Pad', 'desc': 'Laptop cooling pad with 4 fans, adjustable height. Keeps laptop cool during gaming.', 'price': 80, 'cat': 'electronics', 'city': 'Jhang'},

# ========== ELECTRONICS FOR RENT - Sahiwal ==========
{'title': 'Samsung DV150F Camera', 'desc': 'Samsung dual view camera with front LCD, perfect for selfies and group photos.', 'price': 500, 'cat': 'electronics', 'city': 'Sahiwal'},
{'title': 'Wii Console - Nintendo', 'desc': 'Nintendo Wii with 2 remotes, includes 5 games. Perfect for family active gaming.', 'price': 500, 'cat': 'electronics', 'city': 'Sahiwal'},
{'title': 'Printer - HP Deskjet', 'desc': 'HP Deskjet printer with scanner, perfect for home office and students.', 'price': 300, 'cat': 'electronics', 'city': 'Sahiwal'},
{'title': 'Inverter - 1000W', 'desc': '1000W inverter with battery, perfect for backup power for electronics.', 'price': 600, 'cat': 'electronics', 'city': 'Sahiwal'},
{'title': 'Smart Plug - WiFi', 'desc': 'WiFi smart plug, works with Alexa and Google Home. Automate your devices.', 'price': 80, 'cat': 'electronics', 'city': 'Sahiwal'},
{'title': 'Label Maker - Brother', 'desc': 'Brother label maker with tape, perfect for organizing and events.', 'price': 120, 'cat': 'electronics', 'city': 'Sahiwal'},
    {
        'title': 'Laptop - Dell XPS',
        'desc': 'For temporary work/study. i7, 16GB RAM.',
        'price': 1000,
        'cat': 'electronics',
        'city': 'Lahore'
    },
    {
        'title': 'Projector for Home Cinema',
        'desc': '1080p projector for movie night.',
        'price': 1500,
        'cat': 'electronics',
        'city': 'Islamabad'
    },
    {
        'title': 'Speakers for Party',
        'desc': 'Bluetooth speaker, 200W, for small parties.',
        'price': 800,
        'cat': 'electronics',
        'city': 'Karachi'
    },
    {
        'title': 'iPad for Kids/Study',
        'desc': 'iPad 9th gen for temporary use.',
        'price': 600,
        'cat': 'electronics',
        'city': 'Rawalpindi'
    },
    {
        'title': 'Printer - Office Use',
        'desc': 'Laser printer for documents/assignments.',
        'price': 400,
        'cat': 'electronics',
        'city': 'Lahore'
    },
    
    # ========== CAMPING & OUTDOOR ==========
    {
        'title': 'Camping Tent - 6 Person',
        'desc': 'For northern areas trip. Waterproof tent with poles.',
        'price': 800,
        'cat': 'other',
        'city': 'Islamabad'
    },
    {
        'title': 'Sleeping Bags - Set of 4',
        'desc': 'For camping trips. Warm and comfortable.',
        'price': 600,
        'cat': 'other',
        'city': 'Karachi'
    },
    {
        'title': 'BBQ Grill',
        'desc': 'Portable grill for picnic/backyard.',
        'price': 500,
        'cat': 'other',
        'city': 'Lahore'
    },
    {
        'title': 'Power Bank - Heavy',
        'desc': '50000mAh for camping trips.',
        'price': 300,
        'cat': 'electronics',
        'city': 'Islamabad'
    },
    
    # ========== BABY & KIDS ITEMS ==========
    {
        'title': 'Baby Walker',
        'desc': 'For temporary use when guests visit.',
        'price': 200,
        'cat': 'other',
        'city': 'Karachi'
    },
    {
        'title': 'Baby Crib',
        'desc': 'Portable crib for visiting family.',
        'price': 500,
        'cat': 'furniture',
        'city': 'Lahore'
    },
    {
        'title': 'Car Seat for Baby',
        'desc': 'For traveling with infant.',
        'price': 400,
        'cat': 'vehicles',
        'city': 'Islamabad'
    },
    {
        'title': 'Kids Bicycle - 16 inch',
        'desc': 'For visiting grandchildren.',
        'price': 300,
        'cat': 'other',
        'city': 'Rawalpindi'
    },
    
    # ========== HOME APPLIANCES ==========
    {
        'title': 'Air Cooler',
        'desc': 'For temporary summer use.',
        'price': 500,
        'cat': 'other',
        'city': 'Karachi'
    },
    {
        'title': 'Heater - Room',
        'desc': 'Gas heater for winter months.',
        'price': 400,
        'cat': 'other',
        'city': 'Islamabad'
    },
    {
        'title': 'Washing Machine',
        'desc': 'For temporary use when yours is broken.',
        'price': 800,
        'cat': 'other',
        'city': 'Lahore'
    },
    {
        'title': 'Refrigerator - 10 cu ft',
        'desc': 'For temporary need during events.',
        'price': 1000,
        'cat': 'other',
        'city': 'Karachi'
    },
    
    # ========== EDUCATIONAL ==========
    {
        'title': 'Textbooks - Class 9-10',
        'desc': 'Complete set of PTB books for temporary use.',
        'price': 300,
        'cat': 'books',
        'city': 'Lahore'
    },
    {
        'title': 'Calculator - Scientific',
        'desc': 'For exams/tests.',
        'price': 100,
        'cat': 'books',
        'city': 'Karachi'
    },
    {
        'title': 'Laptop for Students',
        'desc': 'Basic laptop for assignment submission.',
        'price': 500,
        'cat': 'electronics',
        'city': 'Islamabad'
    },
    
    # ========== MEDICAL EQUIPMENT ==========
    {
        'title': 'Wheelchair',
        'desc': 'For temporary use during recovery.',
        'price': 300,
        'cat': 'other',
        'city': 'Karachi'
    },
    {
        'title': 'Oxygen Cylinder',
        'desc': 'Medical oxygen for emergency.',
        'price': 500,
        'cat': 'other',
        'city': 'Lahore'
    },
    {
        'title': 'Patient Bed',
        'desc': 'Hospital bed for home care.',
        'price': 800,
        'cat': 'furniture',
        'city': 'Rawalpindi'
    },
    {
        'title': 'BP Machine',
        'desc': 'Digital blood pressure monitor.',
        'price': 150,
        'cat': 'other',
        'city': 'Islamabad'
    },
]

# Add data to database
count = 0
print("\n📝 Adding rental items to database...")
print("-" * 60)

for item in rental_data:
    listing, created = Listing.objects.get_or_create(
        title=item['title'],
        defaults={
            'description': item['desc'],
            'price_per_day': item['price'],
            'category': item['cat'],
            'city': item['city'],
            'owner': seller,
            'is_available': True
        }
    )
    if created:
        count += 1
        print(f"✅ [{count:2d}] {item['title'][:45]} - PKR {item['price']}/day - {item['city']}")

print("-" * 60)
print("\n" + "=" * 60)
print("📊 PAKISTAN RENTAL DATA SUMMARY")
print("=" * 60)
print(f"✅ New rental items added: {count}")
print(f"📦 Total items in database: {Listing.objects.count()}")
print("\n👤 Rental Provider Login:")
print(f"   Username: renter")
print(f"   Password: renter123")
print("\n📍 Available Cities:")
print("   Karachi | Lahore | Islamabad | Rawalpindi")
print("\n📂 Categories:")
print("   Clothing (Wedding) | Vehicles | Electronics | Furniture | Other")
print("=" * 60)
print("\n🎉 Pakistan rental data added successfully!")
print("🌐 Visit: http://127.0.0.1:8000")
print("=" * 60)