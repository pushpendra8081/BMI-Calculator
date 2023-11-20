# importing modules
from pywebio.input import input, FLOAT
from pywebio.output import put_text
from pywebio.output import put_image

# defining method

def bmi():
    name=input('Name', placeholder='Enter Your Name')
    height = input("Your Height(cm)：", type=FLOAT)
    weight = input("Your Weight(kg)：", type=FLOAT)

    BMI = float(weight / (height / 100) ** 2)

    if BMI < 18.5:
        put_text('Your BMI: '+str(BMI)+'\nCategory is Underweight')
        put_text("Diet Chart")
        put_image(open('E:/Manish Scl Proj/Underweight.jpg','rb').read())
        put_text("Breakfast (8:00 - 8:30AM): 2 egg brown bread sandwich + green chutney + 1 cup milk + 3 cashews + 4 almonds + 2 walnuts\n"
                     "Mid-Meal(11:00-11:30AM): 1 cup banana shake\nLunch (2:00-2:30PM): 1 cup arhar dal + 1 cup potato curry + 3 chapatti + 1/2 cup rice + 1/2 cup low fat curd + salad\n"
                     "Evening (4:00-4:30PM): 1 cup strawberry smoothie + 1 cup vegetable poha\nDinner (8:00-8:30PM): 1.5 cup chicken curry + 3 chapatti + salad" )


    if BMI >= 18.5 and BMI<24.9:
        put_text('Your BMI:'+str(BMI)+'\nCategory is Normal')
        put_text("Diet Chart")
        put_image(open('E:/Manish Scl Proj/Normal.jpg', 'rb').read())
        put_text("Breakfast (8:00-8:30AM):2 slices toast + 2 teaspoon margarine + 1/2 cup beans + 250ml milk\n"
                 "Mid-Meal(11:00-11:30AM): 1 Apple + 200ml coffee\n"
                 "Lunch (2:00-2:30PM): 2 slices bread + 65g roast beef + 20g cheese + 1 cup salad\n"
                 "Evening (4:00-4:30PM): 30g Unsalted nuts + 200ml coffee\n"
                 "Dinner (8:00-8:30PM): 100g fish + Boiled rice + 1 cup vegetables + 2 bread")
        #break

    if BMI >= 24.9 and BMI<29.9:
        put_text('Your BMI:'+str(BMI)+'\nCategory is Overweight')
        put_text("Diet Chart")
        put_image(open('E:/Manish Scl Proj/Overweight.jpg', 'rb').read())
        put_text('Breakfast (8:00-8:30AM):	3 egg whites + 1 toasted brown bread + 1/2 cup low fat milk (no sugar)\n'
                 'Mid-Meal (11:00-11:30AM):	1 cup papaya\nLunch (2:00-2:30PM)	1 cup arhar dal + 1 chapatti + 1/2 cup low fat curd + salad\n'
                 'Evening (4:00-4:30PM):	1 cup vegetable soup\nDinner (8:00-8:30PM)	1 cup pumpkin + 1 chapatti + salad')
        #break

    if BMI >= 30:
        put_text('Your BMI:'+str(BMI)+'\nCategory is Obesity')
        put_text("Diet Chart")
        put_image(open('E:/Manish Scl Proj/Obesity.jpg', 'rb').read())
        put_text("Breakfast (8:00-8:30AM):	3 egg whites + 1 toasted brown bread + 1/2 cup low fat milk (no sugar)\n"
                 "Mid-Meal (11:00-11:30AM):	1 cup papaya \nLunch (2:00-2:30PM):	1 cup arhar dal + 1 chapatti + 1/2 cup low fat curd + salad\n"
                 "Evening (4:00-4:30PM):	1 cup vegetable soup\nDinner (8:00-8:30PM)	1 cup pumpkin + 1 chapatti + salad")



if __name__ == '__main__':
    bmi()