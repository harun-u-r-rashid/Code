from django.shortcuts import render

# Create your views here.
def home(request):
   meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "mealDes" : "The BeaverTail is a fried dough pastry that is sold in a variety of flavours. Most flavours of BeaverTails are topped with sweet condiments and confections, such as whipped cream, banana slices, crumbled Oreos, cinnamon sugar, and chocolate hazelnut. "
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "mealDes" : "Hash browns, or hashed brown potatoes, are a breakfast side dish of shredded potatoes that you season with salt, pepper, and any other flavorings and sauté until they are golden brown and crispy on the outside and still soft on the inside."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "mealDes" : "Canadian butter tarts are rich and gooey mini pies that put buttery goodness front and center—perfect for holidays or any day! Butter tarts are a quintessential Canadian dessert."
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "mealDes" : "Montreal-style smoked meat, Montreal smoked meat or simply smoked meat in Quebec is a type of kosher-style deli meat product made by salting and curing beef brisket with spices. The brisket is allowed to absorb the flavours over a week. It is then hot smoked to cook through."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "mealDes" : "The Nanaimo bar is a no-bake dessert named after Nanaimo, a Canadian city in British Columbia. It consists of three layers: a coconut crumb base, a custard filling, and a chocolate ganache topping."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "mealDes" : "The dish is made with layered ground beef (sometimes mixed with sautéed diced onions) on the bottom, canned corn (either whole-kernel, creamed, or a mixture) for the middle layer, and mashed potatoes on top. "
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "mealDes" : "Called “poor man's pudding” or “pudding of the unemployed,” it was made with inexpensive ingredients or pantry items that people already had on hand. Think along the lines of a simple cake batter using flour, butter, sugar, eggs, baking powder, salt, and vanilla."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "mealDes" : "Poutine is a dish of french fries and cheese curds topped with a brown gravy. It emerged in Quebec, in the late 1950s in the Centre-du-Québec region though its exact origins are uncertain and there are several competing claims regarding its invention."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "mealDes" : "This is a traditional Canadian dish. The main ingredient is grated potatoes. This was handed down from my family in Nova Scotia. It was always a special treat because originally it was so much work to make but it really was worth waiting for. "
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "mealDes" : "There's nothing like classic split pea soup to satisfy your comfort food craving. This split pea soup recipe is complete with ham, hearty veggies, and simple seasonings."
        }
    ]
   return render(request,'./A/index.html',{'meals' : meals})

    
    
