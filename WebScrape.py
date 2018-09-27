import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1'


#Opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing
page_soup = soup(page_html, "html.parser")
# selects each graphic card
containers = page_soup.findAll("div", {"class":"item-container"})
container = containers[0]


#print(container.div.div.a.img["title"])

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping, price \n"
f.write(headers)



for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	price_container = container.findAll("li", {"class":"price-current"})
	price_temp1 = price_container[0].text.strip()
	price_temp2 = price_temp1.split()
	for i in price_temp2:
		if(i[0] == "$"):
			price = i

	#price_list = price_container[0].text.split()
	#price = price_list[1]
	#print(price_list)
	#print(price)



	# print("brand: ", brand)
	# print("product_name: ", product_name)
	# print("shipping: ", shipping)

	f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "," + price.replace(",",".") + "\n")

f.close()


# print(title_container)
# print("XXXXXXXXXXX")
# print(title_container[0].text)


#print(container.a)
#print(container.div)
#print(page_soup.h1)
#print(len(containers))
