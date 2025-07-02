# E_market

#### Video Demo:  https://youtu.be/2kLgeH3vi-k

#### Description:
This is my final project for CS50x — it’s a small Django e-commerce website I called E_market. I mainly wanted to test myself and see if I could actually build something functional from scratch after everything we learned. I was inspired by this repo I found: https://github.com/jimdevops19, and thought, okay, let me make my own version and try to build the core features but with my own logic, structure, and style.

So, first, I wanted to do another flask project but i wanted to learn even more and django happened to be used a fair bit in where i am (egypt btw) I set up the basic Django project and made the Item model. It includes name, description, price, stock, and an image. I didn't want to deal with uploading or storing images so I just used Lorem Picsum (https://picsum.photos/) for placeholder images, which worked out fine and looked nice enough and avoids copyrights.

The site has user registration, login, and logout — all basic Django auth stuff, but styled with Bootstrap and some modals to make it feel smoother. you can see a list of products pulled directly from the database without logging in but in order to purchase any item you need to be logged in. Each product is displayed with it's info and has a view details button that opens a modal with the full description and a purchase button.

I wanted to implement was live inventory. so when you buy something, it reduces the stock. If it’s out of stock, it won’t let you buy anymore. It was a bit tricky (but fun ngl) to get right since I had to handle both frontend feedback and backend validation, but I think it works well now. The logic prevents buying anything with 0 stock and reflects stock changes immediately.

tech used:
- python & django
- SQLite
- HTML, CSS, Bootstrap


TODO: (what was done)
- create an item model
- create login page
- create register page
- add items picture using lorem picsum `https://picsum.photos/`
- add landing page
- make the nav bar
- make the items page
- list items dynamically from the database to the items page
- add items modal to check the description before purchase
- implement the purchase logic



#### How to run:
- make a venv `python -m venv .venv`
- activate the venv `source .venv/bin/activate`
- install the requirements `pip install requirements.txt`
- then run the server `python manage.py runserver` 