# CoffeeShop

A simple e-commerce website for a coffee shop built with Django.  
Users can browse products, add them to a session-based cart, update quantities, and proceed to payment (future feature).

## Features

- Product catalog with categories  
- Session-based shopping cart with add, update quantity, and remove functionality  
- Responsive UI using Bootstrap 5  
- User messages for cart actions  
- Media support for product images  
- Basic URL routing and template structure  

## Getting Started

### Prerequisites

- Python 3.8+  
- Django 4.x  
- pip (Python package manager)  
- virtualenv (recommended)  

### Installation

Clone the repository:

   ```bash
   git clone https://github.com/motconkien/coffeeshop.git
   cd coffeeshop

   ```


## Usage

1. **Homepage**  
   Navigate to `/` to see a list of categories and featured products.

2. **Product Ordering**  
   Click “Order” next to a product to add it to the cart.

3. **View Cart**  
   Click the 🛒 cart icon in the navbar or go to `/cart/` to view your cart.

4. **Cart Actions**  
   - Update quantity using the number input.  
   - Remove items.  
   - Total updates automatically.

The following features have been implemented to complete the shopping experience:

5. **User Registration & Login**  
- Users can register an account using a simple form.
- Login and logout functionality integrated with Django's authentication system.
- After login, cart items are preserved and associated with the authenticated user.

6. **Checkout and Payment Flow**
- Users proceed to a **Checkout** page where they provide:
  - Full name
  - Phone number
  - Delivery address
  - Payment method (e.g. Cash on Delivery, Bank Transfer)
- On submission:
  - An order is created and saved in the database.
  - The cart is cleared automatically.
  - Users are redirected to a success confirmation page.


