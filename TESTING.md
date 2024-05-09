# Testing

Return back to the [README.md](README.md) file.

Throughout the development of this project, I've carried out numerous tests to ensure that the site works well. In this section you will find documentation of all tests carried out throughout the site.

## Code Validation

I have validated all of my code using the recommended tools for each language.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home | ![screenshot](docs/w3c/home-page.png) | Pass: No Errors |
| All Products | ![screenshot](docs/w3c/products-page.png) | Pass: No Errors |
| Single Product | ![screenshot](docs/w3c/single-product.png) | Pass: No Errors |
| Contact | ![screenshot](docs/w3c/contact-page.png) | Pass: No Errors |
| Sign Up | ![screenshot](docs/w3c/signup-page.png) | Pass: No Errors |
| Sign In | ![screenshot](docs/w3c/signin-page.png) | Pass: No Errors |
| Password Reset | ![screenshot](docs/w3c/password-reset.png) | Pass: No Errors |
| Shopping Bag | ![screenshot](docs/w3c/shopping-bag.png) | Pass: No Errors |
| Checkout | ![screenshot](docs/w3c/checkout-page.png) | Pass: No Errors |
| Sitemap.html | ![screenshot](docs/w3c/sitemap-page.png) | Pass: No Errors |
| About page | ![screenshot](docs/w3c/about-page.png) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| base.css | ![screenshot](docs/w3c/base-css.png) | Pass: No Errors |
| home.css | ![screenshot](docs/w3c/home-css.png) | Pass: No Errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe.js | ![screenshot](docs/jshint/stripe-js.png) | Pass: No Errors |
| home.js | ![screenshot](docs/jshint/home-js.png) | Pass: No Errors |


### Python

