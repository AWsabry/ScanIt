# ScanIt

## What is added in this branch ?

When you call the url "http://localhost:8000/login" it returns a token expeired after 40 seconds
- This token will be accessable as a Bearer auth in the header of the url of "http://localhost:8000/user" and return user data.
- "http://localhost:8000/register" will create another user with this fields required :

-- email
-- first_name
-- last_name
-- password
-- city
-- PhoneNumber

Otherwise the api will return "serializer not valid" with status_code 400.


Coming to the graphql schema of the vendors, Categories & Products Models 

## Getting all Vendors
- "http://localhost:8000/getVendors" will require this schema to get all the vendors in the database 

{
allVendors {
id
name
vendorSlug
numberOfBranches
logoImage
backgroundImage
Longitude
Latitude
created
active
}
}

## Getting Vendor by id
- "http://localhost:8000/getVendorsById" will require this schema to get the vendor by id from the database

{
getVendor(id:"1") {
id
name
vendorSlug
numberOfBranches
logoImage
backgroundImage
Longitude
Latitude
created
active
}
}


## Getting all Categories
- "http://localhost:8000/getCategories" will require this schema to get all the categories from the database

{
allCategories {

CategoryName
categorySlug
image
active
created
}
}

## Getting all Products
- "http://localhost:8000/getProducts" will require this schema to get all the Products from the database

{
allProducts {

name
ArabicName
productSlug
vendor {
  id
}
description
price
category {
  id
}
active
MostPopular
NewProducts
BestOffer
created
}
}



## Getting product by id
- "http://localhost:8000/getProductById" will require this schema to get Product by id from the database

{
getProduct(id:"1") {
name
ArabicName
productSlug
vendor {
  id
}
description
price
category {
  id
}
active
MostPopular
NewProducts
BestOffer
created
}
}
