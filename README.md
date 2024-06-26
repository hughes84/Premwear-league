# Premwear League Website- PP5
![mockup](docs/mockup/all-sizes.png)

Welcome to our premier destination for all your football gear needs, inspired by the electrifying spirit of the English Premier League. Discover a vast array of authentic football gear, meticulously curated to satisfy the cravings of die-hard fans and aspiring athletes alike. Enjoy a seamless shopping experience with our intuitive website design.

Developed by Paul Hughes

[Live link to website](https://premwear-league-b168782f243c.herokuapp.com/)

## UX

In designing this website, simplicity was a key focus. Complicating the layout of an e-commerce platform can detract from the user experience, which is something I actively sought to avoid.

Throughout the site, I've maintained a straightforward design approach. Users can conveniently track their basket's total as they browse and add items. Unlike platforms that conceal this information until checkout, my approach fosters trust and helps users manage their spending effectively.

Navigation is intuitive, facilitated by a user-friendly main menu that allows easy exploration of all sportswear product categories. This site is crafted to offer seamless access to a wide range of products without overwhelming users with complex menus or structures.

In essence, the website prioritizes simplicity and transparency, aiming to provide users with a positive and stress-free browsing experience from start to finish.

# Table of Contents

1. [Project Goals](#project-goals)
    - [Purpose](#purpose)
    - [Site Goals](#site-goals)
    - [User Goals](#user-goals)
2. [User Stories](#user-stories)
3. [E-Commerce Business Model and Marketing Strategies](#e-commerce-business-model-and-marketing-strategies)
    - [Business Model Overview](#business-model-overview)
    - [Business Model Components](#business-model-components)
    - [Marketing Strategies](#marketing-strategies)
4. [Wireframes](#wireframes)
    - [Desktop wireframes](#desktop-wireframes)
    - [Mobile wireframes](#mobile-wireframes)
5. [Layout and Styling](#layout-and-styling)
    - [Bootstrap](#bootstrap)
6. [Media queries](#media-queries)
7. [Imagery](#imagery)
8. [Colour Scheme](#colour-scheme)
9. [Typography](#typography)
10. [Icons](#icons)
11. [Favicon](#favicon)
12. [Loading spinner](#loading-spinner)
13. [Scope](#scope)
    - [Minimum Viable Product](#minimum-viable-product)
    - [Additional Features](#additional-features)
    - [Future Ideas](#future-ideas)
14. [Python Functionality using Django](#python-functionality-using-django)
15. [Existing Features](#existing-features)
16. [Tools And Technologies Used](#tools-and-technologies-used)
17. [Agile Development Process](#agile-development-process)
    - [GitHub Projects](#gitHub-projects)
    - [GitHub Issues](#gitHub-issues)
    - [MoSCoW Prioritization](#moSCoW-prioritization)
18. [Ecommerce Business Model](#ecommerce-business-model)
19. [Sitemap](#sitemap)
20. [Newsletter Marketing](#newsletter-marketing)
21. [Testing](#testing)
22. [Deployment](#deployment)
    - [Amazon AWS](#amazon-aws)
    - [Stripe API](#stripe-api)
    - [Gmail](#gmail)
    - [Heroku Deployment](#heroku-deployment)
    - [Local Deployment](#local-deployment)
23. [Cloning](#cloning)
    - [Forking](#forking)
24. [Credits](#credits)
    - [Acknowledgements](#acknowledgements)



## Project Goals

### Purpose

An e-commerce site selling Premier League football shirts, hats, shorts, socks and flags, which allows customers to browse and buy, while allowing site admins to add, edit and delete products.

### Site Goals

- Product Showcase: Showcase the latest trends, designs, and innovations in the sportswear industry, highlighting the quality and functionality of the products offered.
- Brand Promotion: Serve as a platform to promote and build brand awareness for the sportswear brand, leveraging digital marketing strategies and engaging content to attract and retain customers.
- Personalization: Utilize data analytics and customer insights to personalize the shopping experience, recommending products based on past purchases, preferences, and browsing behavior.
- Mobile Compatibility: Ensure the website is mobile-responsive, catering to the growing number of customers who prefer to shop on their smartphones and tablets.
- Customer Support: Provide efficient customer support channels, including messaging and email to address inquiries, resolve issues, and ensure customer satisfaction post-purchase.

[Back to Table of Contents](#table-of-contents)

### User Goals

- Customer Convenience: Provide customers with a convenient platform to browse, select, and purchase sportswear products from the comfort of their homes or on the go, enhancing overall shopping experience.
- Find Desired Products Easily: Users aim to quickly locate the sportswear products they are interested in, whether it's specific items, brands, or categories.
- View Product Details: Users seek detailed information about each product, including descriptions, materials, sizing charts, and customer reviews, to make informed purchasing decisions.
- Secure Transactions: Users prioritize secure payment methods and data protection measures to safeguard their personal and financial information during online transactions.
- Satisfactory Customer Service: Users expect responsive customer support services to address inquiries, resolve issues, and provide assistance throughout the shopping experience, ensuring a positive overall interaction with the website.

[Back to Table of Contents](#table-of-contents)

## User Stories

To help with the development of this project, I created user stories to map out tasks I needed to achieve in order to build the website to a good standard. I further split these user stories into epics in order to take an agile approach to its development.

View a full list of user stories [here](https://github.com/users/hughes84/projects/3).

View the Sprints here [here](https://github.com/hughes84/Premwear-league/milestones).

[Back to Table of Contents](#table-of-contents)

# E-Commerce Business Model and Marketing Strategies

## Business Model Overview

Our e-commerce platform operates as a retail store specializing in football (soccer) gear and merchandise. We offer a wide range of products including jerseys, shorts, socks, hats, and flags, catering to football enthusiasts, athletes, and fans worldwide.

## Business Model Components

- Product Selection: We curate a diverse range of high-quality football gear from renowned brands and manufacturers.
- Online Platform: Our website serves as the primary storefront, providing customers with a user-friendly interface for browsing and purchasing products.
- Order Fulfillment: We manage order processing, packaging, and shipping to ensure timely delivery of products to customers.
- Customer Service: Our dedicated customer support team handles inquiries, resolves issues, and ensures customer satisfaction.

## Marketing Strategies

- Search Engine Optimization (SEO):
Optimizing website content and metadata for relevant keywords to improve visibility on search engines like Google.
- Social Media Marketing:
Leveraging platforms like Facebook to showcase products, engage with customers, and drive traffic to the website.
- Email Marketing:
Building and nurturing a subscriber list to send out newsletters, promotions, and product updates to interested customers..
- Seasonal Promotions:
Offering special discounts, deals, and promotions during key football events such as major tournaments, league matches, and holiday seasons.
- Continuous Improvement:
We continuously analyze customer feedback, monitor market trends, and evaluate the performance of our marketing strategies to adapt and optimize our approach for sustainable growth and success in the competitive e-commerce landscape.

[Back to Table of Contents](#table-of-contents)

## Wireframes

To help with the design of the site, I created wireframes for each page. To follow best practice, wireframes were developed for mobile and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

## Desktop wireframes

<details><summary>Click to Desktop wireframes</summary>

![screenshot](wireframes/wf-home.png)<br>
![screenshot](wireframes/wf-products.png)<br>
![screenshot](wireframes/wf-bag.png)<br>
![screenshot](wireframes/wf-checkout.png)<br>
![screenshot](wireframes/wf-ordersuccess.png)

</details>

[Back to Table of Contents](#table-of-contents)

## Mobile wireframes

<details><summary>Click to Mobile wireframes</summary>

![screenshot](wireframes/wf-mobile-home.png)<br>
![screenshot](wireframes/wf-mobile-products.png)<br>
![screenshot](wireframes/wf-mobile-bag.png)<br>
![screenshot](wireframes/wf-mobile-checkout.png)<br>
![screenshot](wireframes/wf-mobile-ordersuccess.png)

</details>

[Back to Table of Contents](#table-of-contents)

Based on prior experience I decided that desktop and mobile wireframes would be sufficient to keep the overall layout of the site on track, the expectation being that [Bootstrap's grid system](https://getbootstrap.com/docs/5.3/layout/grid/) would provide the responsiveness required at different device breakpoints in between (see [Layout and Styling](#layout-and-styling) section below).

Furthermore, I focused the wireframes on the main product purchase workflow, recognising that this was where design choices would be key. The other pages contain simple forms and tables, so I considered there to be little value in producing specific wireframes for those pages.

### Layout and Styling

#### Bootstrap

The site uses the [Bootstrap 5.3 Grid system](https://getbootstrap.com/docs/5.3/layout/grid/) to ensure it is fully responsive on all device and viewport sizes. Bootstrap 5.3 uses the following [breakpoints](https://getbootstrap.com/docs/5.3/layout/breakpoints/), the shorthand references for which are used throughout the rest of this document:

| Breakpoint        | Shorthand   | Dimensions |
|-------------------|-------------|------------|
| Extra small       | xs          | <576px     |
| Small             | sm          | ≥576px     |
| Medium            | md          | ≥768px     |
| Large             | lg          | ≥992px     |
| Extra large       | xl          | ≥1200px    |
| Extra extra large | xxl         | ≥1400px    |

[Back to Table of Contents](#table-of-contents)

In addition, the site uses the following specific components from the Bootstrap library:

- [Navbar](https://getbootstrap.com/docs/5.3/components/navbar/) for the header.
- [Cards](https://getbootstrap.com/docs/5.3/components/card/) to display product information on the products page.
- [Accordion](https://getbootstrap.com/docs/5.3/components/accordion/) to provide a collapsible menu for the FAQs.
- [Alerts](https://getbootstrap.com/docs/5.3/components/alerts/) to display status messages.
- [Modal plugin](https://getbootstrap.com/docs/5.3/components/modal/) to display enlarged product images on click.
- [Spacing](https://getbootstrap.com/docs/5.3/utilities/spacing/) and [typography](https://getbootstrap.com/docs/5.3/content/typography/) utility classes throughout, ensuring the layout and font are appropriate to the device in use.
- [Color](https://getbootstrap.com/docs/5.3/utilities/colors/) utility classes to provide specific meaning to text throughout.
- [Display property](https://getbootstrap.com/docs/5.3/utilities/display/) to toggle the visibility of some components at certain breakpoints.

[Back to Table of Contents](#table-of-contents)

#### Media queries

In addition to the responsive layout provided by Bootstrap, specific media queries are used to rotate the main background image to match the orientation of the device, and to change the sizes of the modal on the home page.

### Imagery

- The **Background image** of footballer's from the English Premier League is depicted of a virtual video game from[PESnewupdate](file:///C:/Users/Owner/pp5/links/PES%202021%20Premier%20League%20Kitpack%202023_2024%20~%20PESNewupdate.com%20_%20Free%20Download%20Latest%20Pro%20Evolution%20Soccer%20Patch%20&%20Updates.html). 
In the image, the group of footballers from various English Premier League teams stands shoulder to shoulder, proudly showcasing their respective team jerseys. The players are arranged in lines, with each athlete donning the iconic colors and designs of their club's uniform. The jerseys are vibrant and meticulously detailed, featuring the distinct logos, crests, and sponsorships associated with each Premier League team.

<details><summary>Background image</summary>
  
  ![Background](media/prem_top.png)
   
  </details>

  [Back to Table of Contents](#table-of-contents)

- The **product images** were taken from various different websites as to capture such a range of a selection. Those websites being; [jdsports](https://www.jdsports.co.uk/sport/football/league/premier-league/), [sportsdirect](https://ie.sportsdirect.com/), [kitbag](https://www.kitbag.com/en/premier-league/football-kits-socks/o-32750439+d-6761548326-128651+z-9-1112756498), [flagladyusa](https://flagladyusa.com/collections/premier-league-flags).

### Colour Scheme

- The **main colours** used for site components (such as navigation items and buttons) are black (#555) and white rgb(255, 255, 255). Using black and white for the navigation on my website I feel it creates a sleek and minimalist design aesthetic while ensuring clear and easy navigation for users. At the top of the website, the white navigation bar spans the width of the page. The navigation links are displayed in bold black text, providing a high contrast that makes them easily visible against the white background.

- The update and remove buttons in the shopping bag are bright and colourful displaying their significance. I chose red (#dc3545) as it displays attention-grabbing, associated with urgency, importance, and alertness. In some contexts, red is used to signal caution, warning, or error. I used green (#28a745) as it is often associated with go, proceed, or confirmation.

- The shopping bag when stocked displays a blue (#17a2b8). I used this brighter color to show the user they have added to their bag which is accompanied by a message. 

- I chose a green (#007b5e) footer from Bootstrap which I feel compliments the color schemes throughout the website. 

[Back to Table of Contents](#table-of-contents)

### Typography

- The site uses [Lato](https://fonts.google.com/specimen/Lato) throughout, imported from [Google Fonts](https://fonts.google.com/). Lato is a popular sans-serif typeface that is widely used in various design contexts, including print and digital media. Lato is known for its modern and elegant appearance, making it suitable for a wide range of design applications.

### Icons

- [Bootstrap Icons](https://icons.getbootstrap.com/) have been used for **navigation items**, **alerts** and various **buttons** throughout the site.

<details><summary>Navigation icons</summary>

  ![Navigation icons](icons/sc-nav1.png)
  ![Navigation icons](icons/sc-nav2.png)
  ![Navigation icons](icons/sc-nav3.png)
  ![Navigation icons](icons/sc-nav4.png)

  </details>

  <details><summary>Alerts</summary>

  ![Success message](icons/sc-success.png)
  ![Info message](icons/sc-info.png)
  ![Warning message](icons/sc-warning.png)
  ![Error message](icons/sc-error1.png)
  ![Error message](icons/sc-error2.png)

  </details>

  <details><summary>Button</summary>

  ![Button](icons/sc-btn1.png)
  ![Button](icons/sc-btn2.png)

  </details>

  [Back to Table of Contents](#table-of-contents)

  ### Favicon

- The **favicon** is the football representing the sites theme, generated using [Favicon Generator](https://favicon.io/favicon-generator/).

  <details><summary>Favicon</summary>

  ![Favicon](static/favicon/android-chrome-192x192.png)

  </details>

  ### Loading spinner

- The site utilises a **loading spinner** on the checkout page to illustrate that a page is loading.

  <details><summary>Loading Spinner</summary>

  ![Loading spinner](icons/sc-spinner.png)

  </details>

  ### Scope

#### Minimum Viable Product

 To be viable as an eCommerce site for sportswear and meet the stated [Project Goals](#project-goals), the website **must have**:
  - Images and details of products for sale.
  - A way for potential customers to browse products.
  - A method for allowing customers to purchase selected products.

  #### Additional Features (in scope)

  To provide a good user experience in line with the stated [Project Goals](#project-goals), the website **should have**:
  - Sophisticated browsing, searching and list ordering functionality to allow customers to find products through a variety of methods.
  - A secure payment system utilising a recognised, trusted payment provider.
  - A user registration system, allowing users to save delivery details and view past orders.
  - A wishlist feature, allowing users to add items to a virtual bag for purchase at a later date.
  - Newsletter sign-up, allowing the business to keep customers up-to-date with news and special offers.

  #### Future Ideas (not currently in scope)
  
   To provide a better user experience and better meet the stated [Project Goals](#project-goals), the website also **could have**:
   - The option for registered users to select their favourite team(s), which would allow for prioritisation of those shirts when browsing, as well as alerts when new items relating to that team are added.
   - The ability for a superuser to dynamically update the team badges displayed on the front page, allowing them to promote different teams at different times based on current events (e.g. promoting the two teams appearing in a cup final).

[Back to Table of Contents](#table-of-contents)

### Python Functionality using Django

Python has been used to build the core backend application which underpins the site, utilising the [Django web framework](https://www.djangoproject.com/). In particular, Python and Django have been used to:

- Provide routing of pages, allowing meaningful URLs to be used to return pages and content to the user.
- Connect to the backend database to retrieve information and serve it to the site, and to allow creation, updating and deletion of records.
- Provide login functionality and security, ensuring only authorised users can access and edit particular information.
- Display messages to the user (via [Bootstrap Alerts](https://getbootstrap.com/docs/5.3/components/alerts/)).

### Existing Features

- **Landing Page**

    - This is the page a user lands on when arriving at the site. It welcomes them to the site and gives them an idea of what the site sells. A button is present that will bring the user to the site's product page.

    ![screenshot](media/sc-homepage.png)
    ![screenshot](media/sc-homepage2.png)

- **Products Page**

    - This is the page containing the products that the site sells.

    ![screenshot](media/sc-products.png)

[Back to Table of Contents](#table-of-contents)

- **Product Card**

    - Each product has its own card which contains the product's price, image, name, favourite button and review count if there are any.
    - If the user is logged in, they will also see a favourite button to add products to there wishlist section in their profile.

    ![screenshot](media/sc-card.png)

- **Product detail page**

    - Every product has a button that lets the user to add it to their basket when viewing individual product page. They can choose the quantity as well.
    - The cart modal shows up after user adds a product confirming the item has been added to their basket.

    ![screenshot](media/sc-productdetail.png)

- **Product Sorting**

    - When the user is viewing products page, they can choose how to sort their search. 

    ![screenshot](media/sc-sorting.png)

[Back to Table of Contents](#table-of-contents)

- **Main Nav Menu**

    - Throughout the whole site the user has access to the main nav menu. Features include a search button, account/profile access, basket link and running total if the user has items added to their baskets.

    ![screenshot](media/sc-main-navmenu.png)

- **Search Bar**
    - Users can use the header search button to open the search input field and search to find specific products. The search term is matched up with products' name and description to give the user a list of products to match their search term.

    ![screenshot](media/sc-searchbar.png)

- **My Account Dropdown**

    - If the user is logged in, the my account dropdown in the nav menu will contain a link to the user's profile, change password, logout and email settings page.
	- If the user is not logged in they will be given the option to sign in. 
    - If admin is logged in an option for product management is displayed also.

   ![screenshot](media/sc-accountdropdown.png)

[Back to Table of Contents](#table-of-contents)

- **Add product**

    - If the user is logged in and has admin permissions, they can add new products.

    ![screenshot](media/sc-addproduct.png)

- **User Sign Up**

    - Users without an account can register for one through the register link in the header. This will present them with a form to add their details and create an account.
	- Users are sent a confirmation email to complete their account sign up to help avoid people from creating spam accounts on the site.

    ![screenshot](media/sc-signup.png)

- **User Sign In**

    - If a user is not signed in to the site but has a profile, they can follow the sign in link in the header where they're presented with a log in page. They must input their username or email address and correct password to do so. There's also a checkbox to remember the user on their current device to avoid having to log in every time they visit the site.
	- There is also a link for users who have forgotten their password.

    ![screenshot](media/sc-signin.png)

[Back to Table of Contents](#table-of-contents)

- **User Sign Out**

    - If a user wants to end their logged in session, they can click logout under the account dropdown in the nav menu.
    - This will bring them to a page confirming they want to log out.

    ![screenshot](media/sc-signout.png)

- **Password Reset**

    - If a user is trying to log in and has forgotten their password they can visit the password reset page. Here a user must enter the email address that they used to sign up with and an email will be sent to them with further instructions on resetting their password to regain access to their account.

    ![screenshot](media/sc-pwreset.png)

- **User Profile**

    - When a user has completed registration on the site, they are given a profile where they can add or edit details.
    - This will also contain past orders and saved wishlists.

    ![screenshot](media/sc-profile.png)

[Back to Table of Contents](#table-of-contents)

- **Site Footer**

    - This appears on every page throughout the site and contains links to the help pages, social media pages and the store's contact details.
  

    ![screenshot](media/sc-footer.png)

- **Newsletter**

    - Using the form in the footer, users can sign up to the site's newsletter by entering their email address and hitting the subscribe button. A confirmation email is then sent confirming signup.

    ![screenshot](media/sc-newsletter.png)

- **Contact Us Page**

    - This page can be accessed from the footer throughout the site in the Help Links.

    ![screenshot](media/sc-contact.png)

[Back to Table of Contents](#table-of-contents)

- **Basket**

    - The basket can be accessed from the main nav menu.
    - In the menu a running total is shown of the items in the user's basket.
    - When the user clicks on this they can see all the items in their basket, individual price of each product, subtotal per product if the quantity is greater than 1 and a quantity selector for each product with buttons to update the quantity or remove the product completely from their basket.
    - If a user does not have anything in their basket, a message will appear prompting the user to continue shopping.

    ![screenshot](media/sc-cart.png)

    ![screenshot](media/sc-empty.png)

- **Cart summary page**

    - On this page the user can update the quantity or remove products and is given a summary of the the order.

    ![screenshot](media/sc-cartsummary.png)

[Back to Table of Contents](#table-of-contents)

- **Checkout**

    - The final step of the users shopping journey on the site is the checkout page.
    - This page contains a form for the user's delivery and payment information and a summary of the user's order.
    - If the user has an account on the site, they can save their delivery information on their profile to automatically be filled in the checkout.

    ![screenshot](media/sc-checkout.png)

- **Order received message**

    - Once the order is complete, the user will receive an order confirmation email informing user that there order has been received.

    ![screenshot](media/sc-ordermsg.png)

- **Order Confirmation Email**

    - Once the order is complete and payment has been received, the user will receive an order confirmation email containing their order number and a receipt with the total paid.

    ![screenshot](media/sc-confirmationemail.png)

[Back to Table of Contents](#table-of-contents)    

## Tools And Technologies Used

This site couldn't have been created without a variety of tools and technologies. I've listed the ones used below.

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.
- [Django Summernote](https://github.com/summernote/django-summernote) used for the body field for blog posts.
- [Pillow](https://pypi.org/project/Pillow/) used for handling images.

[Back to Table of Contents](#table-of-contents)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/hughes84/Premwear-league/projects?query=is%3Aopen) served as an Agile tool for this project.

### GitHub Issues

[GitHub Issues](https://github.com/hughes84/Premwear-league/issues) served as an another Agile tool.

It also helped to keep on top of my [milestones](https://github.com/hughes84/Premwear-league/milestones) for the project.

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered.
- **Should Have**: adds significant value, but not vital.
- **Could Have**: has small impact if left out.
- **Won't Have**: not a priority for this iteration.

[Back to Table of Contents](#table-of-contents)

## Ecommerce Business Model

This site sells goods to individual customers, and therefore follows a `Business to Customer` model.
It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything
such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users.
For example, what items are on special offer, new items in stock,
updates to business hours, notifications of events, and much more!

### Sitemap

I've used the built in 'django.contrib.sitemaps' app to generate the sitemap.xml I also created a
html sitemap for users to view.

[Back to Table of Contents](#table-of-contents)

### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the default settings:

```
User-agent: *
Disallow: /admin/
Sitemap: https://premwear-league-b168782f243c.herokuapp.com/sitemap.xml
```

### Newsletter Marketing

I have incorporate a newsletter sign-up form on my application, to allow users to supply their
email address if they are interested in learning more about what the business has to offer.

I created a custom newsletter app in my project with a custom NewsletterSignup model and added a form to the site's footer to collect user email addresses 

Newsletter model:

```python
class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)

def __str__(self):
    return self.email
```

I set the email address to be unique to avoid users signing up multiple times with the same email address. 

Once a user signs up, I used the `send_mail()` functionality to trigger a welcome email for the user to acknowledge that they've successfully signed up for the newsletter.

[Back to Table of Contents](#table-of-contents)

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://premwear-league-b168782f243c.herokuapp.com/).

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

[Back to Table of Contents](#table-of-contents)

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

[Back to Table of Contents](#table-of-contents)

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or retro-reboot
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

[Back to Table of Contents](#table-of-contents)

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

[Back to Table of Contents](#table-of-contents)

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:
- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

[Back to Table of Contents](#table-of-contents)

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/hughes84/Premwear-league) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/hughes84/Premwear-league.git`
7. Press Enter to create your local clone.

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/hughes84/Premwear-league)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

All snippets are credited in comments in the relevant files or acknowledgements below.

### Acknowledgements

Special thanks to my mentor Adegbenga Adeye for his guidance and help throughout. My course facilitator at Code Institute, Laura Mayock for continued support on weekly stand up calls. My cohort colleagues for taking time out of their busy schedules to join me on several study group sessions and those who took part.

[Back to Table of Contents](#table-of-contents)