I have used the recommended [Black](https://pypi.org/project/black/) to validate all of my Python files.

| File | Screenshot | Notes |
| --- | --- | --- |
| about/views.py | ![screenshot](docs/ci-linter/about-views.png) | Pass: No Errors |
| about/urls.py | ![screenshot](docs/ci-linter/about-urls.png) | Pass: No Errors |
| about/models.py | ![screenshot](docs/ci-linter/about-models.png) | Pass: No Errors |
| bag/contexts.py | ![screenshot](docs/ci-linter/bag-contexts.png) | Pass: No Errors |
| bag/urls.py | ![screenshot](docs/ci-linter/bag-urls.png) | Pass: No Errors |
| bag/views.py | ![screenshot](docs/ci-linter/bag-views.png) | Pass: No Errors |
| checkout/urls.py | ![screenshot](docs/ci-linter/checkout-urls.png) | Pass: No Errors |
| checkout/views.py | ![screenshot](docs/ci-linter/checkout-views.png) | Pass: No Errors |
| checkout/models.py | ![screenshot](docs/ci-linter/checkout-models.png) | Pass: No Errors |
| checkout/forms.py | ![screenshot](docs/ci-linter/checkout-forms.png) | Pass: No Errors |
| checkout/webhooks.py | ![screenshot](docs/ci-linter/checkout-webhooks.png) | Pass: No Errors |
| checkout/webhook_handler.py | ![screenshot](docs/ci-linter/checkout-webhookhandler.png) | Pass: No Errors |
| contact/form.py | ![screenshot](docs/ci-linter/contact-form.png) | Pass: No Errors |
| contact/models.py | ![screenshot](docs/ci-linter/contact-models.png) | Pass: No Errors |
| contact/views.py | ![screenshot](docs/ci-linter/contact-views.png) | Pass: No Errors |
| home/urls.py | ![screenshot](docs/ci-linter/home-urls.png) | Pass: No Errors |
| home/views.py | ![screenshot](docs/ci-linter/home-views.png) | Pass: No Errors |
| newsletter/models.py | ![screenshot](docs/ci-linter/newsletter-models.png) | Pass: No Errors |
| newsletter/forms.py | ![screenshot](docs/ci-linter/newsletter-forms.png) | Pass: No Errors |
| newsletter/views.py | ![screenshot](docs/ci-linter/newsletter-views.png) | Pass: No Errors |
| premwear_league/views.py | ![screenshot](docs/ci-linter/premwear_league-views.png) | Pass: No Errors |
| premwear_league/urls.py | ![screenshot](docs/ci-linter/premwear_league-urls.png) | Pass: No Errors |
| premwear_league/sitemaps.py | ![screenshot](docs/ci-linter/premwear_league-sitemaps.png) | Pass: No Errors |
| products/models.py | ![screenshot](docs/ci-linter/products-models.png) | Pass: No Errors |
| products/forms.py | ![screenshot](docs/ci-linter/products-forms.png) | Pass: No Errors |
| products/urls.py | ![screenshot](docs/ci-linter/products-urls.png) | Pass: No Errors |
| products/views.py | ![screenshot](docs/ci-linter/products-views.png) | Pass: No Errors |
| profiles/forms.py | ![screenshot](docs/ci-linter/profiles-forms.png) | Pass: No Errors |
| profiles/models.py | ![screenshot](docs/ci-linter/profiles-models.png) | Pass: No Errors |
| profiles/urls.py | ![screenshot](docs/ci-linter/profiles-urls.png) | Pass: No Errors |
| profiles/views.py | ![screenshot](docs/ci-linter/profiles-views.png) | Pass: No Errors |
| sitemap/views.py | ![screenshot](docs/ci-linter/sitemap-views.png) | Pass: No Errors |
| sitemap/urls.py | ![screenshot](docs/ci-linter/sitemap-urls.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](docs/browsers/chrome.png) | Works as expected |
| Firefox | ![screenshot](docs/browsers/firefox.png) | Works as expected |
| Edge | ![screenshot](docs/browsers/edge.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness and found no issues here is an example

| mobile | ipad | laptop|
| --- | --- | --- | 
| ![screenshot](docs/responsive/mobile.png) | ![screenshot](docs/responsive/ipad.png) | ![screenshot](docs/responsive/laptop.png) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| **Home Page** | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Shop Now button | Redirection to Products page | Pass | |
| **All Products Page** | | | | |
| | Click on Products link in navbar | Redirection to Products page | Pass | |
| | Click on Products category link in navbar | Redirection to product page | Pass | Products filtered by clicked category |
| | Click on Product card image | Redirection to Product Detail page for that product | Pass | |
| | Click on Add to basket button | Product added to basket | Pass | Product added to cart and cart modal shown |
| **Product Detail Page** | | | | |
| | Click on Product image in products page | Redirection to Product Detail page | Pass | |
| | Click on Keep Shopping button | Redirection to Products page | Pass | |
| | Click Add To Basket button | Product is added to basket and quantity is set to the user's choice | Pass | |
| **Search** | | | | |
| | Enter letter into search bar | All products linked returned | Pass | Products filtered to only show products containing search term |
| **Contact Page** | | | | |
| | Click on Contact link in footer | Redirection to Contact Us page | Pass | |
| | Enter name | Form will only submit if all fields are filled | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message | Form will only submit if all fields are filled | Pass | |
| | Click Send with missing fields | Message lets user know all fields are required | Pass | |
| **Sign Up Page** | | | | |
| | Click on Register button under account on nav menu | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click Sign Up button on sign up page | Sends confirmation email and lets user know to check their email | Pass | |
| | Click link in confirmation email | Redirects user to sign in page | Pass | |
| **Sign In Page** | | | | |
| | Click on the Login button under account on nav menu | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button on login page | Redirects user to homepage | Pass | |
| | Click Forgot Password | Redirects user to password reset page | Pass | |
| | Sign in before confirming account | Redirects to message reminding user to confirm email address | Pass | |
| **Password Reset Page** | | | | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Click Reset Password button | Sends email with instructions to reset password | Pass | |
| **Log Out Page** | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| **Profile Page** | | | | |
| | Click on the My Profile link under account on nav menu | Redirection to profile page page | Pass | Only shows for logged in users |
| | Click Update Information button | Saves form contents to be default information for user | Pass | |
| **Cart** | | | | |
| | Click Bag icon in main nav | Redirects user to shopping bag page | Pass | Shows back to shop button if basket is empty |
| | Click update button under quantity selector form | Updated quantity of product in basket to number in quantity select form | Pass | |
| | Click remove button | Removes product from basket completely | Pass | |
| | Click on Keep Shopping button | Redirection to Products page | Pass | |
| | Click on Secure Checkout button | Redirection to checkout page | Pass | |
| **Checkout** | | | | |
| | Click on Secure Checkout button in basket | Redirection to checkout page | Pass | |
| | Click Complete Order button without all required fields filled out | Message letting user know that required fields need to be filled out | Pass | |
| | Click on Create an account link | Redirection to sign up page | Pass | Only visible to logged out users |
| | Click on login link | Redirection to sign in page | Pass | Only visible to logged out users |
| | Click Complete Order button without card details filled out | Message letting user know that their card number is incomplete | Pass | |
| | Click Complete Order button with all details filled out | Loading spinner appears and order is processed | Pass | |
| | Order completed | Order confirmation email is sent to the user and redirection to checkout success page | Pass | |
| **Checkout Success Page** | | | | |
| | Order completed | Redirection to checkout success page | Pass | |
| **Footer** | | | | |
| | Click on Subscribe button on filled newsletter form | Alert message lets user know they have signed up for the mailing list and welcome email is sent to address provided | Pass | |


