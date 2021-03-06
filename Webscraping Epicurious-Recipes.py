import urllib.request as ul
from bs4 import BeautifulSoup 

term_list=list()

while True:
    term = input("Enter a search term or END to exit: ")
    if term == 'END':
        break
    term_list.append(term)
    list2=list()
    list2=term_list[0].split()
    
    search_link = 'http://www.epicurious.com/tools/searchresults?search='+list2[0]
    for i in range(1,len(list2)):
        search_link +='+'+list2[i]
    
    url_response = ul.urlopen(search_link)
    epicurious_soup = BeautifulSoup(url_response)
    sector_result = epicurious_soup.find('div', class_='sr_rows clearfix firstResult')
    first_recipe = sector_result.find_all('a')[0].get('href')
    
    recipe_link = 'http://www.epicurious.com'+first_recipe
    url_recipe = ul.urlopen(recipe_link)
    recipe_soup = BeautifulSoup(url_recipe)
    
    name = recipe_soup.find('div', class_='title-source').find('h1').get_text()
    
    if recipe_soup.find('div', class_='dek').get_text('p'):
        description = recipe_soup.find('div', class_='dek').get_text('p')
    else: 
        description = "None"
        
    ingredients = recipe_soup.find('div', class_='ingredients-info').get_text(separator = "\n")
    preparation = recipe_soup.find('div', class_='instructions', itemprop = 'recipeInstructions').find('li').get_text(separator = "\n")  
    
    print("\n"+'Name: '+ name +"\n")
    print("Description: "+description+"\n")
    print(ingredients)
    print("Preparation: "+"\n"+preparation)

    term_list.clear()
